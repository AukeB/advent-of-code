import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 17

    https://adventofcode.com/2015/day/17
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
    ## Day 17 - No Such Thing as Too Much
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _():
    from collections.abc import Iterable, Iterator
    from typing import Any

    def combinations(iterable: Iterable[Any], r: int) -> Iterator[tuple[Any, ...]]:
        """Yield all r-length combinations of the items in an iterable.

        This function is a copy of the code that can be accessed by the link
        below, and it contains this docstring and some comments to make the
        algorithm more clear.

        https://docs.python.org/3/library/itertools.html#itertools.combinations

        Combinations are produced in lexicographic order of the positions of
        their items in the input. Each item is used at most once per
        combination, and the items within a combination keep their original
        order, so ('A', 'B') is produced but ('B', 'A') is not. If r is greater
        than the number of items, a ValueError is raised.

        Args:
            iterable (Iterable[Any]): The items to choose from. It is converted
                to a tuple up front, so a one-time iterator such as a generator
                works.
            r (int): The number of items in each combination.

        Yields:
            tuple: One combination of r items from the iterable.

        Raises:
            ValueError: If r is greater than the number of items in the
                iterable.

        Examples:
            >>> list(combinations('ABCD', 2))
            [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
            >>> list(combinations(range(4), 3))
            [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        """
        # Fixed, indexable copy of the items to pick combinations from
        pool = tuple(iterable)
        n = len(pool)

        if r > n:
            raise ValueError(
                f"Subsequence length ({r}) cannot be greater than length of iterable ({n})."
            )

        # `indices` holds the positions of the items you're currently picking from the pool.
        # Each entry is an index into pool, not an item itself.
        indices = list(range(r))

        # First combination is by taking the first `r` elements of the `pool`.
        yield tuple(pool[i] for i in indices)

        while True:
            # `i` is the position in `indices` that gets bumped: the rightmost index
            # that can still move without running past the end of the pool.
            # Since `i` represent the index on the `indices` variable, and `indices`
            # represents which elements from the `pool` to take, `i` is sort of a
            # double index variable, which is why this While loop is pretty hard to
            # understand from the code alone.
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                # No index can move any further, so every combination has been produced.
                return

            indices[i] += 1

            # `j` walks over every position after `i`. Each one is reset to the smallest
            # valid index that follows its left neighbour, which keeps the indices
            # strictly increasing and the output in lexicographic order.
            # This for-loop only gets executed when the `break` is executed in the
            # other for loop.
            for j in range(i + 1, r):
                indices[j] = indices[j - 1] + 1

            yield tuple(pool[i] for i in indices)

    return (combinations,)


@app.cell
def _(combinations):
    def exercise_17_1_find_different_combinations_of_containers(
        puzzle_input: list[str],
        eggnog_target_volume: int,
    ) -> int:
        """Count the container combinations that hold exactly the target volume.

        Instead of starting from the total volume and working down to zero, this
        counts up from zero: each combination of containers is a way to reach
        the target volume. This is the more common framing in mathematics and is
        easier to follow.

        Every subset size from one container up to all containers is checked,
        and each subset whose capacities sum to the target is counted once.

        Args:
            puzzle_input: Capacities of the available containers, as strings
                (for example, read from the puzzle input). They are converted to
                integers before use.
            eggnog_target_volume: The total volume, in liters, that the chosen
                containers must add up to exactly.

        Returns:
            int: The number of distinct combinations of containers whose
                capacities sum to eggnog_target_volume.
        """

        containers = [int(x) for x in puzzle_input]

        total_combinations = 0

        for i in range(1, len(containers) + 1):
            for x in combinations(containers, i):
                if sum(x) == eggnog_target_volume:
                    total_combinations += 1

        return total_combinations

    return (exercise_17_1_find_different_combinations_of_containers,)


@app.cell
def _(exercise_17_1_find_different_combinations_of_containers):
    example_containers = ["20", "15", "10", "5", "5"]
    example_target_volume = 25

    example_solution = exercise_17_1_find_different_combinations_of_containers(
        puzzle_input=example_containers, eggnog_target_volume=example_target_volume
    )

    assert example_solution == 4
    return


@app.cell
def _(exercise_17_1_find_different_combinations_of_containers, read_data):
    containers = read_data(file_path="data/2015/2015_day_17.txt", separator="\n")
    eggnog_target_volume = 150

    solution_17_1 = exercise_17_1_find_different_combinations_of_containers(
        puzzle_input=containers,
        eggnog_target_volume=eggnog_target_volume,
    )

    assert solution_17_1 == 654
    return containers, eggnog_target_volume


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(combinations):
    def exercise_17_2_find_combinations_for_minimum(
        puzzle_input: list[str],
        eggnog_target_volume: int,
    ) -> int:
        """Count the combinations that reach the target volume with the fewest
        containers.

        Combination sizes are checked from smallest to largest. The first size
        that has at least one combination adding up to the target is the
        minimum, and the function returns how many combinations of that size
        reach it. Larger combinations are never counted.

        Args:
            puzzle_input: Capacities of the available containers, as strings
                (for example, read from the puzzle input). They are converted to
                integers before use.
            eggnog_target_volume: The total volume, in liters, that the chosen
                containers must add up to exactly.

        Returns:
            int: The number of combinations using the minimum number of
                containers that sum to eggnog_target_volume. If no combination
                reaches the target, the function returns 0.
        """
        containers = [int(x) for x in puzzle_input]

        total_combinations = 0

        for i in range(1, len(containers) + 1):
            for x in combinations(containers, i):
                if sum(x) == eggnog_target_volume:
                    total_combinations += 1

            if total_combinations:
                return total_combinations

        return 0

    return (exercise_17_2_find_combinations_for_minimum,)


@app.cell
def _(
    containers,
    eggnog_target_volume,
    exercise_17_2_find_combinations_for_minimum,
):
    solution_17_2 = exercise_17_2_find_combinations_for_minimum(
        puzzle_input=containers,
        eggnog_target_volume=eggnog_target_volume,
    )

    assert solution_17_2 == 57
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
