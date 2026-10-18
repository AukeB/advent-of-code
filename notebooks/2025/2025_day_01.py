import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 1

    https://adventofcode.com/2025/day/1
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
    ## Day 1: Secret Entrance
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_1_1_find_exact_zeros(
    rotation_data: list[str],
    start_position: int = 50,
) -> int:
    """Simulate safe dial rotations and count how many times the dial lands on
    zero.

    The dial is rotated one click at a time. It wraps around from 99 to 0 and
    from 0 to 99. The count increases each time the dial ends a rotation
    pointing at zero.

    Args:
        rotation_data (list[str]): List of rotation instructions, each starting
            with 'L' or 'R' followed by an integer number of clicks.
        start_position (int): Starting value on the dial, between 0 and 99.
            Defaults to 50.

    Returns:
        int: The number of times the dial ends a rotation pointing at zero.
    """
    current_position = start_position
    zero_counter = 0

    for rotation in rotation_data:
        step = 1 if rotation[0] == "R" else -1
        number_of_steps = int(rotation[1:])

        for _ in range(number_of_steps):
            current_position = (current_position + step) % 100

        if not current_position:
            zero_counter += 1

    return zero_counter


@app.cell
def _():
    example_rotation_data = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    solution_example_1_1 = exercise_1_1_find_exact_zeros(
        rotation_data=example_rotation_data
    )

    assert solution_example_1_1 == 3
    return (example_rotation_data,)


@app.cell
def _(exercise_1_1_find_exact_zeros, read_data):
    rotation_data = read_data(file_path="data/2025/2025_day_01.txt", separator="\n")

    solution_1_1 = exercise_1_1_find_exact_zeros(rotation_data=rotation_data)

    assert solution_1_1 == 1165
    return (rotation_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_1_2_count_zero_clicks(
    rotation_data: list[str],
    start_position: int = 50,
) -> int:
    """Count how many times the dial points at zero during the given rotations.

    The dial moves one click at a time. Each instruction starts with 'L' or 'R'
    followed by an integer indicating how many clicks to rotate. The dial wraps
    from 99 to 0 and from 0 to 99. The counter increases every time a single
    click causes the dial to land on zero.

    Args:
        rotation_data (list[str]): List of rotation instructions as strings.
            Each has a direction character ('L' or 'R') followed by an integer
            number of clicks.
        start_position (int): Starting value on the dial, between 0 and 99.
            Defaults to 50.

    Returns:
        int: The total number of times any click causes the dial to land on
            zero.
    """
    current_position = start_position
    zero_counter = 0

    for rotation in rotation_data:
        step = 1 if rotation[0] == "R" else -1
        number_of_steps = int(rotation[1:])

        for _ in range(number_of_steps):
            current_position = (current_position + step) % 100

            if not current_position:
                zero_counter += 1

    return zero_counter


@app.cell
def _(example_rotation_data):
    solution_example_1_2 = exercise_1_2_count_zero_clicks(
        rotation_data=example_rotation_data
    )

    assert solution_example_1_2 == 6
    return


@app.cell
def _(exercise_1_2_count_zero_clicks, rotation_data):
    solution_1_2 = exercise_1_2_count_zero_clicks(rotation_data=rotation_data)

    assert solution_1_2 == 6496
    return


if __name__ == "__main__":
    app.run()
