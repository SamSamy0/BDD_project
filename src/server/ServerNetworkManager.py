from DatabaseManager import DatabaseManager

from common.Protocol import Protocol


class ServerNetworkManager:

    def __init__(self,cursor):
        self.db = DatabaseManager(cursor)






    def handle_request(self,dict_request):
        protocol = dict_request.get("protocol")
        data = dict_request.get("data")
        print(f"[{protocol}] avec : {data}")

        match protocol:
            case Protocol.SIGNIN.value:
                result = self.signin(data)
                return {"protocol": protocol, "data": result}
            case Protocol.SIGNUP.value:
                return self.signup(data)

            case Protocol.GET_ALL_COURSES.value:
                result = self.getAllCourses(data)
                return {"protocol": protocol, "data": result}
            case Protocol.GET_BEST_TEN_USERS.value:
                result = self.getBestTenUsers(data)


    

    def signin(self,data):
        return self.db.signin(data)

    def signup(self,data):
        return self.db.signup(data)

    def getAllCourses(self, data):
        return self.db.getAllCourses(data)
    
    def getBestTenUsers(self,data):
        return self.db.getBestTenUsers(data)

    
