import customtkinter as ctk
from View import View


class LeaderBoardView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="LeaderBoard", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        #frame horizontale pour les boutons de stats
        self.stats_boutons_frame = ctk.CTkFrame(self)
        self.stats_boutons_frame.grid(row=1, column=0, padx=20, pady=(0,10))

        #btn du classement de base
        self.btn_leaderboard = ctk.CTkButton(self.stats_boutons_frame,
                                             text="Classement",
                                             command=self.displayLeaderboard)
        self.btn_leaderboard.pack(side="left", padx=5, pady=5)

        #cours ayant le plus de résumés
        self.btn_most_sum = ctk.CTkButton(self.stats_boutons_frame, 
                                          text="Cours avec le plus de résumés", 
                                          command=self.action_most_summariezed_courses)
        self.btn_most_sum.pack(side="left", padx=5, pady=5)

        #utilisateurs ayant plus de 3 résumés
        self.btn_at_least_3_sum = ctk.CTkButton(self.stats_boutons_frame,
                                                text="Utilisateurs avec au moins 3 résumés",
                                                command=self.action_at_least_three)
        self.btn_at_least_3_sum.pack(side="left", padx=5, pady=5)

        #top 10
        self.btn_top_ten = ctk.CTkButton(self.stats_boutons_frame,
                                            text="Top 10 (points)",
                                            command=self.action_topten)
        self.btn_top_ten.pack(side="left", padx=5, pady=5)


        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Classement")
        self.scroll_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.scroll_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # En-têtes
        ctk.CTkLabel(
            self.scroll_frame, text="Rang", font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(
            self.scroll_frame, text="Utilisateur", font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkLabel(
            self.scroll_frame, text="Points", font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=2, padx=10, pady=5)

        # leaderboard vide
        self.leaderboard = []


        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=3, column=0, padx=20, pady=20)

    def back_action(self):
        self.manager.receiver = self.controller.default_receiver
        self.controller.show_view("MENU")

    def displayTop10(self):
        for widget in self.scroll_frame.winfo_children():
                widget.destroy()
        
        ctk.CTkLabel(self.scroll_frame, text="Utilisateur   -   Points", font=ctk.CTkFont(weight="bold")).pack(pady=(10,5))
        
        for i, elem in enumerate(self.top_ten, start=1):
            name = elem.get("Nom", "?")
            points = elem.get("Points", 0)
            ctk.CTkLabel(self.scroll_frame, text=f"{i}. {name} - {points} pts").pack(pady=3)

    def displayMostSumCours(self):
        #vide le scroll_frame
        for widget in self.scroll_frame.winfo_children():
                widget.destroy()
        #Entêtes
        self.scroll_frame.grid_columnconfigure((0, 1), weight=1)
        ctk.CTkLabel(self.scroll_frame, text="Cours", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(self.scroll_frame, text="Nombre de résumés", font=ctk.CTkFont(weight="bold")).grid(row=0, column=1, padx=10, pady=5)

        for i, elem in enumerate(self.most_um_data, start=1):
            name = elem.get("Mnemonique", "?")
            nb_summ = elem.get("Number")
            ctk.CTkLabel(self.scroll_frame, text=name).grid(row=i, column=0, padx=10, pady=5)
            ctk.CTkLabel(self.scroll_frame, text=str(nb_summ)).grid(row=i, column=1, padx=10, pady=5)

    def SumInMoreThanThree(self):
        for widget in self.scroll_frame.winfo_children():
                widget.destroy()
        ctk.CTkLabel(self.scroll_frame, text="Utilisateur", font=ctk.CTkFont(weight="bold")).pack(pady=(10,5))
        for elem in self.sum_in_at_least_three:
            name = elem.get("Nom", "?")
            ctk.CTkLabel(self.scroll_frame, text=name).pack(pady=3)

    def displayLeaderboard(self):
        for widget in self.scroll_frame.winfo_children():
                widget.destroy()

        ctk.CTkLabel(self.scroll_frame, text="Rang", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(self.scroll_frame, text="Utilisateur", font=ctk.CTkFont(weight="bold")).grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkLabel(self.scroll_frame, text="Points", font=ctk.CTkFont(weight="bold")).grid(row=0, column=2, padx=10, pady=5)
        for i, entry in enumerate(self.leaderboard, start=1):
            rang = entry[0]
            nom = entry[1]
            points = entry[2]
            ctk.CTkLabel(self.scroll_frame, text=str(rang)).grid(
                row=i, column=0, padx=10, pady=5
            )
            ctk.CTkLabel(self.scroll_frame, text=nom).grid(
                row=i, column=1, padx=10, pady=5
            )
            ctk.CTkLabel(self.scroll_frame, text=str(points)).grid(
                row=i, column=2, padx=10, pady=5
            )
    def checkLeaderboard(self, data):
        self.leaderboard = data if data else []
        self.after(0, self.displayLeaderboard)
    
    def action_most_summariezed_courses(self):
        self.manager.receiver = self #réponse reviendra sur cette vue
        self.manager.getMostSummCours()#envoie la requete au serveur
        #on pointe le receiver vers soi-même avant  d'envoyer la requete pour que la réponse revienne sur cette vue et pas une autre
    
    def mostSummCours(self, data):
        #appelé par le handle_reponse quand la réponse du serveur arrive.
        self.most_um_data = data if data else []
        self.after(0, self.displayMostSumCours)
    
    def action_at_least_three(self):
        self.manager.receiver = self
        self.manager.getSummInAtLeastThreeCourse()
    
    def SumInAtLeastThree(self, data):
        self.sum_in_at_least_three = data if data else []
        self.after(0, self.SumInMoreThanThree)
    
    def action_topten(self):
        self.manager.receiver = self
        self.manager.getBestTenUsers()
    
    def bestTenUsers(self, data):
        self.top_ten = data if data else []
        self.after(0, self.displayTop10)

