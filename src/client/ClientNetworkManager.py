import socket

# from common import protocol


# Intermédiaire entre client et serveur
class ClientNetworkManager:
    def __init__(self, ip="127.0.0.1", port=8080):
        self.ip = ip
        self.port = port
        pass

    # TODO: Chercher dans la database
    @staticmethod
    def signin(self, username, email):
        print("OK")

    # TODO: Générer un id unique + rajouter dans la database + date_inscription
    def signup(self, username, email):
        pass

    # TODO: Ferme le socket du client
    def disconnection(self, id):
        pass
