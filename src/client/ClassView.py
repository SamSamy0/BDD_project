import customtkinter as ctk
from View import View


class ClassView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="Cours", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        # liste des cours
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Liste des cours")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.courses = list()

        # btn ajouter cours
        self.add_button = ctk.CTkButton(
            self, text="Ajouter un cours", command=self.add_course_action
        )
        self.add_button.grid(row=2, column=0, padx=20, pady=10)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=3, column=0, padx=20, pady=20)

    def select_course(self, mnemonique):
        self.controller.current_cours = mnemonique
        self.controller.show_view("SUMMARY")

    def add_course_action(self, course=None):
        if course is not None:
            # Appelé depuis le popup avec les vraies valeurs
            mnemo = course.get("Mnemonique", "Inconnu")
            name = course.get("Nom", "Sans Nom")
            fac = course.get("Fac", "Sans Fac")
            utc = course.get("Credits", 0)
            year = course.get("Annee", 2025)
            self.courses.append(course)
            self.manager.addCourse(mnemo, name, fac, utc, year)
            self.refresh()
            return

        # Ouvre le popup de saisie
        popup = ctk.CTkToplevel(self)
        popup.title("Ajouter un cours")
        popup.geometry("400x500")
        popup.after(100, popup.grab_set)  # bloque la fenêtre principale
        #pour fixer le problème de focus du popup, on utilise after pour s'assurer que le popup est au premier plan et reçoit le focus
        popup.after(100, popup.lift)  # assure que le popup est au premier plan
        popup.after(100, lambda: popup.focus_force())  # donne le focus au popup

        ctk.CTkLabel(popup, text="Mnémonique").pack(padx=20, pady=(15, 0), anchor="w")
        mnemo_entry = ctk.CTkEntry(popup, placeholder_text="INFO-H303")
        mnemo_entry.pack(padx=20, pady=(0, 10), fill="x")

        ctk.CTkLabel(popup, text="Nom du cours").pack(padx=20, pady=(5, 0), anchor="w")
        nom_entry = ctk.CTkEntry(popup, placeholder_text="Base de données")
        nom_entry.pack(padx=20, pady=(0, 10), fill="x")

        ctk.CTkLabel(popup, text="Faculté").pack(padx=20, pady=(5, 0), anchor="w")
        fac_entry = ctk.CTkEntry(popup, placeholder_text="Sciences")
        fac_entry.pack(padx=20, pady=(0, 10), fill="x")

        ctk.CTkLabel(popup, text="Crédits").pack(padx=20, pady=(5, 0), anchor="w")
        credits_entry = ctk.CTkEntry(popup, placeholder_text="5")
        credits_entry.pack(padx=20, pady=(0, 10), fill="x")

        ctk.CTkLabel(popup, text="Année").pack(padx=20, pady=(5, 0), anchor="w")
        annee_entry = ctk.CTkEntry(popup, placeholder_text="2025")
        annee_entry.pack(padx=20, pady=(0, 10), fill="x")

        def confirm():
            course = {
                "Mnemonique": mnemo_entry.get(),
                "Nom": nom_entry.get(),
                "Fac": fac_entry.get(),
                "Credits": int(credits_entry.get()) if credits_entry.get().isdigit() else 0,
                "Annee": int(annee_entry.get()) if annee_entry.get().isdigit() else 2025
            }
            popup.destroy()
            self.add_course_action(course)

        ctk.CTkButton(popup, text="Confirmer", command=confirm).pack(padx=20, pady=15, fill="x")

    def back_action(self):
        self.controller.show_view("MENU")

    def refresh(self):
        #Vide la liste
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        for cours in self.courses:
            mnemo = cours.get("Mnemonique", "Inconnu")
            name = cours.get("Nom", "Sans Nom")
            fac = cours.get("Fac", "Sans Fac")
            utc = cours.get("Credits", 0)
            year = cours.get("Annee", "Inconnue")

            btn = ctk.CTkButton(
                self.scroll_frame,
                text=f"{mnemo} - {name} - {fac} - {utc} - {year}",
                command=lambda m=mnemo: self.select_course(
                    m
                ),  # m=mnemonique capture la valeur
            )
            btn.pack(padx=10, pady=5, fill="x")

    def displayCourses(self,courses):
        self.courses.extend(courses)
        for cours in self.courses:
            mnemo = cours.get("Mnemonique", "Inconnu")
            name = cours.get("Nom", "Sans Nom")
            fac = cours.get("Fac", "Sans Fac")
            utc = cours.get("Credits", 0)
            year = cours.get("Annee", "Inconnue")

            btn = ctk.CTkButton(
                self.scroll_frame,
                text=f"{mnemo} - {name} - {fac} - {utc} - {year}",
                command=lambda m=mnemo: self.select_course(
                    m
                ),  # m=mnemonique capture la valeur
            )
            btn.pack(padx=10, pady=5, fill="x")

    def rollback_course(self):
        if len(self.courses) > 0:
            self.courses.pop()
            self.after(0, self.refresh)
