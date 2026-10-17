import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 1
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
    ## Day 1: Secret Entrance
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
    The Elves have good news and bad news.

    The good news is that they've discovered project management! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time. The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole! To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.

    Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

    You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:

    "Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."

    The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.

    The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

    So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0. Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0. So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.

    The dial starts by pointing at 50.

    You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

    For example, suppose the attached document contained the following rotations:

    ```
    L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82
    ```

    Following these rotations would cause the dial to move as follows:

    ```
    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32.
    Because the dial points at 0 a total of three times during this process, the password in this example is 3.
    ```

    Analyze the rotations in your attached document. What's the actual password to open the door?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_1_1_find_exact_zeros(
    rotation_data: list[str],
    start_position: int = 50,
) -> int:
    """
    Simulate safe dial rotations and count how many times the dial lands on zero.

    The dial is rotated one click at a time. It wraps around from 99 to 0 and
    from 0 to 99. The count increases each time the dial ends a rotation
    pointing at zero.

    Args:
        rotation_data (list[str]): List of rotation instructions, each starting with 'L'
            or 'R' followed by an integer number of clicks.
        start_position (int): Starting value on the dial, between 0 and 99. Defaults
            to 50.

    Returns:
        int: The number of times the dial ends a rotation pointing at zero.
    """
    current_position = start_position
    zero_counter = 0

    for rotation in rotation_data:
        step = 1 if rotation[0] == "R" else -1
        number_of_steps = int(rotation[1:])

        for _ in range(number_of_steps):
            current_position = (current_position + step) % 100

        if not current_position:
            zero_counter += 1

    return zero_counter


@app.cell
def _():
    example_rotation_data = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    solution_example_1_1 = exercise_1_1_find_exact_zeros(
        rotation_data=example_rotation_data
    )

    assert solution_example_1_1 == 3
    return (example_rotation_data,)


@app.cell
def _(exercise_1_1_find_exact_zeros, read_data):
    rotation_data = read_data(file_path="data/2025/2025_day_01.txt", separator="\n")

    solution_1_1 = exercise_1_1_find_exact_zeros(rotation_data=rotation_data)

    assert solution_1_1 == 1165
    return (rotation_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

    As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

    "Due to newer security protocols, please use password method 0x434C49434B until further notice."

    You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

    Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

    ```
    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
    ```

    In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

    Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

    Using password method 0x434C49434B, what is the password to open the door?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_1_2_count_zero_clicks(
    rotation_data: list[str],
    start_position: int = 50,
) -> int:
    """
    Count how many times the dial points at zero during the given rotations.

    The dial moves one click at a time. Each instruction starts with 'L' or 'R'
    followed by an integer indicating how many clicks to rotate. The dial wraps
    from 99 to 0 and from 0 to 99. The counter increases every time a single
    click causes the dial to land on zero.

    Args:
        rotation_data (list[str]): List of rotation instructions as strings. Each has a
            direction character ('L' or 'R') followed by an integer number of
            clicks.
        start_position (int): Starting value on the dial, between 0 and 99. Defaults
            to 50.

    Returns:
        int: The total number of times any click causes the dial to land on zero.
    """
    current_position = start_position
    zero_counter = 0

    for rotation in rotation_data:
        step = 1 if rotation[0] == "R" else -1
        number_of_steps = int(rotation[1:])

        for _ in range(number_of_steps):
            current_position = (current_position + step) % 100

            if not current_position:
                zero_counter += 1

    return zero_counter


@app.cell
def _(example_rotation_data):
    solution_example_1_2 = exercise_1_2_count_zero_clicks(
        rotation_data=example_rotation_data
    )

    assert solution_example_1_2 == 6
    return


@app.cell
def _(exercise_1_2_count_zero_clicks, rotation_data):
    solution_1_2 = exercise_1_2_count_zero_clicks(rotation_data=rotation_data)

    assert solution_1_2 == 6496
    return


if __name__ == "__main__":
    app.run()
