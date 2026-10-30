import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2026 - Day 3

    https://adventofcode.com/2026/day/3
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
    ## Day 3
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
    def exercise_03_1(puzzle_input: list[str]) -> None: ...

    return (exercise_03_1,)


@app.cell
def _(exercise_03_1, read_data):
    puzzle_input: list[str] = read_data(
        file_path="data/2026/2026_day_03.txt", separator="\n"
    )

    solution_03_1 = exercise_03_1(puzzle_input=puzzle_input)

    assert solution_03_1 is None

    return (puzzle_input,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _():
    def exercise_03_2(puzzle_input: list[str]) -> None: ...

    return (exercise_03_2,)


@app.cell
def _(exercise_03_2, puzzle_input):
    solution_03_2 = exercise_03_2(puzzle_input=puzzle_input)

    assert solution_03_2 is None
    return


if __name__ == "__main__":
    app.run()
