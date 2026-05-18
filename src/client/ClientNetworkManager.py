import datetime
import json
import socket
import threading
from typing import Any

from common.Protocol import Protocol


# Intermédiaire entre client et serveur
class ClientNetworkManager:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiver: Any = None
        self.currentUser: Any = None
        self.objBought = []

    def connect(self, ip="127.0.0.1", port=8080):
        self.ip = ip
        self.port = port
        print("CONNEXION AU SERVER EN COURS...")
        try:
            self.sock.connect((self.ip, self.port))
            print("Connexion établie")
            threading.Thread(target=self.receive_message, daemon=True).start()
        except ConnectionRefusedError:
            print("Erreur : Connexion au server échoué")

    def close(self, sig=None, frame=None):
        """Ferme proprement le socket du client."""
        print("\nDéconnexion du serveur...")
        try:
            self.sock.close()
            print("Déconnexion réussie !")
        except Exception as e:
            print(f"Erreur lors de la déconnexion : {e}")

    """Functions to Receive messages from ServerNetworkManager"""

    def receive_message(self):
        while True:
            try:
                reponse = self.sock.recv(65536)
                if not reponse:
                    break
                data = json.loads(reponse.decode("utf-8"))
                self.handle_reponse(data)
            except Exception as e:
                print(f"Erreur : Connexion interrompue : {e}")
                break

    def handle_reponse(self, rep_dict):
        print("handler")
        protocol = rep_dict["protocol"]
        data = rep_dict["data"]
        # print("dict = ", rep_dict)
        # print(data)
        print("pass")
        match protocol:
            case Protocol.SIGNIN.value:
                if data is not None:
                    self.current_user = data.get("ID")
                    self.receiver.isAcceptedLogin(connect=True)
                else:
                    self.current_user = None
                    self.receiver.isAcceptedLogin(connect=False)

            case Protocol.SIGNUP.value:
                self.receiver.isAcceptedLogin(
                    connect=True if data is not None else False
                )
            case Protocol.GET_ALL_COURSES.value:
                self.receiver.setAllCourse(data)

            case Protocol.GET_PROFILE.value:
                self.receiver.showProfile(data)

            # Shop
            case Protocol.GET_STORE.value:
                self.receiver.displayStore(data)

            case Protocol.GET_LEADERBOARD.value:
                self.receiver.checkLeaderboard(data)

            # Stats
            case Protocol.GET_COURSES_MOST_RESUMES.value:
                self.receiver.mostSummCours(data)

            case Protocol.GET_RES_IN_AT_LEAST_THREE_COURSES.value:
                self.receiver.SumInAtLeastThree(data)

            case Protocol.BUY.value:
                self.receiver.isBought(data)

            # case Protocol.

    """Functions to send messages to ServerNetworkManager"""

    def send_request(self, protocol, data=None):
        if data is None:
            data = {}

        request = json.dumps({"protocol": protocol, "data": data})
        try:
            self.sock.send(request.encode("utf-8"))
        except Exception as e:
            print(f"Erreur : le message {protocol} n'a pas pu etre envoyé : {e}")

    """User connexion queries"""

    def signin(self, username, email):
        self.send_request(Protocol.SIGNIN.value, {"username": username, "email": email})

    def signup(self, username, email):
        date = datetime.date.today()
        self.send_request(
            Protocol.SIGNUP.value, {"username": username, "email": email, "date": date}
        )

    """Courses queries"""

    def getAllCourse(self):
        self.send_request(Protocol.GET_ALL_COURSES.value)

    def addCourse(self, mnemo: str, name: str, fac: str, utc: int, year: int):
        self.send_request(
            Protocol.ADD_COURSE.value,
            {"mnemo": mnemo, "name": name, "fact": fac, utc: "utc", "year": year},
        )

    def deleteCourse(self, mnemo: str):
        self.send_request(Protocol.DELETE_COURSE, {"mnemo": mnemo})

    def getUserCourse(self, userId: int, mnemo: int):
        self.send_request(
            Protocol.GET_USER_COURSES.value, {"userId": userId, "mnemo": mnemo}
        )

    """Reviews queries"""

    def addReview(self, note: str, comment: str, idAuthor: int, idSummary: int):
        self.send_request(
            Protocol.ADD_EVAL.value,
            {
                "note": note,
                "comment": comment,
                "idAuthor": idAuthor,
                "idSummary": idSummary,
            },
        )

    """Shop Queries"""

    def buyObject(self, idUser: int, objId: int, cost: int):
        jour = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.send_request(
            Protocol.BUY.value,
            {
                "idUser": idUser,
                "objId": objId,
                "cost": cost,
                "typ": "dépense",
                "jour": jour,
            },
        )

    def getPoints(self, idUser: int):
        self.send_request(Protocol.GET_POINT.value, {"idUser": idUser})

    def getTransactionHistory(self, idUser: int):
        self.send_request(Protocol.CHECK_TRANSACTION_HISTORY.value, {"idUser": idUser})

    def getObjetInfo(self, idObjet: int):
        self.send_request(Protocol.CHECK_ITEM.value, {"idObjet": idObjet})

    def checkCatalogue(self):
        self.send_request(Protocol.GET_STORE.value)

    """Summaries Queries"""

    def addSummary(
        self,
        title: str,
        desc: str,
        date: int,
        version: int,
        visible: bool,
        mnemo: str,
        idAuthor: int,
    ):
        self.send_request(
            Protocol.ADD_SUMMARY.value,
            {
                "title": title,
                "desc": desc,
                "date": date,
                "version": version,
                "visible": visible,
                "mnemo": mnemo,
                "idAuthor": idAuthor,
            },
        )

    def checkSummary(self, idSumm: int):
        self.send_request(Protocol.READ_SUMMARY.value, {"idSumm": idSumm})

    def deleteSummary(self, idSumm: int):
        self.send_request(Protocol.DELETE_SUMMARY.value, {"idSumm": idSumm})

    def getSummAverage(self, idSumm: int):
        self.send_request(Protocol.GET_SUMMARY_AVERAGE.value, {"idSumm": idSumm})

    """Users Queries"""

    def actObject(self, idUser: int, idObject: int):
        self.send_request(
            Protocol.CHANGE_STATE_OBJ.value,
            {"State": 1, "idUser": idUser, "idObject": idObject},
        )

    def getProfile(self, idUser: int):
        self.send_request(Protocol.GET_PROFILE.value, {"idUser": idUser})

    """Statistic Queries"""

    def checkLeaderBoard(self):
        self.send_request(Protocol.GET_LEADERBOARD.value)

    def getObRanking(self):
        self.send_request(Protocol.GET_RANKING_OBJECT.value)

    def getSpenderRanking(self):
        self.send_request(Protocol.GET_RANKING_SPENDER.value)

    def getMostSummCours(self):
        self.send_request(Protocol.GET_COURSES_MOST_RESUMES.value)

    def getSummInAtLeastThreeCourse(self):
        self.send_request(Protocol.GET_RES_IN_AT_LEAST_THREE_COURSES.value)

    def getBestTenUsers(self):
        self.send_request(Protocol.GET_BEST_TEN_USERS.value)
