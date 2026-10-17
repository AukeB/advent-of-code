import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 7
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
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

    Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

    The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

    For example:

    - 123 -> x means that the signal 123 is provided to wire x.
    - x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    - p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    - NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

    Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

    For example, here is a simple circuit:

    ```
    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i
    ```

    After it is run, these are the signals on the wires:

    ```
    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456
    ```

    In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
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
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
    """)
    return


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
