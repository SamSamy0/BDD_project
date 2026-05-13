import customtkinter as ctk
from View import View

class LoginView(View):
    def initView(self):
        self.grid_columnconfigure(0, weight=1)
        
        self.title_label = ctk.CTkLabel(self, text="Authentification", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.mail_label = ctk.CTkLabel(self, text="Mail")
        self.mail_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")

        self.mail_entry = ctk.CTkEntry(self)
        self.mail_entry.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")

        self.userName_label = ctk.CTkLabel(self, text="UserName")
        self.userName_label.grid(row=3, column=0, padx=20, pady=(10, 0), sticky="w")

        self.userName_entry = ctk.CTkEntry(self, show="*")
        self.userName_entry.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="ew")

        self.login_button = ctk.CTkButton(self, text="Log in", command=self.login_action)
        self.login_button.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        self.register_button = ctk.CTkButton(self, text="Register", command=self.register_action)
        self.register_button.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

    def login_action(self):
        print(f"Tentative de connexion : {self.id_entry.get()}")
        self.controller.show_view("MENU")


    def register_action(self):
        print("Bouton Register cliqué")
        self.controller.show_view("MENU")
