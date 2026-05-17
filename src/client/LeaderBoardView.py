import customtkinter as ctk
from View import View


class LeaderBoardView(View):

    def initView(self):
        self.title_label = ctk.CTkLabel(
            self, text="LeaderBoard", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=1, column=0, padx=20, pady=20)

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
            num = elem.get("COUNT(r.Mnemonique)")
            print(f"{mnemo} || {num}")

    def SumInMoreThanThree(self, data: dict):
        for elem in data:
            name = elem.get("Nom")
            print(f"==={name}===")
