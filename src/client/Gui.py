import customtkinter as ctk
from ClassView import ClassView
from ClientNetworkManager import ClientNetworkManager
from LeaderBoardView import LeaderBoardView
from LoginView import LoginView
from MenuView import MenuView
from ShopView import ShopView


class Gui(ctk.CTk):
    def __init__(self, manager: ClientNetworkManager):
        super().__init__()

        self.title("BDD")
        self.geometry("400x500")

        # Configuration du thème
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Conteneur pour les différentes vues
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Initialisation des vues
        for F in (LoginView, MenuView, LeaderBoardView, ShopView, ClassView):
            page_name = F.__name__.replace("View", "").upper()
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_view("LOGIN")

    def show_view(self, page_name):
        """Affiche une vue spécifique en la mettant au premier plan"""
        frame = self.frames[page_name]
        frame.tkraise()

    def run(self):
        self.mainloop()
