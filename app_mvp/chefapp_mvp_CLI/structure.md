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

### Running the application
```python
python3 run_cli.py --init-db
```
```python
python3 run_cli.py --cost "Pizza"
```

### checking on the DB

```
sqlite3 data/chefapp.db
```

```
| Command                      | What it does         |
| ---------------------------- | -------------------- |
| `.tables`                    | list all tables      |
| `.schema ingredients`        | show table structure |
| `SELECT * FROM ingredients;` | show table contents  |
| `.exit`                      | exit                 |
```