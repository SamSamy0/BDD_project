import socket
import json
import threading
import datetime

from common.Protocol import Protocol


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
            threading.Thread(target=self.receive_message,daemon=True).start()
        except ConnectionRefusedError:
            print("Erreur : Connexion au server échoué")




    def receive_message(self):
        while True:
            try:
                reponse = self.sock.recv(1024)
                if not reponse:
                    break
                print(reponse)
                #data = json.loads(reponse.decode('utf-8'))
                #self.handle_reponse(data)
            except Exception as e:
                print(f"Erreur : Connexion interrompue : {e}")
                break



    def handle_reponse(self,rep_dict):
        print("handler")
        protocol = rep_dict["protocol"]
        data = rep_dict["data"]
        print(data)
        print("pass")

        match protocol:
            case Protocol.SIGNIN.value:
                pass




    def send_request(self,protocol,data = None):
        if data is None:
            data = {}

        request = json.dumps({"protocol" : protocol, "data" : data})
        try:
            self.sock.send(request.encode('utf-8'))
        except Exception as e:
            print(f"Erreur : le message {protocol} n'a pas pu etre envoyé : {e}")


    def signin(self,username,email):
        self.send_request(Protocol.SIGNIN.value,{"username" : username,"email" : email})



    def signup(self,username,email):
        date = datetime.date.today()
        self.send_request(Protocol.SIGNUP.value,{"username":username,"email":email,"date":date})









    def close(self, sig=None, frame=None):
        """Ferme proprement le socket du client."""
        print("\nDéconnexion du serveur...")
        try:
            self.sock.close()
            print("Déconnexion réussie !")
        except Exception as e:
            print(f"Erreur lors de la déconnexion : {e}")

