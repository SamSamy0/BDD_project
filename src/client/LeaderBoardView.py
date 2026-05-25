import customtkinter as ctk
from View import View


class LeaderBoardView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="LeaderBoard", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Classement")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
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
        self.back_button.grid(row=2, column=0, padx=20, pady=20)

    def back_action(self):
        self.controller.show_view("MENU")

    def displayTop10(self, top: dict):
        count = 1
        for elem in top:
            name = elem.get("Nom")
            print(f"{count}==={name}")
            count += 1

    def displayMostSumCours(self, best: dict):
        for elem in best:
            mnemo = elem.get("Mnemonique")
            num = elem.get("Number")
            print(f"{mnemo} || {num}")

    def SumInMoreThanThree(self, data: dict):
        for elem in data:
            name = elem.get("Nom")
            print(f"==={name}===")

    def displayLeaderboard(self):
        for widget in self.scroll_frame.winfo_children():
                widget.destroy()

        ctk.CTkLabel(self.scroll_frame, text="Rang", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(self.scroll_frame, text="Utilisateur", font=ctk.CTkFont(weight="bold")).grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkLabel(self.scroll_frame, text="Points", font=ctk.CTkFont(weight="bold")).grid(row=0, column=2, padx=10, pady=5)
        for i, entry in enumerate(self.leaderboard, start=1):
            rang = entry.get("Rang")
            nom = entry.get("Nom")
            points = entry.get("Points")
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