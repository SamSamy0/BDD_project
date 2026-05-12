from View import View
import customtkinter as ctk

class ShopView(View):

    def initView(self):
        self.title_label = ctk.CTkLabel(self, text="Boutique", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

