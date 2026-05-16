import socket

# from common import protocol


# Intermédiaire entre client et serveur
class ClientNetworkManager:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self,ip="127.0.0.1", port=8080):
        self.ip = ip
        self.port = port
        print("CONNEXION AU SERVER EN COURS...")
        try:
            self.sock.connect((self.ip,self.port))
            print("Connexion établie")
        except ConnectionRefusedError:
            print("Erreur : Connexion au server échoué")


    def close(self):
        print("Deconnexion au server...")
        try:
            self.sock.close()
            print("Déconnexion Reussi !")
        except Exception:
            print("Erreur : Deconnexion échoué")


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
