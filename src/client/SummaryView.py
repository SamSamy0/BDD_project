from View import View
import customtkinter as ctk


class SummaryView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)#dit à la colonne de s'étirer pour remplir l'espace disponible

        self.title_label = ctk.CTkLabel(self, text="Résumés", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)#place le label dans la grille à la ligne 0, colonne 0, avec un padding de 20 pixels autour

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)#crée un bouton "Retour" qui appelle la méthode back_action lorsqu'il est cliqué
        self.back_button.grid(row=1, column=0, padx=20, pady=20)

    def back_action(self):
        self.controller.show_view("CLASS")#c'est l'objet Client qui appelle la méthode show_view pour afficher la vue "CLASS" lorsque le bouton "Retour" est cliqué
