
from flask import (
    Flask, render_template, request,
    redirect, url_for, flash
)

from recipes import RECIPES
from database import (
    init_db,
    add_favorite,
    remove_favorite,
    get_favorites,
    is_favorite,
    save_rating,
    get_rating,
    add_shopping_item,
    get_shopping_items,
    toggle_shopping_item,
    delete_shopping_item,
    clear_shopping_list
)

from utils.recipe_engine import (
    generate_recipes,
    get_recipe_by_id,
    get_surprise_recipe,
    get_all_cuisines,
    get_all_dietary_options,
    parse_ingredients
)

from utils.image_detector import detect_ingredients

app = Flask(__name__)
app.secret_key = "instant-recipe-generator-secret-key"

# Initialize SQLite database
init_db()


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template(
        "index.html",
        cuisines=get_all_cuisines(),
        dietary_options=get_all_dietary_options()
    )


# ---------------- RECIPE SEARCH ----------------

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        ingredients = request.form.get("ingredients", "")
        cuisine = request.form.get("cuisine", "All")
        diet = request.form.get("diet", "All")
        max_time = request.form.get("max_time", "60")

        try:
            max_time = int(max_time)
        except ValueError:
            max_time = 60

        recipes = generate_recipes(
            user_ingredients=ingredients,
            cuisine=cuisine,
            diet=diet,
            max_time=max_time
        )

        return render_template(
            "results.html",
            recipes=recipes,
            ingredients=ingredients,
            cuisine=cuisine,
            diet=diet,
            max_time=max_time,
            favorites=get_favorites()
        )

    return redirect(url_for("home"))


# ---------------- AI IMAGE INGREDIENT DETECTION ----------------

@app.route("/detect-ingredients", methods=["POST"])
def detect_ingredients_route():
    if "fridge_image" not in request.files:
        flash("Please upload an image.", "error")
        return redirect(url_for("home"))

    image = request.files["fridge_image"]

    if not image.filename:
        flash("Please select an image.", "error")
        return redirect(url_for("home"))

    allowed_types = ["image/jpeg", "image/png", "image/webp"]

    if image.mimetype not in allowed_types:
        flash("Please upload a JPG, PNG or WEBP image.", "error")
        return redirect(url_for("home"))

    try:
        image_bytes = image.read()

        if not image_bytes or len(image_bytes) > 5 * 1024 * 1024:
            flash("Image must be non-empty and smaller than 5 MB.", "error")
            return redirect(url_for("home"))

        ingredients = detect_ingredients(
            image_bytes,
            image.mimetype
        )

        if not ingredients:
            flash("No ingredients detected. Please try another photo.", "error")
            return redirect(url_for("home"))

        return render_template(
            "ingredient_review.html",
            ingredients=ingredients,
            cuisines=get_all_cuisines(),
            dietary_options=get_all_dietary_options()
        )

    except Exception as error:
        print("Image detection error:", error)
        flash("Image detection failed. Check your API key and try again.", "error")
        return redirect(url_for("home"))


# ---------------- SEARCH USING DETECTED INGREDIENTS ----------------

@app.route("/search-detected", methods=["POST"])
def search_detected():
    ingredients = request.form.get("ingredients", "")
    cuisine = request.form.get("cuisine", "All")
    diet = request.form.get("diet", "All")
    max_time = request.form.get("max_time", "60")

    if not ingredients.strip():
        flash("Please enter at least one ingredient.", "error")
        return redirect(url_for("home"))

    try:
        max_time = int(max_time)
    except ValueError:
        max_time = 60

    recipes = generate_recipes(
        user_ingredients=ingredients,
        cuisine=cuisine,
        diet=diet,
        max_time=max_time
    )

    return render_template(
        "results.html",
        recipes=recipes,
        ingredients=ingredients,
        cuisine=cuisine,
        diet=diet,
        max_time=max_time,
        favorites=get_favorites()
    )


# ---------------- RECIPE DETAILS ----------------

