import datetime
import json
import socket
import threading
from typing import Any

from Profil import Profile

from common.Protocol import Protocol


# Intermédiaire entre client et serveur
class ClientNetworkManager:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiver: Any = None
        self.user = Profile()
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
        buffer = ""
        decoder = json.JSONDecoder()
        while True:
            try:
                reponse = self.sock.recv(65536)
                if not reponse:
                    break
                buffer += reponse.decode("utf-8")
                while buffer:
                    buffer = buffer.strip()
                    if not buffer:
                        break
                    try:
                        data, index = decoder.raw_decode(buffer)
                        self.handle_reponse(data)
                        buffer = buffer[index:]
                    except json.JSONDecodeError:
                        break

            except Exception as e:
                print(f"Erreur : Connexion interrompue : {e}")
                break

    def handle_reponse(self, rep_dict):

        protocol = rep_dict["protocol"]
        data = rep_dict["data"]
        match protocol:
            case Protocol.SIGNIN.value:
                if data is not None:
                    self.user.initData(data)
                    # self.current_user = data.get("ID")
                    self.receiver.isAcceptedLogin(connect=True)
                else:
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

            case Protocol.READ_SUMMARIES.value:
                print(data)
                self.receiver.checkSummaries(data)

            case Protocol.ADD_COURSE.value:
                self.receiver.addCourse(data)

            case Protocol.GET_USER_OBJECT.value:
                self.receiver.showUserObject(data)

            case Protocol.GET_POINT.value:
                self.receiver.updatePointsInShop(data)

            case Protocol.DELETE_USER_COURSE.value:
                self.receiver.deleteUserCourse(data)

            case Protocol.GET_USER_COURSES.value:
                self.receiver.getUserCourse(data)

            case Protocol.ADD_USER_COURSE.value:
                self.receiver.addUserCourse(data)

            case Protocol.ADD_SUMMARY.value:
                self.receiver.addSummary(data)

            case Protocol.ADD_EVAL.value:
                self.receiver.addReview(data)

            case Protocol.DELETE_SUMMARY.value:
                self.receiver.deleteSummary(data)

            case Protocol.GET_RANKING_OBJECT.value:
                self.receiver.getObRanking(data)

            case Protocol.GET_EVALUATIONS.value:
                self.receiver.getEvaluations(data)

            case Protocol.GET_EVAL.value:
                self.receiver.getEval(data)

            case Protocol.ENOUGH_POINTS.value:
                self.receiver.enoughPoints(data)

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
            {
                "Mnemonique": mnemo,
                "Nom": name,
                "Fac": fac,
                "Credits": utc,
                "Annee": year,
            },
        )

    def addUserCourse(self, mnemo: str, iduser: int):
        self.send_request(
            Protocol.ADD_USER_COURSE.value,
            {"Mnemonique": mnemo, "IdUtilisateur": iduser},
        )

    def deleteUserCourse(self, mnemo: str, iduser: int):
        self.send_request(
            Protocol.DELETE_USER_COURSE.value, {"mnemo": mnemo, "idUser": iduser}
        )

    def getUserCourse(self, userId: int):
        self.send_request(Protocol.GET_USER_COURSES.value, {"idUser": userId})

    """Reviews queries"""

    def addReview(self, note: str, comment: str, idAuthor: int, idSumm: int):
        self.send_request(
            Protocol.ADD_EVAL.value,
            {
                "note": note,
                "comment": comment,
                "idAuthor": idAuthor,
                "idSumm": idSumm,
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
                "cost": -cost,
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
        date: str,
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

    def checkSummaries(self, Mnemonique: str):
        self.send_request(Protocol.READ_SUMMARIES.value, {"Mnemonique": Mnemonique})

    def deleteSummary(self, idSumm, idAuthor):
        self.send_request(
            Protocol.DELETE_SUMMARY.value,
            {"ID": int(idSumm), "IdUtilisateur": idAuthor},
        )

    def getSummAverage(self, idSumm: int):
        self.send_request(Protocol.GET_SUMMARY_AVERAGE.value, {"idSumm": idSumm})

    """Users Queries"""

    def actObject(self, idUser: int, idObject: int, state_val: int):
        self.send_request(
            Protocol.CHANGE_STATE_OBJ.value,
            {"State": state_val, "idUser": idUser, "idObject": idObject},
        )

    def getProfile(self, idUser: int):
        self.send_request(Protocol.GET_PROFILE.value, {"idUser": idUser})

    def getUserObject(self, idUser: int):
        self.send_request(Protocol.GET_USER_OBJECT.value, {"idUser": idUser})

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

    def getEvaluations(self, idResume):
        self.send_request(Protocol.GET_EVALUATIONS.value, {"IdResume": idResume})

    def getEval(self, idEval):
        self.send_request(Protocol.GET_EVAL.value, {"ID": idEval})

    def enoughPoints(self,userId, cost):
        self.send_request(Protocol.ENOUGH_POINTS.value,{"ID":userId,"points" : cost})
