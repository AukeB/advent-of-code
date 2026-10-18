import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 11

    https://adventofcode.com/2025/day/11
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
    ## Day 11 - Reactor
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_11_1_find_all_device_paths(
    list_of_devices: list[str],
    start_device_name: str = "you",
    end_device_name: str = "out",
) -> int:
    """Count all directed paths from a start device to an end device.

    The input defines a directed graph where each line maps a device to its
    output devices. The function builds the graph and uses a memoized DFS to
    count all unique paths from the start device to the end device.

    Args:
        list_of_devices (list[str]): Lines describing device connections.
        start_device_name (str): Device where traversal begins.
        end_device_name (str): Target device for path counting.

    Returns:
        int: Number of distinct paths from start to end.
    """
    device_mapping = {}

    for device in list_of_devices:
        device_name, device_output = device.split(":")
        device_output = device_output.strip().split(" ")
        device_mapping[device_name] = device_output

    number_of_paths = {}

    def find_number_of_paths(node: str) -> int:
        """Return the number of paths from the given node to the end device.

        Results are cached to avoid recomputing path counts for nodes that have
        already been processed.

        Args:
            node (str): The current device being explored.

        Returns:
            int: Number of paths from this node to the end device.
        """
        if node in number_of_paths:
            return number_of_paths[node]

        if node == end_device_name:
            return 1

        number_of_paths[node] = sum(
            find_number_of_paths(next_node) for next_node in device_mapping[node]
        )

        return number_of_paths[node]

    return find_number_of_paths(node=start_device_name)


@app.cell
def _():
    example_list_of_devices_part_1 = [
        "aaa: you hhh",
        "you: bbb ccc",
        "bbb: ddd eee",
        "ccc: ddd eee fff",
        "ddd: ggg",
        "eee: out",
        "fff: out",
        "ggg: out",
        "hhh: ccc fff iii",
        "iii: out",
    ]

    solution_example_11_1 = exercise_11_1_find_all_device_paths(
        list_of_devices=example_list_of_devices_part_1
    )

    assert solution_example_11_1 == 5
    return


@app.cell
def _(exercise_11_1_find_all_device_paths, read_data):
    list_of_devices = read_data(file_path="data/2025/2025_day_11.txt", separator="\n")

    solution_11_1 = exercise_11_1_find_all_device_paths(list_of_devices=list_of_devices)

    assert solution_11_1 == 670
    return (list_of_devices,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_11_2_find_all_device_paths(
    list_of_devices: list[str],
    start_device_name: str = "svr",
    end_device_name: str = "out",
    mid_device_names: list[str] = ["fft", "dac"],
) -> int:
    """Count all directed paths from `start_device_name` to `end_device_name`
    that visit all devices listed in `mid_device_names` at least once. Uses a
    memoized depth-first search (DFS) to efficiently compute the number of valid
    paths.

    Args:
        list_of_devices (list[str]): Each element is a string describing a
            device and its outputs, in the format "device: output1 output2 ...".
        start_device_name (str): The device from which to start path traversal.
            Default is "svr".
        end_device_name (str): The target device where paths end. Default is
            "out".
        mid_device_names (list[str]): Devices that must be visited along the
            path. Default is ["fft", "dac"].

    Returns:
        int: The total number of distinct paths from `start_device_name` to
            `end_device_name` that pass through all devices in
            `mid_device_names`.
    """
    device_mapping = {}

    for device in list_of_devices:
        device_name, device_output = device.split(":")
        device_output = device_output.strip().split(" ")
        device_mapping[device_name] = device_output

    number_of_valid_paths = {}

    def find_number_of_paths(node: str, visited_nodes: frozenset) -> int:
        """Recursively count paths from the current `node` to `end_device_name`,
        while keeping track of which required mid-nodes have been visited.

        Args:
            node (str): The current device in the path.
            visited_nodes (frozenset): The set of mid-device names visited so
                far.

        Returns:
            int: The number of valid paths from this node to `end_device_name`
                that include all required mid-device nodes.
        """

        """Instead of just having the node as key, a tuple is created consisting
        of the node and a frozen set of visited nodes. The set if frozen so that
        it can be used as a key of the dictionary.
        """
        key = (node, visited_nodes)

        if key in number_of_valid_paths:
            return number_of_valid_paths[key]

        """If the current node is in mid_device_names, overwrite the frozen set
        with a new one that contains the current node.
        """
        if node in mid_device_names:
            visited_nodes = visited_nodes | {node}

        if node == end_device_name:
            # Only return 1 if the mid_device_names were traversed.
            count = 1 if visited_nodes == frozenset(mid_device_names) else 0
            number_of_valid_paths[key] = count
            return count

        number_of_valid_paths[key] = sum(
            find_number_of_paths(next_node, visited_nodes)
            for next_node in device_mapping[node]
        )

        return number_of_valid_paths[key]

    return find_number_of_paths(start_device_name, frozenset())


@app.cell
def _():
    example_list_of_devices_part_2 = [
        "svr: aaa bbb",
        "aaa: fft",
        "fft: ccc",
        "bbb: tty",
        "tty: ccc",
        "ccc: ddd eee",
        "ddd: hub",
        "hub: fff",
        "eee: dac",
        "dac: fff",
        "fff: ggg hhh",
        "ggg: out",
        "hhh: out",
    ]

    solution_example_11_2 = exercise_11_2_find_all_device_paths(
        list_of_devices=example_list_of_devices_part_2
    )

    assert solution_example_11_2 == 2
    return


@app.cell
def _(exercise_11_2_find_all_device_paths, list_of_devices):
    solution_11_2 = exercise_11_2_find_all_device_paths(list_of_devices=list_of_devices)

    assert solution_11_2 == 332052564714990
    return


if __name__ == "__main__":
    app.run()
