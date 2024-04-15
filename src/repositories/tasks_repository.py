# u on lyhenne unscheduled ja s scheduled.
class UnscheduledTasksRepository:
    """Tämä luokka vastaa aikatauuttomien tehtävien tallentamisesta."""

    def __init__(self, connection_unscheduled):
        self._connection_unscheduled = connection_unscheduled

    def create_new_u_task(self, u_task):
        cursor = self._connection_unscheduled.cursor()
        cursor.execute(
            """
            INSERT INTO unscheduled_tasks_table
            (creation_time, username, unscheduled_task_content, completion_time, visible)
            VALUES (?, ?, ?, ?, ?)
            """,
            (u_task.u_creation_time, u_task.u_username, u_task.u_task_content,
             u_task.u_completion_time, u_task.u_visible)
        )
        self._connection_unscheduled.commit()

        return u_task

    def get_all_u_undone_tasks(self, username):
        cursor = self._connection_unscheduled.cursor()
        cursor.execute(
            "SELECT id, creation_time, unscheduled_task_content "
            "FROM unscheduled_tasks_table "
            "WHERE username = ? AND visible = 1",
            (username,)
        )
        u_task_list = cursor.fetchall()
        u_tasks = [{'ID': row[0], 'Luotu': row[1], 'Tehtävä': row[2]}
                   for row in u_task_list]

        return u_tasks

    def get_all_u_done_tasks(self, username):
        cursor = self._connection_unscheduled.cursor()
        cursor.execute(
            "SELECT id, creation_time, unscheduled_task_content, completion_time "
            "FROM unscheduled_tasks_table "
            "WHERE username = ? AND visible = 0",
            (username,)
        )
        u_task_list = cursor.fetchall()
        u_tasks = [{'ID': row[0], 'Luotu': row[1],
                    'Tehtävä': row[2], 'Tehty': row[3]} for row in u_task_list]

        return u_tasks

    def mark_u_undone_task_done(self, task_id, username):
        cursor = self._connection_unscheduled.cursor()
        correct_id = self.check_u_task_id(cursor, task_id, username)
        if not correct_id:
            return False

        cursor.execute(
            "UPDATE unscheduled_tasks_table SET visible = 0 WHERE id = ? AND username = ?",
            (task_id, username)
        )
        self._connection_unscheduled.commit()

        return True

    def delete_unscheduled_task(self, task_id, username):
        cursor = self._connection_unscheduled.cursor()
        correct_id = self.check_u_task_id(cursor, task_id, username)
        if not correct_id:
            return False

        cursor.execute(
            """
            DELETE FROM unscheduled_tasks_table
            WHERE id = ? AND username = ?
            """,
            (task_id, username)
        )
        self._connection_unscheduled.commit()

        return True

    def check_u_task_id(self, cursor, task_id, username):
        cursor.execute(
            "SELECT id FROM unscheduled_tasks_table WHERE id = ? AND username = ?",
            (task_id, username)
        )
        result = cursor.fetchone()

        if result is None:
            return False
        return True
