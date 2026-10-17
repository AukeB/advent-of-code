import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 8
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
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _exercise_8_1_special_character_analysis(mo):
    mo.md(r"""
    Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

    It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

    However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

    For example:

    - "\" is 2 characters of code (the two double quotes), but the string contains zero characters.
    - "abc" is 5 characters of code, but 3 characters in the string data.
    - "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
    - "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.

    Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

    Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

    For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
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
        """
        Calculate the total number of characters of code for string literals minus
        the total number of characters in memory for the values of the strings.
        Handles three escape sequences: \\\\ (single backslash), \\" (lone double-quote),
        and \\x followed by two hexadecimal characters (single ASCII character).

        1. Initialise the difference counter with 2 per line to account for the
           surrounding double-quote characters.
        2. For each line, walk character by character; when a backslash is found,
           identify the escape sequence and increment the difference counter by the
           number of code characters that collapse into one in-memory character.

        Args:
            santas_list (list[str]): The double-quoted string literals from Santa's
                digital list, one per line.

        Returns:
            difference_counter (int): Total characters of code minus total characters
                in memory across all string literals.
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
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.

    For example:

    - "\" encodes to "\"\"\", an increase from 2 characters to 6.
    - "abc" encodes to "\"abc\"\", an increase from 5 characters to 9.
    - "aaa\"aaa" encodes to "\"aaa\\\"aaa\"\", an increase from 10 characters to 16.
    - "\x27" encodes to "\"\\x27\"\", an increase from 6 characters to 11.

    Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_8_2_special_character_analysis(santas_list: list[str]) -> int:
    """
    Calculate the total number of characters in the re-encoded string literals
    minus the total number of characters in the original code representation.

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
