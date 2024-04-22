commands = {
    "x": "lopeta",
    "1": "luo uusi käyttäjä",
    "2": "Listaa käyttäjät",
    "3": "Kirjaudu sisään",
}

commands_login = {
    "x": "kirjaudu ulos",
    "1": "Luo uusi aikatauluttamaton tehtävä",
    "2": "Näytä tekemättömät aikatauluttomat tehtävät",
    "3": "Näytä tehdyt aikatauluttomat tehtävät",
    "4": "Merkkaa aikatauluton tehtävä tehdyksi",
    "5": "Poista aikatauluton tehtävä",
    "6": "Luo uusi aikataulutettu tehtävä",
    "7": "Näytä tekemättömät aikataulutetut tehtävät",
    "8": "Näytä tehdyt aikataulutetut tehtävät",
    "9": "Merkkaa aikataulutettu tehtävä tehdyksi",
    "10": "Poista aikataulutettu tehtävä",
    "11": "Mene etusivulle",
}


class HouseDiary:
    """Luokka, jonka kautta toimii sovelluksen tekstikäyttöliittymä,
    joka tullaan päivittämään graaffiseksi jossain vaiheessa
    """

    def __init__(self, house_diary_service):
        self.services = house_diary_service

    def start(self):

        while True:
            print()
            for key, value in commands.items():
                print(f'"{key}": "{value}"')
            print()

            command = input("Komento:")

            if command == "x":
                self._logout()
                break
            if command == "1":
                self._new_user()
            elif command == "2":
                self._get_usernames()
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
            print()
            print("Olet kirjautunut sisään.")
            print()
            for key, value in commands_login.items():
                print(f'"{key}": "{value}"')
            print()
            self._show_undone_unscheduled_tasks()
            print()
            self._show_undone_scheduled_tasks()
            print()

            while True:

                command = input("Komento:")
                print()

                if command == "x":
                    self._logout()
                    break
                if command == "1":
                    self._create_new_unscheduled()
                elif command == "2":
                    self._show_undone_unscheduled_tasks()
                elif command == "3":
                    self._show_done_unscheduled_tasks()
                elif command == "4":
                    self._mark_u_undone_task_done()
                elif command == "5":
                    self._delete_u_task()
                elif command == "6":
                    self._create_new_scheduled()
                elif command == "7":
                    self._show_undone_scheduled_tasks()
                elif command == "8":
                    self._show_done_scheduled_tasks()
                elif command == "9":
                    self._mark_s_undone_task_done()
                elif command == "10":
                    self._delete_s_task()
                elif command == "11":
                    self._go_frontpage()
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

    def _create_new_unscheduled(self):
        unscheduled_task = input("Tehtävä: ")

        self.services.create_u_task(unscheduled_task)

        print("Tehtävä luotu onnistuneesti")

    def _show_undone_unscheduled_tasks(self):
        tasks_list = self.services.get_u_undone_tasks()
        print("Tekemättömät aikatauluttomat tehtävät:")
        for task in tasks_list:
            print(task)

    def _show_done_unscheduled_tasks(self):
        tasks_list = self.services.get_u_done_tasks()
        print("Tehdyt aikatauluttomat tehtävät:")
        for task in tasks_list:
            print(task)

    def _mark_u_undone_task_done(self):
        task_id = input("Merkkaa tehdyksi ID: ")
        success = self.services.mark_u_undone_done(task_id)
        if not success:
            print("Tehtävän merkitseminen tehdyksi epäonnistui.")
        else:
            print("Tehtävä merkitty tehdyksi onnistuneesti.")

    def _delete_u_task(self):
        task_id = input("Poista tehtävä ID: ")
        success = self.services.delete_u_task(task_id)
        if not success:
            print("Tehtävän poistaminen epäonnistui.")
        else:
            print("Tehtävä poistettiin onnistuneesti.")

    def _create_new_scheduled(self):
        scheduled_task = input("Tehtävä: ")
        days = int(input("Monen päivän päästä tehtävä tulee olla tehtynä:"))

        self.services.create_s_task(scheduled_task, days)

        print("Tehtävä luotu onnistuneesti")

    def _show_undone_scheduled_tasks(self):
        tasks_list = self.services.get_s_undone_tasks()
        print("Tekemättömät aikataulutetut tehtävät:")
        for task in tasks_list:
            print(task)

    def _show_done_scheduled_tasks(self):
        tasks_list = self.services.get_s_done_tasks()
        print("Tehdyt aikataulutetut tehtävät:")
        for task in tasks_list:
            print(task)

    def _mark_s_undone_task_done(self):
        task_id = input("Merkkaa tehdyksi ID: ")
        success = self.services.mark_s_undone_done(task_id)
        if not success:
            print("Tehtävän merkitseminen tehdyksi epäonnistui.")
        else:
            print("Tehtävä merkitty tehdyksi onnistuneesti.")

    def _delete_s_task(self):
        task_id = input("Poista tehtävä ID: ")
        success = self.services.delete_s_task(task_id)
        if not success:
            print("Tehtävän poistaminen epäonnistui.")
        else:
            print("Tehtävä poistettiin onnistuneesti.")

    def _go_frontpage(self):
        print()
        for key, value in commands_login.items():
            print(f'"{key}": "{value}"')
        print()
        self._show_undone_unscheduled_tasks()
        print()
        self._show_undone_scheduled_tasks()
        print()
