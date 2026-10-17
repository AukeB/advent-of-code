import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015 - Day 15
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

    from dataclasses import dataclass

    from aoc.utils import read_data

    return dataclass, mo, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 15: Science for Hungry People
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
    Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

    Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

    - capacity (how well it helps the cookie absorb milk)
    - durability (how well it keeps the cookie intact when full of milk)
    - flavor (how tasty it makes the cookie)
    - texture (how it improves the feel of the cookie)
    - calories (how many calories it adds to the cookie)

    You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

    For instance, suppose you have these two ingredients:

    ```
    Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
    Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
    ```

    Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

    - A capacity of 44 * -1 + 56 * 2 = 68
    - A durability of 44 * -2 + 56 * 3 = 80
    - A flavor of 44 * 6 + 56 * -2 = 152
    - A texture of 44 * 3 + 56 * -1 = 76

    Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

    Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(dataclass):
    @dataclass
    class Ingredient:
        """Properties of a single cookie ingredient, as given in the puzzle
        input.
        """

        name: str
        capacity: int
        durability: int
        flavor: int
        texture: int
        calories: int

    return (Ingredient,)


@app.cell
def _(Ingredient):
    def exercise_15_1_find_optimal_ingredient_distribution(
        ingredients_and_properties: list[str], total_number_of_teaspoons: int = 100
    ) -> tuple[str, int]:
        """Finds the highest cookie score achievable by splitting a fixed number
        of teaspoons across four ingredients, along with the recipe that
        achieves it.

        1. Parse each input line into an `Ingredient`.
        2. Enumerate every distribution of teaspoons with three nested loops,
           where the fourth amount is simply the leftover.
        3. Compute each property total (clamped at zero) and multiply the totals
           into a score.
        4. Keep track of the highest score seen and the recipe that produced it.

        Args:
            ingredients_and_properties (list[str]): Raw puzzle input lines, one
                ingredient per line, e.g. "Sugar: capacity 3, durability 0,
                ...".
            total_number_of_teaspoons (int): Total number of teaspoons to
                distribute. Defaults to 100.

        Returns:
            recipe (str): Human-readable description of the best distribution,
                e.g. "44 Sugar, 56 Sprinkles, 0 Candy, 0 Chocolate". Empty if no
                distribution scores above zero.
            highest_score (int): The best score over all valid distributions.
        """
        # First read input and create `Ingredient` objects for each ingredient.
        parsed_ingredients = []

        for ingredient in ingredients_and_properties:
            ingredient_name, ingredient_properties = ingredient.split(": ")
            ingredient_properties = ingredient_properties.split(", ")
            ingredient_properties = [x.split(" ") for x in ingredient_properties]

            ingredient = Ingredient(
                name=ingredient_name,
                capacity=int(ingredient_properties[0][1]),
                durability=int(ingredient_properties[1][1]),
                flavor=int(ingredient_properties[2][1]),
                texture=int(ingredient_properties[3][1]),
                calories=int(ingredient_properties[4][1]),
            )

            parsed_ingredients.append(ingredient)

        # Extract each ingredient into a variable.
        sugar = parsed_ingredients[0]
        sprinkles = parsed_ingredients[1]
        candy = parsed_ingredients[2]
        chocolate = parsed_ingredients[3]

        # Setup variables that are used in the loops below.
        total_sum_for_loops: int = total_number_of_teaspoons + 1
        highest_score: int = 0
        recipe: str = ""

        # Triple nested for loops because we have 4 ingredients.
        for x0 in range(0, total_sum_for_loops):
            for x1 in range(0, total_sum_for_loops - x0):
                for x2 in range(0, total_sum_for_loops - x0 - x1):
                    x3 = total_number_of_teaspoons - x0 - x1 - x2

                    # Compute total score using each ingredient property.
                    total_capacity = max(
                        0,
                        x0 * sugar.capacity
                        + x1 * sprinkles.capacity
                        + x2 * candy.capacity
                        + x3 * chocolate.capacity,
                    )
                    total_durability = max(
                        0,
                        x0 * sugar.durability
                        + x1 * sprinkles.durability
                        + x2 * candy.durability
                        + x3 * chocolate.durability,
                    )
                    total_flavor = max(
                        0,
                        x0 * sugar.flavor
                        + x1 * sprinkles.flavor
                        + x2 * candy.flavor
                        + x3 * chocolate.flavor,
                    )
                    total_texture = max(
                        0,
                        x0 * sugar.texture
                        + x1 * sprinkles.texture
                        + x2 * candy.texture
                        + x3 * chocolate.texture,
                    )

                    total_score = (
                        total_capacity * total_durability * total_flavor * total_texture
                    )

                    if total_score > highest_score:
                        highest_score = total_score
                        recipe = f"{x0} {sugar.name}, {x1} {sprinkles.name}, {x2} {candy.name}, {x3} {chocolate.name}"

        return recipe, highest_score

    return (exercise_15_1_find_optimal_ingredient_distribution,)


