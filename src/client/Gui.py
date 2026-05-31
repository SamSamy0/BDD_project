import customtkinter as ctk
from ClassView import ClassView
from ClientNetworkManager import ClientNetworkManager
from EvalView import EvalView
from HistoryView import HistoryView
from IpView import IpView
from LeaderBoardView import LeaderBoardView
from LoginView import LoginView
from MenuView import MenuView
from MyClassView import MyClassView
from ProfilView import ProfilView
from ShopView import ShopView
from SummaryView import SummaryView


class Gui(ctk.CTk):
    def __init__(self, manager: ClientNetworkManager):
        super().__init__()
        self.manager = manager

        self.title("Project Base de Données INFOH303")
        self.geometry("1000x1000")
        self.middlex = self.winfo_screenwidth() / 2
        self.middley = self.winfo_screenheight() / 2

        # Theme Configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Different View container
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Init of the Views
        for F in (
            IpView,
            LoginView,
            MenuView,
            LeaderBoardView,
            ShopView,
            ClassView,
            ProfilView,
            SummaryView,
            MyClassView,
            EvalView,
            HistoryView,
        ):
            page_name = F.__name__.replace("View", "").upper()
            frame = F(parent=self.container, controller=self, manager=self.manager)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_view("IP")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", self.on_closing)

        # Closing Window
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self, event=None):
        """Closing actions"""
        self.manager.close()
        self.destroy()

    def show_view(self, page_name):
        """Display the view 'page_name'"""
        frame = self.frames[page_name]
        frame.tkraise()

    def run(self):
        self.mainloop()
