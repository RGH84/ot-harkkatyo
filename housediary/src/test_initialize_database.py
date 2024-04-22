from database_connection import test_get_database_connection
from database_operations import drop_tables, create_tables


def test_initialize_database():
    test_connection = test_get_database_connection()
    drop_tables(test_connection)
    create_tables(test_connection)


if __name__ == "__main__":
    test_initialize_database()
