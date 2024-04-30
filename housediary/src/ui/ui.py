from ui.login_view import SignInView
from ui.tasks_view import TaskManagerView
from ui.create_user_view import UserRegistrationView
from ui.done_tasks_view import UnscheduledDoneView, ScheduledDoneView


class UI:
    """Luokka, joka hallitsee käyttöliittymän tilaa eri näkymien välillä \
        siirtymistä ja sovelluksen tilan hallintaa.

    Attributes:
        _diary_service: Palveluluokka, joka tarjoaa liittymän sovelluslogiikan.
        _main_window: Pääikkuna (Tkinter), jossa näkymät näytetään.
        _active_view: Viittaus parhaillaan aktiivisena olevaan näkymään.
    """

    def __init__(self, root, diary_service):
        """Alustaa UI-luokan ja määrittää pääikkunan ja tarvittavat palvelut.

        Args:
            root: Tkinterin pääikkuna.
            diary_service: Backend-palvelut sovelluslogiikalle.
        """
        self._diary_service = diary_service
        self._main_window = root
        self._active_view = None

    def launch(self):
        """Käynnistää sovelluksen oletusnäkymällä, joka on kirjautumisnäkymä."""
        self._switch_to_login_view()

    def _clear_current_view(self):
        """Tyhjentää nykyisen näkymän, jos se on olemassa, ja asettaa \
            aktiivisen näkymän arvoksi None."""
        if self._active_view:
            self._active_view.destroy()
        self._active_view = None

    def _switch_to_login_view(self):
        """Siirtyy kirjautumisnäkymään."""
        self._clear_current_view()
        self._active_view = SignInView(
            self._main_window,
            self._switch_to_task_management_view,
            self._switch_to_user_creation_view,
            self._diary_service
        )
        self._active_view.pack()

    def _switch_to_task_management_view(self):
        """Siirtyy tehtävien hallintanäkymään."""
        self._clear_current_view()
        self._active_view = TaskManagerView(
            self._main_window,
            self._switch_to_login_view,
            self._switch_to_u_done_tasks_view,
            self._switch_to_s_done_tasks_view,
            self._diary_service
        )
        self._active_view.pack()

    def _switch_to_user_creation_view(self):
        """Siirtyy käyttäjän luomisnäkymään."""
        self._clear_current_view()
        self._active_view = UserRegistrationView(
            self._main_window,
            self._switch_to_login_view,
            self._diary_service
        )
        self._active_view.pack()

    def _switch_to_u_done_tasks_view(self):
        """Siirtyy suoritettujen aikatauluttomien tehtävien näkymään."""
        self._clear_current_view()
        self._active_view = UnscheduledDoneView(
            self._main_window,
            self._switch_to_task_management_view,
            self._diary_service
        )
        self._active_view.pack()

    def _switch_to_s_done_tasks_view(self):
        """Siirtyy suoritettujen aikataulutettujen tehtävien näkymään."""
        self._clear_current_view()
        self._active_view = ScheduledDoneView(
            self._main_window,
            self._switch_to_task_management_view,
            self._diary_service
        )
        self._active_view.pack()
