import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 7

    https://adventofcode.com/2015/day/7
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
    ## Day 7: Probably a Fire Hazard
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
    def _get_wire_value(element: str, wire_signal_values: dict[str, int | None]) -> int:
        """Resolve an element to its integer value.

        Accepts either a numeric literal or a wire name. Raises ValueError if
        the wire has not yet been assigned a value, signalling the caller to
        skip this instruction and retry on the next iteration.

        Args:
            element (str): A wire name or numeric literal.
            wire_signal_values (dict[str, int | None]): Current known wire
                values.

        Returns:
            value (int): The resolved integer value.

        Raises:
            ValueError: If the wire has no value yet.
        """
        value = int(element) if element.isdigit() else wire_signal_values.get(element)

        if value is None:
            raise ValueError

        return value

    def exercise_7_1_find_signal_value(
        instruction_booklet: list[str],
        number_of_bits_max_signal: int = 16,
    ) -> dict[str, int | None]:
        """Find the signal value of each wire after processing all instructions.

        Iterates over instructions repeatedly until all wires have been assigned
        a value. Instructions that depend on wires not yet resolved are skipped
        and retried in the next iteration.

        Args:
            instruction_booklet (list[str]): The puzzle input lines.
            number_of_bits_max_signal (int): Bit width of wire signals, defaults
                to 16.

        Returns:
            wire_signal_values (dict[str, int]): Mapping of wire name to its
                final signal.
        """
        arrow_definition = "->"
        max_signal_value = 2**number_of_bits_max_signal - 1
        all_output_wires = {line.split()[-1] for line in instruction_booklet}
        wire_signal_values: dict[str, int | None] = {}

        while any(wire not in wire_signal_values for wire in all_output_wires):
            for instruction_line in instruction_booklet:
                instruction_elements = instruction_line.split()
                index_arrow = instruction_elements.index(arrow_definition)
                instruction_input = instruction_elements[:index_arrow]
                output_wire = instruction_elements[-1]

                try:
                    if len(instruction_input) == 1:
                        wire_signal_values[output_wire] = _get_wire_value(
                            instruction_input[0], wire_signal_values
                        )

                    elif len(instruction_input) == 2:
                        wire_signal_values[output_wire] = (
                            ~_get_wire_value(instruction_input[1], wire_signal_values)
                            & max_signal_value
                        )

                    elif len(instruction_input) == 3:
                        first_element, operator, second_element = instruction_input

                        if operator == "AND":
                            wire_signal_values[output_wire] = _get_wire_value(
                                first_element, wire_signal_values
                            ) & _get_wire_value(second_element, wire_signal_values)
                        elif operator == "OR":
                            wire_signal_values[output_wire] = _get_wire_value(
                                first_element, wire_signal_values
                            ) | _get_wire_value(second_element, wire_signal_values)
                        elif operator == "LSHIFT":
                            wire_signal_values[output_wire] = (
                                _get_wire_value(first_element, wire_signal_values)
                                << int(second_element)
                                & max_signal_value
                            )
                        elif operator == "RSHIFT":
                            wire_signal_values[output_wire] = _get_wire_value(
                                first_element, wire_signal_values
                            ) >> int(second_element)

                except ValueError:
                    continue

        result = dict(sorted(wire_signal_values.items()))

        return result

    return (exercise_7_1_find_signal_value,)


@app.cell
def _(exercise_7_1_find_signal_value):
    example_data_7_1 = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]

    example_wire_signal_values = exercise_7_1_find_signal_value(
        instruction_booklet=example_data_7_1
    )

    assert example_wire_signal_values == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }
    return


@app.cell
def _(exercise_7_1_find_signal_value, read_data):
    instruction_booklet: list[str] = read_data(
        file_path="data/2015/2015_day_07.txt", separator="\n"
    )

    wire_signal_values = exercise_7_1_find_signal_value(
        instruction_booklet=instruction_booklet
    )

    assert wire_signal_values["a"] == 956
    return (instruction_booklet,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(exercise_7_1_find_signal_value, instruction_booklet: list[str]):
    instruction_booklet_2 = instruction_booklet.copy()
    index_b = [line.split()[-1] for line in instruction_booklet_2].index("b")
    instruction_booklet_2[index_b] = "956 -> b"

    wire_signal_values_2 = exercise_7_1_find_signal_value(
        instruction_booklet=instruction_booklet_2
    )

    assert wire_signal_values_2["a"] == 40149
    return


if __name__ == "__main__":
    app.run()
