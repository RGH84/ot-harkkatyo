from database_connection import get_database_connection
from database_operations import drop_tables, create_tables


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