@app.route("/recipe/<int:recipe_id>")
def recipe_details(recipe_id):
    recipe = get_recipe_by_id(recipe_id)

    if not recipe:
        flash("Recipe not found.", "error")
        return redirect(url_for("home"))

    selected_servings = request.args.get(
        "servings", recipe.get("servings", 1)
    )

    try:
        selected_servings = max(1, int(selected_servings))
    except (ValueError, TypeError):
        selected_servings = recipe.get("servings", 1)

    original_servings = recipe.get("servings", 1)
    multiplier = selected_servings / original_servings

    adjusted_ingredients = []

    for ingredient in recipe["ingredients"]:
        adjusted_ingredients.append({
            "name": ingredient["name"],
            "quantity": round(
                float(ingredient["quantity"]) * multiplier, 2
            ),
            "unit": ingredient["unit"]
        })

    return render_template(
        "recipe_details.html",
        recipe=recipe,
        adjusted_ingredients=adjusted_ingredients,
        selected_servings=selected_servings,
        is_favorite=is_favorite(recipe_id),
        rating=get_rating(recipe_id)
    )


# ---------------- FAVORITES ----------------

@app.route("/favorite/<int:recipe_id>", methods=["POST"])
def toggle_favorite(recipe_id):
    if is_favorite(recipe_id):
        remove_favorite(recipe_id)
        flash("Recipe removed from favourites.", "success")
    else:
        add_favorite(recipe_id)
        flash("Recipe added to favourites!", "success")

    return redirect(request.referrer or url_for("home"))


@app.route("/favorites")
def favorites():
    favorite_ids = get_favorites()

    favorite_recipes = [
        recipe for recipe in RECIPES
        if recipe["id"] in favorite_ids
    ]

    return render_template(
        "favorites.html",
        recipes=favorite_recipes,
        favorites=favorite_ids
    )


# ---------------- RECIPE RATINGS ----------------

@app.route("/rate/<int:recipe_id>", methods=["POST"])
def rate_recipe(recipe_id):
    rating = request.form.get("rating", "5")

    try:
        rating = int(rating)

        if rating < 1 or rating > 5:
            raise ValueError

        save_rating(recipe_id, rating)
        flash("Your rating has been saved!", "success")

    except ValueError:
        flash("Please select a rating between 1 and 5.", "error")

    return redirect(
        url_for("recipe_details", recipe_id=recipe_id)
    )


# ---------------- SURPRISE ME ----------------

@app.route("/surprise")
def surprise():
    cuisine = request.args.get("cuisine", "All")
    diet = request.args.get("diet", "All")

    try:
        max_time = int(request.args.get("max_time", 60))
    except ValueError:
        max_time = 60

    recipe = get_surprise_recipe(
        cuisine=cuisine,
        diet=diet,
        max_time=max_time
    )

    if recipe:
        return redirect(
            url_for("recipe_details", recipe_id=recipe["id"])
        )

    flash("No recipes match those filters. Try changing them!", "error")
    return redirect(url_for("home"))


# ---------------- SHOPPING LIST ----------------

@app.route("/shopping-list")
def shopping_list():
    items = get_shopping_items()

    return render_template(
        "shopping_list.html",
        items=items
    )


@app.route("/shopping-list/add", methods=["POST"])
def add_shopping():
    ingredient = request.form.get("ingredient", "").strip()
    quantity = request.form.get("quantity", "").strip()

    if ingredient:
        add_shopping_item(ingredient, quantity)
        flash("Ingredient added to shopping list!", "success")
    else:
        flash("Please enter an ingredient.", "error")

    return redirect(url_for("shopping_list"))


@app.route("/shopping-list/add-recipe/<int:recipe_id>", methods=["POST"])
def add_recipe_to_shopping_list(recipe_id):
    recipe = get_recipe_by_id(recipe_id)

    if not recipe:
        flash("Recipe not found.", "error")
        return redirect(url_for("home"))

    for ingredient in recipe["ingredients"]:
        quantity = (
            f'{ingredient["quantity"]} {ingredient["unit"]}'
        ).strip()

        add_shopping_item(
            ingredient["name"],
            quantity
        )

    flash("Recipe ingredients added to your shopping list!", "success")
    return redirect(url_for("shopping_list"))


@app.route("/shopping-list/toggle/<int:item_id>", methods=["POST"])
def toggle_shopping(item_id):
    toggle_shopping_item(item_id)
    return redirect(url_for("shopping_list"))


@app.route("/shopping-list/delete/<int:item_id>", methods=["POST"])
def delete_shopping(item_id):
    delete_shopping_item(item_id)
    return redirect(url_for("shopping_list"))


@app.route("/shopping-list/clear", methods=["POST"])
def clear_shopping():
    clear_shopping_list()
    flash("Shopping list cleared.", "success")
    return redirect(url_for("shopping_list"))


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)
