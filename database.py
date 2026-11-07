
import os
import sqlite3

# -----------------------------------------
# DATABASE CONFIGURATION
# -----------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "recipes.db")

# Create database folder automatically
os.makedirs(DB_DIR, exist_ok=True)


# -----------------------------------------
# DATABASE CONNECTION
# -----------------------------------------

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


# -----------------------------------------
# INITIALIZE DATABASE
# -----------------------------------------

def init_db():
    with get_connection() as conn:

        # Favorites table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe_id INTEGER UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Ratings table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe_id INTEGER UNIQUE NOT NULL,
                rating INTEGER NOT NULL
                    CHECK(rating BETWEEN 1 AND 5)
            )
        """)

        # Shopping list table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS shopping_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ingredient TEXT NOT NULL UNIQUE,
                quantity TEXT DEFAULT '',
                checked INTEGER DEFAULT 0
            )
        """)


# -----------------------------------------
# FAVORITES
# -----------------------------------------

def add_favorite(recipe_id):
    with get_connection() as conn:
        conn.execute("""
            INSERT OR IGNORE INTO favorites (recipe_id)
            VALUES (?)
        """, (recipe_id,))


def remove_favorite(recipe_id):
    with get_connection() as conn:
        conn.execute("""
            DELETE FROM favorites
            WHERE recipe_id = ?
        """, (recipe_id,))


def get_favorites():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT recipe_id
            FROM favorites
            ORDER BY created_at DESC
        """).fetchall()

        return [row["recipe_id"] for row in rows]


def is_favorite(recipe_id):
    with get_connection() as conn:
        row = conn.execute("""
            SELECT id
            FROM favorites
            WHERE recipe_id = ?
        """, (recipe_id,)).fetchone()

        return row is not None


# -----------------------------------------
# RECIPE RATINGS
# -----------------------------------------

def save_rating(recipe_id, rating):
    rating = max(1, min(5, int(rating)))

    with get_connection() as conn:
        conn.execute("""
            INSERT INTO ratings (recipe_id, rating)
            VALUES (?, ?)
            ON CONFLICT(recipe_id)
            DO UPDATE SET rating = excluded.rating
        """, (recipe_id, rating))


def get_rating(recipe_id):
    with get_connection() as conn:
        row = conn.execute("""
            SELECT rating
            FROM ratings
            WHERE recipe_id = ?
        """, (recipe_id,)).fetchone()

        return row["rating"] if row else 0


# -----------------------------------------
# SHOPPING LIST
# -----------------------------------------

def add_shopping_item(ingredient, quantity=""):
    ingredient = ingredient.strip()
    quantity = str(quantity).strip()

    if not ingredient:
        return

    with get_connection() as conn:
        conn.execute("""
            INSERT INTO shopping_list (ingredient, quantity)
            VALUES (?, ?)
            ON CONFLICT(ingredient)
            DO UPDATE SET quantity = excluded.quantity
        """, (ingredient, quantity))


def get_shopping_items():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT *
            FROM shopping_list
            ORDER BY id DESC
        """).fetchall()

        return [dict(row) for row in rows]


def toggle_shopping_item(item_id):
    with get_connection() as conn:
        conn.execute("""
            UPDATE shopping_list
            SET checked = CASE
                WHEN checked = 0 THEN 1
                ELSE 0
            END
            WHERE id = ?
        """, (item_id,))


def delete_shopping_item(item_id):
    with get_connection() as conn:
        conn.execute("""
            DELETE FROM shopping_list
            WHERE id = ?
        """, (item_id,))


def clear_shopping_list():
    with get_connection() as conn:
        conn.execute("""
            DELETE FROM shopping_list
        """)
