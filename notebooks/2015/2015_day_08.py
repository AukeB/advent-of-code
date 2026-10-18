import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 8

    https://adventofcode.com/2015/day/8
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
    ## Day 8: Matchsticks
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _():
    import string

    def exercise_8_1_special_character_analysis(santas_list: list[str]) -> int:
        """Calculate the total number of characters of code for string literals
        minus the total number of characters in memory for the values of the
        strings. Handles three escape sequences: \\\\ (single backslash), \\"
        (lone double-quote), and \\x followed by two hexadecimal characters
        (single ASCII character).

        1. Initialise the difference counter with 2 per line to account for the
           surrounding double-quote characters.
        2. For each line, walk character by character; when a backslash is
           found, identify the escape sequence and increment the difference
           counter by the number of code characters that collapse into one in-
           memory character.

        Args:
            santas_list (list[str]): The double-quoted string literals from
                Santa's digital list, one per line.

        Returns:
            difference_counter (int): Total characters of code minus total
                characters in memory across all string literals.
        """
        difference_counter = 2 * len(santas_list)

        for line in santas_list:
            char_index: int = 0

            while char_index < len(line):
                if line[char_index] == "\\":
                    next_char = line[char_index + 1]

                    if next_char == "\\" or next_char == '"':
                        difference_counter += 1
                        char_index += 2
                    elif next_char == "x" and all(
                        digit in string.hexdigits
                        for digit in line[char_index + 2 : char_index + 4]
                    ):
                        difference_counter += 3
                        char_index += 4
                    else:
                        char_index += 1
                else:
                    char_index += 1

        return difference_counter

    return (exercise_8_1_special_character_analysis,)


@app.cell
def _(exercise_8_1_special_character_analysis, read_data):
    santas_list: list[str] = read_data(
        file_path="data/2015/2015_day_08.txt", separator="\n"
    )

    difference_special_characters = exercise_8_1_special_character_analysis(
        santas_list=santas_list
    )

    assert difference_special_characters == 1350
    return (santas_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_8_2_special_character_analysis(santas_list: list[str]) -> int:
    """Calculate the total number of characters in the re-encoded string
    literals minus the total number of characters in the original code
    representation.

    Re-encoding wraps each string in a new pair of double-quotes and escapes
    every backslash and double-quote character with an additional backslash.

    Args:
        santas_list (list[str]): The double-quoted string literals from Santa's
            digital list, one per line.

    Returns:
        difference_counter (int): Total characters of re-encoded strings minus
            total characters of the original string literals across all lines.
    """
    difference_counter = 2 * len(santas_list) + sum(
        line.count("\\") + line.count('"') for line in santas_list
    )

    return difference_counter


@app.cell
def _(santas_list: list[str]):
    difference_special_characters_reverse = exercise_8_2_special_character_analysis(
        santas_list=santas_list
    )

    assert difference_special_characters_reverse == 2085
    return


if __name__ == "__main__":
    app.run()
