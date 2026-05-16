import customtkinter as ctk
from ClassView import ClassView
from ClientNetworkManager import ClientNetworkManager
from IpView import IpView
from LeaderBoardView import LeaderBoardView
from LoginView import LoginView
from MenuView import MenuView
from ShopView import ShopView


class Gui(ctk.CTk):
    def __init__(self, manager: ClientNetworkManager):
        super().__init__()
        self.manager = manager

        self.title("BDD")
        self.geometry("1000x1000")
        self.middlex = self.winfo_screenwidth() / 2
        self.middley = self.winfo_screenheight() / 2

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
        for F in (IpView, LoginView, MenuView, LeaderBoardView, ShopView, ClassView):
            page_name = F.__name__.replace("View", "").upper()
            frame = F(parent=self.container, controller=self, manager=self.manager)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_view("IP")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", self.on_closing)

        # Gérer la fermeture de la fenêtre
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self, event=None):
        """Action effectuée à la fermeture de la fenêtre."""
        self.manager.close()
        self.destroy()

    def show_view(self, page_name):
        """Affiche une vue spécifique en la mettant au premier plan"""
        frame = self.frames[page_name]
        frame.tkraise()

    def run(self):
        self.mainloop()
