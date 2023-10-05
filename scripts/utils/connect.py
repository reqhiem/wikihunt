import psycopg2


def get_postgresql_connection(db_params):
    try:
        # Define the connection parameters

        # Establish a connection to the database
        connection = psycopg2.connect(**db_params)

        # Return the connection object
        return connection

    except psycopg2.Error as error:
        print("Error connecting to the database:", error)
        return None
