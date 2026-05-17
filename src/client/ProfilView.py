from View import View
import customtkinter as ctk


class ProfilView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Mon Profil", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        #nom de l'utilisateur
        self.name_label = ctk.CTkLabel(self, text="Nom : Alice")
        self.name_label.grid(row=1, column=0, padx=20, pady=10)
        #points
        self.points_label = ctk.CTkLabel(self, text="Points : 350")
        self.points_label.grid(row=2, column=0, padx=20, pady=10)
        #niveau
        self.level_label = ctk.CTkLabel(self, text="Niveau : 3")
        self.level_label.grid(row=3, column=0, padx=20, pady=10)
        #titre actif
        self.title_active_label = ctk.CTkLabel(self, text="Titre actif : Maitre des résumés")
        self.title_active_label.grid(row=4, column=0, padx=20, pady=10)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=5, column=0, padx=20, pady=20)




    def back_action(self):
        self.controller.show_view("MENU")

