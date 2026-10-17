"""Utility module for solving Advent of Code puzzles.

The only helper function currently in this module is read_data, which loads
puzzle input. It works for all puzzles that have solutions in this repo.
"""


def read_data(file_path: str, separator: str) -> str | list[str]:
    """Reads a file and returns the content of the file as a list of str objects
    or a single str if the file contains only one element. The separator
    determines how the file content is split: by commas or new lines.

    Args:
        file_path (str): The path to the file.
        separator (str): The separator for splitting the file content.

    Returns:
        str | list[str]: A list of strings split based on the separator, or a
            single string if there's only one element.

    Raises:
        ValueError: If the separator is neither "," nor "\\n".
    """
    with open(file_path, "r") as file:
        content = file.read().strip()

    if separator == ",":
        data = content.split(",")
    elif separator == "\n":
        data = content.split("\n")
    else:
        raise ValueError(f"Unsupported separator: {separator!r}")

    if len(data) == 1:
        return data[0]

    return data
