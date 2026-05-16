from View import View
import customtkinter as ctk


class SummaryView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)#dit à la colonne de s'étirer pour remplir l'espace disponible
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Résumés", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)#place le label dans la grille à la ligne 0, colonne 0, avec un padding de 20 pixels autour

        #liste des résumés scrollable
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Liste des résumés")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        #données de test fictives
        resume_fictifs = [
            ("Résumé 1", "Alice", 4.5),
            ("Résumé 2", "Bob", 3.8),
            ("Résumé 3", "Charlie", 2),
        ]
        for titre, auteur, note in resume_fictifs:
            frame = ctk.CTkFrame(self.scroll_frame)
            frame.pack(padx=10, pady=5, fill="x")
            frame.grid_columnconfigure(0, weight=1)
            #info résumé
            info = ctk.CTkLabel(frame, text=f"{titre} | par {auteur} | * {note}/5")
            info.grid(row=0, column=0, padx=10, pady=5, sticky="w")
            #bouton voir
            btn = ctk.CTkButton(frame, text="voir", width=60)
            btn.grid(row=0, column=1, padx=10, pady=5)
            
        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)#crée un bouton "Retour" qui appelle la méthode back_action lorsqu'il est cliqué
        self.back_button.grid(row=1, column=0, padx=20, pady=20)

    def back_action(self):
        self.controller.show_view("CLASS")#c'est l'objet Client qui appelle la méthode show_view pour afficher la vue "CLASS" lorsque le bouton "Retour" est cliqué
