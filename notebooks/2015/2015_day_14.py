import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 14
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
    import plotly.graph_objects as go
    import plotly.express as px

    from aoc.utils import read_data

    return base64, go, mo, px, read_data, warnings


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 14: Reindeer Olympics
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
    This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

    Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

    For example, suppose you have the following Reindeer:

    - Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    - Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

    After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

    In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

    Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_14_1_find_fastest_reinder(
    reindeer_descriptions: list[str], total_time: int = 2503
) -> tuple[dict, int]:
    """Simulate each reindeer's flight and rest cycles to find the winning
    distance.

    1. Parse each reindeer description into its speed, move duration, rest
       duration, and combined cycle duration.
    2. Step through every second up to total_time, tracking each reindeer's
       cumulative distance based on whether it is flying or resting.
    3. Return the distance traveled by the reindeer that is furthest ahead.

    Args:
        reindeer_descriptions (list[str]): Raw puzzle input lines, one per
            reindeer.
        total_time (int): Number of seconds the race runs for.

    Returns:
        reindeers (dict[str, dict[str, Any]]): Mapping of reindeer name to its
            stats, including the full "traveled" history of [time, distance]
            pairs.
        winning_reindeer_distance_traveled (int): Distance traveled by the
            leading reindeer once the race ends.
    """
    reindeers = {}

    for reindeer_description in reindeer_descriptions:
        reindeer_data = reindeer_description.split()

        reindeers[reindeer_data[0]] = {
            "move_speed": int(reindeer_data[3]),
            "move_duration": int(reindeer_data[6]),
            "rest_speed": 0,
            "rest_duration": int(reindeer_data[13]),
            "cycle_duration": int(reindeer_data[6]) + int(reindeer_data[13]),
            "traveled": [[0, 0]],
        }

    for t in range(total_time + 1):
        for reindeer_name, reindeer_stats in reindeers.items():
            t_cycle = t % reindeer_stats["cycle_duration"]

            if t_cycle > 0 and t_cycle <= reindeer_stats["move_duration"]:
                reindeers[reindeer_name]["traveled"].append(
                    [
                        t,
                        reindeer_stats["traveled"][-1][1]
                        + reindeer_stats["move_speed"],
                    ]
                )
            else:
                reindeers[reindeer_name]["traveled"].append(
                    [
                        t,
                        reindeer_stats["traveled"][-1][1]
                        + reindeer_stats["rest_speed"],
                    ]
                )

    winning_reindeer_distance_traveled = max(
        [reindeer_stats["traveled"][-1][1] for _, reindeer_stats in reindeers.items()]
    )

    return reindeers, winning_reindeer_distance_traveled


@app.cell
def _(go, px):
    def exercise_14_plot_reindeer_distances(reindeers: dict) -> go.Figure:  # pyright: ignore[reportInvalidTypeForm]
        """Plot each reindeer's distance (and points, if tracked) over time.

        1. Check whether any reindeer has a "points" history, since only part 2
           tracks it.
        2. Create an empty figure.
        3. For each reindeer, unpack its "traveled" (and "points") history into
           time/value sequences and add each as a line trace, using a solid line
           for distance and a dashed line for points, sharing color per
           reindeer.
        4. Apply layout styling (titles, hover mode) and return the figure.

        Args:
            reindeers (dict[str, dict[str, Any]]): Mapping of reindeer name to
                its stats, including a "traveled" list of [time, distance] pairs
                and, for part 2, a "points" list of [time, points] pairs.

        Returns:
            figure (go.Figure): Interactive Plotly figure with one distance line
                per reindeer, plus a points line per reindeer when tracked,
                sharing colors and a y-axis across both metrics.
        """
        has_points = any(
            "points" in reindeer_stats for reindeer_stats in reindeers.values()
        )

        figure = go.Figure()
        colors = px.colors.qualitative.Plotly

        for index, (reindeer_name, reindeer_stats) in enumerate(reindeers.items()):
            color = colors[index % len(colors)]
            times, distances = zip(*reindeer_stats["traveled"])

            figure.add_trace(
                go.Scatter(
                    x=times,
                    y=distances,
                    mode="lines",
                    name=f"{reindeer_name} (distance)",
                    legendgroup=reindeer_name,
                    line={"color": color, "dash": "solid"},
                    hovertemplate=(
                        f"{reindeer_name}<br>"
                        "Time: %{x}s<br>"
                        "Distance: %{y}km<extra></extra>"
                    ),
                )
            )

            if has_points:
                point_times, points = zip(*reindeer_stats["points"])

                figure.add_trace(
                    go.Scatter(
                        x=point_times,
                        y=points,
                        mode="lines",
                        name=f"{reindeer_name} (points)",
                        legendgroup=reindeer_name,
                        line={"color": color, "dash": "dot"},
                        hovertemplate=("Points: %{y}<extra></extra>"),
                    )
                )

        figure.update_layout(
            title="Reindeer Race: Distance and Points Over Time",
            xaxis_title="Time (seconds)",
            yaxis_title="Distance (km) / Points",
            hovermode="x unified",
            template="plotly_white",
        )

        return figure

    return (exercise_14_plot_reindeer_distances,)


