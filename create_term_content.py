import argparse
import os
import re
import sys
import time
from pathlib import Path

from openai import OpenAI


DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4")
DEFAULT_ROOT_FOLDER = "prompt-engineering"


DEVELOPER_PROMPT = """
You are an expert prompt engineering instructor, curriculum designer, and conversational technical writer.

You are writing a finished markdown lesson for one prompt engineering term.

The source file contains:
- The term
- The stage number
- The total number of stages
- The meaning of the term
- Synonyms for the term
- Acronyms or prompt frameworks that use the term
- Related acronym details

Your job:
Create a polished markdown lesson that teaches the term clearly and practically.

Audience:
- Adults who are learning ChatGPT, prompt engineering, and AI for the first time.
- Many learners are 40+, but do not make that obvious.
- Occasional references to 80s or 90s music, TV, movies, work culture, or technology are allowed, but do not force them.
- The tone should be clear, useful, conversational, professional, slightly funny, and occasionally mildly sarcastic.
- Do not be childish.
- Do not sound like generic AI marketing copy.

Writing rules:
- Use markdown.
- Start with a clear H1 title using the term.
- Do not use em dashes.
- Do not use en dashes as sentence punctuation.
- Use commas, periods, colons, semicolons, or parentheses instead.
- Do not say "in today's digital age."
- Do not say "unlock the power of."
- Do not say "dive into."
- Do not say "whether you're a beginner or an expert."
- Do not include "As an AI language model."
- Do not mention that this was generated from a seed file.
- Do not include a preface like "Here is the markdown."
- Return only the finished markdown.

Content requirements:
1. Write a succinct preamble about the term.
2. Explain why the term is useful for improving or clarifying a prompt.
3. Give an overall description of how the term works in prompt engineering.
4. Mention common terms that mean something similar, using the synonyms from the source file.
5. Include exactly 3 sample prompts that use this term.
6. For each sample prompt, include:
   - The sample prompt itself
   - A short explanation of how the prompt uses the term
   - Why using the term improves the prompt
7. Finish with a witty, funny, or clever concluding sentence or short summary for the term.

Suggested structure:
# Term

Opening preamble.

## What this term means

Explain the term clearly.

## Why it improves a prompt

Explain how using the term makes a prompt clearer, more useful, or more controlled.

## Similar words you might see

Mention synonyms naturally. A short bullet list is fine.

## 3 sample prompts

### Sample prompt 1

> Prompt text here.

Explain how the prompt uses the term and why it improves the prompt.

### Sample prompt 2

> Prompt text here.

Explain how the prompt uses the term and why it improves the prompt.

### Sample prompt 3

> Prompt text here.

Explain how the prompt uses the term and why it improves the prompt.

## Quick summary

End with a witty or clever concluding sentence.

Length:
Aim for 500 to 900 words.
"""


def build_user_prompt(source_content: str, filename: str) -> str:
    return f"""
Create a finished markdown lesson from the source term file below.

The generated lesson should teach the term clearly and practically.

Source filename:
{filename}

SOURCE TERM FILE:
{source_content}
"""


def clean_model_output(text: str) -> str:
    """
    Removes common wrapper artifacts and enforces the no-em-dash preference.
    """
    text = text.strip()

    # Remove accidental markdown fences if the model adds them.
    text = re.sub(r"^```(?:markdown|md)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)

    # Enforce no em dashes.
    text = text.replace("—", ", ")
    text = text.replace("–", "-")

    # Remove excessive blank lines.
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    return text.strip() + "\n"


def generate_lesson(client: OpenAI, model: str, source_content: str, filename: str) -> str:
    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "developer",
                "content": DEVELOPER_PROMPT,
            },
            {
                "role": "user",
                "content": build_user_prompt(source_content, filename),
            },
        ],
    )

    return clean_model_output(response.output_text)


def is_inside_acronyms_folder(path: Path) -> bool:
    """
    Returns True when any parent folder is named acronyms.
    """
    return any(parent.name.lower() == "acronyms" for parent in path.parents)


def is_inside_generated_folder(path: Path) -> bool:
    """
    Returns True when any parent folder is named generated.
    This prevents accidentally regenerating generated lessons.
    """
    return any(parent.name.lower() == "generated" for parent in path.parents)


def find_term_files(root_folder: Path) -> list[Path]:
    """
    Finds all .md files under prompt-engineering, skipping:
    - acronyms folders
    - generated folders
    """
    files = []

    for path in root_folder.rglob("*.md"):
        if not path.is_file():
            continue

        if is_inside_acronyms_folder(path):
            continue

        if is_inside_generated_folder(path):
            continue

        files.append(path)

    return sorted(files)


def output_path_for_term_file(root_folder: Path, source_file: Path) -> Path:
    """
    Writes each generated file into a generated folder inside the same stage folder.

    Example:
    prompt-engineering/stage-01/00-task.md

    becomes:
    prompt-engineering/stage-01/generated/00-task.md
    """
    stage_folder = source_file.parent
    output_folder = stage_folder / "generated"
    output_folder.mkdir(exist_ok=True)

    return output_folder / source_file.name


def generate_all_term_lessons(
    root_folder: Path,
    model: str,
    overwrite: bool,
    delay_seconds: float,
) -> None:
    if not root_folder.exists():
        raise FileNotFoundError(f"Root folder not found: {root_folder}")

    if not root_folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {root_folder}")

    term_files = find_term_files(root_folder)

    if not term_files:
        print(f"No term markdown files found in: {root_folder}")
        return

    client = OpenAI()

    print(f"Using model: {model}")
    print(f"Root folder: {root_folder}")
    print(f"Term files found: {len(term_files)}")
    print()

    for index, source_file in enumerate(term_files, start=1):
        output_file = output_path_for_term_file(root_folder, source_file)

        if output_file.exists() and not overwrite:
            print(f"[{index}/{len(term_files)}] Skipping existing file: {output_file}")
            continue

        print(f"[{index}/{len(term_files)}] Generating lesson: {source_file}")

        source_content = source_file.read_text(encoding="utf-8")

        try:
            generated_content = generate_lesson(
                client=client,
                model=model,
                source_content=source_content,
                filename=source_file.name,
            )

            output_file.write_text(generated_content, encoding="utf-8")
            print(f"    Wrote: {output_file}")

        except Exception as error:
            print(f"    ERROR generating {source_file}: {error}", file=sys.stderr)

        if delay_seconds > 0 and index < len(term_files):
            time.sleep(delay_seconds)

    print()
    print("Term lesson generation complete.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate finished markdown lessons for prompt engineering term files."
    )

    parser.add_argument(
        "--folder",
        default=DEFAULT_ROOT_FOLDER,
        help=f"Root prompt engineering folder. Defaults to {DEFAULT_ROOT_FOLDER}",
    )

    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"OpenAI model to use. Defaults to OPENAI_MODEL or {DEFAULT_MODEL}.",
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite files that already exist in each generated folder.",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds to wait between API calls. Default is 0.5.",
    )

    args = parser.parse_args()

    generate_all_term_lessons(
        root_folder=Path(args.folder),
        model=args.model,
        overwrite=args.overwrite,
        delay_seconds=args.delay,
    )


if __name__ == "__main__":
    main()