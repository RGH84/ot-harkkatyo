from datetime import datetime
import pytz
from entities.user import User
from entities.task_manager import UnscheduledTask

# u on lyhenne unscheduled ja s scheduled.


class HouseDiaryService:
    """Tämä luokka vastaa sovelluslogiikasta"""

    def __init__(self, user_repository, unscheduled_task_repository):
        self._user = None
        self._user_repository = user_repository
        self._unscheduled_task_repository = unscheduled_task_repository

    def create_user(self, username, password):

        if self._user_repository.find_by_username(username):
            return None

        user = self._user_repository.create_new_user(User(username, password))

        return user

    def get_users(self):

        return self._user_repository.find_all_usernames()

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            return None

        self._user = user

        return user

    def logout(self):

        self._user = None

    def check_length(self, a, b):
        """Tarkistaa syötteen pituuden, voi tulla muitakin toimintoja, tälle ei testiä"""
        return len(a) >= 3 and len(b) >= 4

    def create_u_task(self, u_task_content):
        creation_time = self.get_time()

        u_task = self._unscheduled_task_repository.create_new_u_task(UnscheduledTask(
            creation_time, self._user.username, u_task_content,
            u_completion_time=None, u_visible=1))

        return u_task

    def get_u_undone_tasks(self):

        tasks = self._unscheduled_task_repository.get_all_u_undone_tasks(
            self._user.username)

        return tasks

    def get_u_done_tasks(self):

        tasks = self._unscheduled_task_repository.get_all_u_done_tasks(
            self._user.username)

        return tasks

    def mark_u_undone_done(self, task_id):
        done = self._unscheduled_task_repository.mark_u_undone_task_done(
            task_id, self._user.username)
        if done:
            return True
        return False

    def get_time(self):
        helsinki_timezone = pytz.timezone('Europe/Helsinki')
        current_time_in_helsinki = datetime.now(
            pytz.utc).astimezone(helsinki_timezone)
        formatted_time = current_time_in_helsinki.strftime('%d.%m.%Y %H:%M')

        return formatted_time
