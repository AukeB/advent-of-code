import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 3

    https://adventofcode.com/2025/day/3
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
    ## Day 3 - Lobby
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_3_1_find_largest_joltage(
    joltage_ratings: list[str],
    num_batteries: int = 2,
) -> int:
    """Calculates the total maximum joltage that can be produced across all
    banks of batteries.

    This function processes a list of battery banks, where each bank contains
    battery joltage ratings as a string of digits. For each bank, it identifies
    the largest possible joltage that can be produced by turning on a specified
    number of batteries (default is 2). The joltage for a bank is determined by
    forming a number using the digits of the selected batteries in the order
    they appear. The function sums the maximum joltage from all banks to
    calculate the total output.

    Args:
        joltage_ratings (list[str]): A list of strings, where each string
            represents the joltage ratings of batteries in a single bank.
        num_batteries (int, optional): The number of batteries to turn on in
            each bank to maximize the joltage. Defaults to 2.

    Returns:
        int: The total maximum joltage produced across all banks.
    """
    total_joltage_over_all_banks = 0

    for bank_index, bank in enumerate(joltage_ratings):
        largest_battery_ratings = []
        largest_battery_index = -1

        for i in range(num_batteries):
            largest_battery_rating = 0

            for battery_index in range(
                len(bank) - num_batteries + i, largest_battery_index, -1
            ):
                battery_joltage_rating = int(bank[battery_index])
                if battery_joltage_rating >= largest_battery_rating:
                    largest_battery_rating = battery_joltage_rating
                    largest_battery_index = battery_index

            largest_battery_ratings.append(largest_battery_rating)

        total_per_bank = 0

        for i in range(len(largest_battery_ratings) - 1, -1, -1):
            total_per_bank += largest_battery_ratings[i] * 10 ** (
                len(largest_battery_ratings) - 1 - i
            )

        total_joltage_over_all_banks += total_per_bank

    return total_joltage_over_all_banks


@app.cell
def _():
    example_joltage_ratings = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]

    solution_example_3_1 = exercise_3_1_find_largest_joltage(
        joltage_ratings=example_joltage_ratings
    )

    assert solution_example_3_1 == 357
    return (example_joltage_ratings,)


@app.cell
def _(exercise_3_1_find_largest_joltage, read_data):
    joltage_ratings = read_data(file_path="data/2025/2025_day_03.txt", separator="\n")

    solution_3_1 = exercise_3_1_find_largest_joltage(joltage_ratings=joltage_ratings)

    assert solution_3_1 == 16842
    return (joltage_ratings,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_3_2_find_largest_joltage(
    joltage_ratings: list[str],
    num_batteries: int = 12,
) -> int:
    """Calculates the total maximum joltage that can be produced across all
    banks of batteries using a larger number of batteries.

    This function processes a list of battery banks, where each bank contains
    battery joltage ratings as a string of digits. For each bank, it identifies
    the largest possible joltage that can be produced by turning on a specified
    number of batteries (default is 12). The joltage for a bank is determined by
    forming a number using the digits of the selected batteries in the order
    they appear. The function sums the maximum joltage from all banks to
    calculate the total output.

    Args:
        joltage_ratings (list[str]): A list of strings, where each string
            represents the joltage ratings of batteries in a single bank.
        num_batteries (int, optional): The number of batteries to turn on in
            each bank to maximize the joltage. Defaults to 12.

    Returns:
        int: The total maximum joltage produced across all banks using the
            specified number of batteries.
    """
    total_joltage_over_all_banks = 0

    for bank_index, bank in enumerate(joltage_ratings):
        largest_battery_ratings = []
        largest_battery_index = -1

        for i in range(num_batteries):
            largest_battery_rating = 0

            for battery_index in range(
                len(bank) - num_batteries + i, largest_battery_index, -1
            ):
                battery_joltage_rating = int(bank[battery_index])
                if battery_joltage_rating >= largest_battery_rating:
                    largest_battery_rating = battery_joltage_rating
                    largest_battery_index = battery_index

            largest_battery_ratings.append(largest_battery_rating)

        total_per_bank = 0

        for i in range(len(largest_battery_ratings) - 1, -1, -1):
            total_per_bank += largest_battery_ratings[i] * 10 ** (
                len(largest_battery_ratings) - 1 - i
            )

        total_joltage_over_all_banks += total_per_bank

    return total_joltage_over_all_banks


@app.cell
def _(example_joltage_ratings):
    solution_example_3_2 = exercise_3_2_find_largest_joltage(
        joltage_ratings=example_joltage_ratings
    )

    assert solution_example_3_2 == 3121910778619
    return


@app.cell
def _(exercise_3_2_find_largest_joltage, joltage_ratings):
    solution_3_2 = exercise_3_2_find_largest_joltage(joltage_ratings=joltage_ratings)

    assert solution_3_2 == 167523425665348
    return


if __name__ == "__main__":
    app.run()
