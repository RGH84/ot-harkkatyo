from datetime import datetime, timedelta
import pytz
from entities.user import User
from entities.task_manager import UnscheduledTask, ScheduledTask


class HouseDiaryService:
    """Luokka, joka vastaa sovelluslogiikasta."""

    def __init__(self, user_repository, unscheduled_task_repository, scheduled_task_repository):
        """Luokan konstruktori, joka luo sovelluslogiikasta huolehtivan palvelun.

        Args:
            user_repository (UserRepository): Käyttäjätietojen hallintaan käytettävä repositorio.
            unscheduled_task_repository (UnscheduledTasksRepository): Aikatauluttomien tehtävien \
                hallintaan käytettävä repositorio.
            scheduled_task_repository (ScheduledTasksRepository): Aikataulutettujen tehtävien \
                hallintaan käytettävä repositorio.
        """
        self._user = None
        self._user_repository = user_repository
        self._unscheduled_task_repository = unscheduled_task_repository
        self._scheduled_task_repository = scheduled_task_repository

    def create_user(self, username, password):
        """Luo uuden käyttäjän, jos samannimistä ei ole jo olemassa.

        Args:
            username (str): Uuden käyttäjän käyttäjätunnus.
            password (str): Uuden käyttäjän salasana.

        Returns:
            User|None: Luotu käyttäjä-olio tai None, jos käyttäjätunnus on jo käytössä.
        """
        if self._user_repository.find_by_username(username):
            return None

        user = self._user_repository.create_new_user(User(username, password))
        return user

    def get_users(self):
        """Hakee kaikkien käyttäjien käyttäjätunnukset.

        Returns:
            list[str]: Lista käyttäjätunnuksista.
        """
        return self._user_repository.find_all_usernames()

    def login(self, username, password):
        """Kirjaa käyttäjän sisään, jos käyttäjätunnus ja salasana täsmäävät.

        Args:
            username (str): Käyttäjätunnus.
            password (str): Salasana.

        Returns:
            User|None: Kirjautuneen käyttäjän olio tai None, jos tunnistautuminen epäonnistuu.
        """
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            return None

        self._user = user
        return user

    def get_current_user(self):
        """Palauttaa tällä hetkellä kirjautuneen käyttäjän.

        Returns:
            User: Kirjautunut käyttäjä-olio.
        """
        return self._user

    def logout(self):
        """Kirjaa käyttäjän ulos järjestelmästä."""
        self._user = None

    def check_length(self, a, b):
        """Tarkistaa, ovatko kaksi syötettä riittävän pitkiä.

        Args:
            a (str): Ensimmäinen syöte.
            b (str): Toinen syöte.

        Returns:
            bool: True, jos molemmat syötteet ovat riittävän pitkiä, muuten False.
        """
        return len(a) >= 3 and len(b) >= 4

    def create_u_task(self, u_task_content):
        """Luo uuden aikatauluttoman tehtävän kirjautuneelle käyttäjälle.

        Args:
            u_task_content (str): Tehtävän sisältö.

        Returns:
            UnscheduledTask: Luotu tehtävä-olio.
        """
        creation_time = self.get_time()
        u_task = self._unscheduled_task_repository.create_new_u_task(
            UnscheduledTask(creation_time, self._user.username, u_task_content,
                            u_completion_time=None, u_visible=1))
        return u_task

    def get_u_undone_tasks(self):
        """Hakee kirjautuneen käyttäjän kaikki tekemättömät aikatauluttomat tehtävät.

        Returns:
            list[UnscheduledTask]: Lista tekemättömistä tehtävistä.
        """
        tasks = self._unscheduled_task_repository.get_all_u_undone_tasks(
            self._user.username)
        return tasks

    def get_u_done_tasks(self):
        """Hakee kirjautuneen käyttäjän kaikki valmiit aikatauluttomat tehtävät.

        Returns:
            list[UnscheduledTask]: Lista valmiista tehtävistä.
        """
        tasks = self._unscheduled_task_repository.get_all_u_done_tasks(
            self._user.username)
        return tasks

    def mark_u_undone_done(self, task_id):
        """Merkitsee tekemättömän aikatauluttoman tehtävän valmiiksi.

        Args:
            task_id (int): Valmiiksi merkittävän tehtävän tunniste.

        Returns:
            bool: True, jos tehtävä onnistuneesti merkittiin valmiiksi; False, jos ei.
        """

        done = self._unscheduled_task_repository.mark_u_undone_task_done(
            task_id, self._user.username, done_time=self.get_time())
        return done

    def delete_u_task(self, task_id):
        """Poistaa aikatauluttoman tehtävän.

        Args:
            task_id (int): Poistettavan tehtävän tunniste.

        Returns:
            bool: True, jos tehtävä onnistuneesti poistettiin; False, jos ei.
        """
        delete = self._unscheduled_task_repository.delete_unscheduled_task(
            task_id, self._user.username)
        return delete

    def create_s_task(self, s_task_content, days):
        """Luo uuden aikataulutetun tehtävän.

        Args:
            s_task_content (str): Tehtävän sisältö.
            days (int): Päivien määrä nykyhetkestä, jolloin tehtävän tulisi olla valmis.

        Returns:
            ScheduledTask: Luotu aikataulutettu tehtävä-olio.
        """
        creation_time = self.get_time()
        scheduled_time = self.get_scheduled_time(days)
        s_task = self._scheduled_task_repository.create_new_s_task(
            ScheduledTask(creation_time, self._user.username, s_task_content, scheduled_time,
                          s_completion_time=None, s_visible=1))
        return s_task

    def get_s_undone_tasks(self):
        """Hakee kirjautuneen käyttäjän kaikki tekemättömät aikataulutetut tehtävät.

        Returns:
            list[ScheduledTask]: Lista tekemättömistä aikataulutetuista tehtävistä.
        """
        tasks = self._scheduled_task_repository.get_all_s_undone_tasks(
            self._user.username)
        return tasks

    def get_s_done_tasks(self):
        """Hakee kirjautuneen käyttäjän kaikki valmiit aikataulutetut tehtävät.

        Returns:
            list[ScheduledTask]: Lista valmiista aikataulutetuista tehtävistä.
        """
        tasks = self._scheduled_task_repository.get_all_s_done_tasks(
            self._user.username)
        return tasks

    def mark_s_undone_done(self, task_id):
        """Merkitsee tekemättömän aikataulutetun tehtävän valmiiksi.

        Args:
            task_id (int): Valmiiksi merkittävän tehtävän tunniste.

        Returns:
            bool: True, jos tehtävä onnistuneesti merkittiin valmiiksi; False, jos ei.
        """

        done = self._scheduled_task_repository.mark_s_undone_task_done(
            task_id, self._user.username, done_time=self.get_time())
        return done

    def delete_s_task(self, task_id):
        """Poistaa aikataulutetun tehtävän.

        Args:
            task_id (int): Poistettavan tehtävän tunniste.

        Returns:
            bool: True, jos tehtävä onnistuneesti poistettiin; False, jos ei.
        """
        delete = self._scheduled_task_repository.delete_scheduled_task(
            task_id, self._user.username)
        return delete

    def get_time(self):
        """Hakee nykyisen ajan Helsingin aikavyöhykkeellä muodossa \
            'päivä.kuukausi.vuosi tunnit:minuutit'.

        Returns:
            str: Nykyhetken aika merkkijonona.
        """
        helsinki_timezone = pytz.timezone('Europe/Helsinki')
        current_time_in_helsinki = datetime.now(
            pytz.utc).astimezone(helsinki_timezone)
        return current_time_in_helsinki.strftime('%d.%m.%Y %H:%M')

    def get_scheduled_time(self, days):
        """Laskee tulevaisuuden ajan annetun päivämäärän perusteella.

        Args:
            days (int): Päivien määrä, jonka päästä aika lasketaan.

        Returns:
            str: Tulevaisuuden aika Helsingin aikavyöhykkeellä muodossa \
                'päivä.kuukausi.vuosi tunnit:minuutit'.
        """
        helsinki_timezone = pytz.timezone('Europe/Helsinki')
        current_time_in_helsinki = datetime.now(
            pytz.utc).astimezone(helsinki_timezone)
        scheduled_time = current_time_in_helsinki + timedelta(days=days)
        return scheduled_time.strftime('%d.%m.%Y %H:%M')

    def get_scheduled_task_content_by_id(self, s_id):
        """Hakee ja palauttaa tietyn aikataulutetun tehtävän sisällön sen tunnisteen perusteella.

        Args:
            s_id (int): Tehtävän tunniste, jonka sisältö haetaan.

        Returns:
            str: Aikataulutetun tehtävän sisältö merkkijonona, tai None jos tehtävää ei löydy.
        """
        return self._scheduled_task_repository.get_content_by_id(s_id)
