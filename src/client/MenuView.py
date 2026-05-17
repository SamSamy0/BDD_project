import customtkinter as ctk
from View import View


class MenuView(View):
    def initView(self):
        self.label = ctk.CTkLabel(
            self, text="Menu Principal", font=ctk.CTkFont(size=16)
        )
        self.label.pack(padx=20, pady=20)

        self.class_button = ctk.CTkButton(self, text="Cours", command=self.class_action)
        self.class_button.pack(padx=20, pady=20)

        self.leaderboard_button = ctk.CTkButton(
            self, text="LeaderBoard", command=self.leaderboard_action
        )
        self.leaderboard_button.pack(padx=20, pady=20)

        self.shop_button = ctk.CTkButton(
            self, text="Boutique", command=self.shop_action
        )
        self.shop_button.pack(padx=20, pady=20)

        self.logout_button = ctk.CTkButton(
            self, text="Déconnexion", command=self.logout_action
        )
        self.logout_button.pack(padx=20, pady=20)

    def shop_action(self):
        if self.manager.checkCatalogue():
            self.controller.show_view("SHOP")

    def leaderboard_action(self):
        if self.manager.getSummInAtLeastThreeCourse():
            self.controller.show_view("LEADERBOARD")

    def logout_action(self):
        self.controller.show_view("LOGIN")

    def class_action(self):
        if self.manager.getAllCourse():
            self.controller.show_view("CLASS")
