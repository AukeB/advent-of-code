import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025
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
    import sys

    from aoc.utils import read_data

    return mo, read_data, sys


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants
    """)
    return


@app.cell
def _():
    DATA_DIRECTORY_PATH = "data/2025"
    # DATA_DIRECTORY_PATH = "../../" + DATA_DIRECTORY_PATH
    return (DATA_DIRECTORY_PATH,)


@app.cell
def _():
    def convert_string_to_list_of_tuples(str_data: str) -> list[tuple[int]]:
        """
        Convert a string representation of tuples into a list of integer tuples.

        Each tuple in the string should be enclosed in parentheses and separated
        by spaces. Elements within a tuple should be comma-separated integers.

        Args:
            str_data (str): The str data representing one or more tuples.

        Returns:
            list[tuple[int]]: The same data but now with the correct variable
                types.
        """
        list_of_tuples = []
        data_split = str_data.split(" ")

        for element in data_split:
            sub_list_elements = element[1:-1].split(",")
            sub_list_elements = [int(number) for number in sub_list_elements]
            list_of_tuples.append(tuple(sub_list_elements))

        return list_of_tuples

    return (convert_string_to_list_of_tuples,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Just across the hall, you find a large factory. Fortunately, the Elves here have plenty of time to decorate. Unfortunately, it's because the factory machines are all offline, and none of the Elves can figure out the initialization procedure.

    The Elves do have the manual for the machines, but the section detailing the initialization procedure was eaten by a Shiba Inu. All that remains of the manual are some indicator light diagrams, button wiring schematics, and joltage requirements for each machine.

    For example:

    ```
    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    ```

    The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.

    To start a machine, its indicator lights must match those shown in the diagram, where . means off and # means on. The machine has the number of indicator lights shown, but its indicator lights are all initially off.

    So, an indicator light diagram like [.##.] means that the machine has four indicator lights which are initially off and that the goal is to simultaneously configure the first light to be off, the second light to be on, the third to be on, and the fourth to be off.

    You can toggle the state of indicator lights by pushing any of the listed buttons. Each button lists which indicator lights it toggles, where 0 means the first light, 1 means the second light, and so on. When you push a button, each listed indicator light either turns on (if it was off) or turns off (if it was on). You have to push each button an integer number of times; there's no such thing as "0.5 presses" (nor can you push a button a negative number of times).

    So, a button wiring schematic like (0,3,4) means that each time you push that button, the first, fourth, and fifth indicator lights would all toggle between on and off. If the indicator lights were [#.....], pushing the button would change them to be [...##.] instead.

    Because none of the machines are running, the joltage requirements are irrelevant and can be safely ignored.

    You can push each button as many times as you like. However, to save on time, you will need to determine the fewest total presses required to correctly configure all indicator lights for all machines in your list.

    There are a few ways to correctly configure the first machine:

    ```
    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    ```

    - You could press the first three buttons once each, a total of 3 button presses.
    - You could press (1,3) once, (2,3) once, and (0,1) twice, a total of 4 button presses.
    - You could press all of the buttons except (1,3) once each, a total of 5 button presses.

    However, the fewest button presses required is 2. One way to do this is by pressing the last two buttons ((0,2) and (0,1)) once each.

    The second machine can be configured with as few as 3 button presses:

    ```
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    ```

    One way to achieve this is by pressing the last three buttons ((0,4), (0,1,2), and (1,2,3,4)) once each.

    The third machine has a total of six indicator lights that need to be configured correctly:

    ```
    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    ```

    The fewest presses required to correctly configure it is 2; one way to do this is by pressing buttons (0,3,4) and (0,1,2,4,5) once each.

    So, the fewest button presses required to correctly configure the indicator lights on all of the machines is 2 + 3 + 2 = 7.

    Analyze each machine's indicator light diagram and button wiring schematics. What is the fewest button presses required to correctly configure the indicator lights on all of the machines?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(convert_string_to_list_of_tuples, sys):
    def exercise_10_1_find_minimal_button_presses(manual: list[str]) -> int:
        """
        Compute the minimal number of button presses required for a list of
        machines described in a manual.

        Each machine description contains an indicator light diagram and a
        button wiring schematic. The function tries all possible combinations
        of button presses to find the minimal number that achieves the target
        light configuration.

        Args:
            manual (list[str]): A list of strings, each representing a machine.
                Each string has the format "[lights] (buttons)" where lights
                are '#' for on and '.' for off, and buttons are tuples of
                light indices they toggle.

        Returns:
            int: The sum of the minimal number of button presses needed for
                all machines in the manual.
        """
        total_button_press_counter: int = 0

        for machine_description in manual:
            # Get indices.
            index_square_bracket_closing: int = machine_description.index("]")
            index_parenthesis_closing: int = machine_description.rindex(")")

            # Separate machine properties.
            indicator_light_diagram: str = machine_description[
                1:index_square_bracket_closing
            ]
            button_wiring_schematic: str = machine_description[
                index_square_bracket_closing + 2 : index_parenthesis_closing + 1
            ]

            # Additional setup variables.
            number_of_lights: int = len(indicator_light_diagram)
            target_state: list[int] = [
                index
                for index, indicator in enumerate(indicator_light_diagram)
                if indicator == "#"
            ]
            buttons: list[tuple[int]] = convert_string_to_list_of_tuples(
                str_data=button_wiring_schematic
            )
            number_of_buttons: int = len(buttons)

            # Brute force approach.
            number_of_button_states: int = 2**number_of_buttons
            minimal_number_of_button_presses: int = sys.maxsize

            # Loop over all possible states.
            for state_integer in range(number_of_button_states):
                state_binary: str = bin(state_integer)[2:].zfill(number_of_buttons)
                current_state = [0 for _ in range(number_of_lights)]
                button_press_counter: int = 0

                # Loop over the binary representation of the current state.
                for button_index, button_state in enumerate(state_binary):
                    button_state = int(button_state)

                    # Press the button.
                    if button_state:
                        button = buttons[button_index]

                        # Loop over all the light elements present in the button that will be switched on and off.
                        for light_index in button:
                            if current_state[light_index] == 0:
                                current_state[light_index] = 1
                            elif current_state[light_index] == 1:
                                current_state[light_index] = 0

                        button_press_counter += 1

                final_state = [
                    index for index, indicator in enumerate(current_state) if indicator
                ]

                if (
                    target_state == final_state
                    and button_press_counter < minimal_number_of_button_presses
                ):
                    minimal_number_of_button_presses = button_press_counter

            total_button_press_counter += minimal_number_of_button_presses

        return total_button_press_counter

    return (exercise_10_1_find_minimal_button_presses,)


@app.cell
def _(convert_string_to_list_of_tuples, sys):
    def exercise_10_1_find_minimal_button_presses_binary_approach(
        manual: list[str],
    ) -> int:
        """
        Compute the minimal number of button presses required for a list of
        machines using a binary/bitmask approach.

        Each machine description contains an indicator light diagram and a
        button wiring schematic. The function iterates over all possible
        button press combinations using binary numbers to efficiently
        determine the minimal number of presses that achieve the target
        light configuration.

        Args:
            manual (list[str]): A list of strings, each representing a machine.
                Each string has the format "[lights] (buttons)" where lights
                are '#' for on and '.' for off, and buttons are tuples of
                light indices they toggle.

        Returns:
            int: The sum of the minimal number of button presses needed for
                all machines in the manual.
        """
        total_button_press_counter: int = 0

        for machine_description in manual:
            # Get indices.
            index_square_bracket_closing: int = machine_description.index("]")
            index_parenthesis_closing: int = machine_description.rindex(")")

            # Separate machine properties.
            indicator_light_diagram: str = machine_description[
                1:index_square_bracket_closing
            ]
            button_wiring_schematic: str = machine_description[
                index_square_bracket_closing + 2 : index_parenthesis_closing + 1
            ]

            # Additional setup variables.
            number_of_lights: int = len(indicator_light_diagram)
            target_state: list[int] = [
                index
                for index, indicator in enumerate(indicator_light_diagram)
                if indicator == "#"
            ]
            buttons: list[tuple[int]] = convert_string_to_list_of_tuples(
                str_data=button_wiring_schematic
            )
            number_of_buttons: int = len(buttons)

            # Brute force approach.
            minimal_number_of_button_presses: int = sys.maxsize

            # Loop over all possible states
            for state_integer in range(1 << number_of_buttons):
                current_state = [0 for _ in range(number_of_lights)]
                button_press_counter: int = 0

                # Loop over all buttons.
                for button_index in range(number_of_buttons):
                    if state_integer & (1 << button_index):
                        button_press_counter += 1

                        # Loop over all the light elements present in the button that will be switched on and off.
                        for light_index in buttons[button_index]:
                            current_state[light_index] ^= 1

                final_state = [
                    index for index, indicator in enumerate(current_state) if indicator
                ]
                if target_state == final_state:
                    minimal_number_of_button_presses = min(
                        button_press_counter, minimal_number_of_button_presses
                    )

            total_button_press_counter += minimal_number_of_button_presses

        return total_button_press_counter

    return (exercise_10_1_find_minimal_button_presses_binary_approach,)


@app.cell
def _(
    exercise_10_1_find_minimal_button_presses,
    exercise_10_1_find_minimal_button_presses_binary_approach,
):
    example_manual = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
    ]

    solution_example_10_1 = exercise_10_1_find_minimal_button_presses(
        manual=example_manual
    )
    solution_example_10_1_v2 = (
        exercise_10_1_find_minimal_button_presses_binary_approach(manual=example_manual)
    )

    assert solution_example_10_1 == 7
    assert solution_example_10_1_v2 == 7
    return (example_manual,)


@app.cell
def _(
    DATA_DIRECTORY_PATH,
    exercise_10_1_find_minimal_button_presses,
    exercise_10_1_find_minimal_button_presses_binary_approach,
    read_data,
):
    manual = read_data(
        file_path=f"{DATA_DIRECTORY_PATH}/2025_day_10.txt", separator="\n"
    )

    assert exercise_10_1_find_minimal_button_presses(manual=manual) == 578
    assert (
        exercise_10_1_find_minimal_button_presses_binary_approach(manual=manual) == 578
    )
    return (manual,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All of the machines are starting to come online! Now, it's time to worry about the joltage requirements.

    Each machine needs to be configured to exactly the specified joltage levels to function properly. Below the buttons on each machine is a big lever that you can use to switch the buttons from configuring the indicator lights to increasing the joltage levels. (Ignore the indicator light diagrams.)

    The machines each have a set of numeric counters tracking its joltage levels, one counter per joltage requirement. The counters are all initially set to zero.

    So, joltage requirements like {3,5,4,7} mean that the machine has four counters which are initially 0 and that the goal is to simultaneously configure the first counter to be 3, the second counter to be 5, the third to be 4, and the fourth to be 7.

    The button wiring schematics are still relevant: in this new joltage configuration mode, each button now indicates which counters it affects, where 0 means the first counter, 1 means the second counter, and so on. When you push a button, each listed counter is increased by 1.

    So, a button wiring schematic like (1,3) means that each time you push that button, the second and fourth counters would each increase by 1. If the current joltage levels were {0,1,2,3}, pushing the button would change them to be {0,2,2,4}.

    You can push each button as many times as you like. However, your finger is getting sore from all the button pushing, and so you will need to determine the fewest total presses required to correctly configure each machine's joltage level counters to match the specified joltage requirements.

    Consider again the example from before:

    ```
    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    ```

    Configuring the first machine's counters requires a minimum of 10 button presses. One way to do this is by pressing (3) once, (1,3) three times, (2,3) three times, (0,2) once, and (0,1) twice.

    Configuring the second machine's counters requires a minimum of 12 button presses. One way to do this is by pressing (0,2,3,4) twice, (2,3) five times, and (0,1,2) five times.

    Configuring the third machine's counters requires a minimum of 11 button presses. One way to do this is by pressing (0,1,2,3,4) five times, (0,1,2,4,5) five times, and (1,2) once.

    So, the fewest button presses required to correctly configure the joltage level counters on all of the machines is 10 + 12 + 11 = 33.

    Analyze each machine's joltage requirements and button wiring schematics. What is the fewest button presses required to correctly configure the joltage level counters on all of the machines?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(convert_string_to_list_of_tuples):
    import pulp

    def exercise_10_2_find_minimal_button_presses(manual: list[str]) -> int:
        """
        Compute the minimal total number of button presses to reach target states for all
        machines in the manual using integer linear programming.

        Each machine description must include:
        1. Indicator light diagram (e.g., '[#..#]') where '#' indicates a target light.
        2. Button wiring schematic (e.g., '(0,1) (2,3)') showing which lights each button
           affects.
        3. Target joltage levels (e.g., '1,0,1,0') representing the desired state of each
           light.

        The function uses PuLP's CBC solver to determine the minimal number of presses per
        machine and sums them for all machines.

        For each machine:
          - Parse the description to extract lights, buttons, and target states.
          - Build a coefficient matrix where matrix[i][j] = 1 if button j affects light i.
          - Define integer variables for button presses.
          - Minimize the sum of button presses while satisfying the target state constraints.
          - Solve the ILP with CBC.
          - Accumulate the total minimal presses.

        Args:
            manual (list[str]): List of machine descriptions as strings.

        Returns:
            int: Total minimal number of button presses required across all machines.
        """

        total_button_press_counter: int = 0

        for machine_description in manual:
            # Get indices.
            index_square_bracket_closing: int = machine_description.index("]")
            index_parenthesis_closing: int = machine_description.rindex(")")

            # Separate machine properties.
            indicator_light_diagram: str = machine_description[
                1:index_square_bracket_closing
            ]
            button_wiring_schematic: str = machine_description[
                index_square_bracket_closing + 2 : index_parenthesis_closing + 1
            ]
            joltage_requirements: str = machine_description[
                index_parenthesis_closing + 3 : -1
            ]

            # Additional setup variables.
            number_of_lights: int = len(indicator_light_diagram)
            buttons: list[tuple[int]] = convert_string_to_list_of_tuples(
                str_data=button_wiring_schematic
            )
            number_of_buttons: int = len(buttons)
            target_joltage_levels: tuple = tuple(
                int(level) for level in joltage_requirements.split(",")
            )

            # Setup a coefficient matrix and fill it with the effect all the buttons have on the light indicators.
            coefficient_matrix = [
                [0] * number_of_buttons for _ in range(number_of_lights)
            ]
            for col_index in range(len(coefficient_matrix[0])):
                for row_index in range(len(coefficient_matrix)):
                    coefficient_matrix[row_index][col_index] = (
                        1 if row_index in buttons[col_index] else 0
                    )

            # Build the PuLP linear programming model.
            problem = pulp.LpProblem(
                name="MinimalButtonPresses",
                sense=pulp.LpMinimize,  # Minimization is objective.
            )

            # Setup up variables.
            variables = [
                pulp.LpVariable(name=f"x_{j}", lowBound=0, upBound=None, cat="Integer")
                for j in range(number_of_buttons)
            ]

            problem += pulp.lpSum(
                vector=variables
            )  # Minimize the total number of presses

            # Setup constraints.
            for light_index in range(number_of_lights):
                problem += (
                    pulp.lpSum(
                        coefficient_matrix[light_index][button_index]
                        * variables[button_index]
                        for button_index in range(number_of_buttons)
                    )
                    == target_joltage_levels[light_index]
                )

            # The problem is ready to be solved now.
            problem.solve(solver=pulp.PULP_CBC_CMD(msg=False))

            # Obtain results
            solution: list[int] = []
            for variable in variables:
                variable_value = variable.value()

                if variable_value is None:
                    raise ValueError(f"No solution found for {variable.name}")

                solution.append(int(variable_value))

            total_button_press_counter += sum(solution)

        return total_button_press_counter

    return (exercise_10_2_find_minimal_button_presses,)


@app.cell
def _(example_manual, exercise_10_2_find_minimal_button_presses):
    solution_example_10_2 = exercise_10_2_find_minimal_button_presses(
        manual=example_manual
    )

    assert solution_example_10_2 == 33
    return


@app.cell
def _(exercise_10_2_find_minimal_button_presses, manual):
    print(exercise_10_2_find_minimal_button_presses(manual=manual))
    return


if __name__ == "__main__":
    app.run()
