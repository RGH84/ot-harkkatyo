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


class ScheduledTask:
    """Luokka jolla luodaan ajastetut tehtävät"""

    def __init__(self, s_creation_time, s_username, s_task_content, scheduled_time,
                 s_completion_time=None, s_visible=1):

        self.s_creation_time = s_creation_time
        self.s_username = s_username
        self.s_task_content = s_task_content
        self.scheduled_time = scheduled_time
        self.s_completion_time = s_completion_time
        self.s_visible = s_visible
