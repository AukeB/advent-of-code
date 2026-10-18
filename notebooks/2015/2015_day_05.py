import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 5

    https://adventofcode.com/2015/day/5
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

    from collections import defaultdict

    from aoc.utils import read_data

    return defaultdict, mo, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 5 - Doesn't He Have Intern-Elves For this?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_5_1_find_number_of_nice_strings(
    list_of_strings: list[str],
    vowels: set[str] = set("aeiou"),
    disallowed_substrings: set[str] = {"ab", "cd", "pq", "xy"},
) -> int:
    """Count how many strings in a list are considered "nice" according to
    Santa's rules.

    A string is classified as nice if all of the following conditions are met:
    - It contains at least three vowels from the specified vowel set.
    - It contains at least one instance of the same character appearing twice in
      a row.
    - It does not contain any of the specified disallowed substrings.

    Each string is evaluated independently by scanning its characters and
    adjacent character pairs.

    Args:
        list_of_strings (list[str]): The collection of strings to evaluate.
        vowels (set[str]): The set of characters considered vowels when counting
            vowel occurrences. Default is {"a", "e", "i", "o", "u"}.
        disallowed_substrings (set[str]): Substrings that immediately disqualify
            a string if present. Default is {"ab", "cd", "pq", "xy"}.

    Returns:
        int: The number of strings in the input list that satisfy all "nice
            string" conditions.
    """
    number_of_nice_strings: int = 0

    for naughty_or_nice_string in list_of_strings:
        vowel_count: int = 0
        twice_in_a_row: bool = False
        disallowed_substring_detected = False

        # Pythonic way for iterating over consecutive elements.
        for previous_character, current_character in zip(
            naughty_or_nice_string, naughty_or_nice_string[1:]
        ):
            adjacent_characters = previous_character + current_character

            # Check for vowels.
            if previous_character in vowels:
                vowel_count += 1

            # Check if there is a character that appears twice in a row.
            if previous_character == current_character:
                twice_in_a_row = True

            # Check for disallowed substrings.
            if adjacent_characters in disallowed_substrings:
                disallowed_substring_detected = True
                break

        # Check final character of string because we missed that in the loop.
        if naughty_or_nice_string[-1] in vowels:
            vowel_count += 1

        # Final check for naughty or nice string.
        if vowel_count >= 3 and twice_in_a_row and not disallowed_substring_detected:
            number_of_nice_strings += 1

    return number_of_nice_strings


@app.cell
def _(exercise_5_1_find_number_of_nice_strings, read_data):
    naughty_or_nice_strings: list[str] = read_data(
        file_path="data/2015/2015_day_05.txt", separator="\n"
    )

    number_of_nice_strings_5_1 = exercise_5_1_find_number_of_nice_strings(
        list_of_strings=naughty_or_nice_strings,
    )

    assert number_of_nice_strings_5_1 == 255
    return (naughty_or_nice_strings,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(defaultdict):
    def exercise_5_2_find_number_of_nice_strings(
        list_of_strings: list[str],
    ) -> int:
        """Count how many strings in a list are considered "nice" according to
        Santa's updated rules for Part 2.

        A string is classified as nice if both of the following conditions are
        met:
        - It contains a pair of any two letters that appears at least twice in
          the string without overlapping.
        - It contains at least one letter which repeats with exactly one letter
          between them.

        Each string is evaluated independently by scanning its characters and
        adjacent character pairs, storing the indices of each pair to detect
        non-overlapping repetitions.

        Args:
            list_of_strings (list[str]): The collection of strings to evaluate.

        Returns:
            int: The number of strings in the input list that satisfy all "nice
                string" conditions according to the updated rules.
        """
        number_of_nice_strings: int = 0

        for naughty_or_nice_string in list_of_strings:
            unique_adjacent_pairs = defaultdict(list)
            pair_appearing_twice_detected: bool = False
            repeating_character_detected: bool = False

            # Check for pairs of any two letter that appear at leat twice in string without overlapping.
            for index, adjacent_characters in enumerate(
                zip(naughty_or_nice_string, naughty_or_nice_string[1:])
            ):
                adjacent_characters = "".join(adjacent_characters)
                unique_adjacent_pairs[adjacent_characters].append(index)

            for index_value in unique_adjacent_pairs.values():
                if len(index_value) > 1 and max(index_value) - min(index_value) > 1:
                    pair_appearing_twice_detected = True
                    break

            # Check for a letter which repeats with exactly one letter between them.
            for character_index in range(len(naughty_or_nice_string) - 2):
                first_character = naughty_or_nice_string[character_index]
                third_character = naughty_or_nice_string[character_index + 2]

                if first_character == third_character:
                    repeating_character_detected = True
                    break

            if pair_appearing_twice_detected and repeating_character_detected:
                number_of_nice_strings += 1

        return number_of_nice_strings

    return (exercise_5_2_find_number_of_nice_strings,)


@app.cell
def _(
    exercise_5_2_find_number_of_nice_strings,
    naughty_or_nice_strings: list[str],
):
    number_of_nice_strings_5_2 = exercise_5_2_find_number_of_nice_strings(
        list_of_strings=naughty_or_nice_strings,
    )

    assert number_of_nice_strings_5_2 == 55
    return


if __name__ == "__main__":
    app.run()
