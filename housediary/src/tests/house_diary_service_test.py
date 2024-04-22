import unittest
from entities.user import User
from entities.task_manager import UnscheduledTask, ScheduledTask
from services.house_diary_service import HouseDiaryService
from repositories.user_repository import UserRepository
from repositories.tasks_repository import UnscheduledTasksRepository, ScheduledTasksRepository
from database_connection import test_get_database_connection, get_database_connection
from test_initialize_database import test_initialize_database
# u on lyhenne unscheduled ja s scheduled.


class TestHouseDiaryService(unittest.TestCase):
    """Testaa UserRepositoryn myös, nimi muuttunee myöhemmin.."""
    @classmethod
    def setUpClass(cls):
        """Vaihdaa tietokantayhteuden testitietokantaan"""
        cls.operation_connection = get_database_connection()
        cls.connection = test_get_database_connection()
        cls.user_repository = UserRepository(cls.connection)
        cls.tasks_repository = UnscheduledTasksRepository(cls.connection)
        cls.tasks_repository_s = ScheduledTasksRepository(cls.connection)
        cls.service = HouseDiaryService(
            cls.user_repository, cls.tasks_repository, cls.tasks_repository_s)

    def setUp(self):
        self.time = self.service.get_time()
        days = 90
        self.scheduled_time = self.service.get_scheduled_time(days)
        self.user_repository.create_new_user(User("Juho", "1919"))
        self.tasks_repository.create_new_u_task(
            UnscheduledTask(self.time, "Juho", "Korjaa katto"))
        self.tasks_repository_s.create_new_s_task(
            ScheduledTask(self.time, "Juho", "Vaihda IV- suodattimet", self.scheduled_time))

    def test_get_users(self):
        self.user_repository.create_new_user(User("Hanna", "2020"))

        result = self.service.get_users()

        self.assertIn("Juho", result)
        self.assertIn("Hanna", result)

        self.assertEqual(len(result), 2)

    def test_create_user_invalid_username(self):
        """Testaa jo olemassa olevaa nimeä"""
        result = self.service.create_user("Juho", "1212")

        self.assertIsNone(result)

    def test_create_user_valid_username(self):
        """Testaa uutta nimeä"""
        result = self.service.create_user("Jukka", "1212")

        self.assertIsInstance(result, User)

    def test_valid_login_works(self):
        result = self.service.login("Juho", "1919")

        self.assertIsInstance(result, User)

    def test_invalid_login_works(self):
        result = self.service.login("Juhoo", "1919")

        self.assertIsNone(result)

    def test_logout_works(self):
        self.service.login("Juhoo", "1919")
        self.service.logout()

        self.assertIsNone(self.service.get_current_user())

    def test_create_u_task(self):
        self.service.login("Juho", "1919")
        task_content = "Malaa seinät"
        created_task = self.service.create_u_task(task_content)

        self.assertEqual(created_task.u_task_content, task_content)
        self.assertEqual(created_task.u_visible, 1)

    def test_get_u_undone_tasks(self):
        self.service.login("Juho", "1919")
        task_content = "Malaa seinät"
        self.service.create_u_task(task_content)
        result = self.service.get_u_undone_tasks()

        self.assertEqual(len(result), 2)  # Laskee myös setupin

    def test_mark_u_undone_done_valid_id(self):
        self.service.login("Juho", "1919")
        task_content = "Malaa seinät"
        self.service.create_u_task(task_content)
        self.service.mark_u_undone_done(2)
        result = self.service.get_u_done_tasks()

        self.assertEqual(len(result), 1)

    def test_mark_u_undone_done_invalid_id(self):
        self.service.login("Juho", "1919")
        task_content = "Malaa seinät"
        self.service.create_u_task(task_content)
        self.service.mark_u_undone_done(3)
        result = self.service.get_u_done_tasks()

        self.assertEqual(len(result), 0)

    def test_delete_unscheduled_valid_id(self):
        self.service.login("Juho", "1919")
        task_content = "Malaa seinät"
        self.service.create_u_task(task_content)
        self.service.delete_u_task(1)
        result = self.service.get_u_undone_tasks()

        self.assertEqual(len(result), 1)

    def test_delete_unscheduled_invalid_id(self):
        self.service.login("Juho", "1919")
        task_content = "Malaa seinät"
        self.service.create_u_task(task_content)
        self.service.delete_u_task(5)
        result = self.service.get_u_undone_tasks()

        self.assertEqual(len(result), 2)

    def test_create_s_task(self):
        self.service.login("Juho", "1919")
        task_content = "Puhdista ilmalämpöpumput"
        days = 20
        created_task = self.service.create_s_task(task_content, days)

        self.assertEqual(created_task.s_task_content, task_content)
        self.assertEqual(created_task.s_visible, 1)

    def test_get_s_undone_tasks(self):
        self.service.login("Juho", "1919")
        task_content = "Puhdista ilmalämpöpumput"
        days = 20
        self.service.create_s_task(task_content, days)
        result = self.service.get_s_undone_tasks()

        self.assertEqual(len(result), 2)  # Laskee myös setupin

    def test_mark_s_undone_done_valid_id(self):
        self.service.login("Juho", "1919")
        task_content = "Puhdista ilmalämpöpumput"
        days = 20
        self.service.create_s_task(task_content, days)
        self.service.mark_s_undone_done(2)
        result = self.service.get_s_done_tasks()

        self.assertEqual(len(result), 1)

    def test_mark_s_undone_done_invalid_id(self):
        self.service.login("Juho", "1919")
        task_content = "Puhdista ilmalämpöpumput"
        days = 20
        self.service.create_s_task(task_content, days)
        self.service.mark_s_undone_done(3)
        result = self.service.get_s_done_tasks()

        self.assertEqual(len(result), 0)

    def test_delete_scheduled_valid_id(self):
        self.service.login("Juho", "1919")
        task_content = "Puhdista ilmalämpöpumput"
        days = 20
        self.service.create_s_task(task_content, days)
        self.service.delete_s_task(1)
        result = self.service.get_s_undone_tasks()

        self.assertEqual(len(result), 1)

    def test_delete_scheduled_invalid_id(self):
        self.service.login("Juho", "1919")
        task_content = "Puhdista ilmalämpöpumput"
        days = 20
        self.service.create_s_task(task_content, days)
        self.service.delete_s_task(5)
        result = self.service.get_s_undone_tasks()

        self.assertEqual(len(result), 2)

    def tearDown(self):
        """Alustaa testitietokannan jokaisen testin jälkeen"""
        test_initialize_database()
