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
You are an expert prompt engineering instructor, curriculum designer, and YouTube education scriptwriter.

You are writing a finished markdown lesson for one prompt engineering acronym.

The source file contains:
- The acronym
- The stage it belongs to
- The acronym expansion
- The normalized prompt engineering terms for each letter
- Teaching use notes
- Full stage details

Your job:
Create a polished markdown lesson that teaches the acronym clearly, practically, and memorably.

Audience:
- Adults who are learning ChatGPT, prompt engineering, and AI for the first time.
- Many learners are 40+, but do not make that obvious.
- Occasional references to 80s or 90s music, TV, movies, work culture, or technology are allowed, but do not force them.
- The tone should be clear, useful, conversational, professional, slightly funny, and occasionally mildly sarcastic.
- Do not be childish.
- Do not sound like generic AI marketing copy.

Writing purpose:
The final markdown should work as a webpage lesson and also as a quick, catchy YouTube Short style explanation that could be read aloud in up to 180 seconds.

Writing rules:
- Use markdown.
- Start with a clear H1 title using the acronym.
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
1. Write a quick and catchy description of the acronym.
2. Explain what each letter means.
3. Explain how the acronym helps someone write better prompts.
4. Include exactly 3 sample prompts that use this technique.
5. The first sample prompt must be very formal and explicitly label the acronym fields.
   Example style:
   AIM: Write a tweet.
   RESTRICTION: Maximum 180 characters.
   AUDIENCE: Beginners learning ChatGPT.
   PERSONA: Friendly instructor.
6. The second sample prompt should be semi-structured.
   It may use bullets or short labels, but should feel less formal than the first.
7. The third sample prompt should be natural and casual.
   It should not explicitly label the acronym fields.
   Example style:
   Write a story about a cat with a pancake on its head that is less than 500 words long.
8. For each sample prompt, explain how each letter of the acronym appears in the prompt.
9. For each sample prompt, explain why the acronym improves the prompt.
10. Include warnings or extra things to consider.
11. End with a quick summary and a short inspirational suggestion for how learners can test the acronym on their own.

Suggested structure:
# ACRONYM

Opening hook or catchy explanation.

## What the acronym means

Use a markdown table with:
- Letter or word
- Prompt ingredient
- What it does

## Why this acronym works

Explain why this technique helps prompts become clearer, more useful, or more reliable.

## 3 sample prompts

### Sample prompt 1: Formal version

> Prompt text here.

**How the acronym shows up:**
- Letter 1:
- Letter 2:
- Letter 3:

**Why it improves the prompt:**
Explanation here.

### Sample prompt 2: Semi-structured version

> Prompt text here.

**How the acronym shows up:**
- Letter 1:
- Letter 2:
- Letter 3:

**Why it improves the prompt:**
Explanation here.

### Sample prompt 3: Natural version

> Prompt text here.

**How the acronym shows up:**
- Letter 1:
- Letter 2:
- Letter 3:

**Why it improves the prompt:**
Explanation here.

## Warnings and extra tips

Give practical advice. Mention possible overuse, missing context, vague instructions, unrealistic expectations, or when this acronym is not enough.

## Quick summary

End with a short, memorable wrap-up and a suggestion for where the learner should try the acronym next.

Length:
Aim for 700 to 1,100 words.
"""


def build_user_prompt(source_content: str, filename: str) -> str:
    return f"""
Create a finished markdown lesson from the acronym source file below.

The generated lesson should teach the acronym clearly and practically.

Make sure the lesson:
- Explains the acronym
- Explains each letter or expansion word
- Gives exactly 3 sample prompts
- Makes the first sample prompt formal and explicitly labeled
- Makes the second sample prompt semi-structured
- Makes the third sample prompt natural and casual
- Explains how each letter of the acronym appears in each prompt
- Explains why each prompt is improved by the acronym
- Includes warnings or extra considerations
- Ends with a quick summary and a suggestion for learner practice

Source filename:
{filename}

SOURCE ACRONYM FILE:
{source_content}
"""


def clean_model_output(text: str) -> str:
    """
    Removes common wrapper artifacts and enforces the no-em-dash preference.
    """
    text = text.strip()

    # Remove accidental markdown fences.
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


def is_inside_generated_folder(path: Path) -> bool:
    """
    Returns True when any parent folder is named generated.
    This prevents accidentally processing generated lessons.
    """
    return any(parent.name.lower() == "generated" for parent in path.parents)


def is_inside_acronyms_folder(path: Path) -> bool:
    """
    Returns True when any parent folder is named acronyms.
    """
    return any(parent.name.lower() == "acronyms" for parent in path.parents)


def find_acronym_files(root_folder: Path) -> list[Path]:
    """
    Finds all .md files under prompt-engineering that are inside acronyms folders,
    while skipping generated folders.
    """
    files = []

    for path in root_folder.rglob("*.md"):
        if not path.is_file():
            continue

        if is_inside_generated_folder(path):
            continue

        if not is_inside_acronyms_folder(path):
            continue

        files.append(path)

    return sorted(files)


def output_path_for_acronym_file(source_file: Path) -> Path:
    """
    Writes each generated file into a generated folder inside the same acronyms folder.

    Example:
    prompt-engineering/stage-01/acronyms/00-cats.md

    becomes:
    prompt-engineering/stage-01/acronyms/generated/00-cats.md
    """
    acronym_folder = source_file.parent
    output_folder = acronym_folder / "generated"
    output_folder.mkdir(exist_ok=True)

    return output_folder / source_file.name


def generate_all_acronym_lessons(
    root_folder: Path,
    model: str,
    overwrite: bool,
    delay_seconds: float,
) -> None:
    if not root_folder.exists():
        raise FileNotFoundError(f"Root folder not found: {root_folder}")

    if not root_folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {root_folder}")

    acronym_files = find_acronym_files(root_folder)

    if not acronym_files:
        print(f"No acronym markdown files found in: {root_folder}")
        return

    client = OpenAI()

    print(f"Using model: {model}")
    print(f"Root folder: {root_folder}")
    print(f"Acronym files found: {len(acronym_files)}")
    print()

    for index, source_file in enumerate(acronym_files, start=1):
        output_file = output_path_for_acronym_file(source_file)

        if output_file.exists() and not overwrite:
            print(f"[{index}/{len(acronym_files)}] Skipping existing file: {output_file}")
            continue

        print(f"[{index}/{len(acronym_files)}] Generating acronym lesson: {source_file}")

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

        if delay_seconds > 0 and index < len(acronym_files):
            time.sleep(delay_seconds)

    print()
    print("Acronym lesson generation complete.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate finished markdown lessons for prompt engineering acronym files."
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
        help="Overwrite files that already exist in each acronyms/generated folder.",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds to wait between API calls. Default is 0.5.",
    )

    args = parser.parse_args()

    generate_all_acronym_lessons(
        root_folder=Path(args.folder),
        model=args.model,
        overwrite=args.overwrite,
        delay_seconds=args.delay,
    )


if __name__ == "__main__":
    main()