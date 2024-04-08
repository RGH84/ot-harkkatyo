import unittest
from entities.user import User
from services.house_diary_service import HouseDiaryService
from repositories.user_repository import UserRepository
from database_connection import test_get_database_connection
from test_initialize_database import test_initialize_database

class TestHouseDiaryService(unittest.TestCase):
    """Testaa UserRepositoryn myös, nimi muuttunee myöhemmin.."""
    @classmethod
    def setUpClass(cls):
        """Vaihdaa tietokantayhteuden testitietokantaan"""
        cls.connection = test_get_database_connection()
        cls.user_repository = UserRepository(cls.connection)
        cls.service = HouseDiaryService(cls.user_repository)

    def setUp(self):

        self.user_repository.create_new_user(User("Juho", "1919"))

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

    def tearDown(self):
        """Alustaa testitietokannan jokaisen testin jälkeen"""
        test_initialize_database()
