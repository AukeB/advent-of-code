import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 7
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

    from collections import defaultdict

    from aoc.utils import read_data

    return defaultdict, mo, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 7 - Laboratories
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
    You thank the cephalopods for the help and exit the trash compactor, finding yourself in the familiar halls of a North Pole research wing.

    Based on the large sign that says "teleporter hub", they seem to be researching teleportation; you can't help but try it for yourself and step onto the large yellow teleporter pad.

    Suddenly, you find yourself in an unfamiliar room! The room has no doors; the only way out is the teleporter. Unfortunately, the teleporter seems to be leaking magic smoke.

    Since this is a teleporter lab, there are lots of spare parts, manuals, and diagnostic equipment lying around. After connecting one of the diagnostic tools, it helpfully displays error code 0H-N0, which apparently means that there's an issue with one of the tachyon manifolds.

    You quickly locate a diagram of the tachyon manifold (your puzzle input). A tachyon beam enters the manifold at the location marked S; tachyon beams always move downward. Tachyon beams pass freely through empty space (.). However, if a tachyon beam encounters a splitter (^), the beam is stopped; instead, a new tachyon beam continues from the immediate left and from the immediate right of the splitter.

    For example:

    ```
    .......S.......
    ...............
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    In this example, the incoming tachyon beam (|) extends downward from S until it reaches the first splitter:

    ```
    .......S.......
    .......|.......
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    At that point, the original beam stops, and two new beams are emitted from the splitter:

    ```
    .......S.......
    .......|.......
    ......|^|......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    Those beams continue downward until they reach more splitters:

    ```
    .......S.......
    .......|.......
    ......|^|......
    ......|.|......
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    At this point, the two splitters create a total of only three tachyon beams, since they are both dumping tachyons into the same place between them:

    ```
    .......S.......
    .......|.......
    ......|^|......
    ......|.|......
    .....|^|^|.....
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    This process continues until all of the tachyon beams reach a splitter or exit the manifold:

    ```
    .......S.......
    .......|.......
    ......|^|......
    ......|.|......
    .....|^|^|.....
    .....|.|.|.....
    ....|^|^|^|....
    ....|.|.|.|....
    ...|^|^|||^|...
    ...|.|.|||.|...
    ..|^|^|||^|^|..
    ..|.|.|||.|.|..
    .|^|||^||.||^|.
    .|.|||.||.||.|.
    |^|^|^|^|^|||^|
    |.|.|.|.|.|||.|
    ```

    To repair the teleporter, you first need to understand the beam-splitting properties of the tachyon manifold. In this example, a tachyon beam is split a total of 21 times.

    Analyze your manifold diagram. How many times will the beam be split?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_7_1_find_number_of_beam_splits(tachyon_manifold: list[str]) -> int:
    """
    Count the total number of times tachyon beams are split in a manifold.

    A tachyon beam starts at the location marked 'S' in the top row and moves
    downward. Beams pass freely through empty spaces ('.') and are split when
    they encounter a splitter ('^'). When a splitter is hit, the beam stops
    and two new beams are emitted from the immediate left and right positions
    of the splitter. Overlapping beams in the same column are counted only
    once per row.

    Args:
        tachyon_manifold (list[str]): A list of strings representing the grid
            of the tachyon manifold. 'S' marks the starting point, '.' is empty
            space, and '^' is a splitter.

    Returns:
        int: The total number of beam splits that occur in the manifold.
    """
    beam_split_counter: int = 0
    beam_x_coordinates: set[int] = {tachyon_manifold[0].index("S")}

    for row_index in range(len(tachyon_manifold) - 1):
        new_beam_x_coordinates = set()

        for x in beam_x_coordinates:
            if tachyon_manifold[row_index + 1][x] == "^":
                new_beam_x_coordinates.add(x - 1)
                new_beam_x_coordinates.add(x + 1)
                beam_split_counter += 1
            else:
                new_beam_x_coordinates.add(x)

        beam_x_coordinates = new_beam_x_coordinates

    return beam_split_counter


@app.cell
def _():
    example_tachyon_manifold = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]

    solution_example_7_1 = exercise_7_1_find_number_of_beam_splits(
        tachyon_manifold=example_tachyon_manifold
    )

    assert solution_example_7_1 == 21
    return (example_tachyon_manifold,)


@app.cell
def _(exercise_7_1_find_number_of_beam_splits, read_data):
    tachyon_manifold = read_data(file_path="data/2025/2025_day_07.txt", separator="\n")

    solution_7_1 = exercise_7_1_find_number_of_beam_splits(
        tachyon_manifold=tachyon_manifold
    )

    assert solution_7_1 == 1590
    return (tachyon_manifold,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With your analysis of the manifold complete, you begin fixing the teleporter. However, as you open the side of the teleporter to replace the broken manifold, you are surprised to discover that it isn't a classical tachyon manifold - it's a quantum tachyon manifold.

    With a quantum tachyon manifold, only a single tachyon particle is sent through the manifold. A tachyon particle takes both the left and right path of each splitter encountered.

    Since this is impossible, the manual recommends the many-worlds interpretation of quantum tachyon splitting: each time a particle reaches a splitter, it's actually time itself which splits. In one timeline, the particle went left, and in the other timeline, the particle went right.

    To fix the manifold, what you really need to know is the number of timelines active after a single particle completes all of its possible journeys through the manifold.

    In the above example, there are many timelines. For instance, there's the timeline where the particle always went left:

    ```
    .......S.......
    .......|.......
    ......|^.......
    ......|........
    .....|^.^......
    .....|.........
    ....|^.^.^.....
    ....|..........
    ...|^.^...^....
    ...|...........
    ..|^.^...^.^...
    ..|............
    .|^...^.....^..
    .|.............
    |^.^.^.^.^...^.
    |..............
    ```

    Or, there's the timeline where the particle alternated going left and right at each splitter:

    ```
    .......S.......
    .......|.......
    ......|^.......
    ......|........
    ......^|^......
    .......|.......
    .....^|^.^.....
    ......|........
    ....^.^|..^....
    .......|.......
    ...^.^.|.^.^...
    .......|.......
    ..^...^|....^..
    .......|.......
    .^.^.^|^.^...^.
    ......|........
    ```

    Or, there's the timeline where the particle ends up at the same point as the alternating timeline, but takes a totally different path to get there:

    ```
    .......S.......
    .......|.......
    ......|^.......
    ......|........
    .....|^.^......
    .....|.........
    ....|^.^.^.....
    ....|..........
    ....^|^...^....
    .....|.........
    ...^.^|..^.^...
    ......|........
    ..^..|^.....^..
    .....|.........
    .^.^.^|^.^...^.
    ......|........
    ```

    In this example, in total, the particle ends up on 40 different timelines.

    Apply the many-worlds interpretation of quantum tachyon splitting to your manifold diagram. In total, how many different timelines would a single tachyon particle end up on?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def exercise_7_2_find_number_of_timelines(defaultdict):
    def exercise_7_2_find_number_of_timelines(tachyon_manifold: list[str]) -> int:
        """
        Count the total number of quantum timelines for a single tachyon particle
        traversing a quantum tachyon manifold using the many-worlds interpretation.

        Each splitter ('^') splits the current timeline into two: one going left
        and one going right. Timelines do not merge; every possible path is counted
        as a distinct timeline. The particle starts at the location marked 'S' in
        the top row and moves downward, creating new timelines at each splitter.

        Args:
            tachyon_manifold (list[str]): A list of strings representing the quantum
                tachyon manifold. 'S' marks the starting point, '.' is empty space,
                and '^' is a splitter.

        Returns:
            int: Total number of unique timelines after the particle traverses the manifold.
        """
        timeline_counter = {tachyon_manifold[0].index("S"): 1}

        for i in range(len(tachyon_manifold) - 1):
            beam_counter_per_row = defaultdict(int)

            for x, count in timeline_counter.items():
                if tachyon_manifold[i + 1][x] == "^":
                    beam_counter_per_row[x - 1] += count
                    beam_counter_per_row[x + 1] += count
                else:
                    beam_counter_per_row[x] += count

            timeline_counter = beam_counter_per_row

        total_number_of_timelines = sum(timeline_counter.values())
        return total_number_of_timelines

    return (exercise_7_2_find_number_of_timelines,)


@app.cell
def _(example_tachyon_manifold, exercise_7_2_find_number_of_timelines):
    solution_example_7_2 = exercise_7_2_find_number_of_timelines(
        tachyon_manifold=example_tachyon_manifold
    )

    assert solution_example_7_2 == 40
    return


@app.cell
def _(exercise_7_2_find_number_of_timelines, tachyon_manifold):
    solution_7_2 = exercise_7_2_find_number_of_timelines(
        tachyon_manifold=tachyon_manifold
    )

    assert solution_7_2 == 20571740188555
    return


@app.function
def exercise_7_2_find_number_of_timelines_iterative(tachyon_manifold: list[str]) -> int:
    """
    Count the total number of quantum timelines for a single tachyon particle
    traversing a quantum tachyon manifold using an iterative DFS approach.

    A single tachyon particle starts at 'S' in the top row and moves downward.
    Each splitter ('^') creates two new timelines: one moving left and one
    moving right. Empty cells ('.') allow the particle to continue straight down.
    This function explores all possible paths iteratively, using backtracking
    to account for all splits.

    Args:
        tachyon_manifold (list[str]): A list of strings representing the quantum
            tachyon manifold. 'S' marks the starting point, '.' is empty space,
            and '^' is a splitter.

    Returns:
        int: Total number of unique timelines after the particle traverses the manifold.
    """

    def propagate_beam_downward(
        beam_x_coordinates: list[int],
        choices: list[str],
        tachyon_manifold: list[str],
    ) -> tuple[list[int], list[str]]:
        """
        Propagate the beam downward through the manifold until the bottom is reached.

        For each row below the current beam position:
        - If the cell is a splitter ('^'), a left branch is chosen and recorded in choices.
        - If the cell is empty ('.'), the beam continues straight down.

        Args:
            beam_x_coordinates (list[int]): Current x-coordinates of the beam path.
            choices (list[str]): List of choices taken so far ('L', 'R', '-').
            tachyon_manifold (list[str]): The full quantum tachyon manifold grid.

        Returns:
            tuple[list[int], list[str]]: Updated beam x-coordinates and choices after
                propagating to the bottom of the manifold.
        """
        while len(beam_x_coordinates) < len(tachyon_manifold):
            x = beam_x_coordinates[-1]
            char_below = tachyon_manifold[len(beam_x_coordinates)][x]

            # Always go left when encountering a splitter.
            if char_below == "^":
                choices.append("L")
                beam_x_coordinates.append(x - 1)
            elif char_below == ".":
                choices.append("-")
                beam_x_coordinates.append(x)

        return beam_x_coordinates, choices

    timeline_counter = 1
    choices = []
    beam_x_coordinates = [tachyon_manifold[0].index("S")]

    beam_x_coordinates, choices = propagate_beam_downward(
        beam_x_coordinates, choices, tachyon_manifold
    )

    while True:
        for i in range(len(beam_x_coordinates) - 1, -1, -1):
            if choices[i - 1] == "L":
                # Backtrack to the previous choice.
                beam_x_coordinates = beam_x_coordinates[:i].copy()
                choices = choices[: i - 1].copy()

                # Now take the right branch instead.
                choices.append("R")
                beam_x_coordinates.append(beam_x_coordinates[-1] + 1)

                beam_x_coordinates, choices = propagate_beam_downward(
                    beam_x_coordinates, choices, tachyon_manifold
                )

                timeline_counter += 1
                break
        else:
            break

    return timeline_counter


@app.cell
def _(example_tachyon_manifold):
    solution_example_7_2_v2 = exercise_7_2_find_number_of_timelines_iterative(
        tachyon_manifold=example_tachyon_manifold
    )

    assert solution_example_7_2_v2 == 40
    return


@app.cell
def _():
    # I think this code will give the correct answer, however because of the iterative approach,
    # and the scaling with 2 to the power of the number of rows in the Tachyon manifold diagram,
    # this will take way too much time. I don't know how long exactly, but it's not a feasible solution.

    # exercise_7_2_find_number_of_timelines_iterative(tachyon_manifold=tachyon_manifold)
    return


if __name__ == "__main__":
    app.run()
