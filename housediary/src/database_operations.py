def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS unscheduled_tasks_table;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS scheduled_tasks_table;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
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

    cursor.execute('''
        CREATE TABLE scheduled_tasks_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            creation_time DATETIME NOT NULL,
            username TEXT NOT NULL,
            scheduled_task_content TEXT NOT NULL,
            scheduled_time INTEGER,
            completion_time DATETIME,
            visible BOOLEAN DEFAULT 1
        );
    ''')

    connection.commit()
