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
    import base64
    import warnings

    import marimo as mo
    import plotly.express as px
    import plotly.graph_objects as go

    from collections import namedtuple
    from aoc.utils import read_data

    return base64, go, mo, namedtuple, px, read_data, warnings


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 17 - No Such Thing as Too Much
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### General functions
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
    def all_combinations(iterable):
        """Yield all non-empty combinations of the items in an iterable.

        Combinations are yielded by size, starting with every single item and
        ending with the full set. Within each size, they follow the same order
        as `combinations`. The iterable is measured with `len`, so it must be a
        sized collection such as a list, tuple, or string, not a generator.

        Args:
            iterable: The items to choose from.

        Yields:
            tuple: One combination of one or more items from the iterable.

        Examples:
            >>> list(all_combinations('ABC'))
            [('A',), ('B',), ('C',), ('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B', 'C')]
        """
        for i in range(1, len(iterable) + 1):
            yield from combinations(iterable, i)

    return (all_combinations,)


@app.cell
def _(all_combinations, namedtuple):
    ContainerCombination = namedtuple(
        "ContainerCombination",
        ["size", "containers", "container_indices", "fits_target"],
    )

    def get_all_container_combinations(
        puzzle_input: list[str],
        eggnog_target_volume: int,
    ) -> list:
        """Check every container combination against the target volume.

        Args:
            puzzle_input: Capacities of the available containers, as strings.
            eggnog_target_volume: The total volume, in liters, to match.

        Returns:
            list[ContainerCombination]: One entry per combination, with its
                size, the containers it uses, and whether it adds up to the
                target.
        """
        containers = sorted([int(x) for x in puzzle_input], reverse=True)
        all_container_combinations = []

        for container_indices in all_combinations(range(len(containers))):
            combination = tuple(containers[i] for i in container_indices)
            fits_target = sum(combination) == eggnog_target_volume
            all_container_combinations.append(
                ContainerCombination(
                    len(combination), combination, container_indices, fits_target
                )
            )

        return all_container_combinations

    return (get_all_container_combinations,)


@app.cell
def _(go):
    from collections import Counter

    def plot_combinations_per_container_count(
        all_container_combinations: list,
        log_y_axis: bool,
    ) -> go.Figure:  # pyright: ignore[reportInvalidTypeForm]
        """Plot how many combinations of each container count fit the target.

        Each container count is one stacked bar. The bottom segment is the
        number of combinations that add up to the target volume, and the top
        segment is the number that do not.

        Args:
            all_container_combinations: Output of
                get_all_container_combinations, one ContainerCombination per
                combination of containers.
            log_y_axis: Whether to use a logarithmic y-axis.

        Returns:
            go.Figure: Stacked bar chart with one bar per container count.
        """
        fitting_counts = Counter(
            container_combination.size
            for container_combination in all_container_combinations
            if container_combination.fits_target
        )
        not_fitting_counts = Counter(
            container_combination.size
            for container_combination in all_container_combinations
            if not container_combination.fits_target
        )
        container_counts = list(
            range(1, max(c.size for c in all_container_combinations) + 1)
        )

        figure = go.Figure()
        figure.add_trace(
            go.Bar(
                x=container_counts,
                y=[fitting_counts[count] for count in container_counts],
                name="Adds up to target",
                marker={"color": "#2a9d8f"},
            )
        )
        figure.add_trace(
            go.Bar(
                x=container_counts,
                y=[not_fitting_counts[count] for count in container_counts],
                name="Does not add up",
                marker={"color": "#e76f51"},
            )
        )

        figure.update_layout(
            title="Combinations per number of containers",
            xaxis_title="Number of containers",
            yaxis_title="Number of combinations"
            + (" (log scale)" if log_y_axis else ""),
            yaxis_type="log" if log_y_axis else "linear",
            xaxis={"dtick": 1},
            barmode="stack",
            template="plotly_white",
        )

        return figure

    return (plot_combinations_per_container_count,)


