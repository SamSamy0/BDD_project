from DatabaseManager import DatabaseManager
from common.Protocol import Protocol







class ServerNetworkManager:

    def __init__(self,cursor):
        self.db = DatabaseManager(cursor)
        





    def handle_request(self,dict_request):
        protocol = dict_request.get("protocol")
        data = dict_request.get("data")

        match protocol:
            case Protocol.SIGNIN.value:
                return self.signin(data)
            case Protocol.SIGNUP.value:
                return self.signup(data)
            


    def signin(self,data):
        username = data.get("username")
        email = data.get("email")


    def signup(self,data):
        username = data.get("username")
        email = data.get("email")
