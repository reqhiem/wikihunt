import psycopg2

import os

POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "wikihunt_db")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "wikihunt")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "wikihunt")


def get_postgresql_connection():
    try:
        # Define the connection parameters
        db_params = {
            "host": POSTGRES_HOST,
            "database": POSTGRES_DB,
            "user": POSTGRES_USER,
            "password": POSTGRES_PASSWORD,
        }

        # Establish a connection to the database
        connection = psycopg2.connect(**db_params)

        # Return the connection object
        return connection

    except psycopg2.Error as error:
        print("Error connecting to the database:", error)
        return None
