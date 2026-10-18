import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 6

    https://adventofcode.com/2015/day/6
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
    import numpy as np

    from collections import namedtuple

    from aoc.utils import read_data

    return mo, namedtuple, np, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 6: Probably a Fire Hazard
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(namedtuple):
    Point = namedtuple("Point", ["x", "y"])
    return (Point,)


@app.cell
def _(Point, np):
    def exercise_6_1_find_number_of_lit_lights(
        instruction_data: list[str],
    ) -> int:
        """Count how many lights are lit in a 1000x1000 grid after following
        Santa's instructions.

        Each instruction either turns on, turns off, or toggles a rectangular
        region of lights defined by two corner coordinates. The grid starts with
        all lights off and is updated for each instruction using NumPy array
        slicing.

        Args:
            instruction_data (list[str]): A list of instructions, each
                describing an action and two corner coordinates of a rectangle.

        Returns:
            int: The total number of lights that are lit after all instructions
                have been applied.
        """
        grid_size: int = 1000
        grid_of_lights = np.zeros((grid_size, grid_size), dtype=int)

        for instruction in instruction_data:
            instruction = instruction.split(" ")

            # Determine action based on instruction length.
            if len(instruction) == 4:
                action = instruction[0]
            elif len(instruction) == 5:
                action = "_".join(instruction[:2])
            else:
                raise ValueError(f"Unexpected instruction: {instruction}")

            # Determine coordinates backwards.
            c1 = Point(*[int(x) for x in instruction[-1].split(",")])
            c2 = Point(*[int(x) for x in instruction[-3].split(",")])

            # Apply actions to the grid of lights.
            rectangle = (
                slice(min(c1.x, c2.x), max(c1.x, c2.x) + 1),
                slice(min(c1.y, c2.y), max(c1.y, c2.y) + 1),
            )

            if action == "turn_on":
                grid_of_lights[rectangle] = 1
            elif action == "turn_off":
                grid_of_lights[rectangle] = 0
            elif action == "toggle":
                grid_of_lights[rectangle] ^= 1

        number_of_lit_lights = int(grid_of_lights.sum())

        return number_of_lit_lights

    return (exercise_6_1_find_number_of_lit_lights,)


@app.cell
def _(exercise_6_1_find_number_of_lit_lights, read_data):
    instruction_data: list[str] = read_data(
        file_path="data/2015/2015_day_06.txt", separator="\n"
    )

    number_of_lit_lights_6_1 = exercise_6_1_find_number_of_lit_lights(
        instruction_data=instruction_data
    )

    assert number_of_lit_lights_6_1 == 377891
    return (instruction_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(Point, np):
    def exercise_6_2_find_number_of_lit_lights(
        instruction_data: list[str],
    ) -> int:
        """Calculate the total brightness of all lights in a 1000x1000 grid
        after following Santa's updated brightness instructions.

        Each instruction adjusts the brightness of a rectangular region of
        lights defined by two corner coordinates. The grid starts with all
        lights at zero brightness and is updated for each instruction using
        NumPy array slicing.

        The brightness rules are as follows:
        - "turn on" increases the brightness of each light in the rectangle by
          1.
        - "turn off" decreases the brightness of each light by 1, with a minimum
          of 0.
        - "toggle" increases the brightness of each light in the rectangle by 2.

        Args:
            instruction_data (list[str]): A list of instructions, each
                describing an action and two corner coordinates of a rectangle.

        Returns:
            int: The total brightness of all lights after all instructions have
                been applied.
        """
        grid_size: int = 1000
        grid_of_lights = np.zeros((grid_size, grid_size), dtype=int)

        for instruction in instruction_data:
            instruction = instruction.split(" ")

            # Determine action based on instruction length.
            if len(instruction) == 4:
                action = instruction[0]
            elif len(instruction) == 5:
                action = "_".join(instruction[:2])
            else:
                raise ValueError(f"Unexpected instruction: {instruction}")

            # Determine coordinates backwards.
            c1 = Point(*[int(x) for x in instruction[-1].split(",")])
            c2 = Point(*[int(x) for x in instruction[-3].split(",")])

            # Apply actions to the grid of lights.
            rectangle = (
                slice(min(c1.x, c2.x), max(c1.x, c2.x) + 1),
                slice(min(c1.y, c2.y), max(c1.y, c2.y) + 1),
            )

            if action == "turn_on":
                grid_of_lights[rectangle] += 1
            elif action == "turn_off":
                grid_of_lights[rectangle] = np.maximum(grid_of_lights[rectangle] - 1, 0)
            elif action == "toggle":
                grid_of_lights[rectangle] += 2

        number_of_lit_lights = int(grid_of_lights.sum())

        return number_of_lit_lights

    return (exercise_6_2_find_number_of_lit_lights,)


@app.cell
def _(exercise_6_2_find_number_of_lit_lights, instruction_data: list[str]):
    number_of_lit_lights_6_2 = exercise_6_2_find_number_of_lit_lights(
        instruction_data=instruction_data
    )

    assert number_of_lit_lights_6_2 == 14110788
    return


if __name__ == "__main__":
    app.run()
