from enum import Enum
from abc import ABC, abstractmethod
import customtkinter as ctk
from ClientNetworkManager import ClientNetworkManager

class TypeView(Enum):
    LOGIN = 0
    APP = 1

class View(ctk.CTkFrame, ABC):
    def __init__(self, parent, controller, manager: ClientNetworkManager ):
        super().__init__(parent)
        self.controller = controller
        self.manager = manager
        self.initView()

    @abstractmethod
    def initView(self):
        pass
