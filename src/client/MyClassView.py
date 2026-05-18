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

        # liste des cours
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Liste des cours")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.courses = list()

        # btn ajouter cours
        self.add_button = ctk.CTkButton(
            self, text="Ajouter un cours", command=self.delete_user_course_action
        )
        self.add_button.grid(row=2, column=0, padx=20, pady=10)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=3, column=0, padx=20, pady=20)


    def select_course(self, mnemonique):
        self.controller.current_cours = mnemonique
        self.controller.show_view("SUMMARY")

    def add_course_action(self,course=None):
        # TODO: Implémenter un pop up pour récupérer les valeurs
        if course is None:
            course = {
                "Mnemonique": "TEST-123",
                "Nom": "Nouveau Cours",
                "Fac": "Sciences",
                "Credits": 5,
                "Annee": 1
            }
        mnemo = course.get("Mnemonique", "Inconnu")
        name = course.get("Nom", "Sans Nom")
        fac = course.get("Fac", "Sans Fac")
        utc = course.get("Credits", 0)
        year = course.get("Annee", "Inconnue")


        self.manager.addUserCourse(mnemo,self.manager.current_user)
        print("Ajouter un cours -test")

    def confirmedAdd(self,course = None):
        self.courses.append(course)
        self.refresh()

    def refusedAdd(self):
        if len(self.courses) > 0:
            self.courses.pop()
            self.after(0,self.refresh)

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
        self.courses = courses
        self.refresh()

    def delete_user_course_action(self,course = None):
        if course is None:
            course = {
                "Mnemonique": "TEST-123",
                "Nom": "Nouveau Cours",
                "Fac": "Sciences",
                "Credits": 5,
                "Annee": 1
            }
        mnemo = course.get("Mnemonique", "Inconnu")
        name = course.get("Nom", "Sans Nom")
        fac = course.get("Fac", "Sans Fac")
        utc = course.get("Credits", 0)
        year = course.get("Annee", "Inconnue")

        self.manager.deleteUserCourse(mnemo,self.manager.current_user)

    def confirmedDelete(self,course):
        for obj in self.courses:
            if obj["Mnemonique"] == course["mnemo"]:
                self.courses.remove(obj)
                break
        self.refresh()

    def refusedDelete(self,course):
        #TODO:POP-UP
        pass


