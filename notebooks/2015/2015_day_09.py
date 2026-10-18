import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 9

    https://adventofcode.com/2015/day/9
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

    from itertools import permutations

    from aoc.utils import read_data

    return mo, np, permutations, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 9: All in a Single Night
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(np, permutations):
    def exercise_9_1_find_shortest_route(distances: list[str]) -> int:
        """Find the shortest route that visits every location exactly once using
        brute force.

        1. Extract all unique locations and map them to matrix indices.
        2. Build a symmetric distance matrix from the parsed input.
        3. Enumerate all possible routes via permutations and track the
           shortest.

        Args:
            distances (list[str]): Each line describes a distance in the format
                'A to B = N', where A and B are location names and N is the
                distance.

        Returns:
            shortest_route (int): The total distance of the shortest route that
                visits every location exactly once.
        """
        unique_locations = list({x.split()[i] for x in distances for i in (0, 2)})
        number_of_unique_locations = len(unique_locations)
        location_mapping = {
            location: unique_locations.index(location) for location in unique_locations
        }
        distance_matrix = np.zeros(
            [number_of_unique_locations, number_of_unique_locations], dtype=int
        )

        for line in distances:
            line_split = line.split()

            node_start: str = line_split[0]
            node_end: str = line_split[2]
            distance: int = int(line_split[4])

            distance_matrix[location_mapping[node_start]][
                location_mapping[node_end]
            ] = distance
            distance_matrix[location_mapping[node_end]][
                location_mapping[node_start]
            ] = distance

        all_possible_routes = permutations(range(number_of_unique_locations))
        shortest_route = float("inf")

        for route in all_possible_routes:
            distance_current_route = 0

            for cur_loc, next_loc in zip(route, route[1:]):
                distance_current_route += distance_matrix[cur_loc][next_loc]

            if distance_current_route < shortest_route:
                shortest_route = distance_current_route

        return int(shortest_route)

    return (exercise_9_1_find_shortest_route,)


@app.cell
def _(exercise_9_1_find_shortest_route, read_data):
    distances: list[str] = read_data(
        file_path="data/2015/2015_day_09.txt", separator="\n"
    )

    shortest_route = exercise_9_1_find_shortest_route(distances=distances)

    assert shortest_route == 207
    return (distances,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(np, permutations):
    def exercise_9_2_find_longest_route(distances: list[str]) -> int:
        """Find the longest route that visits every location exactly once using
        brute force.

        1. Extract all unique locations and map them to matrix indices.
        2. Build a symmetric distance matrix from the parsed input.
        3. Enumerate all possible routes via permutations and track the longest.

        Args:
            distances (list[str]): Each line describes a distance in the format
                'A to B = N', where A and B are location names and N is the
                distance.

        Returns:
            longest_route (int): The total distance of the longest route that
                visits every location exactly once.
        """
        unique_locations = list({x.split()[i] for x in distances for i in (0, 2)})
        number_of_unique_locations = len(unique_locations)
        location_mapping = {
            location: unique_locations.index(location) for location in unique_locations
        }
        distance_matrix = np.zeros(
            [number_of_unique_locations, number_of_unique_locations], dtype=int
        )

        for line in distances:
            line_split = line.split()

            node_start: str = line_split[0]
            node_end: str = line_split[2]
            distance: int = int(line_split[4])

            distance_matrix[location_mapping[node_start]][
                location_mapping[node_end]
            ] = distance
            distance_matrix[location_mapping[node_end]][
                location_mapping[node_start]
            ] = distance

        all_possible_routes = permutations(range(number_of_unique_locations))
        longest_route = 0

        for route in all_possible_routes:
            distance_current_route = 0

            for cur_loc, next_loc in zip(route, route[1:]):
                distance_current_route += distance_matrix[cur_loc][next_loc]

            if distance_current_route > longest_route:
                longest_route = distance_current_route

        return int(longest_route)

    return (exercise_9_2_find_longest_route,)


@app.cell
def _(distances: list[str], exercise_9_2_find_longest_route):
    longest_route = exercise_9_2_find_longest_route(distances=distances)

    assert longest_route == 804
    return


if __name__ == "__main__":
    app.run()
