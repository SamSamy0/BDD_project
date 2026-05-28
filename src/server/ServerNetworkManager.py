from DatabaseManager import DatabaseManager

from common.Protocol import Protocol


class ServerNetworkManager:

    def __init__(self, cursor):
        self.db = DatabaseManager(cursor)

    def handle_request(self, dict_request):
        protocol = dict_request.get("protocol")
        data = dict_request.get("data")
        print(f"[{protocol}] avec : {data}")

        match protocol:
            case Protocol.SIGNIN.value:
                result = self.db.signin(data)
                return {"protocol": protocol, "data": result}

            case Protocol.SIGNUP.value:
                return self.db.signup(data)

            # Courses
            case Protocol.GET_ALL_COURSES.value:
                result = self.db.getAllCourses(data)
                return {"protocol": protocol, "data": result}
            case Protocol.ADD_COURSE.value:
                result = self.db.addCourse(data)
                return {"protocol": protocol, "data": result}

            case Protocol.DELETE_USER_COURSE.value:
                result = self.db.deleteUserCourse(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_USER_COURSES.value:
                result = self.db.getUserCourse(data)
                return {"protocol": protocol, "data": result}

            # REVIEW
            case Protocol.ADD_EVAL.value:
                result = self.db.addReview(data)
                return {"protocol": protocol, "data": result}

            # SHOP
            case Protocol.BUY.value:
                result = self.db.buyObject(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_POINT.value:
                result = self.db.getPoints(data)
                return {"protocol": protocol, "data": result}

            case Protocol.CHECK_TRANSACTION_HISTORY.value:
                result = self.db.getTransactionHistory(data)
                return {"protocol": protocol, "data": result}

            case Protocol.CHECK_ITEM.value:
                result = self.db.getObjectInfo(data)
                return {"protocol": protocol, "data": result}

            # SUMMARIES
            case Protocol.GET_STORE.value:
                result = self.db.getStore(data)
                return {"protocol": protocol, "data": result}
            case Protocol.ADD_SUMMARY.value:
                result = self.db.addSummary(data)
                return {"protocol": protocol, "data": result}

            case Protocol.READ_SUMMARY.value:
                result = self.db.checkSummary(data)
                return {"protocol": protocol, "data": result}

            case Protocol.READ_SUMMARIES.value:
                result = self.db.checkSummaries(data)
                return {"protocol": protocol, "data": result}

            case Protocol.DELETE_SUMMARY.value:
                result = self.db.deleteSummary(data)
                return {"protocol": protocol, "data": result}
            case Protocol.EDIT_SUMMARY.value:
                result = self.db.editSummary(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_SUMMARY_AVERAGE.value:
                result = self.db.getSummAverage(data)
                return {"protocol": protocol, "data": result}
            # User
            case Protocol.CHANGE_STATE_OBJ.value:
                result = self.db.changeStateObj(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_PROFILE.value:
                result = self.db.getProfile(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_USER_OBJECT.value:
                result = self.db.getUserObjet(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_EVALUATIONS.value:
                result = self.db.getEvaluations(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_EVAL.value:
                result = self.db.getEval(data)
                return {"protocol": protocol, "data": result}

            # Statistic
            case Protocol.GET_LEADERBOARD.value:
                result = self.db.checkLeaderBoard(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_RANKING_OBJECT.value:
                result = self.db.getObRanking(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_RANKING_SPENDER.value:
                result = self.db.getSpenderRanking(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_COURSES_MOST_RESUMES.value:
                result = self.db.getMostSummCours(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_RES_IN_AT_LEAST_THREE_COURSES.value:
                result = self.db.getSummInAtLeastThreeCourse(data)
                return {"protocol": protocol, "data": result}

            case Protocol.GET_BEST_TEN_USERS.value:
                result = self.db.getBestTenUsers(data)
                return {"protocol": protocol, "data": result}

            case Protocol.ADD_USER_COURSE.value:
                result = self.db.addUserCourse(data)
                return {"protocol": protocol, "data": result}

            case Protocol.ENOUGH_POINTS.value:
                result = self.db.enoughPoints(data)
                return {"protocol": protocol, "data": result}
                
