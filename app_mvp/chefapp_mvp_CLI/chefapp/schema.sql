CREATE TABLE Ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    unit TEXT NOT NULL,                -- grams, ml, pieces etc.
    cost_per_unit REAL NOT NULL        -- cost of 1 unit
);

CREATE TABLE Recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE RecipeIngredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    quantity REAL NOT NULL,            -- how many units used
    FOREIGN KEY(recipe_id) REFERENCES Recipes(id),
    FOREIGN KEY(ingredient_id) REFERENCES Ingredients(id)
);

CREATE TABLE Inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_id INTEGER NOT NULL,
    quantity REAL NOT NULL,            -- how many units you have
    FOREIGN KEY(ingredient_id) REFERENCES Ingredients(id)
);

CREATE TABLE Suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER,
    ingredient_id INTEGER,
    quantity REAL,
    total_cost REAL,
    order_date TEXT,
    FOREIGN KEY(supplier_id) REFERENCES Suppliers(id),
    FOREIGN KEY(ingredient_id) REFERENCES Ingredients(id)
);
