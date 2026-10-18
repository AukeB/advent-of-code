import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 18

    https://adventofcode.com/2015/day/18
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
    ## Day 18 - Like a GIF For Your Yard
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
    from dataclasses import dataclass

    @dataclass
    class Light:
        """A single light on the board.

        Attributes:
            state: True if the light is on, False if it is off.
        """

        state: bool

    class Board:
        """Grid of lights that evolves according to Conway's Game of Life rules.

        The board can optionally hold its four corner lights permanently on.
        """

        def __init__(
            self,
            grid_of_lights: list[str],
            num_iterations: int,
            corner_lights_stuck_on: bool = False,
        ) -> None:
            """Create a board from text rows and set up the corner handling.

            Args:
                grid_of_lights: Rows of the grid. Each character is '#' for a
                    lit light or '.' for an unlit one.
                num_iterations: Number of generations to simulate.
                corner_lights_stuck_on: If True, the four corner lights are
                    turned on at the start and stay on after every generation.
            """
            self.board: list[list[Light]] = [
                [Light(state=(light == "#")) for light in row_of_lights]
                for row_of_lights in grid_of_lights
            ]

            self.board_size: tuple[int, int] = (len(self.board), len(self.board[0]))
            self.num_iterations = num_iterations
            self.corner_lights_stuck_on = corner_lights_stuck_on

            self.corner_coordinates: list[tuple[int, int]] = [
                (0, 0),
                (0, self.board_size[1] - 1),
                (self.board_size[0] - 1, 0),
                (self.board_size[0] - 1, self.board_size[1] - 1),
            ]

            if self.corner_lights_stuck_on:
                for cy, cx in self.corner_coordinates:
                    self.board[cy][cx].state = True

            self.relative_neighbor_coordinates: list[tuple[int, int]] = [
                (-1, -1),
                (0, -1),
                (1, -1),
                (-1, 0),
                (1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
            ]

        def get(self, y: int, x: int) -> Light | None:
            """Return the light at a position on the board.

            Args:
                y: Row index, counting from the top, starting at 0.
                x: Column index, counting from the left, starting at 0.

            Returns:
                The Light at (y, x), or None if the position lies outside the
                    grid.
            """
            if 0 <= y < self.board_size[0] and 0 <= x < self.board_size[1]:
                return self.board[y][x]

            return None

        def _compute_number_of_neighbors(self, y: int, x: int) -> int:
            """Count how many of the eight surrounding lights are on.

            Args:
                y: Row index of the light whose neighbors are counted.
                x: Column index of the light whose neighbors are counted.

            Returns:
                The number of lit neighbors, from 0 to 8. Neighbors that fall
                outside the grid are not counted.
            """
            light_on_counter: int = 0

            for dx, dy in self.relative_neighbor_coordinates:
                neighbor = self.get(y + dy, x + dx)
                if neighbor is not None and neighbor.state:
                    light_on_counter += 1

            return light_on_counter

        def _run_iteration(self) -> None:
            """Advance the board by one generation.

            All lights are updated simultaneously from the current state. A lit
            light stays on with 2 or 3 lit neighbors. An unlit light turns on
            with exactly 3 lit neighbors. If corner lights are stuck on, the
            four corners are always on after the update. The new grid replaces
            the old one.
            """
            new_board: list[list[Light]] = []

            for y in range(self.board_size[0]):
                new_row: list[Light] = []

                for x in range(self.board_size[1]):
                    light = self.board[y][x]
                    num_neighbors = self._compute_number_of_neighbors(y=y, x=x)

                    next_is_on = (light.state and num_neighbors in (2, 3)) or (
                        not light.state and num_neighbors == 3
                    )

                    if (
                        self.corner_lights_stuck_on
                        and (y, x) in self.corner_coordinates
                    ):
                        next_is_on = True

                    new_row.append(Light(state=next_is_on))

                new_board.append(new_row)

            self.board = new_board

        def run_simulation(self) -> int:
            """Run the simulation for the configured number of generations.

            Returns:
                The number of lights that are on after the final generation.
            """
            for _ in range(self.num_iterations):
                self._run_iteration()

            number_of_lights_on = sum(
                light.state for row in self.board for light in row
            )

            return number_of_lights_on

    return (Board,)


@app.cell
def _(Board, read_data):
    grid_of_lights: list[str] = read_data(
        file_path="data/2015/2015_day_18.txt", separator="\n"
    )

    board = Board(grid_of_lights=grid_of_lights, num_iterations=100)

    number_of_lights_on = board.run_simulation()
    assert number_of_lights_on == 1061
    return (grid_of_lights,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(Board, grid_of_lights: list[str]):
    board_part_2 = Board(
        grid_of_lights=grid_of_lights, num_iterations=100, corner_lights_stuck_on=True
    )

    number_of_lights_on_part_2 = board_part_2.run_simulation()
    assert number_of_lights_on_part_2 == 1006
    return


if __name__ == "__main__":
    app.run()
