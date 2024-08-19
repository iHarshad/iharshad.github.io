#!/usr/bin/env python3

import argparse

import yaml


def parse_frontmatter(file_path):
    """Parses the frontmatter of a Markdown file and returns the draft value.

    Args:
      file_path: The path to the Markdown file.

    Returns:
      The value of the 'draft' variable in the frontmatter, or None if not found.
    """

    with open(file_path, "r") as file:
        content = file.read()

    # Find the frontmatter (between "---" delimiters)
    frontmatter_start = content.find("---")
    frontmatter_end = content.find("---", frontmatter_start + 3)

    if frontmatter_start != -1 and frontmatter_end != -1:
        frontmatter_yaml = content[frontmatter_start + 3 : frontmatter_end]
        frontmatter_data = yaml.safe_load(frontmatter_yaml)
        return frontmatter_data.get("draft")

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse the draft value from a Markdown file's frontmatter."
    )
    parser.add_argument("-f", "--file_path", required=True, help="Path to file")
    args = parser.parse_args()

    file_path = args.file_path

    # Check if the file is a Markdown file
    if file_path.endswith(".md") or file_path.endswith(".markdown"):
        draft_value = parse_frontmatter(file_path)
        if draft_value is not None:
            print(f"Draft value: {draft_value}")
        else:
            print("Draft variable not found in frontmatter.")
    else:
        print("File is not a Markdown file.")
