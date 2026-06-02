import argparse
import os
import re
import sys
import time
from pathlib import Path

from openai import OpenAI


DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")
DEFAULT_ROOT_FOLDER = "."
DEFAULT_DATE = "2026-05-12 09:00:00 -0400"


COURSE_CONTEXT = """
You are helping create markdown content for a beginner-friendly course and lesson library about ChatGPT, prompt engineering, AI productivity, and reusable prompting techniques.

The course includes:
- A 7 Day Condensed ChatGPT Masterclass
- Day-level course overview pages
- Topic-level lesson pages
- Prompt engineering term lessons
- Prompt engineering acronym lessons
- Stage-based prompt engineering learning paths

The audience:
- Beginners learning ChatGPT, prompt engineering, and AI for the first time
- Adults who want practical, clear, useful AI skills
- Learners interested in productivity, writing, creativity, learning, research, files, workflows, automation, and better prompting

Common content themes:
- ChatGPT basics
- LLMs
- ChatGPT versus Google, Claude, Gemini, Perplexity, and Copilot
- Prompt engineering techniques
- Prompt ingredients such as task, goal, context, audience, tone, format, role, limits, examples, guardrails, evaluation, feedback, refinement, evidence, and confidence
- Acronyms such as CATS, CRAP, FAST, MEOW, PAWS, TREAT, POWER, SNAP, SORT, CHUNK, CLAW, TUTOR, QUIZ, SIM, ACT, DRIFT, LOOP, ROAST, REFINE, RANK, PICK, TILT, LENS, CHECK, VERIFY, FLIP, and DEBATE
- Practical lessons, mini projects, and approachable explanations

Frontmatter goals:
- Create SEO-friendly titles and descriptions
- Keep titles accurate to the page purpose
- Use categories that help organize the site
- Use tags that reflect the content
- Use excerpts that make sense as page previews
"""


DEVELOPER_PROMPT = """
You are an expert SEO editor, Jekyll markdown publisher, and course content organizer.

Your job is to create YAML frontmatter for a markdown page.

You will receive:
- A filename
- The first four paragraphs from the page
- Every markdown heading from the page
- Context about the course and topic library

Return only valid YAML frontmatter, including the opening and closing triple-dash lines.

Required format:

---
layout: post
title: <Create an SEO optimized title that keeps to the purpose of the page>
description: <An SEO optimized description of the content using good SEO keywords>
date: 2026-05-12 09:00:00 -0400
categories: [<category>, <category>]
tags: [<tag>, <tag>, <tag>]
excerpt: "<An excerpt from the page.>"
---

Rules:
- Return only the frontmatter.
- Do not wrap the output in code fences.
- Use layout: post exactly.
- Use the date provided by the user exactly.
- Use a concise SEO title, ideally under 70 characters.
- Use an SEO description, ideally 120 to 160 characters.
- Use lowercase category and tag values.
- Categories should be broad, such as course, lesson, term, acronym, prompt-engineering, chatgpt, automation, multimodal, files, beginner.
- Tags should be more specific and based on the page content.
- Do not invent unrelated tags.
- Use valid YAML.
- Quote strings when needed.
- Do not use em dashes.
- Do not use colons in unquoted title, description, or excerpt values.
- Make the excerpt readable and useful as a page preview.
"""


def has_frontmatter(content: str) -> bool:
    """
    Checks for YAML frontmatter at the very top of the file.
    """
    return content.startswith("---\n") or content.startswith("---\r\n")


def strip_existing_frontmatter(content: str) -> str:
    """
    Not used by default, but useful if you later decide to replace frontmatter.
    """
    if not has_frontmatter(content):
        return content

    match = re.match(r"^---\s*\n.*?\n---\s*\n?", content, flags=re.DOTALL)
    if match:
        return content[match.end():]

    return content


def extract_headings(content: str) -> list[str]:
    """
    Extracts all markdown headings.
    """
    headings = []

    for line in content.splitlines():
        if re.match(r"^\s{0,3}#{1,6}\s+", line):
            headings.append(line.strip())

    return headings


