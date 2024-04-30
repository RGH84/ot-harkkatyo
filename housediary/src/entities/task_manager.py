class UnscheduledTask:
    """Luokka, jolla luodaan aikatauluttomat tehtävät.

    Attributes:
        u_creation_time (datetime): Tehtävän luontiaika.
        u_username (str): Käyttäjänimi, jolle tehtävä kuuluu.
        u_task_content (str): Tehtävän sisältö.
        u_completion_time (datetime, optional): Tehtävän valmistumisaika. Oletusarvo None.
        u_visible (int): 1 tarkoittaa näkyvää tekemättömissä tehtävissä, 0 ei-näkyvää. Oletusarvo 1.
    """

    def __init__(self, u_creation_time, u_username, u_task_content,
                 u_completion_time=None, u_visible=1):
        """Luokan konstruktori aikatauluttomien tehtävien luomiseksi.

        Args:
            u_creation_time (datetime): Tehtävän luontiaika.
            u_username (str): Käyttäjänimi, jolle tehtävä kuuluu.
            u_task_content (str): Tehtävän sisältö.
            u_completion_time (datetime, optional): Tehtävän valmistumisaika. Oletusarvo None.
            u_visible (int): 1 -> näkyy tekemättömissä tehtävissä, 0 ei-näy. Oletusarvo 1.
        """

        self.u_creation_time = u_creation_time
        self.u_username = u_username
        self.u_task_content = u_task_content
        self.u_completion_time = u_completion_time
        self.u_visible = u_visible


class ScheduledTask:
    """Luokka, jolla luodaan aikataulutetut tehtävät.

    Attributes:
        s_creation_time (datetime): Tehtävän luontiaika.
        s_username (str): Käyttäjänimi, jolle tehtävä kuuluu.
        s_task_content (str): Tehtävän sisältö.
        scheduled_time (datetime): Aika, johon mennessä tehtävä on määrä toteuttaa.
        s_completion_time (datetime, optional): Tehtävän valmistumisaika. Oletusarvo None.
        s_visible (int): 1 -> näkyy tekemättömissä tehtävissä, 0 ei-näy. Oletusarvo 1.
    """

    def __init__(self, s_creation_time, s_username, s_task_content, scheduled_time,
                 s_completion_time=None, s_visible=1):
        """Luokan konstruktori ajastettujen tehtävien luomiseksi.

        Args:
            s_creation_time (datetime): Tehtävän luontiaika.
            s_username (str): Käyttäjänimi, jolle tehtävä kuuluu.
            s_task_content (str): Tehtävän sisältö.
            scheduled_time (datetime): Aika, johon mennessä tehtävä on määrä toteuttaa.
            s_completion_time (datetime, optional): Tehtävän valmistumisaika. Oletusarvo None.
            s_visible (int): 1 -> näkyy tekemättömissä tehtävissä, 0 ei-näy. Oletusarvo 1.
        """

        self.s_creation_time = s_creation_time
        self.s_username = s_username
        self.s_task_content = s_task_content
        self.scheduled_time = scheduled_time
        self.s_completion_time = s_completion_time
        self.s_visible = s_visible
