# Description: This script populates the inverted index table in the database

import os
from utils.connect import get_postgresql_connection

POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "wikihunt_db")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "wikihunt")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "wikihunt")

db_params = {
    "host": POSTGRES_HOST,
    "database": POSTGRES_DB,
    "user": POSTGRES_USER,
    "password": POSTGRES_PASSWORD,
}

conn = get_postgresql_connection(db_params)

cur = conn.cursor()

sql_query = "INSERT INTO iindex (word, hashes) VALUES (%s, %s)"

# Specify the path to your file
file_path = "inverted_index.output"

# Read the file line by line
with open(file_path, "r") as file:
    for line in file:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            string, hashes = parts
            string = string.strip()
            hash_data = hashes.split()
            cur.execute(sql_query, (string, hash_data))
            # Commit the changes to the database
            conn.commit()
# Close the cursor and connection
cur.close()
conn.close()
