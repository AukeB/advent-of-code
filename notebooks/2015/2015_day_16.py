import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 16

    https://adventofcode.com/2015/day/16
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

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 16 - Aunt Sue
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


app._unparsable_cell(
    r"""
    def exercise_16_1_aunt_sue(
        puzzle_input: list[str]
    ) -> None:
        ...
    """,
    name="_",
)


app._unparsable_cell(
    r"""
    puzzle_input = read_data(file_path="data/2015/2015_day_16.txt", separator="\n")

    solution_16_1 = exercise_16_1_aunt_sue(puzzle_input=puzzle_input)

    assert solution_16_1 is None
    """,
    name="_",
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


app._unparsable_cell(
    r"""
    def exercise_16_2_aunt_sue(
        puzzle_input: list[str]
    ) -> None:
        ...
    """,
    name="_",
)


app._unparsable_cell(
    r"""
    solution_16_2 = exercise_16_2_aunt_sue(puzzle_input=puzzle_input)

    assert solution_16_2 is None
    """,
    name="_",
)


if __name__ == "__main__":
    app.run()
