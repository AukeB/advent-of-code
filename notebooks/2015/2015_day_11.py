import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 11
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
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Santa's previous password expired, and he needs help choosing a new one.

    To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

    Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

    - Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    - Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    - Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

    For example:

    ```
    - hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
    - abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
    - abbcegjk fails the third requirement, because it only has one double letter (bb).
    - The next password after abcdefgh is abcdffaa.
    - The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
    ```

    Given Santa's current password (your puzzle input), what should his next password be?

    Your puzzle input is `cqjxjnds`.
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


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
