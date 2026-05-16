from DatabaseManager import DatabaseManager
from common.Protocol import Protocol







class ServerNetworkManager:

    def __init__(self):
        self.db = DatabaseManager()
        





    def handle_request(self,dict_request):
        protocol = dict_request.get("protocol")
        data = dict_request.get("data")

        match protocol:
            case Protocol.SIGNIN.value:
                pass
            case Protocol.SIGNUP.value:
                pass
            


