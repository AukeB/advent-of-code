import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 12
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Imports
    """)
    return


@app.cell
def _():
    import marimo as mo

    from aoc.utils import read_data

    return mo, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 12: JSAbacusFramework.io
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

    They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

    For example:

    - `[1,2,3]` and `{"a":2,"b":4}` both have a sum of `6`.
    - `[[[3]]]` and `{"a":{"b":4},"c":-1}` both have a sum of `3`.
    - `{"a":[-1,1]}` and `[-1,{"a":1}]` both have a sum of `0`.
    - `[]` and `{}` both have a sum of `0`.

    You will not encounter any strings containing numbers.

    What is the sum of all numbers in the document?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_12_1_find_sum_of_all_numbers(
    json_document: str,
) -> int:
    """Sum every integer found in a JSON document without parsing it.

    The document is scanned character by character, looking one character ahead,
    so that each run of consecutive digits is collected into a single number. A
    minus sign directly before the first digit makes that number negative.

    1. Walk the document in (current, next) character pairs.
    2. Accumulate digits while the next character is a digit, recording on the
       first digit whether the preceding character is a minus sign.
    3. When a non-digit follows, convert the collected digits to an integer,
       apply the sign, and store it.
    4. Sum all stored integers.

    Args:
        json_document (str): The raw JSON text to scan.

    Returns:
        total_sum (int): The sum of all integers in the document.
    """
    number_already_detected: bool = False
    is_negative: bool = False
    digits: str = ""
    all_integers: list[int] = []

    for char, next_char in zip(json_document, json_document[1:]):
        if next_char.isdigit():
            digits += next_char
            if not number_already_detected:
                is_negative = True if char == "-" else False
                number_already_detected = True
        else:
            if digits:
                all_integers.append(
                    -1 * int(digits)
                ) if is_negative else all_integers.append(int(digits))
            number_already_detected = False
            digits = ""

    total_sum = sum(all_integers)

    return total_sum


@app.cell
def _(exercise_12_1_find_sum_of_all_numbers, read_data):
    json_document: str = read_data(
        file_path="data/2015/2015_day_12.txt", separator="\n"
    )

    total_sum_12_1 = exercise_12_1_find_sum_of_all_numbers(json_document=json_document)

    assert total_sum_12_1 == 191164
    return (json_document,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Uh oh - the Accounting-Elves have realized that they double-counted everything red.

    Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

    - `[1,2,3]` still has a sum of 6.
    - `[1,{"c":"red","b":2},3]` now has a sum of `4`, because the middle object is ignored.
    - `{"d":"red","e":[1,2,3,4],"f":5}` now has a sum of `0`, because the entire structure is ignored.
    - `[1,"red",5]` has a sum of `6`, because "red" in an array has no effect.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_12_2_find_sum_without_red(
    json_document: str,
    ignore_value: str = "red",
) -> int:
    """Sum every integer in a JSON document, ignoring objects that contain a
    value.

    The document is parsed with the json module and then traversed recursively.
    Any object with ignore_value among its direct values is excluded along with
    all of its nested content. Arrays are never excluded, even if they contain
    ignore_value.

    Args:
        json_document (str): The raw JSON text to process.
        ignore_value (str): The value that disqualifies an object from being
            counted.

    Returns:
        total_sum (int): The sum of all integers outside of ignored objects.
    """
    import json

    json_content = json.loads(json_document)

    def process_json_content(
        json_content: list | dict | int | str,
        total_sum: int,
    ) -> int:
        """Recursively add every integer in a parsed JSON node to a running
        total.

        Lists are traversed element by element. Dicts are skipped entirely,
        along with everything nested inside them, if ignore_value (read from the
        enclosing function) is among their direct values. Strings and any other
        types contribute nothing.

        Args:
            json_content (list | dict | int | str): A parsed JSON value.
            total_sum (int): The running total accumulated so far.

        Returns:
            total_sum (int): The running total including all integers in this
                node.
        """
        if isinstance(json_content, list):
            for json_element in json_content:
                total_sum = process_json_content(json_element, total_sum)
        elif isinstance(json_content, dict):
            if ignore_value in json_content.values():
                pass
            else:
                for json_element in json_content.values():
                    total_sum = process_json_content(json_element, total_sum)
        elif isinstance(json_content, int):
            total_sum += json_content

        return total_sum

    total_sum = process_json_content(json_content, 0)

    return total_sum


@app.cell
def _(exercise_12_2_find_sum_without_red, json_document: str):
    total_sum_12_2 = exercise_12_2_find_sum_without_red(json_document=json_document)

    assert total_sum_12_2 == 87842
    return


if __name__ == "__main__":
    app.run()
