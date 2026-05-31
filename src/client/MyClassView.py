import customtkinter as ctk
from View import View


class MyClassView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="Cours", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        # Course List
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Liste des cours")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.courses = list()

        # btn add course
        self.add_button = ctk.CTkButton(
            self, text="Ajouter un cours", command=self.add_course_action
        )
        self.add_button.grid(row=2, column=0, padx=20, pady=10)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=3, column=0, padx=20, pady=20)

    def select_course(self, mnemonique):
        self.controller.current_cours = mnemonique
        self.controller.frames["SUMMARY"].mnemonique = mnemonique
        self.manager.checkSummaries(mnemonique)
        self.controller.previous_view = "MYCLASS"
        self.controller.show_view("SUMMARY")

    def add_course_action(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Ajouter un cours")
        popup.geometry("400x200")
        popup.after(100, popup.grab_set)
        popup.after(100, popup.lift)
        popup.after(100, lambda: popup.focus_force())

        ctk.CTkLabel(popup, text="Mnémonique du cours").pack(
            padx=20, pady=(15, 0), anchor="w"
        )
        mnemo_entry = ctk.CTkEntry(popup, placeholder_text="INFO-H303")
        mnemo_entry.pack(padx=20, pady=(0, 10), fill="x")

        def confirm():
            mnemo = mnemo_entry.get()
            if not mnemo:
                return
            popup.destroy()
            self.manager.addUserCourse(mnemo, self.manager.user.idUser)

        ctk.CTkButton(popup, text="Rejoindre", command=confirm).pack(
            padx=20, pady=15, fill="x"
        )

    def confirmedAdd(self, course=None):
        self.courses.append(course)
        self.refresh()

    def refusedAdd(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Erreur")
        popup.geometry("300x120")
        popup.after(100, popup.grab_set)
        popup.after(100, popup.lift)
        ctk.CTkLabel(
            popup,
            text="Impossible d'ajouter ce cours.\n(Déjà inscrit ou mnémonique invalide)",
        ).pack(padx=20, pady=20)
        ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=5)

    def back_action(self):
        self.controller.show_view("MENU")

    def refresh(self):
        # Vide la liste
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        for cours in self.courses:
            mnemo = cours.get("Mnemonique", "Inconnu")
            name = cours.get("Nom", "Sans Nom")
            fac = cours.get("Fac", "Sans Fac")
            utc = cours.get("Credits", 0)
            year = cours.get("Annee", "Inconnue")

            frame = ctk.CTkFrame(self.scroll_frame)
            frame.pack(padx=10, pady=5, fill="x")
            frame.grid_columnconfigure(0, weight=1)

            btn = ctk.CTkButton(
                frame,
                text=f"{mnemo} - {name} - {fac} - {utc} - {year}",
                command=lambda m=mnemo: self.select_course(
                    m
                ),  # m=mnemonique capture la valeur
            )
            btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

            btn_del = ctk.CTkButton(
                frame,
                text="Supprimer",
                fg_color="red",
                hover_color="darkred",
                command=lambda c=cours: self.delete_user_course_action(c),
            )
            btn_del.grid(row=0, column=1, padx=5, pady=5)

    def displayCourses(self, courses):
        self.courses = courses
        self.refresh()

    def delete_user_course_action(self, course):
        mnemo = course.get("Mnemonique", "Inconnu")
        self.manager.deleteUserCourse(mnemo, self.manager.user.idUser)

    def confirmedDelete(self, course):
        for obj in self.courses:
            if obj["Mnemonique"] == course["mnemo"]:
                self.courses.remove(obj)
                break
        self.refresh()

    def refusedDelete(self, course):
        pass

    def getUserCourse(self, data):
        self.courses = data if data else []
        self.after(0, self.refresh)

    def addUserCourse(self, data):
        if data:
            self.after(0, lambda: self.confirmedAdd(data))
        else:
            self.after(0, self.refusedAdd)

    def deleteUserCourse(self, data):
        if data:
            self.after(0, lambda: self.confirmedDelete(data))
        else:
            self.after(0, lambda: self.refusedDelete(None))
