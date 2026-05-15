import threading

from ClientNetworkManager import ClientNetworkManager
from Gui import Gui


class Client:
    def __init__(self):
        self.manager = ClientNetworkManager()
        # NOTE: je lance la gui sur un thread et je pense qu'on lancera le manager sur un autre
        self.gui = Gui(self.manager)
        threading.Thread(target=self.gui.run(), daemon=True).start()


if __name__ == "__main__":
    client = Client()
