import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 1

    https://adventofcode.com/2015/day/1
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
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(defaultdict):
    def exercise_1_1_find_the_final_floor_number(
        floor_instructions: str, starting_floor_number: int = 0
    ) -> int:
        """Calculate the final floor Santa ends up on based on floor
        instructions.

        Santa starts on `starting_floor_number` (defaults to 0) and follows a
        sequence of instructions where '(' means going up one floor and ')'
        means going down one floor. This function counts the ups and downs to
        determine the final floor.

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
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_1_2_find_position_first_character_basement_entry(
    floor_instructions: str,
    starting_floor_number: int = 0,
) -> int:
    """Determine the position of the first instruction that causes Santa to
    enter the basement.

    Santa starts on `starting_floor_number` (defaults to 0) and follows a
    sequence of instructions where '(' increases the floor by one and ')'
    decreases it by one. The function returns the 1-based position of the first
    character that brings Santa to floor -1 (the basement).

    Args:
        floor_instructions (str): A string of '(' and ')' characters
            representing Santa's floor movements.
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