@app.cell
def _(go, px):
    def plot_fitting_combinations(
        all_container_combinations: list,
    ) -> go.Figure:  # pyright: ignore[reportInvalidTypeForm]
        """Plot every fitting container combination as a stacked bar.

        Each fitting combination is one bar. Every container has a fixed color,
        so containers with the same capacity still get separate colors, and all
        bars have the same total height: the target volume.

        Args:
            all_container_combinations: Output of
                get_all_container_combinations, one ContainerCombination per
                combination of containers.

        Returns:
            go.Figure: Stacked bar chart with one bar per fitting combination.
        """
        fitting_combinations = [
            container_combination
            for container_combination in all_container_combinations
            if container_combination.fits_target
        ]

        capacity_by_index = {
            index: capacity
            for container_combination in all_container_combinations
            for index, capacity in zip(
                container_combination.container_indices,
                container_combination.containers,
            )
        }

        # Containers are ranked by capacity, so containers of similar size get
        # neighbouring colors on the gradient, while equal sizes still differ.
        ranked_indices = sorted(
            capacity_by_index, key=lambda index: (capacity_by_index[index], index)
        )
        gradient_positions = [
            rank / max(len(ranked_indices) - 1, 1)
            for rank in range(len(ranked_indices))
        ]
        gradient_colors = px.colors.sample_colorscale("Turbo", gradient_positions)
        color_by_index = dict(zip(ranked_indices, gradient_colors))

        fitting_sizes = sorted(
            {
                container_combination.size
                for container_combination in fitting_combinations
            }
        )
        if len(fitting_sizes) == 1:
            title = (
                f"{len(fitting_combinations)} combinations of {fitting_sizes[0]} "
                "containers holding the target volume"
            )
        else:
            title = (
                f"All {len(fitting_combinations)} container combinations holding "
                "the target volume"
            )

        figure = go.Figure()

        for index in sorted(capacity_by_index):
            capacity = capacity_by_index[index]
            heights = [
                capacity if index in container_combination.container_indices else 0
                for container_combination in fitting_combinations
            ]

            figure.add_trace(
                go.Bar(
                    x=list(range(len(fitting_combinations))),
                    y=heights,
                    name=f"Container {index + 1} ({capacity} L)",
                    marker={
                        "color": color_by_index[index],
                        "line": {"width": 0},
                    },
                    hovertemplate=f"Container {index + 1} ({capacity} L)<br>"
                    "Combination %{x}<extra></extra>",
                )
            )

        figure.update_layout(
            title=title,
            xaxis_title="Combination",
            yaxis_title="Liters",
            barmode="stack",
            bargap=0,
            template="plotly_white",
        )

        return figure

    return (plot_fitting_combinations,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Solution - Part 1
    """)
    return


@app.function
def exercise_17_1_find_different_combinations_of_containers(
    all_container_combinations: list,
) -> int:
    """Count the container combinations that fit the target volume.

    Args:
        all_container_combinations: Output of get_all_container_combinations,
            one ContainerCombination per combination of containers.

    Returns:
        int: The number of combinations whose capacities add up to the target
            volume.
    """
    number_of_different_combinations = len(
        [
            container_combination
            for container_combination in all_container_combinations
            if container_combination.fits_target
        ]
    )

    return number_of_different_combinations


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Example data
    """)
    return


@app.cell
def _(get_all_container_combinations):
    example_containers = ["20", "15", "10", "5", "5"]
    example_target_volume = 25

    example_container_combinations = get_all_container_combinations(
        puzzle_input=example_containers, eggnog_target_volume=example_target_volume
    )

    example_solution = exercise_17_1_find_different_combinations_of_containers(
        all_container_combinations=example_container_combinations
    )

    assert example_solution == 4
    return (example_container_combinations,)


@app.cell
def _(
    example_container_combinations,
    mo,
    plot_combinations_per_container_count,
):
    figure_17_1_example_counts = plot_combinations_per_container_count(
        all_container_combinations=example_container_combinations,
        log_y_axis=False,
    )

    mo.accordion({"Interactive plot": figure_17_1_example_counts})  # pyright: ignore[reportUnusedExpression]
    return (figure_17_1_example_counts,)


@app.cell
def _(base64, figure_17_1_example_counts, mo, warnings):
    # Kaleido 0.2.1 (pinned, as kaleido 1.x needs Chrome) raises a deprecation warning here.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        figure_png_17_1_example_counts = figure_17_1_example_counts.to_image(
            format="png"
        )

    encoded_17_1_example_counts = base64.b64encode(
        figure_png_17_1_example_counts
    ).decode()

    mo.md(
        f"![Combinations per container count (example data)](data:image/png;base64,{encoded_17_1_example_counts})"
    )
    return


@app.cell
def _(example_container_combinations, mo, plot_fitting_combinations):
    figure_17_1_example = plot_fitting_combinations(
        all_container_combinations=example_container_combinations,
    )

    mo.accordion({"Interactive plot": figure_17_1_example})  # pyright: ignore[reportUnusedExpression]
    return (figure_17_1_example,)


