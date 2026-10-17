import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 5
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
    ## Day 5 - Cafetaria
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
    As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

    You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

    "If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

    The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

    The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

    ```
    3-5
    10-14
    16-20
    12-18
    ```

    ```
    1
    5
    8
    11
    17
    32
    ```

    The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

    The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

    - Ingredient ID 1 is spoiled because it does not fall into any range.
    - Ingredient ID 5 is fresh because it falls into range 3-5.
    - Ingredient ID 8 is spoiled.
    - Ingredient ID 11 is fresh because it falls into range 10-14.
    - Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
    - Ingredient ID 32 is spoiled.

    So, in this example, 3 of the available ingredient IDs are fresh.

    Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_5_1_identify_fresh_ingredients(
    ingredient_data: list[str],
) -> int:
    """
    Count how many available ingredient IDs are within any fresh ID range.

    The input consists of lines describing inclusive fresh ingredient ID ranges
    (each formatted as two integers separated by a hyphen, e.g. ``"3-5"``),
    followed by a blank line, and then lines containing individual ingredient
    IDs. An ingredient ID is considered fresh if it falls within at least one
    of the provided ranges.

    Args:
        ingredient_data (list[str]): The raw lines from the inventory database.
            These should include fresh ID ranges (two integers separated by a
            hyphen), a blank separator line, and available ingredient IDs.

    Returns:
        int: The number of available ingredient IDs that fall within any
            fresh ID range.
    """
    ingredient_id_ranges = []
    available_ingredient_ids = []

    for ingredient_data_row in ingredient_data:
        ingredient_data_row = ingredient_data_row.strip()

        if "-" in ingredient_data_row:
            separated_ids = ingredient_data_row.split("-")
            first_id = int(separated_ids[0])
            last_id = int(separated_ids[1])
            ingredient_id_ranges.append((first_id, last_id))
        elif ingredient_data_row == "":
            pass
        else:
            available_ingredient_ids.append(int(ingredient_data_row))

    counter = 0

    for ingredient_id in available_ingredient_ids:
        for lb, ub in ingredient_id_ranges:
            if ingredient_id >= lb and ingredient_id <= ub:
                counter += 1
                break

    return counter


@app.cell
def _():
    example_ingredient_data = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]

    solution_example_5_1 = exercise_5_1_identify_fresh_ingredients(
        ingredient_data=example_ingredient_data
    )

    assert solution_example_5_1 == 3
    return (example_ingredient_data,)


@app.cell
def _(exercise_5_1_identify_fresh_ingredients, read_data):
    ingredient_data = read_data(file_path="data/2025/2025_day_05.txt", separator="\n")

    solution_5_1 = exercise_5_1_identify_fresh_ingredients(
        ingredient_data=ingredient_data
    )

    assert solution_5_1 == 694
    return (ingredient_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

    So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

    Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

    ```
    3-5
    10-14
    16-20
    12-18
    ```

    The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

    Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_5_2_find_total_number_of_fresh_ingredients(
    ingredient_data: list[str],
) -> int:
    """
    Calculate the total number of distinct fresh ingredient IDs from a list of ranges.

    This function processes a list of ingredient ID ranges (ignoring individual
    available ingredient IDs) and counts how many unique IDs are considered fresh.
    The key challenge is that ranges can overlap, so a naive count could
    double-count IDs. To handle this, the function iteratively breaks ranges
    into subranges and resolves overlaps until all ranges are non-overlapping.

    High-level approach:
        1. Parse the input to extract all ingredient ID ranges as (start, end) tuples.
        2. Maintain a list of "non-overlapping" ranges and iteratively process each
           initial range against this list:
              - If a range overlaps with existing ranges, split it into subranges
                to isolate the non-overlapping portions.
              - If a range is entirely contained in an existing range, it is ignored.
        3. Repeat this process until no further changes occur, i.e., until the
           set of ranges reaches a stable state (a fixpoint).
        4. Sum the lengths of all non-overlapping ranges to get the total count
           of unique fresh ingredient IDs.

    Args:
        ingredient_data (list[str]): A list of strings representing the ingredient
            database. Each string is either a fresh ID range formatted as
            two integers separated by a hyphen (e.g., "3-5") or a blank line
            separating sections. Individual ingredient IDs are ignored.

    Returns:
        int: The total number of distinct ingredient IDs that are considered
            fresh according to the provided ranges.
    """
    intial_ingredient_id_ranges = []
    non_overlapping_ingredient_id_ranges = []

    for ingredient_data_row in ingredient_data:
        ingredient_data_row = ingredient_data_row.strip()

        if "-" in ingredient_data_row:
            separated_ids = ingredient_data_row.split("-")
            first_id = int(separated_ids[0])
            last_id = int(separated_ids[1])
            intial_ingredient_id_ranges.append((first_id, last_id))
        else:
            pass

    iterate = True

    while iterate:
        for first_id, last_id in intial_ingredient_id_ranges:
            updated_range = []
            entirely_covered = False

            for lb, ub in non_overlapping_ingredient_id_ranges:
                if first_id < lb:
                    if last_id < lb:
                        pass
                    elif last_id >= lb and last_id <= ub:
                        updated_range.append((first_id, lb - 1))
                        break
                    elif last_id > ub:
                        updated_range.append((first_id, lb - 1))
                        updated_range.append((ub + 1, last_id))
                        break
                elif first_id >= lb and first_id <= ub:
                    if last_id <= ub:
                        entirely_covered = True
                    elif last_id > ub:
                        updated_range.append((ub + 1, last_id))
                        break
                elif first_id > ub:
                    pass

            if not updated_range and not entirely_covered:
                updated_range.append((first_id, last_id))

            if updated_range:
                for first_id, last_id in updated_range:
                    if (first_id, last_id) not in non_overlapping_ingredient_id_ranges:
                        non_overlapping_ingredient_id_ranges.append((first_id, last_id))

        if sorted(intial_ingredient_id_ranges) == sorted(
            non_overlapping_ingredient_id_ranges
        ):
            iterate = False
        else:
            intial_ingredient_id_ranges = non_overlapping_ingredient_id_ranges.copy()
            non_overlapping_ingredient_id_ranges = []

    counter = 0

    for first_id, last_id in non_overlapping_ingredient_id_ranges:
        counter += len(range(first_id, last_id)) + 1

    return counter


@app.cell
def _(example_ingredient_data):
    solution_example_5_2 = exercise_5_2_find_total_number_of_fresh_ingredients(
        ingredient_data=example_ingredient_data
    )

    assert solution_example_5_2 == 14
    return


@app.cell
def _(exercise_5_2_find_total_number_of_fresh_ingredients, ingredient_data):
    solution_5_2 = exercise_5_2_find_total_number_of_fresh_ingredients(
        ingredient_data=ingredient_data
    )

    assert solution_5_2 == 352716206375547
    return


if __name__ == "__main__":
    app.run()
