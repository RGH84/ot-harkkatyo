from database_connection import test_get_database_connection

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

    connection.commit()

def test_initialize_database():
    connection = test_get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    test_initialize_database()