def extract_first_paragraphs(content: str, count: int = 4) -> list[str]:
    """
    Extracts the first N non-empty markdown paragraphs.

    This skips:
    - headings
    - frontmatter
    - fenced code blocks
    - table rows
    - list-only lines

    It keeps normal prose paragraphs.
    """
    content = strip_existing_frontmatter(content)

    paragraphs = []
    current = []
    in_code_block = False

    for line in content.splitlines():
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        if not stripped:
            if current:
                paragraph = " ".join(current).strip()
                if paragraph:
                    paragraphs.append(paragraph)
                    current = []

                if len(paragraphs) >= count:
                    break
            continue

        if re.match(r"^#{1,6}\s+", stripped):
            continue

        if stripped.startswith("|"):
            continue

        if re.match(r"^[-*+]\s+", stripped):
            continue

        if re.match(r"^\d+\.\s+", stripped):
            continue

        current.append(stripped)

    if current and len(paragraphs) < count:
        paragraphs.append(" ".join(current).strip())

    return paragraphs[:count]


def build_user_prompt(
    filename: str,
    relative_path: str,
    paragraphs: list[str],
    headings: list[str],
    date_value: str,
) -> str:
    paragraph_text = "\n\n".join(
        f"Paragraph {index + 1}: {paragraph}"
        for index, paragraph in enumerate(paragraphs)
    )

    heading_text = "\n".join(headings) if headings else "No markdown headings found."

    return f"""
Create YAML frontmatter for this markdown file.

Use this exact date:
{date_value}

Course and site context:
{COURSE_CONTEXT}

File:
{filename}

Relative path:
{relative_path}

First four paragraphs:
{paragraph_text if paragraph_text else "No paragraph text found."}

Markdown headings:
{heading_text}
"""


def clean_frontmatter(text: str, date_value: str) -> str:
    """
    Cleans the model response and makes sure it looks like frontmatter.
    """
    text = text.strip()

    # Remove accidental code fences.
    text = re.sub(r"^```(?:yaml|yml)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)

    # Enforce no em dash or en dash punctuation.
    text = text.replace("—", ", ")
    text = text.replace("–", "-")

    # Extract only the frontmatter block if extra text slipped in.
    match = re.search(r"---\s*\n.*?\n---", text, flags=re.DOTALL)
    if match:
        text = match.group(0).strip()

    if not text.startswith("---"):
        text = "---\n" + text

    if not text.endswith("---"):
        text = text.rstrip() + "\n---"

    # Ensure the required date is present.
    text = re.sub(
        r"^date:\s*.*$",
        f"date: {date_value}",
        text,
        flags=re.MULTILINE,
    )

    if "date:" not in text:
        text = text.replace("description:", f"description:", 1)
        text = text.replace("\ncategories:", f"\ndate: {date_value}\ncategories:", 1)

    return text.strip() + "\n"


def generate_frontmatter(
    client: OpenAI,
    model: str,
    filename: str,
    relative_path: str,
    paragraphs: list[str],
    headings: list[str],
    date_value: str,
) -> str:
    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "developer",
                "content": DEVELOPER_PROMPT,
            },
            {
                "role": "user",
                "content": build_user_prompt(
                    filename=filename,
                    relative_path=relative_path,
                    paragraphs=paragraphs,
                    headings=headings,
                    date_value=date_value,
                ),
            },
        ],
    )

    return clean_frontmatter(response.output_text, date_value)


def should_skip_file(path: Path, root_folder: Path, skip_generated: bool) -> bool:
    """
    Skips common folders you normally do not want to process.
    """
    ignored_folder_names = {
        ".git",
        ".github",
        ".idea",
        ".vscode",
        "__pycache__",
        "node_modules",
        ".venv",
        "venv",
        "env",
    }

    parts = {part.lower() for part in path.relative_to(root_folder).parts}

    if parts.intersection(ignored_folder_names):
        return True

    if skip_generated and "generated" in parts:
        return True

    return False


