if __name__ == __main__:

def calculate_recipe_cost(db, recipe_id):
    ingredients = db.get_recipe_ingredients(recipe_id)
    total = 0
    for ing in ingredients:
        total += ing["quantity"] * ing["cost_per_unit"]
    return round(total, 2)

main();