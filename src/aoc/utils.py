"""Utility module for solving Advent of Code puzzles.

This module contains utility functions that are used throughout all Advent of
Code puzzles.
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


def convert_string_to_list_of_tuples(str_data: str) -> list[tuple[int]]:
    """Convert a string representation of tuples into a list of integer tuples.

    Each tuple in the string should be enclosed in parentheses and separated by
    spaces. Elements within a tuple should be comma-separated integers.

    Args:
        str_data (str): The str data representing one or more tuples.

    Returns:
        list[tuple[int]]: The same data but now with the correct variable types.
    """
    list_of_tuples = []
    data_split = str_data.split(" ")

    for element in data_split:
        sub_list_elements = element[1:-1].split(",")
        sub_list_elements = [int(number) for number in sub_list_elements]
        list_of_tuples.append(tuple(sub_list_elements))

    return list_of_tuples
