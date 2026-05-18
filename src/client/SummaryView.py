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
        for title, auteur, note in resume_fictifs:
            frame = ctk.CTkFrame(self.scroll_frame)
            frame.pack(padx=10, pady=5, fill="x")
            frame.grid_columnconfigure(0, weight=1)
            #info résumé
            info = ctk.CTkLabel(frame, text=f"{title} | par {auteur} | * {note}/5")
            info.grid(row=0, column=0, padx=10, pady=8, sticky="w")
            #bouton voir
            btn = ctk.CTkButton(frame, text="voir", width=60, command=lambda t=title: self.eval_action(t))
            btn.grid(row=0, column=1, padx=5, pady=8)
            #btn supprimer
            btn = ctk.CTkButton(frame, text="supprimer", width=80, fg_color="red", hover_color="darkred", command=lambda f=frame: self.delete_action(f))
            btn.grid(row=0, column=2, padx=5, pady=8)
            #btn modfication
            btn_edit = ctk.CTkButton(frame, text="modifier", width=80, fg_color="orange", hover_color="darkorange", command=lambda f=frame, t=title: self.toggle_eval(f, t))#pour l'instant, réutilise le même formulaire que pour voir, à différencier plus tard
            btn_edit.grid(row=0, column=3, padx=5, pady=8)
        
        self.btn_publish = ctk.CTkButton(self, text="Publier un résumé", command=self.publish_action)
        self.btn_publish.grid(row=2, column=0, padx=20, pady=10)


        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)#crée un bouton "Retour" qui appelle la méthode back_action lorsqu'il est cliqué
        self.back_button.grid(row=3, column=0, padx=20, pady=20)

    def back_action(self):
        self.controller.show_view("CLASS")#c'est l'objet Client qui appelle la méthode show_view pour afficher la vue "CLASS" lorsque le bouton "Retour" est cliqué

    def publish_action(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Publier un résumé")
        popup.geometry("400x300")
        popup.grab_set()  # bloque la fenêtre principale

        ctk.CTkLabel(popup, text="Titre").pack(padx=20, pady=(15, 0), anchor="w")
        self.title_entry = ctk.CTkEntry(popup, placeholder_text="Titre du résumé")
        self.title_entry.pack(padx=20, pady=(0, 10), fill="x")

        ctk.CTkLabel(popup, text="Description").pack(padx=20, pady=(5, 0), anchor="w")
        self.content_entry = ctk.CTkEntry(popup, placeholder_text="Contenu du résumé")
        self.content_entry.pack(padx=20, pady=(0, 10), fill="x")

        def confirm():
            title = self.title_entry.get()
            content = self.content_entry.get()
            if not title:
                print("Le titre est requis pour publier un résumé.")
                return
            popup.destroy()
            print(f"Publier résumé : {title} - {content} pour le cours {self.controller.current_cours}")
            # Plus tard : appel au manager pour publier le résumé dans la BDD

        ctk.CTkButton(popup, text="Publier", command=confirm).pack(padx=20, pady=15, fill="x")
    
    def delete_action(self, frame):
        print("Supprimer résumé - test")
        frame.destroy()
        #que un test, plus tard appel au manager pour supp de la BDD

    def eval_action(self, title):
        popup = ctk.CTkToplevel(self)
        popup.title("Évaluer un résumé")
        popup.geometry("400x300")
        popup.grab_set()

        note_label = ctk.CTkLabel(popup, text="Note : 3")
        note_label.pack(padx=20, pady=(15, 0), anchor="w")

        slider = ctk.CTkSlider(
            popup,
            from_=1, to=5,
            number_of_steps=8,
            command=lambda val: note_label.configure(text=f"Note : {float(val):.1f}")
        )
        slider.set(3)
        slider.pack(padx=20, pady=5, fill="x")

        ctk.CTkLabel(popup, text="Commentaire").pack(padx=20, pady=(10, 0), anchor="w")
        comment_entry = ctk.CTkEntry(popup, placeholder_text="Commentaire...")
        comment_entry.pack(padx=20, pady=(0, 10), fill="x")

        def confirm():
            note = float(slider.get())
            comment = comment_entry.get()
            popup.destroy()
            self.send_eval(title, note, comment)

        ctk.CTkButton(popup, text="Soumettre", command=confirm).pack(padx=20, pady=15, fill="x")
    
    def send_eval(self, title, note, comment):
        print(f"Evaluer résumé {title} avec note {note} et commentaire : {comment}")
        #plus tard appel au manager pour envoyer l'évaluation à la BDD