import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025 - Day 6
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
    ## Day 6 - Trash Compactor
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
    After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

    A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

    As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

    Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to either be either added (+) or multiplied (*) together.

    However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

    ```
    123 328  51 64
     45 64  387 23
      6 98  215 314
    *   +   *   +
    ```

    Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

    So, this worksheet contains four problems:

    - 123 * 45 * 6 = 33210
    - 328 + 64 + 98 = 490
    - 51 * 387 * 215 = 4243455
    - 64 + 23 + 314 = 401

    To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

    Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

    Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_6_1_help_with_math_homework(math_homework: list[str]) -> int:
    """
    Parses and solves a horizontally unrolled cephalopod math worksheet.

    Each column in the input represents one math problem. A problem consists of
    several numbers stacked vertically, with either '+' or '*' at the bottom
    indicating whether all numbers in that column should be added or multiplied.

    Columns are separated by whitespace, and the horizontal alignment of numbers
    is irrelevant. This function reconstructs the worksheet by splitting each
    row into meaningful tokens (integers or operators), then processes the grid
    column by column.

    For each column:
      - Read upward to collect all numbers.
      - Read the bottom cell to determine whether to sum or multiply them.
      - Compute the column’s result.

    The final answer is the sum of all individual column results.

    Args:
        math_homework (list[str]): The raw worksheet input, where each string is
            one row of the printed cephalopod homework.

    Returns
        int: The grand total: the sum of the results of all column-wise problems.
    """
    mult_and_add_matrix = []

    for row in math_homework:
        split_row = row.split(" ")
        formatted_row = []

        for row_element in split_row:
            if row_element == "":
                pass
            elif row_element == "+":
                formatted_row.append(row_element)
            elif row_element == "*":
                formatted_row.append(row_element)
            else:
                formatted_row.append(int(row_element))

        mult_and_add_matrix.append(formatted_row)

    total_sum_of_additions_and_multiplications = 0

    for j in range(len(mult_and_add_matrix[0])):
        add_or_multiply = ""
        numbers_to_add_or_multiply = []

        for i in range(len(mult_and_add_matrix) - 1, -1, -1):
            matrix_element = mult_and_add_matrix[i][j]

            if i == len(mult_and_add_matrix) - 1:
                if matrix_element == "+":
                    add_or_multiply = "add"
                elif matrix_element == "*":
                    add_or_multiply = "multiply"
            else:
                numbers_to_add_or_multiply.append(matrix_element)

        if add_or_multiply == "add":
            total_sum_of_additions_and_multiplications += sum(
                numbers_to_add_or_multiply
            )
        elif add_or_multiply == "multiply":
            product = 1
            for number in numbers_to_add_or_multiply:
                product *= number
            total_sum_of_additions_and_multiplications += product

    return total_sum_of_additions_and_multiplications


@app.cell
def _():
    example_math_homework = [
        "123 328  51 64",
        " 45 64  387 23",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]

    solution_example_6_1 = exercise_6_1_help_with_math_homework(
        math_homework=example_math_homework
    )

    assert solution_example_6_1 == 4277556
    return (example_math_homework,)


@app.cell
def _(exercise_6_1_help_with_math_homework, read_data):
    math_homework = read_data(file_path="data/2025/2025_day_06.txt", separator="\n")

    solution_6_1 = exercise_6_1_help_with_math_homework(math_homework=math_homework)

    assert solution_6_1 == 4771265398012
    return (math_homework,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

    Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

    Here's the example worksheet again:

    ```
    123 328  51 64
     45 64  387 23
      6 98  215 314
    *   +   *   +
    ```

    Reading the problems right-to-left one column at a time, the problems are now quite different:

    - The rightmost problem is 4 + 431 + 623 = 1058
    - The second problem from the right is 175 * 581 * 32 = 3253600
    - The third problem from the right is 8 + 248 + 369 = 625
    - Finally, the leftmost problem is 356 * 24 * 1 = 8544

    Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

    Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_6_2_help_with_math_homework(math_homework: list[str]) -> int:
    """
    Compute the grand total of all cephalopod math problems read right-to-left.

    Each puzzle row represents part of a very wide worksheet where multiple
    vertical math problems are arranged side-by-side. In cephalopod math,
    numbers are written top-to-bottom with the most significant digit first,
    and entire problems are read right-to-left, one column at a time.

    This function processes the worksheet by:

    1. Reversing each input row so that scanning left-to-right corresponds to
       the intended cephalopod right-to-left reading order.
    2. Padding all rows with leading spaces to equalize their width, ensuring
       each column accurately represents a digit column across all rows.
    3. Iterating through each column, reconstructing numbers by stacking digits
       from top to bottom.
    4. Detecting a problem boundary when an entire column contains only spaces.
       At that moment, the collected numbers are either summed or multiplied,
       depending on the operator at the bottom of the problem.
    5. Accumulating the results of all problems into a grand total.

    This approach effectively parses the worksheet as a column-wise stream,
    treating each contiguous column block as a single problem and using
    structural whitespace to separate them.

    Args:
        math_homework (list[str]): A list of strings representing the worksheet
            rows, containing digits, spaces, and '+'/'*' operators.

    Returns:
        int: The grand total obtained by evaluating all parsed right-to-left
            cephalopod math problems.
    """
    character_matrix = []

    for row in math_homework:
        character_row = []
        for character in row[::-1]:
            character_row.append(character)
        character_matrix.append(character_row)

    max_row_length = 0

    for row in character_matrix:
        if len(row) > max_row_length:
            max_row_length = len(row)

    for i, row in enumerate(character_matrix):
        row_length_difference = max_row_length - len(row)
        for _ in range(row_length_difference):
            character_matrix[i].insert(0, " ")
        character_matrix[i].append(" ")

    total_sum_of_additions_and_multiplications = 0
    add_or_multiply = ""
    numbers_to_add_or_multiply = []

    for j in range(len(character_matrix[0])):
        only_spaces_in_column = True
        number: str = ""

        for i in range(len(character_matrix)):
            matrix_element = character_matrix[i][j]

            if matrix_element == " ":
                pass
            elif matrix_element == "+":
                add_or_multiply = "add"
                only_spaces_in_column = False
            elif matrix_element == "*":
                add_or_multiply = "multiply"
                only_spaces_in_column = False
            else:
                number += matrix_element
                only_spaces_in_column = False

        if number:
            numbers_to_add_or_multiply.append(int(number))

        if only_spaces_in_column:
            if add_or_multiply == "add":
                total_sum_of_additions_and_multiplications += sum(
                    numbers_to_add_or_multiply
                )
            elif add_or_multiply == "multiply":
                product: int = 1
                for n in numbers_to_add_or_multiply:
                    product *= n
                total_sum_of_additions_and_multiplications += product

            add_or_multiply = ""
            numbers_to_add_or_multiply = []

    return total_sum_of_additions_and_multiplications


@app.cell
def _(example_math_homework):
    solution_example_6_2 = exercise_6_2_help_with_math_homework(
        math_homework=example_math_homework
    )

    assert solution_example_6_2 == 3263827
    return


@app.cell
def _(exercise_6_2_help_with_math_homework, math_homework):
    solution_6_2 = exercise_6_2_help_with_math_homework(math_homework=math_homework)

    assert solution_6_2 == 10695785245101
    return


if __name__ == "__main__":
    app.run()