@app.cell
def _(
    exercise_15_1_find_optimal_ingredient_distribution,
    read_data,
):
    ingredients_and_properties: list[str] = read_data(
        file_path="data/2015/2015_day_15.txt", separator="\n"
    )

    recipe_15_1, highest_score_15_1 = (
        exercise_15_1_find_optimal_ingredient_distribution(
            ingredients_and_properties=ingredients_and_properties,
        )
    )

    assert recipe_15_1 == "21 Sugar, 5 Sprinkles, 31 Candy, 43 Chocolate"
    assert highest_score_15_1 == 222870
    return (ingredients_and_properties,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

    For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

    Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(Ingredient):
    def exercise_15_2_find_optimal_ingredient_distribution_with_calorie_constraint(
        ingredients_and_properties: list[str],
        total_number_of_teaspoons: int = 100,
        calorie_constraint: int = 500,
    ) -> tuple[str, int]:
        """Finds the highest cookie score achievable by splitting a fixed number
        of teaspoons across four ingredients such that the cookie has an exact
        calorie count, along with the recipe that achieves it.

        1. Parse each input line into an `Ingredient`.
        2. Enumerate every distribution of teaspoons with three nested loops,
           where the fourth amount is simply the leftover.
        3. Compute the total calories and skip distributions that do not match
           the calorie constraint.
        4. Compute each remaining property total (clamped at zero) and multiply
           the totals into a score.
        5. Keep track of the highest score seen and the recipe that produced it.

        Args:
            ingredients_and_properties (list[str]): Raw puzzle input lines, one
                ingredient per line, e.g. "Sugar: capacity 3, durability 0,
                ...".
            total_number_of_teaspoons (int): Total number of teaspoons to
                distribute. Defaults to 100.
            calorie_constraint (int): Exact total calorie count the cookie must
                have. Defaults to 500.

        Returns:
            recipe (str): Human-readable description of the best distribution,
                e.g. "40 Sugar, 60 Sprinkles, 0 Candy, 0 Chocolate". Empty if no
                distribution satisfies the calorie constraint with a score above
                zero.
            highest_score (int): The best score over all distributions that meet
                the calorie constraint.
        """
        # First read input and create `Ingredient` objects for each ingredient.
        parsed_ingredients = []

        for ingredient in ingredients_and_properties:
            ingredient_name, ingredient_properties = ingredient.split(": ")
            ingredient_properties = ingredient_properties.split(", ")
            ingredient_properties = [x.split(" ") for x in ingredient_properties]

            ingredient = Ingredient(
                name=ingredient_name,
                capacity=int(ingredient_properties[0][1]),
                durability=int(ingredient_properties[1][1]),
                flavor=int(ingredient_properties[2][1]),
                texture=int(ingredient_properties[3][1]),
                calories=int(ingredient_properties[4][1]),
            )

            parsed_ingredients.append(ingredient)

        # Extract each ingredient into a variable.
        sugar = parsed_ingredients[0]
        sprinkles = parsed_ingredients[1]
        candy = parsed_ingredients[2]
        chocolate = parsed_ingredients[3]

        # Setup variables that are used in the loops below.
        total_sum_for_loops: int = total_number_of_teaspoons + 1
        highest_score: int = 0
        recipe: str = ""

        # Triple nested for loops because we have 4 ingredients.
        for x0 in range(0, total_sum_for_loops):
            for x1 in range(0, total_sum_for_loops - x0):
                for x2 in range(0, total_sum_for_loops - x0 - x1):
                    x3 = total_number_of_teaspoons - x0 - x1 - x2

                    # Compute total score using each ingredient property.
                    total_capacity = max(
                        0,
                        x0 * sugar.capacity
                        + x1 * sprinkles.capacity
                        + x2 * candy.capacity
                        + x3 * chocolate.capacity,
                    )
                    total_durability = max(
                        0,
                        x0 * sugar.durability
                        + x1 * sprinkles.durability
                        + x2 * candy.durability
                        + x3 * chocolate.durability,
                    )
                    total_flavor = max(
                        0,
                        x0 * sugar.flavor
                        + x1 * sprinkles.flavor
                        + x2 * candy.flavor
                        + x3 * chocolate.flavor,
                    )
                    total_texture = max(
                        0,
                        x0 * sugar.texture
                        + x1 * sprinkles.texture
                        + x2 * candy.texture
                        + x3 * chocolate.texture,
                    )
                    total_calories = (
                        x0 * sugar.calories
                        + x1 * sprinkles.calories
                        + x2 * candy.calories
                        + x3 * chocolate.calories
                    )

                    if total_calories == calorie_constraint:
                        total_score = (
                            total_capacity
                            * total_durability
                            * total_flavor
                            * total_texture
                        )

                        if total_score > highest_score:
                            highest_score = total_score
                            recipe = f"{x0} {sugar.name}, {x1} {sprinkles.name}, {x2} {candy.name}, {x3} {chocolate.name}"

        return recipe, highest_score

    return (exercise_15_2_find_optimal_ingredient_distribution_with_calorie_constraint,)


@app.cell
def _(
    exercise_15_2_find_optimal_ingredient_distribution_with_calorie_constraint,
    ingredients_and_properties: list[str],
):
    recipe_15_2, highest_score_15_2 = (
        exercise_15_2_find_optimal_ingredient_distribution_with_calorie_constraint(
            ingredients_and_properties=ingredients_and_properties,
        )
    )

    assert recipe_15_2 == "21 Sugar, 8 Sprinkles, 26 Candy, 45 Chocolate"
    assert highest_score_15_2 == 117936
    return


if __name__ == "__main__":
    app.run()
