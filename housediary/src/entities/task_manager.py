# u on lyhenne unscheduled ja s scheduled.
class UnscheduledTask:
    """Luokka jolla luodaan ei ajastetut tehtävät"""

    def __init__(self, u_creation_time, u_username, u_task_content,
                 u_completion_time=None, u_visible=1):

        self.u_creation_time = u_creation_time
        self.u_username = u_username
        self.u_task_content = u_task_content
        self.u_completion_time = u_completion_time
        self.u_visible = u_visible
