```
chefapp/
│
├── data/
│   └── chefapp.db          # SQLite database file (created at runtime)
│
├── chefapp/
│   ├── __init__.py
│   ├── schema.sql          # CREATE TABLE statements (your file)
│   ├── db.py               # connection + schema loader
│   ├── models.py           # CRUD operations
│   ├── logic.py            # costing + inventory logic
│   ├── cli.py
│   └── gui/
│       ├── __init__.py
│       └── main_window.py
│
└── run_cli.py
```