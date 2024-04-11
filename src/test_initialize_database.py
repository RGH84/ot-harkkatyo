from database_connection import test_get_database_connection


def drop_tables(test_connection):
    test_cursor = test_connection.cursor()

    test_cursor.execute('''
        drop table if exists users;
    ''')

    test_connection.commit()


def create_tables(test_connection):
    test_cursor = test_connection.cursor()

    test_cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')

    test_connection.commit()


def test_initialize_database():
    test_connection = test_get_database_connection()

    drop_tables(test_connection)
    create_tables(test_connection)


if __name__ == "__main__":
    test_initialize_database()
