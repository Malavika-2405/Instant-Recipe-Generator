
import random
import re
from recipes import RECIPES


# Common ingredient name corrections
INGREDIENT_ALIASES = {
    "tomatoes": "tomato",
    "onions": "onion",
    "potatoes": "potato",
    "eggs": "egg",
    "carrots": "carrot",
    "mushrooms": "mushroom",
    "chickpeas": "chickpeas",
    "capsicums": "capsicum",
    "bell pepper": "capsicum",
    "bell peppers": "capsicum",
    "chilli": "green chilli",
    "chilies": "green chilli",
    "chillies": "green chilli",
    "chilis": "green chilli",
    "noodle": "noodles",
    "spaghetti": "pasta",
    "chicken breast": "chicken",
    "paneer cubes": "paneer",
    "curd": "yogurt",
    "dahi": "yogurt",
    "coriander powder": "coriander",
    "salt": "salt"
}


def normalize_ingredient(ingredient):
    """Normalize ingredient names for accurate matching."""

    ingredient = ingredient.lower().strip()
    ingredient = re.sub(r"[^a-z0-9 ]", "", ingredient)
    ingredient = re.sub(r"\s+", " ", ingredient)

    return INGREDIENT_ALIASES.get(ingredient, ingredient)


def parse_ingredients(user_input):
    """Convert user-entered ingredients into a clean list."""

    if isinstance(user_input, str):
        ingredients = re.split(r"[,;\n]+", user_input)
    else:
        ingredients = user_input or []

    cleaned = {
        normalize_ingredient(item)
        for item in ingredients
        if item and normalize_ingredient(item)
    }

    return sorted(cleaned)


def get_recipe_ingredients(recipe):
    """Get normalized ingredient names from a recipe."""

    return {
        normalize_ingredient(item["name"])
        for item in recipe["ingredients"]
    }


def calculate_match(recipe, user_ingredients):
    """Calculate recipe ingredient matching percentage."""

    recipe_ingredients = get_recipe_ingredients(recipe)

    matched = recipe_ingredients.intersection(user_ingredients)
    missing = recipe_ingredients.difference(user_ingredients)

    total = len(recipe_ingredients)

    percentage = round((len(matched) / total) * 100) if total else 0

    return {
        "matched_ingredients": sorted(matched),
        "missing_ingredients": sorted(missing),
        "match_percentage": percentage,
        "matched_count": len(matched),
        "total_ingredients": total
    }


def generate_recipes(
    user_ingredients,
    cuisine="All",
    diet="All",
    max_time=60,
    limit=20
):
    """
    Generate recipes based on available ingredients
    and selected filters.
    """

    available = set(parse_ingredients(user_ingredients))
    results = []

    if not available:
        return []

    for recipe in RECIPES:

        recipe_cuisine = recipe["cuisine"]
        recipe_diets = recipe["diet"]

        # Cuisine filter
        if cuisine != "All" and recipe_cuisine != cuisine:
            continue

        # Dietary filter
        if diet != "All" and diet not in recipe_diets:
            continue

        # Cooking time filter
        total_time = recipe["prep_time"] + recipe["cook_time"]

        if total_time > int(max_time):
            continue

        match_data = calculate_match(recipe, available)

        # At least one ingredient must match
        if match_data["matched_count"] == 0:
            continue

        recipe_result = recipe.copy()
        recipe_result.update(match_data)

        recipe_result["total_time"] = total_time

        results.append(recipe_result)

    # Best matching recipes appear first
    results.sort(
        key=lambda item: (
            item["match_percentage"],
            item["matched_count"]
        ),
        reverse=True
    )

    return results[:int(limit)]


def get_recipe_by_id(recipe_id):
    """Find a recipe using its ID."""

    for recipe in RECIPES:
        if recipe["id"] == int(recipe_id):
            return recipe

    return None


def get_missing_ingredients(recipe, user_ingredients):
    """Return ingredients that the user does not have."""

    available = set(parse_ingredients(user_ingredients))
    recipe_ingredients = get_recipe_ingredients(recipe)

    return sorted(recipe_ingredients - available)


def get_surprise_recipe(
    cuisine="All",
    diet="All",
    max_time=60
):
    """Choose a random recipe matching selected filters."""

    matching_recipes = []

    for recipe in RECIPES:

        total_time = recipe["prep_time"] + recipe["cook_time"]

        if cuisine != "All" and recipe["cuisine"] != cuisine:
            continue

        if diet != "All" and diet not in recipe["diet"]:
            continue

        if total_time > int(max_time):
            continue

        matching_recipes.append(recipe)

    if not matching_recipes:
        return None

    return random.choice(matching_recipes)


def get_all_cuisines():
    """Return available cuisine options."""

    return sorted({
        recipe["cuisine"]
        for recipe in RECIPES
    })


def get_all_dietary_options():
    """Return available dietary options."""

    return sorted({
        diet
        for recipe in RECIPES
        for diet in recipe["diet"]
    })


def get_all_recipes():
    """Return the complete recipe collection."""

    return RECIPES
