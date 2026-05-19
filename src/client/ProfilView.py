import customtkinter as ctk
from View import View


class ProfilView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="Mon Profil", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=5, column=0, padx=20, pady=20)

    def back_action(self):
        self.controller.show_view("MENU")
    

    def showProfile(self, data):
        self.after(0, lambda: self.displayStats(data))

    def displayStats(self, data):
        name = data.get("Nom")
        level = data.get("Niveau")
        points = data.get("Points")
        title = data.get("IdObjet")
        # nom de l'utilisateur
        self.name_label = ctk.CTkLabel(self, text=f"Nom : {name}")
        self.name_label.grid(row=1, column=0, padx=20, pady=10)
        # points
        self.points_label = ctk.CTkLabel(self, text=f"Points : {points}")
        self.points_label.grid(row=2, column=0, padx=20, pady=10)
        # niveau
        self.level_label = ctk.CTkLabel(self, text=f"Niveau : {level}")
        self.level_label.grid(row=3, column=0, padx=20, pady=10)
        # titre actif
        if title:
            title_text = f"Titre : {title}"
        else:
            title_text = "Aucun objet équipé"
        self.title_active_label = ctk.CTkLabel(self, text=title_text)

        self.title_active_label.grid(row=4, column=0, padx=20, pady=10)
