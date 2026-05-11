import customtkinter as ctk
from View import View

class AppView(View):
    def initView(self):
        self.label = ctk.CTkLabel(self, text="Bienvenue dans l'application principale !", font=ctk.CTkFont(size=16))
        self.label.pack(padx=20, pady=20)
        
        self.logout_button = ctk.CTkButton(self, text="Déconnexion", command=lambda: self.controller.show_view("LOGIN"))
        self.logout_button.pack(padx=20, pady=10)
