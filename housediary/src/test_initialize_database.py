from database_connection import test_get_database_connection


def drop_tables(test_connection):
    test_cursor = test_connection.cursor()

    test_cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    test_cursor.execute('''
        DROP TABLE IF EXISTS unscheduled_tasks_table;
    ''')

    test_connection.commit()


def create_tables(test_connection):
    test_cursor = test_connection.cursor()

    test_cursor.execute('''
        CREATE TABLE users (
            username text primary key,
            password text
        );
    ''')

    test_cursor.execute('''
        CREATE TABLE unscheduled_tasks_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            creation_time DATETIME NOT NULL,
            username TEXT NOT NULL,
            unscheduled_task_content TEXT NOT NULL,
            completion_time DATETIME,
            visible BOOLEAN DEFAULT 1
        );
    ''')

    test_connection.commit()


def test_initialize_database():
    test_connection = test_get_database_connection()

    drop_tables(test_connection)
    create_tables(test_connection)


if __name__ == "__main__":
    test_initialize_database()
