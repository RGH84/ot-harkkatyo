from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')

    cursor.execute('''
        CREATE TABLE unscheduled_tasks_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            creation_time DATETIME NOT NULL,
            username TEXT NOT NULL,
            unscheduled_task_content TEXT NOT NULL,
            completion_time DATETIME,
            visible BOOLEAN DEFAULT 1
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
