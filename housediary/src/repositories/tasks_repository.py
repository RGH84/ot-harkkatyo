class UnscheduledTasksRepository:
    """Luokka, joka vastaa aikatauluttomien tehtävien tallentamisesta ja hallinnasta tietokannassa.
    """

    def __init__(self, connection_unscheduled):
        """Luokan konstruktori, joka alustaa tietokantayhteyden.

        Args:
            connection_unscheduled (Connection): Tietokantayhteys, \
                jota käytetään aikatauluttomien tehtävien käsittelyyn.
        """
        self._connection_unscheduled = connection_unscheduled

    def create_new_u_task(self, u_task):
        """Luo uuden aikatauluttoman tehtävän tietokantaan.

        Args:
            u_task (UnscheduledTask): Aikatauluttoman tehtävän olio.

        Returns:
            UnscheduledTask: Palauttaa luodun tehtävän olion.
        """
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
        """Hakee kaikki käyttäjän tekemättömät aikatauluttomat tehtävät.

        Args:
            username (str): Käyttäjänimi, jonka tehtävät haetaan.

        Returns:
            list[dict]: Lista sanakirjoja, jotka sisältävät tekemättömien tehtävien tiedot.
        """
        cursor = self._connection_unscheduled.cursor()
        cursor.execute(
            "SELECT id, creation_time, unscheduled_task_content "
            "FROM unscheduled_tasks_table "
            "WHERE username = ? AND visible = 1",
            (username,)
        )
        u_task_list = cursor.fetchall()
        return [{'ID': row[0], 'Luotu': row[1], 'Tehtävä': row[2]} for row in u_task_list]

    def get_all_u_done_tasks(self, username):
        """Hakee kaikki käyttäjän valmiit aikatauluttomat tehtävät.

        Args:
            username (str): Käyttäjänimi, jonka valmiit tehtävät haetaan.

        Returns:
            list[dict]: Lista sanakirjoja, jotka sisältävät valmiiden tehtävien tiedot.
        """
        cursor = self._connection_unscheduled.cursor()
        cursor.execute(
            "SELECT id, creation_time, unscheduled_task_content, completion_time "
            "FROM unscheduled_tasks_table "
            "WHERE username = ? AND visible = 0",
            (username,)
        )
        u_task_list = cursor.fetchall()
        return [{'ID': row[0], 'Luotu': row[1], 'Tehtävä': row[2],
                 'Tehty': row[3]} for row in u_task_list]

    def mark_u_undone_task_done(self, task_id, username, done_time):
        """Merkitsee tekemättömän tehtävän valmiiksi.

        Args:
            task_id (int): Tehtävän tunniste.
            username (str): Käyttäjänimi, jonka tehtävä merkitään valmiiksi.
            done_time (datetime): Aika, joka asetetaan tehtävän valmistumisajaksi.

        Returns:
            bool: True, jos tehtävä onnistuneesti merkitty valmiiksi; False, jos tehtävää ei löydy.
        """
        cursor = self._connection_unscheduled.cursor()
        if not self.check_u_task_id(cursor, task_id, username):
            return False
        cursor.execute(
            "UPDATE unscheduled_tasks_table SET visible = 0, completion_time = ? "
            "WHERE id = ? AND username = ?",
            (done_time, task_id, username)
        )
        self._connection_unscheduled.commit()
        return True

    def delete_unscheduled_task(self, task_id, username):
        """Poistaa aikatauluttoman tehtävän tietokannasta.

        Args:
            task_id (int): Tehtävän tunniste, joka poistetaan.
            username (str): Käyttäjänimi, jonka tehtävä poistetaan.

        Returns:
            bool: True, jos tehtävä onnistuneesti poistettu; False, jos tehtävää ei löydy.
        """
        cursor = self._connection_unscheduled.cursor()
        if not self.check_u_task_id(cursor, task_id, username):
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
        """Tarkistaa, onko tehtävän tunniste (ID) ja käyttäjänimi voimassa tietokannassa.

        Args:
            cursor (Cursor): Tietokantakursori, jota käytetään SQL-kyselyn suorittamiseen.
            task_id (int): Tarkistettavan tehtävän tunniste.
            username (str): Käyttäjänimi, jonka tehtävästä ollaan kiinnostuneita.

        Returns:
            bool: Palauttaa True, jos tehtävä tunniste löytyy käyttäjälle, muutoin False.
        """
        cursor.execute(
            "SELECT id FROM unscheduled_tasks_table WHERE id = ? AND username = ?",
            (task_id, username)
        )
        result = cursor.fetchone()
        return result is not None


