import threading

from ClientNetworkManager import ClientNetworkManager
from Gui import Gui
import signal


class Client:
    def __init__(self):
        # NOTE: je lance la gui sur un thread et je pense qu'on lancera le manager sur un autre

        self.manager = ClientNetworkManager()
        self.gui = Gui(self.manager)




        self.gui.run()




if __name__ == "__main__":
    client = Client()
    signal.signal(signal.SIGINT, client.manager.close)


