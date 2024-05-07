from tkinter import ttk, StringVar, constants


class SignInView:
    """Luokka, joka hallitsee käyttäjän kirjautumisprosessia.

    Attributes:
        _root: Viite pääikkunaan, jossa näkymä sijaitsee.
        _on_successful_login: Funktio, joka suoritetaan onnistuneen kirjautumisen jälkeen.
        _on_switch_to_create_user: Funktio, joka aktivoi käyttäjän luontinäkymän.
        _services: Palvelut, jotka tarjoavat kirjautumislogiikan.
    """

    def __init__(self, root, on_successful_login, on_switch_to_create_user, services):
        """Alustaa kirjautumisnäkymän ja määrittelee sen riippuvuudet.

        Args:
            root: Pääikkunan viite.
            on_successful_login: Funktio, joka suoritetaan onnistuneen kirjautumisen jälkeen.
            on_switch_to_create_user: Funktio, joka vaihtaa käyttäjän luontinäkymään.
            services: Backend-palvelut sovelluslogiikalle.
        """
        self._root = root
        self._on_successful_login = on_successful_login
        self._on_switch_to_create_user = on_switch_to_create_user
        self._services = services
        self._initialize_interface()

    def pack(self):
        """Asettaa pääkehyksen näkyväksi käyttöliittymässä."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Poistaa pääkehyksen ja sen sisältämät komponentit."""
        self._frame.destroy()

    def _handle_login(self):
        """Käsittelee kirjautumistoiminnon, tarkistaa käyttäjänimen ja salasanan ja \
            kutsuu onnistuneen kirjautumisen toimintoa."""
        username = self._username_entry.get()
        password = self._password_entry.get()
        if self._services.login(username, password):
            self._on_successful_login()
        else:
            self._display_error("Väärä käyttäjänimi tai salasana")

    def _display_error(self, message):
        """Näyttää virheviestin käyttäjälle.

        Args:
            message: Virheviestin sisältö.
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Piilottaa virheviestin."""
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        """Alustaa käyttäjätunnuskentän."""
        username_label = ttk.Label(self._frame, text="Käyttäjänimi")
        self._username_entry = ttk.Entry(self._frame)
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        """Alustaa salasanakentän."""
        password_label = ttk.Label(self._frame, text="Salasana")
        self._password_entry = ttk.Entry(self._frame)
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_interface(self):
        """Rakentaa kaikki näkymän komponentit."""
        self._frame = ttk.Frame(self._root)
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(self._frame, textvariable=self._error_variable,
                                      foreground="red")
        self._error_label.grid(padx=5, pady=5)
        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            self._frame, text="Kirjaudu", command=self._handle_login)
        create_user_button = ttk.Button(self._frame, text="Luo käyttäjä",
                                        command=self._on_switch_to_create_user)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        self._hide_error()
