import signal
import threading

from ClientNetworkManager import ClientNetworkManager
from Gui import Gui
from ReceiverInWindow import ReceiverInWindow as rw


class Client:
    def __init__(self):
        # NOTE: je lance la gui sur un thread et je pense qu'on lancera le manager sur un autre

        self.manager = ClientNetworkManager()
        self.gui = Gui(self.manager)
        self.receiver = rw(self.gui)
        self.manager.receiver = self.receiver
        self.gui.default_receiver = self.receiver

        self.gui.run()


if __name__ == "__main__":
    client = Client()
    signal.signal(signal.SIGINT, client.manager.close)
