import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 8
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

    from collections import Counter

    from aoc.utils import read_data

    return Counter, mo, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 8 - Playground
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
    Equipped with a new understanding of teleporter maintenance, you confidently step onto the repaired teleporter pad.

    You rematerialize on an unfamiliar teleporter pad and find yourself in a vast underground space which contains a giant playground!

    Across the playground, a group of Elves are working on setting up an ambitious Christmas decoration project. Through careful rigging, they have suspended a large number of small electrical junction boxes.

    Their plan is to connect the junction boxes with long strings of lights. Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes.

    The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

    For example:

    ```
    162,817,812
    57,618,57
    906,360,560
    592,479,940
    352,342,300
    466,668,158
    542,29,236
    431,825,988
    739,650,466
    52,470,668
    216,146,977
    819,987,18
    117,168,530
    805,96,715
    346,949,466
    970,615,88
    941,993,340
    862,61,35
    984,92,344
    425,690,689
    ```

    This list describes the position of 20 junction boxes, one per line. Each position is given as X,Y,Z coordinates. So, the first junction box in the list is at X=162, Y=817, Z=812.

    To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible according to straight-line distance. In this example, the two junction boxes which are closest together are 162,817,812 and 425,690,689.

    By connecting these two junction boxes together, because electricity can flow between them, they become part of the same circuit. After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.

    Now, the two junction boxes which are closest together but aren't already directly connected are 162,817,812 and 431,825,988. After connecting them, since 162,817,812 is already connected to another junction box, there is now a single circuit which contains three junction boxes and an additional 17 circuits which contain one junction box each.

    The next two junction boxes to connect are 906,360,560 and 805,96,715. After connecting them, there is a circuit containing 3 junction boxes, a circuit containing 2 junction boxes, and 15 circuits which contain one junction box each.

    The next two junction boxes are 431,825,988 and 425,690,689. Because these two junction boxes were already in the same circuit, nothing happens!

    This process continues for a while, and the Elves are concerned that they don't have enough extension cables for all these circuits. They would like to know how big the circuits will be.

    After making the ten shortest connections, there are 11 circuits: one circuit which contains 5 junction boxes, one circuit which contains 4 junction boxes, two circuits which contain 2 junction boxes each, and seven circuits which each contain a single junction box. Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces 40.

    Your list contains many junction boxes; connect together the 1000 pairs of junction boxes which are closest together. Afterward, what do you get if you multiply together the sizes of the three largest circuits?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(Counter):
    def exercise_8_1_find_closest_junctions(
        junction_positions: list[str],
        number_of_connections: int,
    ) -> int:
        """Connects junction boxes based on closest distances and computes the
        product of the sizes of the three largest resulting circuits.

        Each junction box is represented by 3D coordinates. The function finds
        the specified number of closest junction pairs, merges them into
        circuits, and keeps track of connected components. After processing, it
        multiplies the sizes of the three largest circuits.

        Args:
            junction_positions (list[str]): List of junction positions as comma-
                separated strings "X,Y,Z".
            number_of_connections (int): Number of closest junction pairs to
                connect.

        Returns:
            int: Product of the sizes of the three largest connected circuits.
        """
        junction_coordinates = [
            [int(num) for num in row.split(",")] for row in junction_positions
        ]

        # First create a distance matrix.
        distance_matrix = []

        for i in range(len(junction_coordinates)):
            distance_matrix_row = []

            for j in range(len(junction_coordinates)):
                if j < i:
                    first_junction = junction_coordinates[i]
                    second_junction = junction_coordinates[j]

                    distance_sum = 0
                    for x1, x2 in zip(first_junction, second_junction):
                        distance_sum += (x1 - x2) ** 2

                    distance_matrix_row.append(distance_sum)
                else:
                    distance_matrix_row.append(None)
            distance_matrix.append(distance_matrix_row)

        # Next turn this distance matrix into a dictionary that is sorted by distance.
        distance_pairs = {}

        for i in range(len(distance_matrix)):
            for j in range(len(distance_matrix[0])):
                if j < i:
                    distance_pairs[(i, j)] = distance_matrix[i][j]

        sorted_distance_pairs = dict(
            sorted(
                distance_pairs.items(),
                key=lambda item: (item[1], item[0][0], item[0][1]),
            )
        )

        # This variable keeps track of all the chains of junction boxes. Every coordinate
        # of a junction box is initialized with a value of -1 (the id for the chain), which
        # means it is not part of a chain yet.
        chains = {tuple(coordinates): -1 for coordinates in junction_coordinates}
        processed_pairs: int = 0

        for i, j in sorted_distance_pairs.keys():
            processed_pairs += 1

            if processed_pairs > number_of_connections:
                break

            junction_1 = tuple(junction_coordinates[i])
            junction_2 = tuple(junction_coordinates[j])

            set_1 = chains[junction_1]
            set_2 = chains[junction_2]

            if set_1 == -1 and set_2 == -1:
                new_chain_id = max(chains.values()) + 1

                chains[junction_1] = new_chain_id
                chains[junction_2] = new_chain_id
            elif set_1 > -1 and set_2 == -1:
                chains[junction_2] = set_1
            elif set_2 > -1 and set_1 == -1:
                chains[junction_1] = set_2
            elif set_1 > -1 and set_2 > -1:
                if set_1 == set_2:
                    pass
                elif set_1 != set_2:
                    for chain in chains:
                        if chains[chain] == set_2:
                            chains[chain] = set_1

        counts_per_chain = Counter(chains.values())
        chain_counter = [
            count for chain_id, count in counts_per_chain.items() if chain_id != -1
        ]
        chain_counter.sort(reverse=True)
        final_answer = chain_counter[0] * chain_counter[1] * chain_counter[2]

        return final_answer

    return (exercise_8_1_find_closest_junctions,)


