import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 3
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
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

    "Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."
    |
    You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

    "But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

    There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:

    ```
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    ```

    The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

    You'll need to find the largest possible joltage each bank can produce. In the above example:

    - In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
    - In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
    - In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    - In 818181911112111, the largest joltage you can produce is 92.

    The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

    There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?
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
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

    Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

    The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

    Consider again the example from before:

    ```
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    ```

    Now, the joltages are much larger:

    - In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    - In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    - In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    - In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.

    The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

    What is the new total output joltage?
    """)
    return


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
