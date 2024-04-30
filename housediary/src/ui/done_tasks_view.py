from tkinter import ttk, constants, messagebox


class UnscheduledDoneView:
    def __init__(self, root, to_task_management_view, services):
        self._root = root
        self._frame = None
        self._tasks_frame = None
        self._task_delete_entry = None
        self._to_task_management_view = to_task_management_view
        self._services = services
        self._user = self._services.get_current_user()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _frontpage_handler(self):
        self._to_task_management_view()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame, text=f"Kirjautunut sisään nimellä {self._user.username}")
        frontpage_button = ttk.Button(
            master=self._frame, text="Mene etusivulle", command=self._frontpage_handler)
        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        frontpage_button.grid(row=0, column=1, padx=5,
                              pady=5, sticky=constants.EW)

    def _initialize_tasks_display(self):
        task_list_label = ttk.Label(
            self._frame, text="Tehdyt aikatauluttamattomat tehtävät:", font=('Arial', 14))
        task_list_label.grid(row=1, column=0, columnspan=4,
                             sticky=constants.EW, pady=(10, 0))
        self._tasks_frame = ttk.Frame(self._frame)
        self._tasks_frame.grid(row=2, column=0, columnspan=4,
                               sticky=(constants.EW, constants.NS))
        self._frame.grid_columnconfigure(0, weight=1)

        self._show_done_unscheduled_tasks()

        self._task_delete_entry = ttk.Entry(self._frame)
        self._task_delete_entry.insert(0, 'Anna ID')
        self._task_delete_entry.bind("<FocusIn>", lambda event: self._clear_placeholder(
            event, self._task_delete_entry, 'Anna ID'))
        self._task_delete_entry.bind("<FocusOut>", lambda event: self._add_placeholder(
            event, self._task_delete_entry, 'Anna ID'))
        self._task_delete_entry.grid(
            row=3, column=0, padx=5, pady=5, sticky=constants.EW)

        delete_button = ttk.Button(
            master=self._frame, text="Poista tehtävä", command=self._delete_task)
        delete_button.grid(row=3, column=1, padx=5,
                           pady=5, sticky=constants.EW)

    def _delete_task(self):
        task_id = self._task_delete_entry.get().strip()
        if task_id and task_id != 'Anna ID':
            success = self._services.delete_u_task(task_id)
            if success:
                messagebox.showinfo(
                    "Onnistui", "Tehtävä poistettiin onnistuneesti.")
                self._show_done_unscheduled_tasks()
            else:
                messagebox.showerror(
                    "Virhe", "Tehtävän poistaminen epäonnistui.")
        else:
            messagebox.showwarning("Huomio", "Anna kelvollinen tehtävän ID.")

    def _clear_placeholder(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, 'end')

    def _add_placeholder(self, event, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)

    def _show_done_unscheduled_tasks(self):
        for widget in self._tasks_frame.winfo_children():
            widget.destroy()
        tasks_list = self._services.get_u_done_tasks()
        for task in tasks_list:
            ttk.Label(self._tasks_frame, text=task).pack(anchor='w')

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()
        self._initialize_tasks_display()
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
        self._frame.grid_columnconfigure(3, weight=1)


class ScheduledDoneView:
    def __init__(self, root, to_task_management_view, services):
        self._root = root
        self._frame = None
        self._tasks_frame = None
        self._task_delete_entry = None
        self._to_task_management_view = to_task_management_view
        self._services = services
        self._user = self._services.get_current_user()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _frontpage_handler(self):
        self._to_task_management_view()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame, text=f"Kirjautunut sisään nimellä {self._user.username}")
        frontpage_button = ttk.Button(
            master=self._frame, text="Mene etusivulle", command=self._frontpage_handler)
        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        frontpage_button.grid(row=0, column=1, padx=5,
                              pady=5, sticky=constants.EW)

    def _initialize_tasks_display(self):
        task_list_label = ttk.Label(
            self._frame, text="Tehdyt aikataulutetut tehtävät:", font=('Arial', 14))
        task_list_label.grid(row=1, column=0, columnspan=4,
                             sticky=constants.EW, pady=(10, 0))
        self._tasks_frame = ttk.Frame(self._frame)
        self._tasks_frame.grid(row=2, column=0, columnspan=4,
                               sticky=(constants.EW, constants.NS))
        self._frame.grid_columnconfigure(0, weight=1)

        self._show_done_scheduled_tasks()

        self._task_delete_entry = ttk.Entry(self._frame)
        self._task_delete_entry.insert(0, 'Anna ID')
        self._task_delete_entry.bind("<FocusIn>", lambda event: self._clear_placeholder(
            event, self._task_delete_entry, 'Anna ID'))
        self._task_delete_entry.bind("<FocusOut>", lambda event: self._add_placeholder(
            event, self._task_delete_entry, 'Anna ID'))
        self._task_delete_entry.grid(
            row=3, column=0, padx=5, pady=5, sticky=constants.EW)

        delete_button = ttk.Button(
            master=self._frame, text="Poista tehtävä", command=self._delete_task)
        delete_button.grid(row=3, column=1, padx=5,
                           pady=5, sticky=constants.EW)

    def _delete_task(self):
        task_id = self._task_delete_entry.get().strip()
        if task_id and task_id != 'Anna ID':
            success = self._services.delete_s_task(task_id)
            if success:
                messagebox.showinfo(
                    "Onnistui", "Tehtävä poistettiin onnistuneesti.")
                self._show_done_scheduled_tasks()
            else:
                messagebox.showerror(
                    "Virhe", "Tehtävän poistaminen epäonnistui.")
        else:
            messagebox.showwarning("Huomio", "Anna kelvollinen tehtävän ID.")

    def _clear_placeholder(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, 'end')

    def _add_placeholder(self, event, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)

    def _show_done_scheduled_tasks(self):
        for widget in self._tasks_frame.winfo_children():
            widget.destroy()
        tasks_list = self._services.get_s_done_tasks()
        for task in tasks_list:
            ttk.Label(self._tasks_frame, text=task).pack(anchor='w')

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()
        self._initialize_tasks_display()
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
        self._frame.grid_columnconfigure(3, weight=1)
