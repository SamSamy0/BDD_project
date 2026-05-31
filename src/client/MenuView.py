import customtkinter as ctk
from View import View


class MenuView(View):
    def initView(self):
        self.label = ctk.CTkLabel(
            self, text="Menu Principal", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label.pack(padx=20, pady=20)

        self.profil_button = ctk.CTkButton(
            self, text="Profil", command=self.profil_action
        )
        self.profil_button.pack(padx=100, pady=20)

        self.class_button = ctk.CTkButton(
            self, text="List de cours", command=self.class_action
        )
        self.class_button.pack(padx=20, pady=20)

        self.leaderboard_button = ctk.CTkButton(
            self, text="LeaderBoard", command=self.leaderboard_action
        )
        self.leaderboard_button.pack(padx=20, pady=20)

        self.shop_button = ctk.CTkButton(
            self, text="Boutique", command=self.shop_action
        )
        self.shop_button.pack(padx=20, pady=20)

        self.mycourse_button = ctk.CTkButton(
            self, text="Mes cours", command=self.mycourse_action
        )
        self.mycourse_button.pack(padx=20, pady=20)

        self.history_button = ctk.CTkButton(
            self, text="Historique transactions", command=self.history_action)
        self.history_button.pack(padx=20, pady=20)
        
        self.logout_button = ctk.CTkButton(
            self, text="Déconnexion", command=self.logout_action
        )
        self.logout_button.pack(padx=20, pady=20)

    def history_action(self):
        self.manager.getTransactionHistory(self.manager.user.idUser)
        self.controller.show_view("HISTORY")

    def shop_action(self):
        self.manager.getUserObject(self.manager.user.idUser)
        self.manager.checkCatalogue()
        self.controller.show_view("SHOP")


    def leaderboard_action(self):
        self.manager.checkLeaderBoard()

    def logout_action(self):
        self.controller.show_view("LOGIN")

    def class_action(self):
        self.manager.getAllCourse()
        self.controller.show_view("CLASS")

    def profil_action(self):
        self.manager.getProfile(self.manager.user.idUser)
        self.controller.show_view("PROFIL")

    def mycourse_action(self):
        self.manager.getUserCourse(self.manager.user.idUser)
        self.controller.show_view("MYCLASS")
