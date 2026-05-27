from View import View
import customtkinter as ctk
import datetime


class SummaryView(View):

    def initView(self):

        self.average_label = ctk.CTkLabel(self, text="Calcul de la moyenne...", text_color="gray", font=ctk.CTkFont(slant="italic"))
        self.average_label.grid(row=0, column=0, sticky="e", padx=20)

        self.grid_columnconfigure(0, weight=1)#dit à la colonne de s'étirer pour remplir l'espace disponible
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Résumés", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)#place le label dans la grille à la ligne 0, colonne 0, avec un padding de 20 pixels autour

        #liste des résumés scrollable
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Liste des résumés")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.mnemonique = ""
        self.summaries = []
        self.btn_publish = ctk.CTkButton(self, text="Publier", command=self.publish_action)
        self.btn_publish.grid(row=2, column=0, padx=20, pady=10)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)#crée un bouton "Retour" qui appelle la méthode back_action lorsqu'il est cliqué
        self.back_button.grid(row=3, column=0, padx=20, pady=20)




    def back_action(self):
        previous = getattr(self.controller, 'previous_view', 'CLASS')
        self.mnemonique = ""
        self.controller.show_view(previous)

    def delete_action(self, frame, id_summ):
        self.manager.deleteSummary(id_summ, self.manager.user.idUser)
        # On ne rafraîchit plus ici, on attend le retour du serveur via le manager

    def publish_action(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Publier un résumé")
        popup.geometry("400x380")
        popup.after(100, popup.grab_set)
        popup.after(100, popup.lift)
        popup.after(100, popup.focus_force)

        ctk.CTkLabel(popup, text="Titre").pack(padx=20, pady=(15, 0), anchor="w")
        self.title_entry = ctk.CTkEntry(popup, placeholder_text="Titre du résumé")
        self.title_entry.pack(padx=20, pady=(0, 10), fill="x")

        ctk.CTkLabel(popup, text="Description").pack(padx=20, pady=(5, 0), anchor="w")
        self.content_entry = ctk.CTkTextbox(popup, height=120)
        self.content_entry.pack(padx=20, pady=(0, 10), fill="x")

        def confirm():
            title = self.title_entry.get()
            content = self.content_entry.get("1.0", "end-1c")#pour récupérer le contenu du Textbox, on utilise la méthode get avec les indices "1.0" (début du texte) et "end-1c" (fin du texte moins un caractère pour éviter d'avoir un saut de ligne en trop)
            if not title:
                print("Le titre est requis pour publier un résumé.")
                return
            popup.destroy()
            self.manager.addSummary(title, content, str(datetime.date.today()), 1, True, self.mnemonique, self.manager.user.idUser)#WARNING: HARDCODE VISIBILITE

        ctk.CTkButton(popup, text="Publier", command=confirm).pack(padx=20, pady=15, fill="x")
        self.average()


    def view_action(self, title, auteur, note):
        popup = ctk.CTkToplevel(self)
        popup.title("Voir le résumé")
        popup.geometry("500x400")

        popup.after(100, popup.grab_set)
        popup.after(100, popup.lift)
        popup.after(100, popup.focus_force)

        # Titre et auteur
        ctk.CTkLabel(popup, text=title, font=ctk.CTkFont(size=18, weight="bold")).pack(padx=20, pady=(15, 0))
        ctk.CTkLabel(popup, text=f"par {auteur}", text_color="gray").pack(padx=20, pady=(0, 10))
        # Séparateur
        ctk.CTkLabel(popup, text="─" * 50, text_color="gray").pack()

        # Contenu fictif
        ctk.CTkLabel(popup, text="Description du résumé...", wraplength=400).pack(padx=20, pady=15)
        # Note moyenne
        ctk.CTkLabel(popup, text=f"Note moyenne : ★ {note}/5", text_color="gray").pack(padx=20, pady=(0, 15))

        # Boutons
        btn_frame = ctk.CTkFrame(popup, fg_color="transparent")
        btn_frame.pack(padx=20, pady=10, fill="x")
        btn_frame.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkButton(btn_frame,text="Évaluer",command=lambda: [popup.destroy(), self.eval_action(title)]).grid(row=0, column=0, padx=5)

        ctk.CTkButton(btn_frame,text="Fermer",fg_color="gray",hover_color="darkgray",command=popup.destroy).grid(row=0, column=1, padx=5)

    def send_eval(self, title, note, comment, id_summ):
        self.manager.addReview(note,comment,self.manager.user.idUser,id_summ)

    def eval_action(self, title,id_summ):
        popup = ctk.CTkToplevel(self)
        popup.title("Évaluer un résumé")
        popup.geometry("400x300")
        popup.after(100, popup.grab_set)
        popup.after(100, popup.lift)
        popup.after(100, popup.focus_force)

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
            self.send_eval(title, note, comment,id_summ)

        ctk.CTkButton(popup, text="Soumettre", command=confirm).pack(padx=20, pady=15, fill="x")


    def displaySummaries(self):

        self.average()

        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        for id_summ, title, auteur, note in self.summaries:

            frame = ctk.CTkFrame(self.scroll_frame)
            frame.pack(padx=10, pady=5, fill="x")
            frame.grid_columnconfigure(0, weight=1)
            #info résumé
            if note:
                info = ctk.CTkLabel(frame, text=f"{title} | par {auteur} | {note}/5")
            else:
                #s'il n'y a pas de note on n'affiche pas la moyenne (moyenne == NONE)
                info = ctk.CTkLabel(frame, text=f"{title} | par {auteur} | ")
            info.grid(row=0, column=0, padx=10, pady=8, sticky="w")
            #bouton voir
            btn = ctk.CTkButton(frame, text="voir", width=60, command=lambda t=title, a=auteur, n=note: self.view_action(t, a, n))
            btn.grid(row=0, column=1, padx=5, pady=8)
            #btn supprimer
            btn = ctk.CTkButton(frame, text="supprimer", width=80, fg_color="red", hover_color="darkred", command=lambda f=frame, i=id_summ: self.delete_action(f, i))
            btn.grid(row=0, column=2, padx=5, pady=8)
            #btn modifier
            btn_edit = ctk.CTkButton(frame, text="modifier", width=80, fg_color="orange", hover_color="darkorange", command=lambda t=title, i=id_summ: self.eval_action(t,i))
            btn_edit.grid(row=0, column=3, padx=5, pady=8)



    def average(self):
        self.manager.getSummAverage()

    def update_average(self, data):
        average = data.get("AVG(compteur)","NULL")
        self.average_label.configure(text=f"Moyenne par étudiant : {average}  résumés")