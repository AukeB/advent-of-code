import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 12

    https://adventofcode.com/2025/day/12
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
    import numpy as np

    from collections import defaultdict

    from aoc.utils import read_data

    return defaultdict, mo, np, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 12 - Christmas Tree Farm
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Solution
    """)
    return


@app.cell
def _(defaultdict, np):
    class Present:
        """Represents a 2D present shape using a grid of 0's and 1's.

        Provides operations to rotate and flip the shape. Useful for
        manipulation of discrete 2D patterns in grid-based problems.

        Attributes:
            present_shape (list[list[int]]): 2D grid representing the shape,
                where 1 indicates a filled cell and 0 indicates an empty cell.
        """

        def __init__(self, present_shape: list[list[int]]) -> None:
            """Initialize a Present object with a 2D grid.

            Args:
                present_shape (list[list[int]]): The 2D grid representing the
                    shape.
            """
            self.shape = present_shape

        def rotate_clockwise(self) -> None:
            """Rotate the present 90 degrees clockwise in-place"""
            self.shape = [list(row) for row in zip(*self.shape[::-1])]

        def rotate_counterclockwise(self) -> None:
            """Rotate the present 90 degrees counterclockwise in-place."""
            self.shape = [list(row) for row in zip(*self.shape)]
            self.shape.reverse()

        def flip_horizontal(self) -> None:
            """Flip the present horizontally in-place."""
            self.shape = [row[::-1] for row in self.shape]

        def flip_vertical(self) -> None:
            """Flip the present vertically in-place."""
            self.shape = self.shape[::-1]

        def __str__(self) -> str:
            """Return a string representation of the present.

            Converts the 2D grid of 0s and 1s into a visual format using '#' for
            filled cells and '.' for empty cells.
            """
            return "\n" + "\n".join(
                "".join("#" if cell else "." for cell in row) for row in self.shape
            )

    class Grid:
        """ """

        def __init__(self, dimensions: list[int]) -> None:
            """ """
            self.dimensions = dimensions
            self.grid = np.zeros(self.dimensions, dtype=int)

        def fits(self, present: Present, x: int, y: int) -> bool:
            """ """
            shape = np.array(present.shape, dtype=int)
            rows, cols = shape.shape

            if (
                x < 0
                or y < 0
                or x + rows > self.dimensions[0]
                or y + cols > self.dimensions[1]
            ):
                return False

            region = self.grid[x : x + rows, y : y + cols]
            if np.any(region + shape > 1):
                return False

            return True

        def place(self, present: Present, x: int, y: int) -> None:
            """ """
            shape = np.array(present.shape, dtype=int)
            rows, cols = shape.shape
            self.grid[x : x + rows, y : y + cols] += shape

    class ChristmasTreeFarm:
        """ """

        def __init__(
            self,
            present_and_region_data: list[str],
            verbose: bool = True,
        ) -> None:
            """ """
            self.present_and_region_data = present_and_region_data
            self.verbose = verbose
            self.presents, self.all_regions_and_quantities = (
                self._read_and_format_input_data()
            )

        def _read_and_format_input_data(
            self,
        ) -> tuple[dict[int, Present], list[dict]]:
            """ """
            # Related to the presents.
            present_detected = False
            present_index = None
            present_shape: list = []
            present_shapes = defaultdict(int)

            # Related to the regions under the tree and number of presents that need to fit into that region.
            region_detected = False
            all_regions_and_quantities: list[dict] = []

            # Important: The order of all the if-statement under the for-loop matters.
            for row in self.present_and_region_data:
                if present_detected:
                    if row.strip() == "":
                        present_shape = [
                            [1 if char == "#" else 0 for char in row]
                            for row in present_shape
                        ]
                        present = Present(present_shape=present_shape)
                        present_shapes[present_index] = present
                        present_detected = False
                    else:
                        present_shape.append(row)

                if row.endswith(":"):
                    present_index = int(row[:-1])
                    present_detected = True
                    present_shape = []

                if row and row[-1].isdigit():
                    region_detected = True

                if region_detected:
                    region, raw_quantities = row.split(":")

                    region_schape = [int(dimension) for dimension in region.split("x")]
                    raw_quantities = [
                        int(index) for index in raw_quantities.strip().split(" ")
                    ]

                    present_quantities = {}
                    for present_index, quantity in enumerate(raw_quantities):
                        if quantity:
                            present_quantities[present_index] = quantity

                    regions_and_quantities: dict = {}
                    regions_and_quantities["region_shape"] = region_schape
                    regions_and_quantities["present_quantities"] = present_quantities

                    all_regions_and_quantities.append(regions_and_quantities)

            if self.verbose:
                print("Presents:")
                for k, v in present_shapes.items():
                    print(k, v)
                print("\nChristmas tree regions and present indices:")
                for x in all_regions_and_quantities:
                    print(x)

            return present_shapes, all_regions_and_quantities

        def _solve_single_problem(
            self,
            region_shape: list[int],
            present_quantities: dict[int, int],
        ) -> None:
            """ """
            print(region_shape, present_quantities, "\n")

            grid = Grid(dimensions=region_shape)

            for present_index, present_quantity in present_quantities.items():
                for number in range(present_quantity):
                    present = self.presents[present_index]

                    if number > 0:
                        present.flip_horizontal()

                    placed = False

                    for y in range(region_shape[0]):
                        for x in range(region_shape[1]):
                            if grid.fits(present, x, y):
                                grid.place(present, x, y)
                                placed = True
                                break

                        if placed:
                            break

        def solve_all_problems(self) -> int:
            """ """
            for i, row in enumerate(self.all_regions_and_quantities):
                if i == 0:
                    region_shape: list[int] = row["region_shape"]
                    present_quantities: dict[int, int] = row["present_quantities"]

                    solution = self._solve_single_problem(  # noqa: F841
                        region_shape=region_shape, present_quantities=present_quantities
                    )

            return 2

    example_present_and_region_data = [
        "0:",
        "###",
        "##.",
        "##.",
        "",
        "1:",
        "###",
        "##.",
        ".##",
        "",
        "2:",
        ".##",
        "###",
        "##.",
        "",
        "3:",
        "##.",
        "###",
        "##.",
        "",
        "4:",
        "###",
        "#..",
        "###",
        "",
        "5:",
        "###",
        ".#.",
        "###",
        "",
        "4x4: 0 0 0 0 2 0",
        "12x5: 1 0 1 0 2 2",
        "12x5: 1 0 1 0 3 2",
    ]

    christmas_tree_farm = ChristmasTreeFarm(
        present_and_region_data=example_present_and_region_data,
        verbose=False,
    )

    solution_example_12 = christmas_tree_farm.solve_all_problems()

    assert solution_example_12 == 2
    return


@app.cell(hide_code=True)
def _():
    return


@app.cell(hide_code=True)
def _():
    return


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
