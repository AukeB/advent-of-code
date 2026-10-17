import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 11
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
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ou hear some loud beeping coming from a hatch in the floor of the factory, so you decide to check it out. Inside, you find several large electrical conduits and a ladder.

    Climbing down the ladder, you discover the source of the beeping: a large, toroidal reactor which powers the factory above. Some Elves here are hurriedly running between the reactor and a nearby server rack, apparently trying to fix something.

    One of the Elves notices you and rushes over. "It's a good thing you're here! We just installed a new server rack, but we aren't having any luck getting the reactor to communicate with it!" You glance around the room and see a tangle of cables and devices running from the server rack to the reactor. She rushes off, returning a moment later with a list of the devices and their outputs (your puzzle input).

    For example:

    ```
    aaa: you hhh
    you: bbb ccc
    bbb: ddd eee
    ccc: ddd eee fff
    ddd: ggg
    eee: out
    fff: out
    ggg: out
    hhh: ccc fff iii
    iii: out
    ```

    Each line gives the name of a device followed by a list of the devices to which its outputs are attached. So, bbb: ddd eee means that device bbb has two outputs, one leading to device ddd and the other leading to device eee.

    The Elves are pretty sure that the issue isn't due to any specific device, but rather that the issue is triggered by data following some specific path through the devices. Data only ever flows from a device through its outputs; it can't flow backwards.

    After dividing up the work, the Elves would like you to focus on the devices starting with the one next to you (an Elf hastily attaches a label which just says you) and ending with the main output to the reactor (which is the device with the label out).

    To help the Elves figure out which path is causing the issue, they need you to find every path from you to out.

    In this example, these are all of the paths from you to out:

    - Data could take the connection from you to bbb, then from bbb to ddd, then from ddd to ggg, then from ggg to out.
    - Data could take the connection to bbb, then to eee, then to out.
    - Data could go to ccc, then ddd, then ggg, then out.
    - Data could go to ccc, then eee, then out.
    - Data could go to ccc, then fff, then out.

    In total, there are 5 different paths leading from you to out.

    How many different paths lead from you to out?
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
    """
    Count all directed paths from a start device to an end device.

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
        """
        Return the number of paths from the given node to the end device.

        Results are cached to avoid recomputing path counts for nodes that
        have already been processed.

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
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Thanks in part to your analysis, the Elves have figured out a little bit about the issue. They now know that the problematic data path passes through both dac (a digital-to-analog converter) and fft (a device which performs a fast Fourier transform).

    They're still not sure which specific path is the problem, and so they now need you to find every path from svr (the server rack) to out. However, the paths you find must all also visit both dac and fft (in any order).

    For example:

    ```
    svr: aaa bbb
    aaa: fft
    fft: ccc
    bbb: tty
    tty: ccc
    ccc: ddd eee
    ddd: hub
    hub: fff
    eee: dac
    dac: fff
    fff: ggg hhh
    ggg: out
    hhh: out
    ```

    This new list of devices contains many paths from svr to out:

    ```
    svr,aaa,fft,ccc,ddd,hub,fff,ggg,out
    svr,aaa,fft,ccc,ddd,hub,fff,hhh,out
    svr,aaa,fft,ccc,eee,dac,fff,ggg,out
    svr,aaa,fft,ccc,eee,dac,fff,hhh,out
    svr,bbb,tty,ccc,ddd,hub,fff,ggg,out
    svr,bbb,tty,ccc,ddd,hub,fff,hhh,out
    svr,bbb,tty,ccc,eee,dac,fff,ggg,out
    svr,bbb,tty,ccc,eee,dac,fff,hhh,out
    ```

    However, only 2 paths from svr to out visit both dac and fft.

    Find all of the paths that lead from svr to out. How many of those paths visit both dac and fft?
    """)
    return


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
    """
    Count all directed paths from `start_device_name` to `end_device_name` that
    visit all devices listed in `mid_device_names` at least once. Uses a
    memoized depth-first search (DFS) to efficiently compute the number of
    valid paths.

    Args:
        list_of_devices (list[str]): Each element is a string describing a device
            and its outputs, in the format "device: output1 output2 ...".
        start_device_name (str): The device from which to start path traversal.
            Default is "svr".
        end_device_name (str): The target device where paths end. Default is "out".
        mid_device_names (list[str]): Devices that must be visited along the path.
            Default is ["fft", "dac"].

    Returns:
        int: The total number of distinct paths from `start_device_name` to
            `end_device_name` that pass through all devices in `mid_device_names`.
    """
    device_mapping = {}

    for device in list_of_devices:
        device_name, device_output = device.split(":")
        device_output = device_output.strip().split(" ")
        device_mapping[device_name] = device_output

    number_of_valid_paths = {}

    def find_number_of_paths(node: str, visited_nodes: frozenset) -> int:
        """
        Recursively count paths from the current `node` to `end_device_name`,
        while keeping track of which required mid-nodes have been visited.

        Args:
            node (str): The current device in the path.
            visited_nodes (frozenset): The set of mid-device names visited so far.

        Returns:
            int: The number of valid paths from this node to `end_device_name`
                that include all required mid-device nodes.
        """

        """
        Instead of just having the node as key, a tuple is created consisting
        of the node and a frozen set of visited nodes. The set if frozen
        so that it can be used as a key of the dictionary.
        """
        key = (node, visited_nodes)

        if key in number_of_valid_paths:
            return number_of_valid_paths[key]

        """
        If the current node is in mid_device_names, overwrite the frozen set
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
