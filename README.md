# GameStore

## python version: 3.12.0

for venv git ignore: echo "*" > .venv/.gitignore


GameStore/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # Environment and app config
│   │   ├── security.py      # Password hashing, JWT tokens
│   │   └── database.py      # Database connection setup
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── users.py     # User routes
│   │   │   └── products.py  # Product routes
│   │   └── deps.py          # Dependencies (auth, db)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py         # User DB model
│   │   └── product.py      # Product DB model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py         # User Pydantic models
│   │   └── product.py      # Product Pydantic models
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── base.py         # Base CRUD operations
│   │   ├── user.py         # User CRUD operations
│   │   └── product.py      # Product CRUD operations
│   └── utils/
│       ├── __init__.py
│       └── utils.py        # Utility functions
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_users.py
│   └── test_products.py
├── alembic/                # Database migrations
│   ├── versions/
│   ├── env.py
│   └── alembic.ini
├── .env                    # Environment variables
├── requirements.txt
└── README.md