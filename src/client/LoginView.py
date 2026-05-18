import customtkinter as ctk
from View import View


class LoginView(View):
    def initView(self):
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="Authentification", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.mail_label = ctk.CTkLabel(self, text="Adresse mail")
        self.mail_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")

        self.mail_entry = ctk.CTkEntry(self, placeholder_text="emma.bernard@univ.be")
        self.mail_entry.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")

        self.userName_label = ctk.CTkLabel(self, text="Nom")
        self.userName_label.grid(row=3, column=0, padx=20, pady=(10, 0), sticky="w")

        self.userName_entry = ctk.CTkEntry(
            self, show="*", placeholder_text="emma_bernard"
        )
        self.userName_entry.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="ew")

        self.signIn_button = ctk.CTkButton(
            self, text="Sign In", command=self.login_action
        )
        self.signIn_button.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        self.signUp_button = ctk.CTkButton(
            self, text="Sign Up", command=self.register_action
        )
        self.signUp_button.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

    def login_action(self):
        if self.manager.signin("emma_bernard", "emma.bernard@univ.be"):
            # if self.manager.signin(self.userName_entry.get(),self.mail_entry.get()):
            self.controller.show_view("MENU")

    def register_action(self):
        if self.manager.signup(self.userName_entry.get(), self.mail_entry.get()):
            self.controller.show_view("MENU")