@app.cell
def _(exercise_8_1_find_closest_junctions):
    example_junction_positions = [
        "162,817,812",
        "57,618,57",
        "906,360,560",
        "592,479,940",
        "352,342,300",
        "466,668,158",
        "542,29,236",
        "431,825,988",
        "739,650,466",
        "52,470,668",
        "216,146,977",
        "819,987,18",
        "117,168,530",
        "805,96,715",
        "346,949,466",
        "970,615,88",
        "941,993,340",
        "862,61,35",
        "984,92,344",
        "425,690,689",
    ]

    solution_example_8_1 = exercise_8_1_find_closest_junctions(
        junction_positions=example_junction_positions, number_of_connections=10
    )

    assert solution_example_8_1 == 40
    return (example_junction_positions,)


@app.cell
def _(exercise_8_1_find_closest_junctions, read_data):
    junction_positions = read_data(
        file_path="data/2025/2025_day_08.txt", separator="\n"
    )

    solution_8_1 = exercise_8_1_find_closest_junctions(
        junction_positions=junction_positions, number_of_connections=1000
    )

    assert solution_8_1 == 102816
    return (junction_positions,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in one large circuit.

    Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.

    Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_8_2_merge_until_one_chain(
    junction_positions: list[str],
) -> int:
    """Connects junction boxes until all boxes form a single circuit, then
    returns the product of the X coordinates of the last two boxes connected.

    Each junction box is represented by 3D coordinates. The function repeatedly
    connects the closest unconnected pairs and merges their chains. Once all
    boxes belong to a single circuit, it multiplies the X coordinates of the
    final pair that merged the last two chains.

    Args:
        junction_positions (list[str]): List of junction positions as comma-
            separated strings "X,Y,Z".

    Returns:
        int: Product of the X coordinates of the last two junctions merged to
            form a single circuit.
    """
    junction_coordinates = [
        [int(num) for num in row.split(",")] for row in junction_positions
    ]

    # First create a distance matrix.
    distance_matrix = []

    for i in range(len(junction_coordinates)):
        distance_matrix_row = []

        for j in range(len(junction_coordinates)):
            if j < i:
                first_junction = junction_coordinates[i]
                second_junction = junction_coordinates[j]

                distance_sum = 0
                for x1, x2 in zip(first_junction, second_junction):
                    distance_sum += (x1 - x2) ** 2

                distance_matrix_row.append(distance_sum)
            else:
                distance_matrix_row.append(None)
        distance_matrix.append(distance_matrix_row)

    # Next turn this distance matrix into a dictionary that is sorted by distance.
    distance_pairs = {}

    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix[0])):
            if j < i:
                distance_pairs[(i, j)] = distance_matrix[i][j]

    sorted_distance_pairs = dict(
        sorted(
            distance_pairs.items(), key=lambda item: (item[1], item[0][0], item[0][1])
        )
    )

    # This variable keeps track of all the chains of junction boxes. Every coordinate
    # of a junction box is initialized with a value of -1 (the id for the chain), which
    # means it is not part of a chain yet.
    chains = {tuple(coordinates): -1 for coordinates in junction_coordinates}

    for i, j in sorted_distance_pairs.keys():
        junction_1 = tuple(junction_coordinates[i])
        junction_2 = tuple(junction_coordinates[j])

        set_1 = chains[junction_1]
        set_2 = chains[junction_2]

        if set_1 == -1 and set_2 == -1:
            new_chain_id = max(chains.values()) + 1

            chains[junction_1] = new_chain_id
            chains[junction_2] = new_chain_id
        elif set_1 > -1 and set_2 == -1:
            chains[junction_2] = set_1
        elif set_2 > -1 and set_1 == -1:
            chains[junction_1] = set_2
        elif set_1 > -1 and set_2 > -1:
            if set_1 == set_2:
                pass
            elif set_1 != set_2:
                for chain in chains:
                    if chains[chain] == set_2:
                        chains[chain] = set_1

        if -1 not in chains.values() and len(set(chains.values())) == 1:
            final_answer = junction_1[0] * junction_2[0]

            return final_answer

    raise ValueError("Junctions never merged into a single circuit")


@app.cell
def _(example_junction_positions):
    solution_example_8_2 = exercise_8_2_merge_until_one_chain(
        junction_positions=example_junction_positions
    )

    assert solution_example_8_2 == 25272
    return


@app.cell
def _(exercise_8_2_merge_until_one_chain, junction_positions):
    solution_8_2 = exercise_8_2_merge_until_one_chain(
        junction_positions=junction_positions
    )

    assert solution_8_2 == 100011612
    return


if __name__ == "__main__":
    app.run()
