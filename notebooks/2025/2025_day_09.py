import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 9
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

    from collections import namedtuple

    from aoc.utils import read_data

    return base64, go, mo, namedtuple, read_data, warnings


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 9 - Movie Theater
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
    You slide down the firepole in the corner of the playground and land in the North Pole base movie theater!

    The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. Some of the tiles are red; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).

    For example:

    ```
    7,1
    11,1
    11,7
    9,7
    9,5
    2,5
    2,3
    7,3
    ```

    Showing red tiles as # and other tiles as ., the above arrangement of red tiles would look like this:

    ```
    ..............
    .......#...#..
    ..............
    ..#....#......
    ..............
    ..#......#....
    ..............
    .........#.#..
    ..............
    ```

    You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.

    For example, you could make a rectangle (shown as O) with an area of 24 between 2,5 and 9,7:

    ```
    ..............
    .......#...#..
    ..............
    ..#....#......
    ..............
    ..OOOOOOOO....
    ..OOOOOOOO....
    ..OOOOOOOO.#..
    ..............
    ```

    Or, you could make a rectangle with area 35 between 7,1 and 11,7:

    ```
    ..............
    .......OOOOO..
    .......OOOOO..
    ..#....OOOOO..
    .......OOOOO..
    ..#....OOOOO..
    .......OOOOO..
    .......OOOOO..
    ..............
    ```

    You could even make a thin rectangle with an area of only 6 between 7,3 and 2,3:

    ```
    ..............
    .......#...#..
    ..............
    ..OOOOOO......
    ..............
    ..#......#....
    ..............
    .........#.#..
    ..............
    ```

    Ultimately, the largest rectangle you can make in this example has area 50. One way to do this is between 2,5 and 11,1:

    ```
    ..............
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..............
    .........#.#..
    ..............
    ```

    Using two red tiles as opposite corners, what is the largest area of any rectangle you can make?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(go):
    def plot_red_tiles(
        red_tile_coordinates: list[list[int]],
        largest_rect_coordinates: list[list[int]],
        line_color: str = "black",
        marker_color: str = "black",
    ) -> None:
        """
        Plot connected tile coordinates and a largest rectangle overlay.

        This function visualizes two closed polygonal paths using Plotly:
        one representing red tiles and another representing the largest
        rectangle. Both shapes are plotted with equal x/y scaling.

        Args:
            red_tile_coordinates: List of [x, y] pairs defining red tiles.
            largest_rect_coordinates: List of [x, y] pairs defining a rectangle.
            line_color: Line color for the red tile connections.
            marker_color: Marker color for the red tile points.
        """

        def plot_connections(
            fig: go.Figure,  # pyright: ignore[reportInvalidTypeForm]
            coordinates: list[list[int]],
            line_color: str,
            marker_color: str,
        ) -> go.Figure:  # pyright: ignore[reportInvalidTypeForm]
            """
            Add a closed polygon trace to an existing Plotly figure.

            The first coordinate is appended to the end to close the loop.
            A single scatter trace with markers and lines is added.

            Args:
                fig: Plotly figure to which the trace is added.
                coordinates: List of [x, y] coordinate pairs.
                line_color: Color of the connecting lines.
                marker_color: Color of the markers.

            Returns:
                The updated Plotly figure.
            """
            coordinates.append(coordinates[0])
            x_coordinates, y_coordinates = zip(*coordinates)

            fig.add_trace(
                go.Scatter(
                    x=x_coordinates,
                    y=y_coordinates,
                    mode="markers+lines",
                    line=dict(color=line_color),
                    marker=dict(color=marker_color),
                )
            )

            return fig

        fig = go.Figure()

        fig = plot_connections(fig, red_tile_coordinates, line_color, marker_color)
        fig = plot_connections(fig, largest_rect_coordinates, "red", "red")

        fig.update_layout(
            yaxis_scaleanchor="x",
            template="plotly_white",
        )

        return fig

    return (plot_red_tiles,)


