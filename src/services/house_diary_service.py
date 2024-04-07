from entities.user import User

class HouseDiaryService:
    """Tämä luokka vastaa sovelluslogiikasta"""

    def __init__(self, user_repository):
        self._user = None
        self._user_repository = user_repository

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

    def get_current_user(self):
        return self._user

    def check_length(self, a, b):
        """Tarkistaa syötteen pituuden, voi tulla muitakin toimintoja, tälle ei testiä"""
        return len(a) >= 3 and len(b) >= 4
