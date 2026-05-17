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
                result = self.db.signin(data)
                return {"protocol": protocol, "data": result}
            case Protocol.SIGNUP.value:
                return self.db.signup(data)

            case Protocol.GET_ALL_COURSES.value:
                result = self.db.getAllCourses(data)
                return {"protocol": protocol, "data": result}
            
            case Protocol.GET_LEADERBOARD.value:
                result = self.db.checkLeaderBoard(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_RANKING_OBJECT.value:
                result = self.db.getObRanking(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_RANKING_SPENDER.value:
                result = self.db.getSpenderRanking(data)
                return {"protocol" : protocol, "data" : result}

            case Protocol.GET_COURSES_MOST_RESUMES.value:
                result = self.db.getMostSummCours(data)
                return {"protocol" : protocol, "data" : result}

            case Protocol.GET_RES_IN_AT_LEAST_THREE_COURSES.value:
                result = self.db.getSummInAtLeastThreeCourse(data)
                return {"protocol" : protocol, "data": result}

            case Protocol.GET_BEST_TEN_USERS.value:
                result = self.db.getBestTenUsers(data)
                return {"protocol" : protocol, "data": result}




    

