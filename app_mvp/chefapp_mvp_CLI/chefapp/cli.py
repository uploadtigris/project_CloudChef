import argparse
from . import db, models, logic

def run():
    parser = argparse.ArgumentParser(description="ChefApp CLI")
    parser.add_argument("--init-db", action="store_true")
    parser.add_argument("--cost", type=str, help="Calculate cost of recipe")
    args = parser.parse_args()

    if args.init_db:
        db.init_database()
        print("Database initialized.")
        return

    if args.cost:
        cost = logic.calculate_recipe_cost(args.cost)
        print(f"Cost of {args.cost}: ${cost:.2f}")
        return

    print("No command specified. Try --help.")
