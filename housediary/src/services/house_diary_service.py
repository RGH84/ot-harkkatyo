from datetime import datetime, timedelta
import pytz
from entities.user import User
from entities.task_manager import UnscheduledTask, ScheduledTask

# u on lyhenne unscheduled ja s scheduled.


class HouseDiaryService:
    """Tämä luokka vastaa sovelluslogiikasta"""

    def __init__(self, user_repository, unscheduled_task_repository, scheduled_task_repository):
        self._user = None
        self._user_repository = user_repository
        self._unscheduled_task_repository = unscheduled_task_repository
        self._scheduled_task_repository = scheduled_task_repository

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

    def get_current_user(self):
        return self._user

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

    def delete_u_task(self, task_id):
        delete = self._unscheduled_task_repository.delete_unscheduled_task(
            task_id, self._user.username)
        if delete:
            return True
        return False

    def create_s_task(self, s_task_content, days):
        creation_time = self.get_time()
        scheduled_time = self.get_scheduled_time(days)

        s_task = self._scheduled_task_repository.create_new_s_task(ScheduledTask(
            creation_time, self._user.username, s_task_content, scheduled_time,
            s_completion_time=None, s_visible=1))

        return s_task

    def get_s_undone_tasks(self):

        tasks = self._scheduled_task_repository.get_all_s_undone_tasks(
            self._user.username)

        return tasks

    def get_s_done_tasks(self):

        tasks = self._scheduled_task_repository.get_all_s_done_tasks(
            self._user.username)

        return tasks

    def mark_s_undone_done(self, task_id):
        done = self._scheduled_task_repository.mark_s_undone_task_done(
            task_id, self._user.username)
        if done:
            return True
        return False

    def delete_s_task(self, task_id):
        delete = self._scheduled_task_repository.delete_scheduled_task(
            task_id, self._user.username)
        if delete:
            return True
        return False

    def get_time(self):
        helsinki_timezone = pytz.timezone('Europe/Helsinki')
        current_time_in_helsinki = datetime.now(
            pytz.utc).astimezone(helsinki_timezone)
        formatted_time = current_time_in_helsinki.strftime('%d.%m.%Y %H:%M')

        return formatted_time

    def get_scheduled_time(self, days):
        helsinki_timezone = pytz.timezone('Europe/Helsinki')
        current_time_in_helsinki = datetime.now(
            pytz.utc).astimezone(helsinki_timezone)
        scheduled_time = current_time_in_helsinki + timedelta(days=days)

        return scheduled_time.strftime('%d.%m.%Y %H:%M')
