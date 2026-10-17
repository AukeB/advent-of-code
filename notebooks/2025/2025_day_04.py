import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 4
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
    ## Day 4 - Printing Department
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
    You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

    Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

    "Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

    If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

    The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

    For example:

    ```
    ..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.
    ```

    The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

    In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

    ```
    ..xx.xx@x.
    x@@.@.@.@@
    @@@@@.x.@@
    @.@@@@..@.
    x@.@@@@.@x
    .@@@@@@@.@
    .@.@.@.@@@
    x.@@@.@@@@
    .@@@@@@@@.
    x.x.@@@.x.
    ```

    Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_4_1_find_accessible_paper_rolls(
    paper_roll_data: list[str], max_neighbours: int = 3
) -> int:
    """
    Determines the number of paper rolls that can be accessed by forklifts.

    The function evaluates each paper roll in a grid (provided as input) to check
    if it has fewer than or equal to a specified number of adjacent paper rolls.
    Forklifts can access a roll of paper if there are fewer than `max_neighbours`
    paper rolls in the eight adjacent positions.

    Args:
        paper_roll_data (list[str]): A list of strings representing the grid of paper rolls.
            Each string corresponds to a row in the grid, where '@' represents a paper roll
            and '.' represents an empty space.
        max_neighbours (int): The maximum number of allowable adjacent paper rolls for a forklift
            to access a roll. Defaults to 3.

    Returns:
        int: The count of paper rolls that can be accessed by forklifts.
    """
    paper_roll_matrix = []

    for paper_roll_row in paper_roll_data:
        paper_roll_row_list: list[str] = []

        for element in paper_roll_row:
            paper_roll_row_list.append(element)

        paper_roll_matrix.append(paper_roll_row_list)

    paper_roll_count = 0

    for i in range(len(paper_roll_matrix)):
        for j in range(len(paper_roll_matrix[i])):
            if paper_roll_matrix[i][j] == "@":
                num_neighbours = 0

                all_neighbour_coordinates = [
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j - 1),
                    (i, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j),
                    (i + 1, j + 1),
                ]

                for neighbour_coordinates in all_neighbour_coordinates:
                    if (
                        neighbour_coordinates[0] >= 0
                        and neighbour_coordinates[0] < len(paper_roll_matrix)
                        and neighbour_coordinates[1] >= 0
                        and neighbour_coordinates[1] < len(paper_roll_matrix[i])
                    ):
                        if (
                            paper_roll_matrix[neighbour_coordinates[0]][
                                neighbour_coordinates[1]
                            ]
                            == "@"
                        ):
                            num_neighbours += 1

                if num_neighbours <= max_neighbours:
                    paper_roll_count += 1

    return paper_roll_count


@app.cell
def _():
    example_paper_roll_data = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]

    solution_example_4_1 = exercise_4_1_find_accessible_paper_rolls(
        paper_roll_data=example_paper_roll_data
    )

    assert solution_example_4_1 == 13
    return (example_paper_roll_data,)


