from enum import Enum
from ABC import ABC, abstractmethod


class TypeView(Enum):
    LOGIN = 0
    APP = 1


class View:

    def __init__(self,window):
        self.window = window

    @abstractmethod
    def initButton():
        pass
        