class ScheduledTasksRepository:
    """Luokka, joka vastaa aikataulutettujen tehtävien tallentamisesta tietokantaan.
    """

    def __init__(self, connection_scheduled):
        """Luokan konstruktori, joka alustaa tietokantayhteyden.

        Args:
            connection_scheduled (Connection): Tietokantayhteys, \
                jota käytetään aikataulutettujen tehtävien käsittelyyn.
        """
        self._connection_scheduled = connection_scheduled

    def create_new_s_task(self, s_task):
        """Luo uuden aikataulutetun tehtävän tietokantaan.

        Args:
            s_task (ScheduledTask): Aikataulutetun tehtävän olio.

        Returns:
            ScheduledTask: Palauttaa luodun tehtävän olion.
        """

        cursor = self._connection_scheduled.cursor()
        cursor.execute(
            """
            INSERT INTO scheduled_tasks_table
            (creation_time, username, scheduled_task_content, scheduled_time,
            completion_time, visible)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (s_task.s_creation_time, s_task.s_username, s_task.s_task_content,
             s_task.scheduled_time, s_task.s_completion_time, s_task.s_visible)
        )
        self._connection_scheduled.commit()
        return s_task

    def get_all_s_undone_tasks(self, username):
        """Hakee kaikki käyttäjän tekemättömät aikataulutetut tehtävät.

        Args:
            username (str): Käyttäjänimi, jonka tehtävät haetaan.

        Returns:
            list[dict]: Lista sanakirjoja, jotka sisältävät tekemättömien \
                aikataulutettujen tehtävien tiedot.
        """
        cursor = self._connection_scheduled.cursor()
        cursor.execute(
            "SELECT id, creation_time, scheduled_task_content, scheduled_time "
            "FROM scheduled_tasks_table "
            "WHERE username = ? AND visible = 1",
            (username,)
        )
        s_task_list = cursor.fetchall()
        return [{'ID': row[0], 'Luotu': row[1], 'Tehtävä': row[2], 'Aikataulu': row[3]}
                for row in s_task_list]

    def get_all_s_done_tasks(self, username):
        """Hakee kaikki käyttäjän valmiit aikataulutetut tehtävät.

        Args:
            username (str): Käyttäjänimi, jonka valmiit tehtävät haetaan.

        Returns:
            list[dict]: Lista sanakirjoja, jotka sisältävät valmiiden \
                aikataulutettujen tehtävien tiedot.
        """
        cursor = self._connection_scheduled.cursor()
        cursor.execute(
            "SELECT id, creation_time, scheduled_task_content, scheduled_time, completion_time "
            "FROM scheduled_tasks_table "
            "WHERE username = ? AND visible = 0",
            (username,)
        )
        s_task_list = cursor.fetchall()
        return [{'ID': row[0], 'Luotu': row[1], 'Tehtävä': row[2], 'Aikataulu': row[3],
                 'Tehty': row[4]} for row in s_task_list]

    def mark_s_undone_task_done(self, task_id, username, done_time):
        """Merkitsee tekemättömän aikataulutetun tehtävän valmiiksi.

        Args:
            task_id (int): Tehtävän tunniste.
            username (str): Käyttäjänimi, jonka tehtävä merkitään valmiiksi.
            done_time (datetime): Aika, joka asetetaan tehtävän valmistumisajaksi.

        Returns:
            bool: True, jos tehtävä onnistuneesti merkitty valmiiksi; False, jos tehtävää ei löydy.
        """
        cursor = self._connection_scheduled.cursor()
        if not self.check_s_task_id(cursor, task_id, username):
            return False
        cursor.execute(
            "UPDATE scheduled_tasks_table SET visible = 0, completion_time = ? "
            "WHERE id = ? AND username = ?",
            (done_time, task_id, username)
        )
        self._connection_scheduled.commit()
        return True

    def delete_scheduled_task(self, task_id, username):
        """Poistaa aikataulutetun tehtävän tietokannasta.

        Args:
            task_id (int): Tehtävän tunniste, joka poistetaan.
            username (str): Käyttäjänimi, jonka tehtävä poistetaan.

        Returns:
            bool: True, jos tehtävä onnistuneesti poistettu; False, jos tehtävää ei löydy.
        """
        cursor = self._connection_scheduled.cursor()
        if not self.check_s_task_id(cursor, task_id, username):
            return False
        cursor.execute(
            """
            DELETE FROM scheduled_tasks_table
            WHERE id = ? AND username = ?
            """,
            (task_id, username)
        )

        self._connection_scheduled.commit()
        return True

    def check_s_task_id(self, cursor, task_id, username):
        """Tarkistaa, onko annettu tehtävän tunniste ja käyttäjänimi voimassa tietokannassa.

        Args:
            task_id (int): Tarkistettavan tehtävän tunniste.
            username (str): Käyttäjänimi, jonka tehtävästä ollaan kiinnostuneita.

        Returns:
            bool: Palauttaa True, jos tehtävän tunniste löytyy käyttäjälle, muutoin False.
        """
        cursor.execute(
            "SELECT id FROM scheduled_tasks_table WHERE id = ? AND username = ?",
            (task_id, username)
        )
        result = cursor.fetchone()
        return result is not None

    def get_content_by_id(self, s_id):
        """Hakee tietyn aikataulutetun tehtävän sisällön ID:n perusteella.

        Args:
            s_id (int): Tehtävän yksilöivä tunniste.

        Returns:
            str: Haetun aikataulutetun tehtävän sisältö merkkijonona.
        """
        cursor = self._connection_scheduled.cursor()
        cursor.execute(
            "SELECT scheduled_task_content FROM scheduled_tasks_table WHERE id = ?",
            (s_id,)
        )
        result = cursor.fetchone()
        return result[0] if result else None
