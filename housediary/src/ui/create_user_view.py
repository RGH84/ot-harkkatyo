from tkinter import ttk, StringVar, constants


class UserRegistrationView:
    """Luokka, joka hallitsee uusien käyttäjien rekisteröintiprosessia.

    Attributes:
        _root: Viite pääikkunaan, jossa näkymä sijaitsee.
        _navigate_to_login: Funktio, joka aktivoi kirjautumisnäkymän.
        _frame: Kehys, joka sisältää käyttöliittymäkomponentit.
        _username_entry: Käyttäjänimikenttä.
        _password_entry: Salasanakenttä.
        _error_variable: Muuttuja virheilmoituksille.
        _error_label: Tekstikenttä virheilmoituksia varten.
        _services: Palvelut, jotka tarjoavat rekisteröintilogiikan.
    """

    def __init__(self, root, navigate_to_login, services):
        """Alustaa käyttäjärekisteröintinäkymän ja määrittää sen riippuvuudet.

        Args:
            root: Pääikkunan viite.
            navigate_to_login: Funktio, joka vaihtaa kirjautumisnäkymään.
            services: Backend-palvelut sovelluslogiikalle.S
        """
        self._root = root
        self._navigate_to_login = navigate_to_login
        self._services = services
        self._initialize_components()

    def pack(self):
        """Pakkaa käyttöliittymän pääkehyksen näkyviin."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Poistaa käyttöliittymän pääkehyksen ja sen sisältämät komponentit."""
        self._frame.destroy()

    def _register_user(self):
        """Luo käyttäjän syötettyjen tietojen perusteella ja käsittelee rekisteröintiprosessin."""
        username = self._username_entry.get()
        password = self._password_entry.get()
        if not self._services.check_length(username, password):
            self._display_error(
                "Tarkista kenttien pituudet: Käyttäjänimi vähintään 3 \
                    merkkiä ja salasana vähintään 4.")
            return
        try:
            if self._services.create_user(username, password):
                self._navigate_to_login()
            else:
                self._display_error("Käyttäjänimi on jo olemassa.")
        except Exception as e:
            self._display_error(str(e))

    def _display_error(self, message):
        """Näyttää virheviestin käyttäjälle.

        Args:
            message: Virheviestin sisältö.
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Piilottaa virheviestin näkyvistä."""
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

    def _initialize_components(self):
        """Rakentaa kaikki näkymän komponentit."""
        self._frame = ttk.Frame(self._root)
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._error_label.grid(padx=5, pady=5)
        self._initialize_username_field()
        self._initialize_password_field()

        create_user_button = ttk.Button(
            self._frame, text="Luo", command=self._register_user)
        login_button = ttk.Button(
            self._frame, text="Kirjaudu", command=self._navigate_to_login)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        self._hide_error()
