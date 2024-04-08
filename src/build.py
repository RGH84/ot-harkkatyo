from initialize_database import initialize_database
from test_initialize_database import test_initialize_database

def build():
    initialize_database()
    test_initialize_database()

if __name__ == "__main__":
    build()
