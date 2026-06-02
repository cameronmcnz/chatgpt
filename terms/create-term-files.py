import json
import re
import argparse
from pathlib import Path


DEFAULT_JSON_FILE = "prompt-engineering-map.json"
OUTPUT_FOLDER = "prompt-engineering"


def slugify(text):
    """
    Converts text into a clean lowercase filename slug.

    Example:
    "Input Material" -> "input-material"
    "Trade-offs" -> "trade-offs"
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def two_digit(number):
    return f"{number:02d}"


def format_list(items):
    if not items:
        return "None"

    return "\n".join(f"- {item}" for item in items)


def format_acronym_expansion(acronym_detail):
    """
    Formats an acronym expansion as markdown.
    """
    acronym = acronym_detail.get("acronym", "")
    expansion = acronym_detail.get("expansion", [])

    lines = [f"## {acronym} expansion", ""]

    for item in expansion:
        word = item.get("word", "")
        normalized_term = item.get("normalizedTerm", "")
        lines.append(f"- **{word}**: {normalized_term}")

    return "\n".join(lines)


def find_acronyms_for_term(stage, term):
    """
    Finds acronym details in the current stage that use either the term
    or one of the term's synonyms.

    Matching is done against:
    - normalizedTerm
    - word
    """
    term_name = term.get("term", "")
    synonyms = term.get("synonyms", [])

    search_terms = {term_name.lower()}
    search_terms.update(synonym.lower() for synonym in synonyms)

    matching_acronyms = []

    for acronym_detail in stage.get("acronymDetails", []):
        expansion_items = acronym_detail.get("expansion", [])

        for item in expansion_items:
            word = item.get("word", "").lower()
            normalized_term = item.get("normalizedTerm", "").lower()

            if word in search_terms or normalized_term in search_terms:
                matching_acronyms.append(acronym_detail)
                break

    return matching_acronyms


def build_term_markdown(stage, term, stage_count):
    stage_id = stage.get("stageId")
    term_name = term.get("term", "")
    meaning = term.get("meaning", "")
    synonyms = term.get("synonyms", [])

    matching_acronyms = find_acronyms_for_term(stage, term)

    acronym_names = [item.get("acronym", "") for item in matching_acronyms]

    lines = []

    lines.append(f"# {term_name}")
    lines.append("")
    lines.append(f"This is stage {stage_id} of {stage_count} stages for learning prompt engineering.")
    lines.append("")
    lines.append(
        f"The current term is **{term_name}**, which has this meaning when used to create a prompt: {meaning}."
    )
    lines.append("")
    lines.append("Synonyms for this include:")
    lines.append("")
    lines.append(format_list(synonyms))
    lines.append("")
    lines.append("Some prompt engineering techniques that use this term or its synonyms include:")
    lines.append("")
    lines.append(format_list(acronym_names))
    lines.append("")

    if matching_acronyms:
        lines.append("## Related acronym details")
        lines.append("")

        for acronym_detail in matching_acronyms:
            acronym = acronym_detail.get("acronym", "")
            expansion = acronym_detail.get("expansion", [])

            expansion_text = ", ".join(
                f"{item.get('word', '')} ({item.get('normalizedTerm', '')})"
                for item in expansion
            )

            lines.append(f"### {acronym}")
            lines.append("")
            lines.append(f"**{acronym}**: {expansion_text}")
            lines.append("")
            lines.append(acronym_detail.get("teachingUse", ""))
            lines.append("")
    else:
        lines.append("## Related acronym details")
        lines.append("")
        lines.append("No acronym in this stage directly uses this term or its synonyms.")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_acronym_markdown(stage, acronym_detail):
    acronym = acronym_detail.get("acronym", "")

    lines = []

    lines.append(f"# {acronym}")
    lines.append("")
    lines.append("## Acronym details")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(acronym_detail, indent=2, ensure_ascii=False))
    lines.append("```")
    lines.append("")
    lines.append("## Full stage details")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(stage, indent=2, ensure_ascii=False))
    lines.append("```")
    lines.append("")

    return "\n".join(lines).strip() + "\n"


def write_term_files(stage, stage_folder, stage_count):
    terms = stage.get("terms", [])

    for index, term in enumerate(terms):
        term_name = term.get("term", "term")
        filename = f"{two_digit(index)}-{slugify(term_name)}.md"
        file_path = stage_folder / filename

        content = build_term_markdown(
            stage=stage,
            term=term,
            stage_count=stage_count,
        )

        file_path.write_text(content, encoding="utf-8")


def write_acronym_files(stage, stage_folder):
    acronym_folder = stage_folder / "acronyms"
    acronym_folder.mkdir(exist_ok=True)

    acronym_details = stage.get("acronymDetails", [])

    for index, acronym_detail in enumerate(acronym_details):
        acronym = acronym_detail.get("acronym", "acronym")
        filename = f"{two_digit(index)}-{slugify(acronym)}.md"
        file_path = acronym_folder / filename

        content = build_acronym_markdown(
            stage=stage,
            acronym_detail=acronym_detail,
        )

        file_path.write_text(content, encoding="utf-8")


def generate_prompt_engineering_files(json_path):
    if not json_path.exists():
        raise FileNotFoundError(f"Could not find JSON file: {json_path}")

    data = json.loads(json_path.read_text(encoding="utf-8"))

    base_folder = json_path.parent / OUTPUT_FOLDER
    base_folder.mkdir(exist_ok=True)

    stages = data.get("stages", [])
    stage_count = data.get("stageCount", len(stages))

    for stage in stages:
        stage_id = stage.get("stageId")
        stage_folder_name = f"stage-{two_digit(stage_id)}"
        stage_folder = base_folder / stage_folder_name
        stage_folder.mkdir(exist_ok=True)

        write_term_files(
            stage=stage,
            stage_folder=stage_folder,
            stage_count=stage_count,
        )

        write_acronym_files(
            stage=stage,
            stage_folder=stage_folder,
        )

    print(f"Created prompt engineering files in: {base_folder}")


def main():
    parser = argparse.ArgumentParser(
        description="Create prompt engineering markdown seed files from a staged JSON learning map."
    )

    parser.add_argument(
        "json_file",
        nargs="?",
        default=DEFAULT_JSON_FILE,
        help=f"Path to the JSON file. Defaults to {DEFAULT_JSON_FILE}",
    )

    args = parser.parse_args()

    json_path = Path(args.json_file).resolve()
    generate_prompt_engineering_files(json_path)


if __name__ == "__main__":
    main()