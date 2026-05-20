from View import View
import customtkinter as ctk
import datetime


class SummaryView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)#dit à la colonne de s'étirer pour remplir l'espace disponible
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Résumés", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)#place le label dans la grille à la ligne 0, colonne 0, avec un padding de 20 pixels autour

        #liste des résumés scrollable
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Liste des résumés")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        #resumé vide
        self.mnemonique = ""
        self.summaries = []

        #Sep vis
        self.separator = ctk.CTkLabel(self, text="---Publier un résumé---", font=ctk.CTkFont(size=16, weight="bold"))
        self.separator.grid(row=2, column=0, padx=20, pady=(20,5))
        #remplissage resume
        self.title_entry = ctk.CTkEntry(self, placeholder_text="Titre du résumé")
        self.title_entry.grid(row=3, column=0, padx=20, pady=5, sticky="ew")
        self.content_entry = ctk.CTkEntry(self, placeholder_text="Description du résumé")
        self.content_entry.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

        self.btn_publish = ctk.CTkButton(self, text="Publier", command=self.publish_action)
        self.btn_publish.grid(row=5, column=0, padx=20, pady=10)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)#crée un bouton "Retour" qui appelle la méthode back_action lorsqu'il est cliqué
        self.back_button.grid(row=6, column=0, padx=20, pady=20)

    def back_action(self):
        previous = getattr(self.controller, 'previous_view', 'CLASS')
        self.mnemonique = ""
        self.controller.show_view(previous)

    def publish_action(self):
        title = self.title_entry.get()
        content = self.content_entry.get()

        if title and content:
            self.manager.addSummary(title,content,str(datetime.date.today()),1,True,self.mnemonique,self.manager.user.idUser) #WARNING: HARDCODE VISIBILITE
            self.manager.checkSummaries(self.mnemonique)
        else:
            print("faut un titre et une description zinc") 

    
    def delete_action(self, frame):
        print("Supprimer résumé - test")
        frame.destroy()
        #que un test, plus tard appel au manager pour supp de la BDD

    def toggle_eval(self, frame, title, id_summ):
        # si le formulaire d'évaluation existe déjà, on le ferme, sinon on l'ouvre
        if hasattr(frame, "eval_frame"):
            frame.eval_frame.destroy()
            del frame.eval_frame
            return
        # eval_frame utilise grid() comme ses frères info/btn dans frame
        frame.eval_frame = ctk.CTkFrame(frame)
        frame.eval_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
        frame.eval_frame.grid_columnconfigure(0, weight=1)

        # slider note — pack() OK ici car eval_frame est un conteneur indépendant
        note_label = ctk.CTkLabel(frame.eval_frame, text="Note : 3")
        note_label.pack(padx=10, pady=5, anchor="w")

        slider = ctk.CTkSlider(
            frame.eval_frame,
            from_=1, to=5,
            number_of_steps=8, #pour permettre des demi-points (1, 1.5, 2, ..., 5)
            command=lambda val: note_label.configure(text=f"Note : {float(val)}")
        )
        slider.set(3)
        slider.pack(padx=10, pady=5, fill="x")

        # champ commentaire
        comment_entry = ctk.CTkEntry(frame.eval_frame, placeholder_text="Commentaire")
        comment_entry.pack(padx=10, pady=5, fill="x")

        # bouton soumettre — création et .pack() séparés
        btn_submit = ctk.CTkButton(
            frame.eval_frame,
            text="Soumettre",
            command=lambda: self.send_eval(title, int(slider.get()), comment_entry.get(), id_summ)
        )
        btn_submit.pack(padx=10, pady=5, fill="x")

    def send_eval(self, title, note, comment, id_summ):
        self.manager.addReview(note,comment,self.manager.user.idUser,id_summ)
        self.manager.checkSummaries(self.mnemonique)



    def displaySummaries(self):
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
            btn = ctk.CTkButton(frame, text="voir", width=60, command=lambda t=title, f=frame, i=id_summ: self.toggle_eval(f, t, i))
            btn.grid(row=0, column=1, padx=5, pady=8)
            #btn supprimer
            btn = ctk.CTkButton(frame, text="supprimer", width=80, fg_color="red", hover_color="darkred", command=lambda f=frame: self.delete_action(f))
            btn.grid(row=0, column=2, padx=5, pady=8)
            #btn modfication
            btn_edit = ctk.CTkButton(frame, text="modifier", width=80, fg_color="orange", hover_color="darkorange", command=lambda f=frame, t=title, i=id_summ: self.toggle_eval(f, t, i))#pour l'instant, réutilise le même formulaire que pour voir, à différencier plus tard
            btn_edit.grid(row=0, column=3, padx=5, pady=8)