@app.cell
def _(exercise_4_1_find_accessible_paper_rolls, read_data):
    paper_roll_data = read_data(file_path="data/2025/2025_day_04.txt", separator="\n")

    solution_4_1 = exercise_4_1_find_accessible_paper_rolls(
        paper_roll_data=paper_roll_data
    )

    assert solution_4_1 == 1602
    return (paper_roll_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, the Elves just need help accessing as much of the paper as they can.

    Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

    Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

    ```
    Initial state:
    ..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.

    Remove 13 rolls of paper:
    ..xx.xx@x.
    x@@.@.@.@@
    @@@@@.x.@@
    @.@@@@..@.
    x@.@@@@.@x
    .@@@@@@@.@
    .@.@.@.@@@
    x.@@@.@@@@
    .@@@@@@@@.
    x.x.@@@.x.

    Remove 12 rolls of paper:
    .......x..
    .@@.x.x.@x
    x@@@@...@@
    x.@@@@..x.
    .@.@@@@.x.
    .x@@@@@@.x
    .x.@.@.@@@
    ..@@@.@@@@
    .x@@@@@@@.
    ....@@@...

    Remove 7 rolls of paper:
    ..........
    .x@.....x.
    .@@@@...xx
    ..@@@@....
    .x.@@@@...
    ..@@@@@@..
    ...@.@.@@x
    ..@@@.@@@@
    ..x@@@@@@.
    ....@@@...

    Remove 5 rolls of paper:
    ..........
    ..x.......
    .x@@@.....
    ..@@@@....
    ...@@@@...
    ..x@@@@@..
    ...@.@.@@.
    ..x@@.@@@x
    ...@@@@@@.
    ....@@@...

    Remove 2 rolls of paper:
    ..........
    ..........
    ..x@@.....
    ..@@@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@x.
    ....@@@...

    Remove 1 roll of paper:
    ..........
    ..........
    ...@@.....
    ..x@@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@..
    ....@@@...

    Remove 1 roll of paper:
    ..........
    ..........
    ...x@.....
    ...@@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@..
    ....@@@...

    Remove 1 roll of paper:
    ..........
    ..........
    ....x.....
    ...@@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@..
    ....@@@...

    Remove 1 roll of paper:
    ..........
    ..........
    ..........
    ...x@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@..
    ....@@@...
    ```

    Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

    Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_4_2_iteratively_remove_paper_rolls(
    paper_roll_data: list[str], max_neighbours: int = 3
) -> int:
    """
    Determines the total number of paper rolls that can be iteratively removed by forklifts.

    Forklifts can remove a roll of paper if there are fewer than or equal to `max_neighbours`
    rolls of paper in the eight adjacent positions. Removing a roll may make other rolls accessible,
    and the process continues until no more rolls can be removed.

    Args:
        paper_roll_data (list[str]): A list of strings representing the grid of paper rolls.
            Each string corresponds to a row in the grid, where '@' represents a paper roll
            and '.' represents an empty space.
        max_neighbours (int): The maximum number of allowable adjacent paper rolls for a forklift
            to access and remove a roll. Defaults to 3.

    Returns:
        int: The total number of paper rolls removed.
    """
    paper_roll_matrix = []

    for paper_roll_row in paper_roll_data:
        paper_roll_row_list: list[str] = []

        for element in paper_roll_row:
            paper_roll_row_list.append(element)

        paper_roll_matrix.append(paper_roll_row_list)

    total_paper_roll_count = 0
    iterate = True

    while iterate:
        new_matrix = []
        paper_roll_count = 0

        for i in range(len(paper_roll_matrix)):
            new_row = []

            for j in range(len(paper_roll_matrix[i])):
                if paper_roll_matrix[i][j] == "@":
                    num_neighbours = 0

                    all_neighbour_coordinates = [
                        (i - 1, j - 1),
                        (i - 1, j),
                        (i - 1, j + 1),
                        (i, j - 1),
                        (i, j + 1),
                        (i + 1, j - 1),
                        (i + 1, j),
                        (i + 1, j + 1),
                    ]

                    for neighbour_coordinates in all_neighbour_coordinates:
                        if (
                            neighbour_coordinates[0] >= 0
                            and neighbour_coordinates[0] < len(paper_roll_matrix)
                            and neighbour_coordinates[1] >= 0
                            and neighbour_coordinates[1] < len(paper_roll_matrix[i])
                        ):
                            if (
                                paper_roll_matrix[neighbour_coordinates[0]][
                                    neighbour_coordinates[1]
                                ]
                                == "@"
                            ):
                                num_neighbours += 1

                    if num_neighbours <= max_neighbours:
                        paper_roll_count += 1
                        new_row.append(".")
                    else:
                        new_row.append("@")
                else:
                    new_row.append(".")

            new_matrix.append(new_row)

        if paper_roll_count > 0:
            total_paper_roll_count += paper_roll_count
            paper_roll_matrix = new_matrix.copy()
        elif paper_roll_count == 0:
            iterate = False

    return total_paper_roll_count


@app.cell
def _(example_paper_roll_data):
    solution_example_4_2 = exercise_4_2_iteratively_remove_paper_rolls(
        paper_roll_data=example_paper_roll_data
    )

    assert solution_example_4_2 == 43
    return


@app.cell
def _(exercise_4_2_iteratively_remove_paper_rolls, paper_roll_data):
    solution_4_2 = exercise_4_2_iteratively_remove_paper_rolls(
        paper_roll_data=paper_roll_data
    )

    assert solution_4_2 == 9518
    return


if __name__ == "__main__":
    app.run()
