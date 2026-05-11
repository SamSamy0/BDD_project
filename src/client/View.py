from enum import Enum
from abc import ABC, abstractmethod


class TypeView(Enum):
    LOGIN = 0
    APP = 1


class View(ABC):

    def __init__(self,window):
        self.window = window

    @abstractmethod
    def initView(self):
        pass
        

