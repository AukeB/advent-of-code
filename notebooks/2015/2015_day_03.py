import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 3

    https://adventofcode.com/2015/day/3
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
    ## Day 3 - Perfectly Spherical Houses in a Vacuum
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_3_1_find_unique_houses(
    directional_data: str, starting_position: list[int] = [0, 0]
) -> int:
    """Count how many unique houses receive at least one present.

    Santa starts at the given starting position on an infinite 2D grid. He
    follows a sequence of movement instructions and delivers a present at each
    visited house. Houses visited multiple times are only counted once.

    Args:
        directional_data (str): A string of movement instructions. Each
            character must be one of '^', 'v', '<', or '>', representing north,
            south, west, and east respectively.
        starting_position (list[int]): The (x, y) coordinates where Santa
            starts.

    Returns:
        int: The number of unique houses that receive at least one present.
    """
    current_position = starting_position.copy()
    visited_houses = {tuple(starting_position)}
    directional_mapping = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    for move in directional_data:
        dx, dy = directional_mapping[move]

        current_position[0] += dx
        current_position[1] += dy

        visited_houses.add(tuple(current_position))

    return len(visited_houses)


@app.cell
def _(exercise_3_1_find_unique_houses, read_data):
    directional_data = read_data(file_path="data/2015/2015_day_03.txt", separator="\n")

    number_of_unique_visited_houses = exercise_3_1_find_unique_houses(
        directional_data=directional_data
    )

    assert number_of_unique_visited_houses == 2565
    return (directional_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_3_2_find_unique_houses(
    directional_data: str, starting_position: list[int] = [0, 0]
) -> int:
    """Count how many unique houses receive at least one present when Santa and
    Robo-Santa deliver presents alternately.

    Santa and Robo-Santa start at the given starting position on an infinite 2D
    grid, delivering a present at the starting house. They then take turns
    moving according to the sequence of movement instructions. Houses visited
    multiple times are only counted once.

    Args:
        directional_data (str): A string of movement instructions. Each
            character must be one of '^', 'v', '<', or '>', representing north,
            south, west, and east respectively.
        starting_position (list[int]): The (x, y) coordinates where both Santa
            and Robo-Santa start.

    Returns:
        int: The number of unique houses that receive at least one present.
    """
    santa_current_position = starting_position.copy()
    robo_santa_current_position = starting_position.copy()

    visited_houses = {tuple(starting_position)}
    directional_mapping = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    for index, move in enumerate(directional_data):
        dx, dy = directional_mapping[move]

        if index % 2 == 0:
            santa_current_position[0] += dx
            santa_current_position[1] += dy
            visited_houses.add(tuple(santa_current_position))
        else:
            robo_santa_current_position[0] += dx
            robo_santa_current_position[1] += dy
            visited_houses.add(tuple(robo_santa_current_position))

    return len(visited_houses)


@app.cell
def _(directional_data, exercise_3_2_find_unique_houses):
    santa_and_robo_santa_unique_visited_houses = exercise_3_2_find_unique_houses(
        directional_data=directional_data
    )

    assert santa_and_robo_santa_unique_visited_houses == 2639
    return


if __name__ == "__main__":
    app.run()
