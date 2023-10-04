import psycopg2

from crawler.constants import (
    POSTGRES_HOST,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
)


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


def insert_hash_url(hash, url, clean_title, connection):
    try:
        cursor = connection.cursor()

        # Insert a new record
        cursor.execute(
            "INSERT INTO hashes_urls_titles (hash, url, clean_title) VALUES (%s, %s, %s)",
            (hash, url, clean_title),
        )

        # Commit the changes to the database
        connection.commit()

    except psycopg2.Error as error:
        print("Error inserting record:", error)
