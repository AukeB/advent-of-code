import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 2
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
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

    Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

    For example:

    - A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    - A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

    All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
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
    """
    Calculate total wrapping paper needed for a list of box dimensions.

    Each dimension string is formatted as "LxWxH". For every present, the
    required paper equals its surface area plus the area of its smallest
    side. Surface area is computed as 2*l*w + 2*w*h + 2*h*l.

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
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

    For example:

    - A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    - A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

    How many total feet of ribbon should they order?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_2_2_find_total_feet_of_ribbon(present_dimensions: list[str]) -> int:
    """
    Calculate total ribbon needed for a list of box dimensions.

    Each dimension string is formatted as "LxWxH". Ribbon needed equals
    the smallest perimeter of any face plus the volume of the box for
    the bow.

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
