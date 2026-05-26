import customtkinter as ctk
from View import View


class EvalView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)#dit à la colonne de s'étirer pour remplir l'espace disponible
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Evaluations", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)#place le label dans la grille à la ligne 0, colonne 0, avec un padding de 20 pixels autour

        #liste des résumés scrollable
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Liste des évaluations")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.evaluations = []
        
        self.btn_eval = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.btn_eval.grid(row=2, column=0, padx=20, pady=10)


    def back_action(self):
        self.manager.checkSummaries(self.controller.frames["SUMMARY"].mnemonique)
        # self.controller.show_view("SUMMARIES") #WARNING: NE MET PAS A JOUR LES SUMMARIES MAIS PAS GRAVE


    def eval_action(self,eval_id):
        self.manager.getEval(eval_id)



    def displayEvaluations(self):
        for widget in self.scroll_frame.winfo_children():
                widget.destroy()

        for auteur, note, id_eval in self.evaluations:
            
            frame = ctk.CTkFrame(self.scroll_frame)
            frame.pack(padx=10, pady=5, fill="x")
            frame.grid_columnconfigure(0, weight=1)
            #info résumé
            info = ctk.CTkLabel(frame, text=f"par {auteur} | * {note}/5")
            info.grid(row=0, column=0, padx=10, pady=8, sticky="w")
            #bouton voir
            btn = ctk.CTkButton(frame, text="voir", width=60, command=lambda i = id_eval: self.eval_action(i))
            btn.grid(row=0, column=1, padx=5, pady=8)



    def displayEval(self, auteur, commentaire, note):
        popup = ctk.CTkToplevel(self)
        popup.title("Voir le résumé")
        popup.geometry("500x400")

        popup.after(100, popup.grab_set)
        popup.after(100, popup.lift)
        popup.after(100, popup.focus_force)

        # Titre et auteur
        ctk.CTkLabel(popup, text=f"par {auteur}", text_color="gray").pack(padx=20, pady=(0, 10))
        # Séparateur
        ctk.CTkLabel(popup, text="─" * 50, text_color="gray").pack()

        # Contenu fictif
        ctk.CTkLabel(popup, text=commentaire, wraplength=400).pack(padx=20, pady=15)
        # Note moyenne
        ctk.CTkLabel(popup, text=f"Note moyenne : ★ {note}/5", text_color="gray").pack(padx=20, pady=(0, 15))

        # Boutons
        btn_frame = ctk.CTkFrame(popup, fg_color="transparent")
        btn_frame.pack(padx=20, pady=10, fill="x")
        btn_frame.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkButton(btn_frame,text="Fermer",fg_color="gray",hover_color="darkgray",command=popup.destroy).grid(row=0, column=1, padx=5)
