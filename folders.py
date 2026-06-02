from pathlib import Path


def write_markdown_file_map(root_folder="."):
    root = Path(root_folder).resolve()
    output_file = root / "files-and-folders.txt"

    ignored_folders = {
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

    markdown_files = []

    for path in root.rglob("*.md"):
        if not path.is_file():
            continue

        relative_parts = path.relative_to(root).parts

        if any(part in ignored_folders for part in relative_parts):
            continue

        markdown_files.append(path.relative_to(root))

    markdown_files.sort()

    lines = []
    lines.append("# Markdown File Map")
    lines.append("")
    lines.append("This is a list of markdown files in the project.")
    lines.append("")
    lines.append(f"Markdown files found: {len(markdown_files)}")
    lines.append("")

    for path in markdown_files:
        lines.append(f"- `{path}`")

    output_file.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote file map to: {output_file}")


if __name__ == "__main__":
    write_markdown_file_map(".")