def find_markdown_files(root_folder: Path, skip_generated: bool) -> list[Path]:
    files = []

    for path in root_folder.rglob("*.md"):
        if not path.is_file():
            continue

        if should_skip_file(path, root_folder, skip_generated):
            continue

        files.append(path)

    return sorted(files)


def prepend_frontmatter(path: Path, frontmatter: str, original_content: str) -> None:
    new_content = frontmatter.strip() + "\n\n" + original_content.lstrip()
    path.write_text(new_content, encoding="utf-8")


def update_markdown_files(
    root_folder: Path,
    model: str,
    date_value: str,
    delay_seconds: float,
    dry_run: bool,
    skip_generated: bool,
) -> None:
    if not root_folder.exists():
        raise FileNotFoundError(f"Root folder not found: {root_folder}")

    if not root_folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {root_folder}")

    markdown_files = find_markdown_files(root_folder, skip_generated)

    if not markdown_files:
        print(f"No markdown files found in: {root_folder}")
        return

    client = OpenAI()

    print(f"Using model: {model}")
    print(f"Root folder: {root_folder}")
    print(f"Markdown files found: {len(markdown_files)}")
    print(f"Skip generated folders: {skip_generated}")
    print(f"Dry run: {dry_run}")
    print()

    updated_count = 0
    skipped_count = 0
    error_count = 0

    for index, path in enumerate(markdown_files, start=1):
        relative_path = str(path.relative_to(root_folder))

        try:
            content = path.read_text(encoding="utf-8")

            if has_frontmatter(content):
                print(f"[{index}/{len(markdown_files)}] Skipping, frontmatter exists: {relative_path}")
                skipped_count += 1
                continue

            paragraphs = extract_first_paragraphs(content, count=4)
            headings = extract_headings(content)

            print(f"[{index}/{len(markdown_files)}] Creating frontmatter: {relative_path}")

            frontmatter = generate_frontmatter(
                client=client,
                model=model,
                filename=path.name,
                relative_path=relative_path,
                paragraphs=paragraphs,
                headings=headings,
                date_value=date_value,
            )

            if dry_run:
                print(frontmatter)
            else:
                prepend_frontmatter(path, frontmatter, content)
                print(f"    Updated: {relative_path}")

            updated_count += 1

            if delay_seconds > 0 and index < len(markdown_files):
                time.sleep(delay_seconds)

        except Exception as error:
            print(f"    ERROR processing {relative_path}: {error}", file=sys.stderr)
            error_count += 1

    print()
    print("Frontmatter update complete.")
    print(f"Updated: {updated_count}")
    print(f"Skipped existing frontmatter: {skipped_count}")
    print(f"Errors: {error_count}")


def main():
    parser = argparse.ArgumentParser(
        description="Add AI-generated YAML frontmatter to markdown files that do not already have it."
    )

    parser.add_argument(
        "--folder",
        default=DEFAULT_ROOT_FOLDER,
        help="Root folder to scan. Defaults to the current folder.",
    )

    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"OpenAI model to use. Defaults to OPENAI_MODEL or {DEFAULT_MODEL}.",
    )

    parser.add_argument(
        "--date",
        default=DEFAULT_DATE,
        help=f"Date value for frontmatter. Defaults to {DEFAULT_DATE}",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds to wait between API calls. Default is 0.5.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print generated frontmatter without modifying files.",
    )

    parser.add_argument(
        "--include-generated",
        action="store_true",
        help="Also process files inside generated folders.",
    )

    args = parser.parse_args()

    update_markdown_files(
        root_folder=Path(args.folder).resolve(),
        model=args.model,
        date_value=args.date,
        delay_seconds=args.delay,
        dry_run=args.dry_run,
        skip_generated=not args.include_generated,
    )


if __name__ == "__main__":
    main()