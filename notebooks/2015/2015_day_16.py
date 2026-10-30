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

    from aoc.utils import read_data

    return mo, read_data


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


@app.function
def exercise_16_1_aunt_sue(
    mfcsam_results: dict[str, int], puzzle_input: list[str]
) -> int | None:
    """Find the number of the Aunt Sue whose remembered gifts match the MFCSAM
    readout.

    Each line of the puzzle input describes one Aunt Sue and up to three of her
    known properties. Sue is the match when every property listed for her has
    the same count as in the MFCSAM results. Properties not listed for Sue are
    ignored.

    Args:
        mfcsam_results: Compound counts from the MFCSAM readout, keyed by
            property name.
        puzzle_input: Lines such as "Sue 213: cars: 9, akitas: 3, goldfish: 0".

    Returns:
        The number of the first Aunt Sue whose listed properties all match.
    """
    # Parsing logic.
    all_sue_properties = {}

    for sue_data in puzzle_input:
        sue_and_number, sue_properties_str = sue_data.split(":", maxsplit=1)
        sue_number = int(sue_and_number.split(" ")[1])
        sue_items = sue_properties_str.split(",")
        sue_properties = {
            k.strip(): int(v.strip()) for x in sue_items for k, v in [x.split(":")]
        }
        all_sue_properties[sue_number] = sue_properties

    # Puzzle solving logic.
    for sue_number, sue_properties in all_sue_properties.items():
        if all(
            sue_item_count == mfcsam_results[sue_item]
            for sue_item, sue_item_count in sue_properties.items()
        ):
            return sue_number


@app.cell
def _(read_data):
    mfcsam_results = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    puzzle_input = read_data(file_path="data/2015/2015_day_16.txt", separator="\n")

    solution_16_1_sue_number = exercise_16_1_aunt_sue(
        mfcsam_results=mfcsam_results, puzzle_input=puzzle_input
    )

    assert solution_16_1_sue_number == 213
    return mfcsam_results, puzzle_input


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_16_2_aunt_sue(
    mfcsam_results: dict[str, int], puzzle_input: list[str]
) -> int | None:
    """Find the number of the Aunt Sue whose remembered gifts match the MFCSAM
    readout, with retroactive rules.

    Each line of the puzzle input describes one Aunt Sue and up to three of her
    known properties. The MFCSAM readout is a lower or upper bound for some
    properties rather than an exact count. The "cats" and "trees" counts must be
    greater than the readout, the "pomeranians" and "goldfish" counts must be
    fewer, and every other property must match exactly. Sue is the match when
    every property listed for her satisfies its rule.

    Args:
        mfcsam_results: Compound counts from the MFCSAM readout, keyed by
            property name.
        puzzle_input: Lines such as "Sue 213: cars: 9, akitas: 3, goldfish: 0".

    Returns:
        The number of the first Aunt Sue whose listed properties all satisfy
            their rules,
        or None if no Aunt Sue matches.
    """
    # Parsing logic.
    all_sue_properties = {}

    for sue_data in puzzle_input:
        sue_and_number, sue_properties_str = sue_data.split(":", maxsplit=1)
        sue_number = int(sue_and_number.split(" ")[1])
        sue_items = sue_properties_str.split(",")
        sue_properties = {
            k.strip(): int(v.strip()) for x in sue_items for k, v in [x.split(":")]
        }
        all_sue_properties[sue_number] = sue_properties

    # Puzzle solving logic.
    for sue_number, sue_properties in all_sue_properties.items():
        for sue_item, sue_item_count in sue_properties.items():
            if (
                (
                    sue_item in ("cats", "trees")
                    and sue_item_count <= mfcsam_results[sue_item]
                )
                or (
                    sue_item in ("pomeranians", "goldfish")
                    and sue_item_count >= mfcsam_results[sue_item]
                )
                or (
                    sue_item not in ("cats", "trees", "pomeranians", "goldfish")
                    and sue_item_count != mfcsam_results[sue_item]
                )
            ):
                break
        else:
            return sue_number


@app.cell
def _(mfcsam_results, puzzle_input):
    solution_16_2 = exercise_16_2_aunt_sue(
        mfcsam_results=mfcsam_results, puzzle_input=puzzle_input
    )

    assert solution_16_2 == 323
    return


if __name__ == "__main__":
    app.run()
