import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 10
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

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 10: Elves Look, Elves Say
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
    Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

    Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

    For example:

    - 1 becomes 11 (1 copy of digit 1).
    - 11 becomes 21 (2 copies of digit 1).
    - 21 becomes 1211 (one 2 followed by one 1).
    - 1211 becomes 111221 (one 1, one 2, and two 1s).
    - 111221 becomes 312211 (three 1s, two 2s, and one 1).

    Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

    Your puzzle input is 1113222113
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_10_1_compute_look_and_say_sequence(
    start_value: str, number_of_iterations: int
) -> list[str]:
    """
    Apply the look-and-say transformation iteratively, returning the full sequence.

    Each step reads the current value as runs of identical digits and encodes
    each run as its length followed by the digit. The returned list includes
    the original start_value as the first element.

    Args:
        start_value (str): The initial digit string to begin the sequence from.
        number_of_iterations (int): The number of look-and-say steps to apply.

    Returns:
        look_and_say_sequence (list[str]): All values in the sequence, from
            start_value through the final transformed value.
    """
    look_and_say_sequence = [start_value]
    current_value = start_value

    for _ in range(number_of_iterations):
        next_value = ""
        char_index = 0

        while char_index < len(current_value):
            cur_char = current_value[char_index]
            char_counter = 1

            while (
                char_index + char_counter < len(current_value)
                and current_value[char_index + char_counter] == cur_char
            ):
                char_counter += 1

            next_value += f"{char_counter}{cur_char}"
            char_index += char_counter

        look_and_say_sequence.append(next_value)
        current_value = next_value

    return look_and_say_sequence


@app.cell
def _():
    solution_10_1_length_result = exercise_10_1_compute_look_and_say_sequence(
        start_value="1113222113", number_of_iterations=40
    )

    assert len(solution_10_1_length_result[-1]) == 252594
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

    Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _():
    solution_10_2_length_result = exercise_10_1_compute_look_and_say_sequence(
        start_value="1113222113", number_of_iterations=50
    )

    assert len(solution_10_2_length_result[-1]) == 3579328
    return


if __name__ == "__main__":
    app.run()
