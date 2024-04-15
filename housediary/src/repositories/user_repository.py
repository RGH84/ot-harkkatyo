from entities.user import User


def get_user_from_user_row(user_row):

    if user_row:
        username = user_row["username"]
        password = user_row["password"]
        return User(username, password)
    return None


class UserRepository:
    """Tämä luokka vastaa käyttäjiin liittyvistä tietokantaoperaatioista."""

    def __init__(self, connection):
        self._connection = connection

    def create_new_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()

        return user

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user_row = cursor.fetchone()

        return get_user_from_user_row(user_row)

    def find_all_usernames(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT username FROM users")
        users = cursor.fetchall()

        return [user[0] for user in users]
