import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 2

    https://adventofcode.com/2015/day/2
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
    ## Day 2 - I Was Told There Would Be No Math
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_2_1_find_total_square_feet_wrapping_paper(
    present_dimensions: list[str],
) -> int:
    """Calculate total wrapping paper needed for a list of box dimensions.

    Each dimension string is formatted as "LxWxH". For every present, the
    required paper equals its surface area plus the area of its smallest side.
    Surface area is computed as 2*l*w + 2*w*h + 2*h*l.

    Args:
        present_dimensions (list[str]): List of box dimensions.

    Returns:
        int: Total square feet of wrapping paper needed.
    """
    total_square_feet = 0

    for present_dim in present_dimensions:
        length, width, height = [int(dim) for dim in present_dim.split("x")]
        smallest_side_area = min(length * width, width * height, height * length)
        total_square_feet += (
            2 * length * width
            + 2 * width * height
            + 2 * height * length
            + smallest_side_area
        )

    return total_square_feet


@app.cell
def _(exercise_2_1_find_total_square_feet_wrapping_paper, read_data):
    present_dimensions = read_data(
        file_path="data/2015/2015_day_02.txt", separator="\n"
    )

    total_square_feet = exercise_2_1_find_total_square_feet_wrapping_paper(
        present_dimensions=present_dimensions
    )

    assert total_square_feet == 1588178
    return (present_dimensions,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_2_2_find_total_feet_of_ribbon(present_dimensions: list[str]) -> int:
    """Calculate total ribbon needed for a list of box dimensions.

    Each dimension string is formatted as "LxWxH". Ribbon needed equals the
    smallest perimeter of any face plus the volume of the box for the bow.

    Args:
        present_dimensions (list[str]): List of box dimensions.

    Returns:
        int: Total feet of ribbon required.
    """
    total_feet_of_ribbon = 0

    for present_dim in present_dimensions:
        length, width, height = [int(dim) for dim in present_dim.split("x")]
        smallest_perimeter = 2 * (
            (length + width + height) - max(length, width, height)
        )
        volume = length * width * height
        total_feet_of_ribbon += smallest_perimeter + volume

    return total_feet_of_ribbon


@app.cell
def _(exercise_2_2_find_total_feet_of_ribbon, present_dimensions):
    total_feet_of_ribbon = exercise_2_2_find_total_feet_of_ribbon(
        present_dimensions=present_dimensions
    )

    assert total_feet_of_ribbon == 3783758
    return


if __name__ == "__main__":
    app.run()
