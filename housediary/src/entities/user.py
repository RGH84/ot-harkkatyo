class User:
    """class that describes an individual user.
    Attributes:
        username: string value that describes the user's username.
        password: string value that describes the user's password.
    """

    def __init__(self, username, password):
        """The class constructor that creates a new user.
            Args:
                username: string value that describes the user's username.
                password: string value that describes the user's password.
        """

        self.username = username
        self.password = password
