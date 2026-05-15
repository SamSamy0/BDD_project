from View import View
import customtkinter as ctk


class IpView(View):


    def initView(self):
        self.title_label = ctk.CTkLabel(self, text="Connexion au server", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.ip_label = ctk.CTkLabel(self, text="Adresse IP")
        self.ip_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")

        self.ip_entry = ctk.CTkEntry(self,placeholder_text="127.0.0.1")
        self.ip_entry.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")


        self.connect_button = ctk.CTkButton(self, text="Se connecter", command=self.connectAction)
        self.connect_button.grid(row=5, column=0, padx=20, pady=10, sticky="ew")




    def connectAction(self): 
        #NOTE: IL Y A AUCUNE VERIFICATION SUR L'ENTREE DE L'IP NSM C'EST PAS LE BUT DU COURS
        self.manager.connect(self.ip_entry.get())
