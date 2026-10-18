import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 4

    https://adventofcode.com/2015/day/4
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
    ## Day 4 - The Ideal Stocking Suffer
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_4_find_lowest_number(secret_key: str, number_of_leading_zeros: int) -> int:
    """Find the lowest positive number that produces an MD5 hash with a
    specified number of leading zeroes when appended to the secret key.

    The MD5 hash is computed for the concatenation of the secret key and
    successive positive integers (starting at 0) until a hash is found that
    starts with the specified number of zeroes.

    Args:
        secret_key (str): The secret key string to use as the base of the hash.
        number_of_leading_zeros (int): The required number of leading zeroes in
            the hash. Default is 5.

    Returns:
        int: The lowest positive integer that, when appended to the secret key,
            produces an MD5 hash starting with the specified number of zeroes.
    """
    from hashlib import md5

    hash_prefix = "0" * number_of_leading_zeros
    number = 0

    while True:
        hash_input = secret_key + str(number)
        md5_hash = md5(hash_input.encode()).hexdigest()

        if md5_hash.startswith(hash_prefix):
            return number

        number += 1


@app.cell
def _(exercise_4_find_lowest_number, read_data):
    secret_key = read_data(file_path="data/2015/2015_day_04.txt", separator="\n")

    lowest_integer_to_mine_advent_coins = exercise_4_find_lowest_number(
        secret_key=secret_key, number_of_leading_zeros=5
    )

    assert lowest_integer_to_mine_advent_coins == 346386
    return (secret_key,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(exercise_4_find_lowest_number, secret_key):
    lowest_integer_to_mine_advent_coins_part_2 = exercise_4_find_lowest_number(
        secret_key=secret_key, number_of_leading_zeros=6
    )

    assert lowest_integer_to_mine_advent_coins_part_2 == 9958218
    return


if __name__ == "__main__":
    app.run()
