import customtkinter as ctk
from View import View


class ShopView(View):

    def initView(self):
        self.title_label = ctk.CTkLabel(
            self, text="Boutique", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=1, column=0, padx=20, pady=20)

    def back_action(self):
        self.controller.show_view("MENU")

    def displayStore(self, obj: dict):
        for elem in obj:
            nom = elem.get("Nom")
            id = elem.get("ID")
            typeObj = elem.get("TypeObjet")
            price = elem.get("Prix")
            desc = elem.get("Desc")
            print(f"{nom} || {id} || {typeObj} || {price} || {desc}")
            print()
