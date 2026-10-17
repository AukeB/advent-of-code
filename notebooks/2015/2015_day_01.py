import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 1
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

    from collections import defaultdict

    from aoc.utils import read_data

    return defaultdict, mo, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 1 - Not Quite Lisp
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
    Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

    Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

    Here's an easy puzzle to warm you up.

    Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

    An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

    The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

    For example:

    - (()) and ()() both result in floor 0.
    - ((( and (()(()( both result in floor 3.
    - ))((((( also results in floor 3.
    - ()) and ))( both result in floor -1 (the first basement level).
    - ))) and )())()) both result in floor -3.

    To what floor do the instructions take Santa?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(defaultdict):
    def exercise_1_1_find_the_final_floor_number(
        floor_instructions: str, starting_floor_number: int = 0
    ) -> int:
        """
        Calculate the final floor Santa ends up on based on floor instructions.

        Santa starts on `starting_floor_number` (defaults to 0) and follows a sequence
        of instructions where '(' means going up one floor and ')' means going
        down one floor. This function counts the ups and downs to determine the
        final floor.

        Args:
            floor_instructions (str): A string containing '(' and ')' characters
                representing Santa's floor movements.
            starting_floor_number (int, optional): The floor Santa starts on.
                Defaults to 0.

        Returns:
            int: The final floor number after following all instructions.
        """
        direction_count = defaultdict(int)

        for character in floor_instructions:
            if character == "(":
                direction_count["up"] += 1
            elif character == ")":
                direction_count["down"] += 1

        final_floor_number = (
            starting_floor_number + direction_count["up"] - direction_count["down"]
        )

        return final_floor_number

    return (exercise_1_1_find_the_final_floor_number,)


@app.cell
def _(exercise_1_1_find_the_final_floor_number, read_data):
    floor_instructions = read_data(
        file_path="data/2015/2015_day_01.txt", separator="\n"
    )

    final_floor_number = exercise_1_1_find_the_final_floor_number(
        floor_instructions=floor_instructions
    )

    assert final_floor_number == 232
    return (floor_instructions,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

    For example:

    - ) causes him to enter the basement at character position 1.
    - ()()) causes him to enter the basement at character position 5.

    What is the position of the character that causes Santa to first enter the basement?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_1_2_find_position_first_character_basement_entry(
    floor_instructions: str,
    starting_floor_number: int = 0,
) -> int:
    """
    Determine the position of the first instruction that causes Santa to enter
    the basement.

    Santa starts on `starting_floor_number` (defaults to 0) and follows a sequence
    of instructions where '(' increases the floor by one and ')' decreases it
    by one. The function returns the 1-based position of the first character
    that brings Santa to floor -1 (the basement).

    Args:
        floor_instructions (str): A string of '(' and ')' characters representing
            Santa's floor movements.
        starting_floor_number (int, optional): The floor Santa starts on.
            Defaults to 0.

    Returns:
        int: The 1-based position of the first character that causes entry into
            the basement.
    """
    starting_index = 1
    current_floor_number = starting_floor_number

    for index, character in enumerate(floor_instructions, start=starting_index):
        current_floor_number += 1 if character == "(" else -1

        if current_floor_number == -1:
            return index

    raise ValueError("Santa never enters the basement")


@app.cell
def _(floor_instructions):
    basement_entry_position = exercise_1_2_find_position_first_character_basement_entry(
        floor_instructions=floor_instructions
    )

    assert basement_entry_position == 1783
    return


if __name__ == "__main__":
    app.run()
