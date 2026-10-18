import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 11

    https://adventofcode.com/2015/day/11
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
    ## Day 11: Corporate Policy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_11_1_find_next_password(input_password: str) -> None:
    """ """
    num_iter = 50

    next_password = input_password

    for _ in range(num_iter):
        print(next_password)
        final_character = next_password[-1]

        if final_character == "z":
            new_password = []
            z_detected = False

            for character in next_password[::-1]:
                if character == "z":
                    z_detected = True
                    new_password.insert(0, "a")
                else:
                    if z_detected:
                        new_password.insert(0, chr(ord(character) + 1))
                        z_detected = False
                    else:
                        new_password.insert(0, character)

            next_password = "".join(new_password)
        else:
            next_password = next_password[0:-1] + chr(ord(next_password[-1]) + 1)


@app.cell
def _():
    input_password = "cqjxjzzs"

    next_password = exercise_11_1_find_next_password(input_password=input_password)

    # Unsolved: the solver does not return a password yet, so this is None.
    assert next_password is None
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
