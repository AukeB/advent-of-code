import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code {year} - Day {day}
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
    ## Day {day} - {day_description}
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
    def exercise_{day}_1_{description}(
        puzzle_input: list[str]
    ) -> None:
        ...
    """,
    name="_"
)


@app.cell
def _(read_data):
    puzzle_input = read_data(file_path="data/{year}/{year}_day_{day}.txt", separator="\n")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


app._unparsable_cell(
    r"""
    def exercise_{day}_2_{description}(
        puzzle_input: list[str]
    ) -> None:
        ...
    """,
    name="_"
)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