@app.cell
def _(base64, figure_17_1_example, mo, warnings):
    # Kaleido 0.2.1 (pinned, as kaleido 1.x needs Chrome) raises a deprecation warning here.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        figure_png_17_1_example = figure_17_1_example.to_image(format="png")

    encoded_17_1_example = base64.b64encode(figure_png_17_1_example).decode()

    mo.md(
        f"![Fitting combinations (example data)](data:image/png;base64,{encoded_17_1_example})"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Real data
    """)
    return


@app.cell
def _(get_all_container_combinations, read_data):
    containers = read_data(file_path="data/2015/2015_day_17.txt", separator="\n")
    eggnog_target_volume = 150

    container_combinations = get_all_container_combinations(
        puzzle_input=containers, eggnog_target_volume=eggnog_target_volume
    )

    solution_17_1 = exercise_17_1_find_different_combinations_of_containers(
        all_container_combinations=container_combinations
    )

    assert solution_17_1 == 654
    return (container_combinations,)


@app.cell
def _(container_combinations, mo, plot_combinations_per_container_count):
    figure_17_1_counts = plot_combinations_per_container_count(
        all_container_combinations=container_combinations,
        log_y_axis=True,
    )

    mo.accordion({"Interactive plot": figure_17_1_counts})  # pyright: ignore[reportUnusedExpression]
    return (figure_17_1_counts,)


@app.cell
def _(base64, figure_17_1_counts, mo, warnings):
    # Kaleido 0.2.1 (pinned, as kaleido 1.x needs Chrome) raises a deprecation warning here.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        figure_png_17_1_counts = figure_17_1_counts.to_image(format="png")

    encoded_17_1_counts = base64.b64encode(figure_png_17_1_counts).decode()

    mo.md(
        f"![Combinations per container count (real data)](data:image/png;base64,{encoded_17_1_counts})"
    )
    return


@app.cell
def _(container_combinations, mo, plot_fitting_combinations):
    figure_17_1 = plot_fitting_combinations(
        all_container_combinations=container_combinations,
    )

    mo.accordion({"Interactive plot": figure_17_1})  # pyright: ignore[reportUnusedExpression]
    return (figure_17_1,)


@app.cell
def _(base64, figure_17_1, mo, warnings):
    # Kaleido 0.2.1 (pinned, as kaleido 1.x needs Chrome) raises a deprecation warning here.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        figure_png_17_1 = figure_17_1.to_image(format="png")

    encoded_17_1 = base64.b64encode(figure_png_17_1).decode()

    mo.md(f"![Fitting combinations (real data)](data:image/png;base64,{encoded_17_1})")
    return


@app.cell
def _(container_combinations, mo, plot_fitting_combinations):
    fitting_sizes = sorted({c.size for c in container_combinations if c.fits_target})

    figures_per_container_count = {
        size: plot_fitting_combinations(
            all_container_combinations=[
                container_combination
                for container_combination in container_combinations
                if container_combination.size == size
            ],
        )
        for size in fitting_sizes
    }

    mo.vstack(  # pyright: ignore[reportUnusedExpression]
        [
            mo.accordion({f"Interactive plot ({size} containers)": figure})
            for size, figure in figures_per_container_count.items()
        ]
    )
    return (figures_per_container_count,)


@app.cell
def _(base64, figures_per_container_count, mo, warnings):
    # Kaleido 0.2.1 (pinned, as kaleido 1.x needs Chrome) raises a deprecation warning here.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        encoded_figures_per_container_count = {
            size: base64.b64encode(figure.to_image(format="png")).decode()
            for size, figure in figures_per_container_count.items()
        }

    mo.md(  # pyright: ignore[reportUnusedExpression]
        "\n\n".join(
            f"#### {size} containers\n\n![Fitting combinations ({size} containers)](data:image/png;base64,{encoded})"
            for size, encoded in encoded_figures_per_container_count.items()
        )
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_17_2_find_combinations_for_minimum(
    all_container_combinations: list,
) -> int:
    """Count the fitting combinations that use the fewest containers.

    Args:
        all_container_combinations: Output of get_all_container_combinations,
            one ContainerCombination per combination of containers.

    Returns:
        int: The number of combinations with the smallest size that add up to
            the target volume. If no combination fits, the function returns 0.
    """
    fitting_combinations = [
        container_combination
        for container_combination in all_container_combinations
        if container_combination.fits_target
    ]

    if not fitting_combinations:
        return 0

    smallest_size = min(
        container_combination.size for container_combination in fitting_combinations
    )

    number_of_different_combinations = len(
        [
            container_combination
            for container_combination in fitting_combinations
            if container_combination.size == smallest_size
        ]
    )

    return number_of_different_combinations


@app.cell
def _(container_combinations):
    solution_17_2 = exercise_17_2_find_combinations_for_minimum(
        all_container_combinations=container_combinations,
    )

    assert solution_17_2 == 57
    return


if __name__ == "__main__":
    app.run()
