import threading
from Gui import Gui
from ClientNetworkManager import ClientNetworkManager

class Client:
    def __init__(self):
        # self.manager = ClientNetworkManager()
        #NOTE: je lance la gui sur un thread et je pense qu'on lancera le manager sur un autre
        threading.Thread(target=self.gui.run(),daemon=True).start()
        self.gui = Gui(self.manager)





if __name__ == "__main__":
    client = Client()
