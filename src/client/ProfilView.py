import customtkinter as ctk
from View import View


class ProfilView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="Mon Profil", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.name_label = ctk.CTkLabel(self, text="")
        self.name_label.grid(row=1, column=0, padx=20, pady=10)

        self.points_label = ctk.CTkLabel(self, text="")
        self.points_label.grid(row=2, column=0, padx=20, pady=10)

        self.level_label = ctk.CTkLabel(self, text="")
        self.level_label.grid(row=3, column=0, padx=20, pady=10)

        self.title_active_label = ctk.CTkLabel(self, text="")
        self.title_active_label.grid(row=4, column=0, padx=20, pady=10)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=5, column=0, padx=20, pady=20)

    def back_action(self):
        self.controller.show_view("MENU")

    def displayStats(self, data):
        name = data.get("Nom", "Sans Nom")
        level = data.get("Niveau", "Sans Niveau")
        points = data.get("Points", "Pas de Points")
        title = data.get("NomObjet", "Aucun Objet équipé")

        title_text = f"Titre : {title}" if title else "Aucun objet équipé"

        self.name_label.configure(text=f"Nom : {name}")
        self.points_label.configure(text=f"Points : {points}")
        self.level_label.configure(text=f"Niveau : {level}")
        self.title_active_label.configure(text=title_text)
