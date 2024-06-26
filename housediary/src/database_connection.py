import sqlite3
from config import DATABASE_FILE_PATH, TEST_DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row

test_connection = sqlite3.connect(TEST_DATABASE_FILE_PATH)
test_connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection


def test_get_database_connection():
    return test_connection
