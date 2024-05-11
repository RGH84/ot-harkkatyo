import tkinter as tk
from tkinter import ttk, constants, simpledialog, messagebox


class TaskManagerView:
    """
    Näkymä tehtävienhallintaa varten, jossa käyttäjät voivat luoda uusia tehtäviä ja merkitä tehtäviä tehdyiksi.

    Attributes:
        _root (tk.Tk): Sovelluksen pääikkuna.
        _on_logout (function): Funktio, jota kutsutaan käyttäjän kirjautuessa ulos.
        _frame (ttk.Frame): Kehys, joka sisältää kaikki näkymän widgetit.
        _task_entry (ttk.Entry): Syötekenttä uusien tehtävien luomista varten.
        _task_list_frame (ttk.Frame): Kehys, jossa näytetään tehtävälista.
        _to_u_done (function): Funktio, joka siirtää näkymän suoritettuihin aikatauluttomiin tehtäviin.
        _to_s_done (function): Funktio, joka siirtää näkymän suoritettuihin aikataulutettuihin tehtäviin.
        _services (HouseDiaryService): Palvelu, joka tarjoaa sovelluslogiikan.
        _user (User): Kirjautunut käyttäjä.
    """

    def __init__(self, root, on_logout, to_unscheduled_done, to_scheduled_done, services):
        """
        Luo tehtävienhallintanäkymän.

        Args:
            root (tk.Tk): Sovelluksen pääikkuna.
            on_logout (function): Funktio, jota kutsutaan käyttäjän kirjautuessa ulos.
            to_unscheduled_done (function): Funktio, joka siirtää näkymän suoritettuihin aikatauluttomiin tehtäviin.
            to_scheduled_done (function): Funktio, joka siirtää näkymän suoritettuihin aikataulutettuihin tehtäviin.
            services (HouseDiaryService): Palvelu, joka tarjoaa sovelluslogiikan.
        """
        self._root = root
        self._on_logout = on_logout
        self._frame = None
        self._task_entry = None
        self._task_list_frame = None
        self._to_u_done = to_unscheduled_done
        self._to_s_done = to_scheduled_done
        self._services = services
        self._user = self._services.get_current_user()
        self._initialize()

    def pack(self):
        """Pakkaa näkymän kehyksen näkyviin."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän kehyksen."""
        self._frame.destroy()

    def _logout_handler(self):
        """Kirjautuu ulos sovelluksesta."""
        self._services.logout()
        self._on_logout()

    def _initialize_header(self):
        """Alustaa näkymän ylätunnisteen, joka sisältää käyttäjätiedot ja kirjautumisulospainikkeen."""
        user_label = ttk.Label(
            master=self._frame, text=f"Kirjautunut sisään nimellä {self._user.username}")
        logout_button = ttk.Button(
            master=self._frame, text="Kirjaudu ulos", command=self._logout_handler)
        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        logout_button.grid(row=0, column=1, padx=5,
                           pady=5, sticky=constants.EW)

    def _initialize_footer(self):
        """
        Alustaa näkymän alaosan, jossa käyttäjät voivat lisätä uusia tehtäviä ja merkitä tehtäviä tehdyiksi.
        """
        self._task_entry = ttk.Entry(master=self._frame, width=30)
        self._task_entry.insert(0, 'Kirjoita tehtävä:')
        self._task_entry.bind("<FocusIn>", lambda event: self._clear_placeholder(
            event, self._task_entry, 'Kirjoita tehtävä:'))
        self._task_entry.bind("<FocusOut>", lambda event: self._add_placeholder(
            event, self._task_entry, 'Kirjoita tehtävä:'))
        create_button = ttk.Button(
            master=self._frame, text="Luo aikatauluttamaton tehtävä", command=self._create_new_task)
        done_button = ttk.Button(
            master=self._frame, text="Merkkaa aikatauluttamaton tehdyksi", command=self._mark_u_undone_task_done)

        self._scheduled_task_entry = ttk.Entry(master=self._frame, width=30)
        self._scheduled_task_entry.insert(0, 'Kirjoita tehtävä:')
        self._scheduled_task_entry.bind("<FocusIn>", lambda event: self._clear_placeholder(
            event, self._scheduled_task_entry, 'Kirjoita tehtävä:'))
        self._scheduled_task_entry.bind("<FocusOut>", lambda event: self._add_placeholder(
            event, self._scheduled_task_entry, 'Kirjoita tehtävä:'))

        self._days_entry = ttk.Entry(master=self._frame, width=30)
        self._days_entry.insert(0, 'Monen päivän päästä oltava tehty:')
        self._days_entry.bind("<FocusIn>", lambda event: self._clear_placeholder(
            event, self._days_entry, 'Monen päivän päästä oltava tehty:'))
        self._days_entry.bind("<FocusOut>", lambda event: self._add_placeholder(
            event, self._days_entry, 'Monen päivän päästä oltava tehty:'))

        create_scheduled_button = ttk.Button(
            master=self._frame, text="Luo aikataulutettu tehtävä", command=self._create_new_scheduled)
        done_scheduled_button = ttk.Button(
            master=self._frame, text="Merkkaa aikataulutettu tehdyksi", command=self._mark_s_undone_task_done)

        self._task_entry.grid(row=3, column=0, padx=5,
                              pady=5, sticky=constants.EW)
        self._scheduled_task_entry.grid(
            row=8, column=0, padx=5, pady=5, sticky=constants.EW)
        self._days_entry.grid(row=8, column=1, padx=5,
                              pady=5, sticky=constants.EW)
        create_button.grid(row=3, column=1, padx=5,
                           pady=5, sticky=constants.EW)
        done_button.grid(row=3, column=2, padx=5, pady=5, sticky=constants.EW)
        create_scheduled_button.grid(
            row=8, column=2, padx=5, pady=5, sticky=constants.EW)
        done_scheduled_button.grid(
            row=8, column=3, padx=5, pady=5, sticky=constants.EW)

    def _create_new_task(self):
        """
        Luo uuden aikatauluttoman tehtävän syötteen perusteella.
        Ottaa käyttäjän syöttämän tehtävän ja luo sen, mikäli syöte ei
        ole tyhjä eikä pelkkä placeholder.
        """
        new_task = self._task_entry.get().strip()
        if new_task and new_task != 'Kirjoita tehtävä:':
            self._services.create_u_task(new_task)
            self._task_entry.delete(0, 'end')
            self._reload_task_list()
            messagebox.showinfo(
                "Onnistui", "Aikatauluton tehtävä luotu onnistuneesti")
        else:
            messagebox.showwarning("Huomio", "Tehtävää ei annettu.")

    def _create_new_scheduled(self):
        """
        Luo uuden aikataulutetun tehtävän syötteen ja päivämäärän perusteella.
        Ottaa käyttäjän syöttämät tiedot ja luo uuden aikataulutetun tehtävän,
        jos syötteet ovat kelvollisia.
        """
        scheduled_task = self._scheduled_task_entry.get().strip()
        days = self._days_entry.get().strip()
        if scheduled_task and scheduled_task != 'Kirjoita tehtävä:' and days.isdigit():
            self._services.create_s_task(scheduled_task, int(days))
            self._scheduled_task_entry.delete(0, 'end')
            self._days_entry.delete(0, 'end')
            self._reload_scheduled_task_list()
            messagebox.showinfo(
                "Onnistui", "Aikataulutettu tehtävä luotu onnistuneesti")
        else:
            messagebox.showwarning(
                "Virhe", "Anna kelvollinen tehtävän nimi ja päivien määrä")

    def _clear_placeholder(self, event, entry, placeholder):
        """
        Poistaa placeholder-tekstin syötekentästä, kun kenttä saa fokuksen.

        Args:
            event: Fokuksen saamisen tapahtuma.
            entry: Syötekenttä, josta placeholder poistetaan.
            placeholder: Teksti, joka poistetaan.
        """
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def _add_placeholder(self, event, entry, placeholder):
        """
        Lisää placeholder-tekstin syötekenttään, jos kenttä on tyhjä ja menettää fokuksen.

        Args:
            event: Fokuksen menettämisen tapahtuma.
            entry: Syötekenttä, johon placeholder lisätään.
            placeholder: Teksti, joka lisätään.
        """
        if not entry.get():
            entry.insert(0, placeholder)

    def _reload_task_list(self):
        """
        Päivittää näkymän, jossa näytetään kaikki tekemättömät aikatauluttamattomat tehtävät.
        """
        for widget in self._task_list_frame.winfo_children():
            widget.destroy()
        tasks_list = self._services.get_u_undone_tasks()
        for task in tasks_list:
            ttk.Label(self._task_list_frame, text=task).pack(anchor='w')

    def _reload_scheduled_task_list(self):
        """
        Päivittää näkymän, jossa näytetään kaikki tekemättömät aikataulutetut tehtävät.
        """
        for widget in self._scheduled_task_list_frame.winfo_children():
            widget.destroy()
        tasks_list = self._services.get_s_undone_tasks()
        for task in tasks_list:
            ttk.Label(self._scheduled_task_list_frame,
                      text=task).pack(anchor='w')

    def _mark_u_undone_task_done(self):
        """
        Merkitsee aikatauluttoman tehtävän tehdyksi annetun ID:n perusteella.
        Kysyy käyttäjältä tehtävän ID:n ja merkitsee tehtävän tehdyksi, jos ID on kelvollinen.
        Näyttää virheilmoituksen, jos ID on kelvoton.
        """
        task_id = simpledialog.askstring(
            "Merkkaa tehdyksi", "Anna tehtävän ID:")
        if task_id:
            success = self._services.mark_u_undone_done(task_id)
            if not success:
                messagebox.showerror(
                    "Virhe", "Tehtävän merkitseminen tehdyksi epäonnistui.")
            else:
                messagebox.showinfo(
                    "Onnistui", "Tehtävä merkitty tehdyksi onnistuneesti.")
                self._reload_task_list()
        else:
            messagebox.showinfo("Info", "Tehtävän ID:tä ei annettu.")

    def _mark_s_undone_task_done(self):
        """
        Merkitsee aikataulutetun tehtävän tehdyksi ja kysyy, haluaako käyttäjä uusia tehtävän.
        Jos käyttäjä päättää uusia tehtävän, pyydetään uusi aikataulu ja luodaan tehtävä uudelleen
        annetulla aikataululla. Näyttää virheilmoituksen, jos ID on kelvoton tai
        tehtävän sisältöä ei löydy.
        """
        task_id = simpledialog.askstring(
            "Merkkaa aikataulutettu tehtävä tehdyksi", "Anna tehtävän ID:")
        if task_id:
            success = self._services.mark_s_undone_done(task_id)
            if success:
                self._reload_scheduled_task_list()
                messagebox.showinfo(
                    "Onnistui", "Tehtävä merkitty tehdyksi onnistuneesti.")
                renew = messagebox.askyesno(
                    "Uusi tehtävä", "Haluatko uusia tämän tehtävän?")
                if renew:
                    task_content = self._services.get_scheduled_task_content_by_id(
                        task_id)
                    if task_content:
                        new_days = simpledialog.askinteger(
                            "Uusi aikataulu", "Anna päivien määrä, milloin tehtävä tulisi olla valmis:")
                        if new_days is not None:
                            self._services.create_s_task(
                                task_content, new_days)
                            self._reload_scheduled_task_list()
                            messagebox.showinfo(
                                "Onnistui", "Tehtävä on uusittu onnistuneesti.")
                        else:
                            messagebox.showinfo(
                                "Info", "Uutta aikataulua ei annettu.")
                    else:
                        messagebox.showerror(
                            "Virhe", "Tehtävän sisältöä ei löytynyt.")
            else:
                messagebox.showerror(
                    "Virhe", "Tehtävän merkitseminen tehdyksi epäonnistui.")
        else:
            messagebox.showinfo("Info", "Tehtävän ID:tä ei annettu.")

    def _go_to_done_u_tasks_view(self):
        """
        Siirtyy näkymään, jossa näytetään suoritetut aikatauluttamattomat tehtävät.
        """
        self._to_u_done()

    def _go_to_done_s_tasks_view(self):
        """
        Siirtyy näkymään, jossa näytetään suoritetut aikataulutetut tehtävät.
        """
        self._to_s_done()

    def _initialize(self):
        """
        Alustaa kaikki näkymän komponentit. Sisältää pääkehyksen rakentamisen
        ja ala- ja yläosien alustamisen.
        """
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()

        task_list_label = ttk.Label(
            self._frame, text="Tekemättömät aikatauluttamattomat tehtävät:", font=('Arial', 14))
        task_list_label.grid(row=1, column=0, columnspan=4,
                             sticky=constants.EW, pady=(10, 0))
        self._task_list_frame = ttk.Frame(master=self._frame)
        self._task_list_frame.grid(
            row=2, column=0, columnspan=4, sticky=constants.EW)

        scheduled_task_list_label = ttk.Label(
            self._frame, text="Tekemättömät aikataulutetut tehtävät:", font=('Arial', 14))
        scheduled_task_list_label.grid(
            row=5, column=0, columnspan=4, sticky=constants.EW, pady=(10, 0))
        self._scheduled_task_list_frame = ttk.Frame(master=self._frame)
        self._scheduled_task_list_frame.grid(
            row=6, column=0, columnspan=4, sticky=constants.EW)

        self._initialize_footer()

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
        self._frame.grid_columnconfigure(3, weight=1)

        self._reload_task_list()
        self._reload_scheduled_task_list()

        done_u_tasks_button = ttk.Button(
            self._frame, text="Näytä tehdyt aikatauluttomat tehtävät", command=self._go_to_done_u_tasks_view)
        done_s_tasks_button = ttk.Button(
            self._frame, text="Näytä tehdyt aikataulutetut tehtävät", command=self._go_to_done_s_tasks_view)
        done_u_tasks_button.grid(
            row=10, column=0, padx=10, pady=10, sticky=constants.EW)
        done_s_tasks_button.grid(
            row=10, column=1, padx=10, pady=10, sticky=constants.EW)
