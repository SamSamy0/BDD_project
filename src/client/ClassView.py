import customtkinter as ctk
from View import View


class ClassView(View):

    def initView(self):
        self.title_label = ctk.CTkLabel(
            self, text="Cours", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=350, height=300)
        self.scrollable_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=2, column=0, padx=20, pady=(10, 20))

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def back_action(self):
        self.controller.show_view("MENU")

    def displayCourses(self, dictCours: dict):
        for cours in dictCours:
            mnemo = cours.get("Mnemonique", "Inconnu")
            name = cours.get("Nom", "Sans Nom")
            fac = cours.get("Fac", "Sans Fac")
            utc = cours.get("Credits", 0)
            year = cours.get("Annee", "Inconnue")

            texte_ligne = f"{mnemo} - {name} - {fac} - {utc} - {year}"
            label_cours = ctk.CTkLabel(self.scrollable_frame, text=texte_ligne)
            label_cours.pack(anchor="w", padx=10, pady=2)
