from View import View
import customtkinter as ctk

class ShopView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)#deux colonnes de taille identique
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Boutique", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)
        #gauche: catalogue
        self.catalog_frame = ctk.CTkScrollableFrame(self, label_text="Catalogue")
        self.catalog_frame.grid(row=1, column=0, padx=(20,10), pady=10, sticky="nsew")
        self.catalog_frame.grid_columnconfigure((0,1,2), weight=1)

        ctk.CTkLabel(self.catalog_frame, text="Objet", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(self.catalog_frame, text="Prix", font=ctk.CTkFont(weight="bold")).grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkLabel(self.catalog_frame, text="", ).grid(row=0, column=2, padx=10, pady=5)
        #données fictives du catalogue
        catalog_fictif = [
        ("Badge Or", 500),
        ("Titre Maître", 300),
        ("Badge Argent", 200),
        ("Titre Expert", 150),
        ("Badge Bronze", 100),
        ]

        for i, (nom, prix) in enumerate(catalog_fictif, start=1):
            ctk.CTkLabel(self.catalog_frame, text=nom).grid(row=i, column=0, padx=10, pady=5)
            ctk.CTkLabel(self.catalog_frame, text=f"{prix} pts").grid(row=i, column=1, padx=10, pady=5)
            ctk.CTkButton(
                self.catalog_frame,
                text="Acheter",
                width=80,
                command=lambda n=nom, p=prix: self.buy_action(n, p)
            ).grid(row=i, column=2, padx=10, pady=5)

        # --- Colonne droite : Mes objets ---
        self.inventory_frame = ctk.CTkScrollableFrame(self, label_text="Mes objets")
        self.inventory_frame.grid(row=1, column=1, padx=(10, 20), pady=10, sticky="nsew")
        self.inventory_frame.grid_columnconfigure((0, 1), weight=1)

        # En-têtes inventaire
        ctk.CTkLabel(self.inventory_frame, text="Objet", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(self.inventory_frame, text="", ).grid(row=0, column=1, padx=10, pady=5)
        #données fictives de l'inventaire
        inventory_fictif = [
        "Badge Argent",
        "Titre Expert",
        ]
        self.actif_states = {}#garde l'état de chaque objet

        for i, nom in enumerate(inventory_fictif, start=1):
            ctk.CTkLabel(self.inventory_frame, text=nom).grid(row=i, column=0, padx=10, pady=5)
            self.actif_states[nom] = False#inactif par défaut

            btn = ctk.CTkButton(
                self.inventory_frame,
                text="Activer",
                width=80,
                fg_color="green",
                hover_color="darkgreen",
                command=lambda n=nom: self.toggle_activate(n)
            )
            btn.grid(row=i, column=1, padx=10, pady=5)
            self.actif_states[nom] = {"actif": False, "btn": btn}#stocke le bouton pour pouvoir le mettre à jour


        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=2, column=0, columnspan = 2 ,padx=20, pady=20)


    def back_action(self):
        self.controller.show_view("MENU")
    
    def buy_action(self, nom, prix):
        #Acheter l'objet (à implémenter plus tard)
        print(f"Acheter {nom} pour {prix} points - test")
    
    def toggle_activate(self, nom):
        #Activer l'objet (à implémenter plus tard)
        state = self.actif_states[nom]
        if state["actif"]:
            state["actif"] = False
            state["btn"].configure(text="Activer", fg_color="green", hover_color="darkgreen")
            print(f"{nom} désactivé")
        else:
            state["actif"] = True
            state["btn"].configure(text="Désactiver", fg_color="gray", hover_color="darkgray")
            print(f"{nom} activé")


