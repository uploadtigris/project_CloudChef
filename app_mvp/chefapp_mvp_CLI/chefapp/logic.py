from .db import get_connection

def calculate_recipe_cost(recipe_name):
    conn = get_connection()
    data = conn.execute("""
        SELECT i.name, ri.quantity, i.cost_per_unit
        FROM recipes r
        JOIN recipe_ingredients ri ON ri.recipe_id = r.id
        JOIN ingredients i ON ri.ingredient_id = i.id
        WHERE r.name = ?
    """, (recipe_name,)).fetchall()

    total = sum(row["quantity"] * row["cost_per_unit"] for row in data)
    conn.close()
    return total


def check_inventory_for_recipe(recipe_name):
    conn = get_connection()
    rows = conn.execute("""
        SELECT i.name, ri.quantity AS needed,
               COALESCE(inv.quantity, 0) AS available
        FROM recipe_ingredients ri
        JOIN recipes r ON ri.recipe_id = r.id
        JOIN ingredients i ON ri.ingredient_id = i.id
        LEFT JOIN inventory inv ON inv.ingredient_id = i.id
        WHERE r.name = ?
    """, (recipe_name,)).fetchall()

    missing = [
        (row["name"], row["needed"] - row["available"])
        for row in rows if row["available"] < row["needed"]
    ]

    conn.close()
    return missing
