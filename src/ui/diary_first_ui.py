commands = {
    "x": "x lopeta/kirjaudu ulos",
    "1": "1 luo uusi käyttäjä",
    "2": "Listaa käyttäjät",
    "3": "Kirjaudu sisään",
}


class HouseDiary:
    """Luokka, jonka kautta toimii sovelluksen tekstikäyttöliittymä,
    joka tullaan päivittämään graaffiseksi jossain vaiheessa
    """

    def __init__(self, house_diary_service):
        self.services = house_diary_service

    def start(self):
        for key, value in commands.items():
            print(f'"{key}": "{value}"')

        while True:
            command = input("Komento:")

            if command == "x":
                self._logout()
                break
            if command == "2":
                self._get_usernames()
            elif command == "1":
                self._new_user()
            elif command == "3":
                self._login()

    def _new_user(self):
        username = input("Käyttäjänimi: ")
        password = input("Salasana: ")

        if not self.services.check_length(username, password):
            print(
                "Tarkista kenttien pituudet, Käyttäjänimi min 3 kirjainta ja salasana min 4.")

        elif self.services.create_user(username, password):
            print("Käyttäjä luotu onnistuneesti.")
        else:
            print("Käyttäjänimi on jo olemassa.")

    def _login(self):
        username = input("Käyttäjänimi: ")
        password = input("Salasana: ")

        if self.services.login(username, password):
            print("Olet kirjautunut sisään.")
        else:
            print("Tarkista käyttäjätunnus ja salasana.")

    def _logout(self):

        self.services.logout()

    def _get_usernames(self):
        users = self.services.get_users()
        if users:
            for user in users:
                print(user)
        else:
            print("Ei käyttäjiä.")
