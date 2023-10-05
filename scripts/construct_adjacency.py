# Description: This script constructs the adjacency list from the database

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

sql_query = """
    SELECT
        from_ AS source,
        ARRAY_AGG(to_) AS destinations
    FROM
        from_to_hashes
    GROUP BY
        from_
    ORDER BY
        from_;
"""

# Execute the query
cur.execute(sql_query)

# Fetch all the results
results = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

# Open file
file = open("inverted_index.input", "w")

# Process and print the results
for row in results:
    source, destinations = row
    str_destinations = " ".join(destinations)
    line = f"{source} {str_destinations}"
    file.write(line + "\n")
