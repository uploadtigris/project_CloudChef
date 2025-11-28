from .db import get_connection

# INGREDIENTS ---------------------------------------------------------

def add_ingredient(name, unit, cost_per_unit):
    conn = get_connection()
    conn.execute(
        "INSERT INTO ingredients (name, unit, cost_per_unit) VALUES (?, ?, ?)",
        (name, unit, cost_per_unit)
    )
    conn.commit()
    conn.close()

def get_ingredient(name):
    conn = get_connection()
    cur = conn.execute("SELECT * FROM ingredients WHERE name = ?", (name,))
    row = cur.fetchone()
    conn.close()
    return row


# RECIPES -------------------------------------------------------------

def add_recipe(name):
    conn = get_connection()
    conn.execute("INSERT INTO recipes (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def add_recipe_ingredient(recipe_name, ingredient_name, qty):
    conn = get_connection()

    recipe_id = conn.execute(
        "SELECT id FROM recipes WHERE name = ?", (recipe_name,)
    ).fetchone()["id"]

    ingredient_id = conn.execute(
        "SELECT id FROM ingredients WHERE name = ?", (ingredient_name,)
    ).fetchone()["id"]

    conn.execute(
        """INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity)
           VALUES (?, ?, ?)""",
        (recipe_id, ingredient_id, qty)
    )
    conn.commit()
    conn.close()


# INVENTORY -----------------------------------------------------------

def update_inventory(ingredient_name, quantity):
    conn = get_connection()
    ingredient_id = conn.execute(
        "SELECT id FROM ingredients WHERE name = ?", (ingredient_name,)
    ).fetchone()["id"]

    conn.execute(
        """INSERT INTO inventory (ingredient_id, quantity)
           VALUES (?, ?)""",
        (ingredient_id, quantity)
    )
    conn.commit()
    conn.close()