@app.cell
def _(exercise_14_1_find_fastest_reinder, read_data):
    reindeer_descriptions: list[str] = read_data(
        file_path="data/2015/2015_day_14.txt", separator="\n"
    )

    reindeers_14_1, winning_reindeer_distance_traveled = (
        exercise_14_1_find_fastest_reinder(reindeer_descriptions=reindeer_descriptions)
    )

    assert winning_reindeer_distance_traveled == 2660
    return reindeer_descriptions, reindeers_14_1


@app.cell
def _(exercise_14_plot_reindeer_distances, mo, reindeers_14_1):
    figure_14_1 = exercise_14_plot_reindeer_distances(reindeers=reindeers_14_1)

    mo.accordion({"Interactive plot": figure_14_1})  # pyright: ignore[reportUnusedExpression]
    return (figure_14_1,)


@app.cell
def _(base64, figure_14_1, mo, warnings):
    # Kaleido 0.2.1 (pinned, as kaleido 1.x needs Chrome) raises a deprecation warning here.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        figure_png_1 = figure_14_1.to_image(format="png")

    encoded_figure_14_1 = base64.b64encode(figure_png_1).decode()

    mo.md(f"![Reindeer distances](data:image/png;base64,{encoded_figure_14_1})")  # pyright: ignore[reportUnusedExpression]


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

    Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

    Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

    After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

    Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_14_2_find_fastest_reindeer(
    reindeer_descriptions: list[str], total_time: int = 2503
) -> tuple[dict, int]:
    """Simulate each reindeer's flight and rest cycles to find the winning
    score.

    1. Parse each reindeer description into its speed, move duration, rest
       duration, and combined cycle duration.
    2. Step through every second, updating each reindeer's cumulative distance
       based on whether it is flying or resting.
    3. After each second, award a point to every reindeer currently tied for the
       furthest distance, recording the running point total.
    4. Return the reindeer with the most points once the race ends.

    Args:
        reindeer_descriptions (list[str]): Raw puzzle input lines, one per
            reindeer.
        total_time (int): Number of seconds the race runs for.

    Returns:
        reindeers (dict): Mapping of reindeer name to its stats, including the
            full "traveled" and "points" histories as [time, value] pairs.
        winning_reindeer_most_points (int): Highest point total among all
            reindeer once the race ends.
    """
    reindeers = {}

    for reindeer_description in reindeer_descriptions:
        reindeer_data = reindeer_description.split()

        reindeers[reindeer_data[0]] = {
            "move_speed": int(reindeer_data[3]),
            "move_duration": int(reindeer_data[6]),
            "rest_speed": 0,
            "rest_duration": int(reindeer_data[13]),
            "cycle_duration": int(reindeer_data[6]) + int(reindeer_data[13]),
            "traveled": [[0, 0]],
            "points": [[0, 0]],
        }

    for t in range(1, total_time + 1):
        for reindeer_name, reindeer_stats in reindeers.items():
            t_cycle = t % reindeer_stats["cycle_duration"]
            current_distance = reindeer_stats["traveled"][-1][1]

            if t_cycle > 0 and t_cycle <= reindeer_stats["move_duration"]:
                reindeers[reindeer_name]["traveled"].append(
                    [t, current_distance + reindeer_stats["move_speed"]]
                )
            else:
                reindeers[reindeer_name]["traveled"].append(
                    [t, current_distance + reindeer_stats["rest_speed"]]
                )

        furthest_distance_so_far = max(
            reindeer_stats["traveled"][-1][1] for reindeer_stats in reindeers.values()
        )

        furthest_reindeer_names = [
            reindeer_name
            for reindeer_name, reindeer_stats in reindeers.items()
            if reindeer_stats["traveled"][-1][1] == furthest_distance_so_far
        ]

        for reindeer_name, reindeer_stats in reindeers.items():
            current_points = reindeer_stats["points"][-1][1]

            if reindeer_name in furthest_reindeer_names:
                reindeers[reindeer_name]["points"].append([t, current_points + 1])
            else:
                reindeers[reindeer_name]["points"].append([t, current_points])

    winning_reindeer_most_points = max(
        reindeer_stats["points"][-1][1] for reindeer_stats in reindeers.values()
    )

    return reindeers, winning_reindeer_most_points


@app.cell
def _(exercise_14_2_find_fastest_reindeer, reindeer_descriptions: list[str]):
    reindeers_14_2, winning_reindeer_most_points = exercise_14_2_find_fastest_reindeer(
        reindeer_descriptions=reindeer_descriptions
    )

    assert winning_reindeer_most_points == 1256
    return (reindeers_14_2,)


@app.cell
def _(exercise_14_plot_reindeer_distances, mo, reindeers_14_2):
    figure_14_2 = exercise_14_plot_reindeer_distances(reindeers=reindeers_14_2)

    mo.accordion({"Interactive plot": figure_14_2})  # pyright: ignore[reportUnusedExpression]
    return (figure_14_2,)


@app.cell
def _(base64, figure_14_2, mo, warnings):
    # Kaleido 0.2.1 (pinned, as kaleido 1.x needs Chrome) raises a deprecation warning here.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        figure_png_2 = figure_14_2.to_image(format="png")

    encoded_figure_14_2 = base64.b64encode(figure_png_2).decode()

    mo.md(f"![Reindeer distances](data:image/png;base64,{encoded_figure_14_2})")  # pyright: ignore[reportUnusedExpression]


if __name__ == "__main__":
    app.run()
