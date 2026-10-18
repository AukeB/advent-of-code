import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 4

    https://adventofcode.com/2025/day/4
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
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_4_1_find_accessible_paper_rolls(
    paper_roll_data: list[str], max_neighbours: int = 3
) -> int:
    """Determines the number of paper rolls that can be accessed by forklifts.

    The function evaluates each paper roll in a grid (provided as input) to
    check if it has fewer than or equal to a specified number of adjacent paper
    rolls. Forklifts can access a roll of paper if there are fewer than
    `max_neighbours` paper rolls in the eight adjacent positions.

    Args:
        paper_roll_data (list[str]): A list of strings representing the grid of
            paper rolls. Each string corresponds to a row in the grid, where '@'
            represents a paper roll and '.' represents an empty space.
        max_neighbours (int): The maximum number of allowable adjacent paper
            rolls for a forklift to access a roll. Defaults to 3.

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
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_4_2_iteratively_remove_paper_rolls(
    paper_roll_data: list[str], max_neighbours: int = 3
) -> int:
    """Determines the total number of paper rolls that can be iteratively
    removed by forklifts.

    Forklifts can remove a roll of paper if there are fewer than or equal to
    `max_neighbours` rolls of paper in the eight adjacent positions. Removing a
    roll may make other rolls accessible, and the process continues until no
    more rolls can be removed.

    Args:
        paper_roll_data (list[str]): A list of strings representing the grid of
            paper rolls. Each string corresponds to a row in the grid, where '@'
            represents a paper roll and '.' represents an empty space.
        max_neighbours (int): The maximum number of allowable adjacent paper
            rolls for a forklift to access and remove a roll. Defaults to 3.

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
