# Project CloudChef

## Application Scope

### 1 - Core Features

1. Recipe Management
- Store ingradients, quantities, and instructions
- Categorize recipes (breakfast, lunch, dessert, etc)
- Search/filter recipes
2. Menu Costing
- Calculate cost per recipe based on ingredient prices
- Track profit margin for menu items
3. Inventory Control 
- Track stock level of ingredients
- Reduce stock when recipes are used
- Notify when stock is low
4. Purchasing & Ordering
- Generate shopping lists based on low inventory or planned menus
5. User Interface
- Desktop GUI (for Ubuntu, likely GTK or Qt)
6. Multi-user support
- Elastic scaling for multi-user workloads

### 2 - Technology Stack

Backend / Core Logic:
- GTK with Python --> for a native Linux feel
- **for later**: Flask backend / Reach frontend
Development Tools:
- Git for version control
- Poetry for Python dependency management
- Docker (for isolating dev environment)

### 3 - MVP
Step 1: Database schema
- Tables: Ingredients, Recipes, RecipeIngredients, Inventory, Suppliers, Orders
- Start with SQLite for simplicity

Step 2: CLI prototype

Before building GUI, making a command-line interface to test core features:
- Add recipes
- Calculate cost
- Manage inventory

Step 3: GUI
- Once CLI works, map functionality to GTK windows/buttons
- Use Glad to design GTK layouts visually

### 5 - Development Workflow
1. Plan & Prototype
- Write schema and core functions in Python
2. Test Core Logic
- Ensure costing and inventory calculations work
3. Add GUI
- Start with main window --> Recipe CRUD --> Inventory --> Menu costing
4. Package for Ubuntu
- Use ```pyinstaller``` to create a .deb or binary for Ubuntu 24.04
