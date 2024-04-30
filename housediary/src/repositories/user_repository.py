from entities.user import User


def get_user_from_user_row(user_row):
    """Muuntaa tietokantarivin User-olioksi.

    Args:
        user_row: Sisältää käyttäjätiedot, kuten käyttäjänimen ja salasanan.

    Returns:
        User|None: Palauttaa User-olion, jos user_row on määritelty, muutoin None.
    """
    if user_row:
        username = user_row["username"]
        password = user_row["password"]
        return User(username, password)
    return None


class UserRepository:
    """Luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteys, jonka kautta tapahtuu kommunikointi tietokannan kanssa.
        """
        self._connection = connection

    def create_new_user(self, user):
        """Luo uuden käyttäjän tietokantaan.

        Args:
            user (User): User-olio, joka sisältää uuden käyttäjän tiedot.

        Returns:
            User: Palauttaa User-olion, joka on luotu tietokantaan.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_by_username(self, username):
        """Etsii käyttäjän käyttäjänimen perusteella.

        Args:
            username (str): Käyttäjänimi, jonka perusteella käyttäjä etsitään.

        Returns:
            User|None: Palauttaa User-olion, jos käyttäjä löytyy; muutoin None.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user_row = cursor.fetchone()
        return get_user_from_user_row(user_row)

    def find_all_usernames(self):
        """Hakee kaikki käyttäjänimet tietokannasta.

        Returns:
            list[str]: Lista, joka sisältää kaikkien käyttäjien käyttäjänimet.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT username FROM users")
        users = cursor.fetchall()
        return [user[0] for user in users]