@app.cell
def _():
    def exercise_9_1_find_largest_rectangle(
        red_tile_data: list[str],
    ) -> tuple[int, list[list[int]] | None]:
        """
        Find the largest possible rectangle area formed by any two red tiles as opposite corners.

        Each coordinate is given as a string "x,y". Two tiles define a rectangle whose area is
        computed as (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1). All unique tile pairs are evaluated,
        and the largest resulting rectangle area is returned.

        Args:
            red_tile_data (list[str]): List of red tile positions as "x,y" strings.

        Returns:
            tuple[int, list[list[int]] | None]: The largest rectangle area formed
                by any pair of red tiles, and the corner coordinates of that rectangle.
        """
        red_tile_coordinates = [
            [int(num) for num in row.split(",")] for row in red_tile_data
        ]

        largest_rect_area = 0
        largest_rect_coordinates = None

        for i in range(len(red_tile_coordinates)):
            for j in range(i):
                c1 = red_tile_coordinates[i]
                c2 = red_tile_coordinates[j]

                rectangle_area = (1 + abs(c1[0] - c2[0])) * (1 + abs(c1[1] - c2[1]))

                if rectangle_area > largest_rect_area:
                    largest_rect_area = rectangle_area

                    largest_rect_coordinates = [c1, c2]
                    largest_rect_coordinates.insert(1, [c2[0], c1[1]])
                    largest_rect_coordinates.append([c1[0], c2[1]])

        return largest_rect_area, largest_rect_coordinates

    return (exercise_9_1_find_largest_rectangle,)


@app.cell
def _(exercise_9_1_find_largest_rectangle):
    example_red_tile_data = [
        "7,1",
        "11,1",
        "11,7",
        "9,7",
        "9,5",
        "2,5",
        "2,3",
        "7,3",
    ]

    solution_example_9_1, _ = exercise_9_1_find_largest_rectangle(
        red_tile_data=example_red_tile_data
    )

    assert solution_example_9_1 == 50
    return (example_red_tile_data,)


@app.cell
def _(exercise_9_1_find_largest_rectangle, read_data):
    red_tile_data = read_data(file_path="data/2025/2025_day_09.txt", separator="\n")

    solution_9_1, largest_rect_coordinates_9_1 = exercise_9_1_find_largest_rectangle(
        red_tile_data=red_tile_data
    )

    assert solution_9_1 == 4738108384
    return largest_rect_coordinates_9_1, red_tile_data


@app.cell
def _(largest_rect_coordinates_9_1, mo, plot_red_tiles, red_tile_data):
    red_tile_coordinates_9_1 = [
        [int(num) for num in row.split(",")] for row in red_tile_data
    ]

    figure_9_1 = plot_red_tiles(
        red_tile_coordinates=red_tile_coordinates_9_1,
        largest_rect_coordinates=largest_rect_coordinates_9_1,
    )

    mo.accordion({"Interactive plot": figure_9_1})  # pyright: ignore[reportUnusedExpression]
    return (figure_9_1,)


