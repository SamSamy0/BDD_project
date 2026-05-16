from View import View
import customtkinter as ctk



class ClassView(View):

    def initView(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Cours", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)
        
        #liste des cours
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Liste des cours")
        self.scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        #données de test fictives
        cours_fictifs = [
            ("INFO-H303", "Base de données"),
            ("INFO-H301", "Algorithmes et structures de données"),
            ("MATH-H201", "Analyse"),
            ("INFO-H304", "Systèmes d'exploitation"),
        ]
        for mnemonique, nom in cours_fictifs:
            btn = ctk.CTkButton(
                self.scroll_frame,
                text=f"{mnemonique} - {nom}",
                command=lambda m=mnemonique: self.select_course(m)#m=mnemonique capture la valeur
            )
            btn.pack(padx=10, pady=5, fill="x")
        #btn ajouter cours
        self.add_button = ctk.CTkButton(self, text="Ajouter un cours", command=self.add_course_action)
        self.add_button.grid(row=2, column=0, padx=20, pady=10)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=3, column=0, padx=20, pady=20)

    def select_course(self, mnemonique):
        self.controller.current_cours = mnemonique
        self.controller.show_view("SUMMARY")
    
    def add_course_action(self):
        #Ajouter plus tard
        print("Ajouter un cours -test")
        
    def back_action(self):
        self.controller.show_view("MENU")

