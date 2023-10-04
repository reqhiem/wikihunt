import os

POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "wikihunt_db")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "wikihunt")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "wikihunt")