@app.cell
def _(base64, figure_9_1, mo, warnings):
    # Kaleido 0.2.1 (pinned, as kaleido 1.x needs Chrome) raises a deprecation warning here.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        figure_png_9_1 = figure_9_1.to_image(format="png")

    encoded_figure_9_1 = base64.b64encode(figure_png_9_1).decode()

    mo.md(f"![Largest rectangle](data:image/png;base64,{encoded_figure_9_1})")  # pyright: ignore[reportUnusedExpression]


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.

    In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

    Using the same example as before, the tiles marked X would be green:

    ```
    ..............
    .......#XXX#..
    .......X...X..
    ..#XXXX#...X..
    ..X........X..
    ..#XXXXXX#.X..
    .........X.X..
    .........#X#..
    ..............
    ```

    In addition, all of the tiles inside this loop of red and green tiles are also green. So, in this example, these are the green tiles:

    ```
    ..............
    .......#XXX#..
    .......XXXXX..
    ..#XXXX#XXXX..
    ..XXXXXXXXXX..
    ..#XXXXXX#XX..
    .........XXX..
    .........#X#..
    ..............
    ```

    The remaining tiles are never red nor green.

    The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.

    For example, you could make a rectangle out of red and green tiles with an area of 15 between 7,3 and 11,1:

    ```
    ..............
    .......OOOOO..
    .......OOOOO..
    ..#XXXXOOOOO..
    ..XXXXXXXXXX..
    ..#XXXXXX#XX..
    .........XXX..
    .........#X#..
    ..............
    ```

    Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:

    ```
    ..............
    .......#XXX#..
    .......XXXXX..
    ..#XXXX#XXXX..
    ..XXXXXXXXXX..
    ..#XXXXXXOXX..
    .........OXX..
    .........OX#..
    ..............
    ```

    The largest rectangle you can make in this example using only red and green tiles has area 24. One way to do this is between 9,5 and 2,3:

    ```
    ..............
    .......#XXX#..
    .......XXXXX..
    ..OOOOOOOOXX..
    ..OOOOOOOOXX..
    ..OOOOOOOOXX..
    .........XXX..
    .........#X#..
    ..............
    ```

    Using two red tiles as opposite corners, what is the largest area of any rectangle you can make using only red and green tiles?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(namedtuple):
    def exercise_9_2_find_largest_area(
        red_tile_data: list[str], number_of_sampled_edge_points: int
    ) -> tuple[int, list[list[int]] | None]:
        """
        Find the largest axis-aligned rectangle using only red and green tiles.

        Red tiles form the vertices of a closed, orthogonal loop. Consecutive
        red tiles are connected by straight lines of green tiles, and all tiles
        inside this loop are also green. The loop defines a simple orthogonal
        polygon without holes.

        The rectangle must use two red tiles as opposite corners. All tiles
        inside the rectangle, including its boundary, must lie entirely within
        the red-green region defined by the polygon.

        The core geometric insight is:
        - A point is inside if it is bounded on all sides.

        For each candidate rectangle, only points on the rectangle boundary
        are tested. If every sampled boundary point is bounded on all four
        cardinal directions by polygon edges, the rectangle is guaranteed to
        lie fully inside the allowed region.

        Early pruning is applied to discard rectangle candidates whose area
        cannot exceed the current maximum.

        Args:
            red_tile_coordinates (list[str]):
                Ordered list of red tile coordinates as "x,y" strings. Adjacent
                entries are connected by straight horizontal or vertical paths.
            number_of_sampled_edge_points (int): Number of points to sample on
                the rectangle edges, includes the corner points, so the minimum
                value for this variable is 2.

        Returns:
            tuple[int, list[list[int]] | None]:
                The largest rectangle area that can be formed using only red
                and green tiles, and the corner coordinates of that rectangle.
        """
        Point = namedtuple("Point", ["x", "y"])

        # Get data in appropriate format.
        red_tile_coordinates = [
            Point(*[int(num) for num in row.split(",")]) for row in red_tile_data
        ]

        # Build edges (normalized)
        horizontal_edges = []
        vertical_edges = []

        for current, next in zip(
            red_tile_coordinates, red_tile_coordinates[1:] + red_tile_coordinates[:1]
        ):
            if current.y == next.y:
                horizontal_edges.append(
                    (current.y, (min(current.x, next.x), max(current.x, next.x)))
                )
            elif current.x == next.x:
                vertical_edges.append(
                    (current.x, (min(current.y, next.y), max(current.y, next.y)))
                )

        horizontal_edges.sort()
        vertical_edges.sort()

        def is_surrounded(
            corner: Point,  # pyright: ignore[reportInvalidTypeForm]
            horizontal_edges: list[tuple[int, tuple[int, int]]] = horizontal_edges,
            vertical_edges: list[tuple[int, tuple[int, int]]] = vertical_edges,
        ) -> bool:
            """
            Determine whether a point lies inside the red-green polygon.

            The polygon is represented implicitly by horizontal and vertical edges.
            A point is considered inside (or on the boundary) if it is blocked by
            at least one polygon edge in all four cardinal directions.

            This function checks for:
            - A vertical edge to the left
            - A vertical edge to the right
            - A horizontal edge below
            - A horizontal edge above

            The defining principle is:
            A point is inside if it is bounded on all sides.

            This test is a specialized ray-casting variant optimized for simple
            orthogonal polygons without holes.

            Args:
                corner (Point):
                    The point to test for containment.
                horizontal_edges (list[tuple[int, tuple[int, int]]]):
                    Horizontal polygon edges as (y, (x_min, x_max)).
                vertical_edges (list[tuple[int, tuple[int, int]]]):
                    Vertical polygon edges as (x, (y_min, y_max)).

            Returns:
                bool:
                    True if the point is inside or on the boundary of the polygon,
                    False otherwise.
            """
            horizontal_left = False
            horizontal_right = False
            vertical_down = False
            vertical_up = False

            for _, (low, high) in ((k, v) for k, v in vertical_edges if k <= corner.x):
                if low <= corner.y <= high:
                    horizontal_left = True
                    break

            for _, (low, high) in ((k, v) for k, v in vertical_edges if k >= corner.x):
                if low <= corner.y <= high:
                    horizontal_right = True
                    break

            for _, (low, high) in (
                (k, v) for k, v in horizontal_edges if k <= corner.y
            ):
                if low <= corner.x <= high:
                    vertical_down = True
                    break

            for _, (low, high) in (
                (k, v) for k, v in horizontal_edges if k >= corner.y
            ):
                if low <= corner.x <= high:
                    vertical_up = True
                    break

            return (
                horizontal_left and horizontal_right and vertical_down and vertical_up
            )

        def interpolate_edge_points(
            start_coordinate: int,
            end_coordinate: int,
            number_of_interpolated_points: int,
        ) -> list[int]:
            """
            Construct integer sample points along a rectangle edge by interpolation.

            Args:
                start_coordinate (int): Start coordinate.
                end_coordinate (int): End coordinate.
                number_of_interpolated_points (int): Number of points to sample along the
                    edge (must be >= 2).

            Returns:
                list[int]: Integer coordinates sampled between the start and end values,
                    inclusive.
            """
            assert number_of_interpolated_points >= 2, (
                "number_of_interpolated_points must be at least 2"
            )

            if number_of_interpolated_points == 2:
                return [start_coordinate, end_coordinate]

            step = (end_coordinate - start_coordinate) / (
                number_of_interpolated_points - 1
            )
            interpolated_coordinates = [
                round(start_coordinate + i * step)
                for i in range(number_of_interpolated_points)
            ]

            return interpolated_coordinates

        largest_rect_area = 0
        largest_rect_coordinates = None

        # Main loop
        for i in range(len(red_tile_coordinates)):
            for j in range(i):
                c1 = red_tile_coordinates[i]
                c3 = red_tile_coordinates[j]

                if c1.x != c3.x and c1.y != c3.y:
                    width = 1 + abs(c1.x - c3.x)
                    height = 1 + abs(c1.y - c3.y)
                    rectangle_area = width * height

                    # Early pruning
                    if rectangle_area <= largest_rect_area:
                        continue

                    c4 = Point(x=c1.x, y=c3.y)
                    c2 = Point(x=c3.x, y=c1.y)

                    xs = interpolate_edge_points(
                        c1.x, c3.x, number_of_sampled_edge_points
                    )
                    ys = interpolate_edge_points(
                        c1.y, c3.y, number_of_sampled_edge_points
                    )

                    test_points = []

                    for x in xs:
                        test_points.append(Point(x, c1.y))
                        test_points.append(Point(x, c3.y))

                    for y in ys:
                        test_points.append(Point(c1.x, y))
                        test_points.append(Point(c3.x, y))

                    if all(is_surrounded(p) for p in test_points):
                        largest_rect_area = rectangle_area
                        largest_rect_coordinates = [c1, c4, c3, c2]

        return largest_rect_area, largest_rect_coordinates

    return (exercise_9_2_find_largest_area,)


@app.cell
def _(example_red_tile_data, exercise_9_2_find_largest_area):
    solution_example_9_2, _ = exercise_9_2_find_largest_area(
        red_tile_data=example_red_tile_data, number_of_sampled_edge_points=2
    )

    assert solution_example_9_2 == 24
    return


@app.cell
def _(exercise_9_2_find_largest_area, red_tile_data):
    # Empirically determined that 44 is the first integer that produces the correct answer.
    # Takes about 40 seconds to retrieve the result.
    # Replacing the sampling method with a more sophisticated method that does not perform
    # duplicate computations will significantly improve the computation time.
    number_of_sampled_edge_points = 44

    solution_9_2, largest_rect_coordinates_9_2 = exercise_9_2_find_largest_area(
        red_tile_data=red_tile_data,
        number_of_sampled_edge_points=number_of_sampled_edge_points,
    )

    assert solution_9_2 == 1513792010
    return (largest_rect_coordinates_9_2,)


@app.cell
def _(largest_rect_coordinates_9_2, mo, plot_red_tiles, red_tile_data):
    red_tile_coordinates_9_2 = [
        [int(num) for num in row.split(",")] for row in red_tile_data
    ]

    figure_9_2 = plot_red_tiles(
        red_tile_coordinates=red_tile_coordinates_9_2,
        largest_rect_coordinates=largest_rect_coordinates_9_2,
    )

    mo.accordion({"Interactive plot": figure_9_2})  # pyright: ignore[reportUnusedExpression]
    return (figure_9_2,)


@app.cell
def _(base64, figure_9_2, mo, warnings):
    # Kaleido 0.2.1 (pinned, as kaleido 1.x needs Chrome) raises a deprecation warning here.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        figure_png_9_2 = figure_9_2.to_image(format="png")

    encoded_figure_9_2 = base64.b64encode(figure_png_9_2).decode()

    mo.md(f"![Largest rectangle](data:image/png;base64,{encoded_figure_9_2})")  # pyright: ignore[reportUnusedExpression]


if __name__ == "__main__":
    app.run()
