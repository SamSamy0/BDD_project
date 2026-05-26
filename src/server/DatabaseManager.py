import mysql.connector
from getUserLevel import getUserLevel


class DatabaseManager:
    def __init__(self, cursor):
        self.cursor = cursor.cursor(dictionary=True)
        self.conn = cursor
        self.path_signin = "DB/queries/users/signin.sql"
        self.path_signup = "DB/queries/users/signup.sql"
        # Courses

        self.path_getAllCourses = "DB/queries/courses/list_courses.sql"
        self.path_addCourse = "DB/queries/courses/add_course.sql"
        self.path_addUserCourse = "DB/queries/users/add_usercourse.sql"
        self.path_deleteUserCourse = "DB/queries/users/delete_user_course.sql"
        self.path_getUserCourse = "DB/queries/courses/list_user_cours.sql"
        # Review
        self.path_addReview = "DB/queries/reviews/add_evaluation.sql"
        # Shop
        self.path_buyObjet = "DB/queries/shop/add_object_to_users.sql"
        self.path_getPoints = "DB/queries/shop/check_points.sql"
        self.path_getTransactionHistory = (
            "DB/queries/shop/check_transaction_history.sql"
        )
        self.path_getStore = "DB/queries/shop/check_catalogue.sql"
        self.path_getObjectInfo = "DB/queries/shop/inspect_object.sql"
        self.path_debitPoints = "DB/queries/shop/debit_users_points.sql"
        self.path_addTransaction = "DB/queries/shop/add_transaction.sql"
        # Summaries
        self.path_addSummary = "DB/queries/summaries/add_summary.sql"
        self.path_checkSummary = "DB/queries/summaries/check_summary.sql"
        self.path_checkSummaries = "DB/queries/summaries/check_summaries.sql"
        self.path_deleteSummary = "DB/queries/summaries/delete_summary.sql"
        self.path_getSummAverage = "DB/queries/stats/summary_average.sql"
        self.path_getEvaluations = "DB/queries/summaries/get_evaluations.sql"
        self.path_getEval = "DB/queries/summaries/get_eval.sql"
        # User
        self.path_changeStateObj = "DB/queries/users/change_state_object.sql"
        self.path_getProfile = "DB/queries/users/check_profile.sql"
        self.path_getUserObject = "DB/queries/users/get_user_object.sql"
        self.path_getUserAllPoints = "DB/queries/users/get_alltime_points_user.sql"
        self.path_updateUserLevel = "DB/queries/users/update_level.sql"
        # Statistic
        self.path_checkLeaderBoard = "DB/queries/stats/check_leaderboard.sql"
        self.path_getObRanking = "DB/queries/stats/ranking_object.sql"
        self.path_getSpenderRanking = "DB/queries/stats/ranking_spender.sql"
        self.path_getMostSummCours = "DB/queries/stats/most_summarize_course.sql"
        self.path_getSummInAtLeastThreeCours = (
            "DB/queries/stats/at_least_three_differents.sql"
        )
        self.path_getBestTenUsers = "DB/queries/stats/ranking_ten_users_points.sql"

    def check_and_upgrade_level(self, idUser: int):
        try:
            with open(self.path_getUserAllPoints, "r", encoding="utf-8") as fichier:
                self.cursor.execute(fichier.read(), {"idUser": idUser})
                res = self.cursor.fetchone()
            total = res.get("Total") if (res and res.get("Total") is not None) else 0
            level = getUserLevel(total)
            with open(self.path_updateUserLevel, "r", encoding="utf-8") as fichier2:
                sql_update_level = fichier2.read()

            self.cursor.execute(sql_update_level, {"level": level, "idUser": idUser})
            self.conn.commit()
            print("CONGRATULATIONS, YOU UPGRADED")

        except Exception as e:
            print(f"Error when upgrading: {e}")

    def reader_query(self, path, fetch="all", insert=False, params=None):
        with open(path, "r", encoding="utf-8") as fichier:

            script_sql = fichier.read()
            try:
                self.cursor.execute(script_sql, params)

                # Valider les modifications (utile seulement pour INSERT/UPDATE/DELETE)
                if insert:
                    self.conn.commit()

                # Récupérer les résultats directement depuis le curseur
                if fetch == "one":
                    results = self.cursor.fetchone()
                    print("results in DM", results)
                elif fetch == "all":
                    results = self.cursor.fetchall()
                    print("results in DM", results)
                else:
                    results = params

                # Retourne sous forme de liste de liste si c'est ce qu'attendait le reste du code
                return results

            except mysql.connector.Error as erreur:
                print(f"Erreur d'exécution : {erreur}")
                return None

    def signin(self, data):
        print("DM")
        return self.reader_query(self.path_signin, "one", False, params=data)

    def signup(self, data):
        return self.reader_query(self.path_signup, "one", True, params=data)

    # Courses
    def getAllCourses(self, data):
        return self.reader_query(self.path_getAllCourses, "all", False, params=data)

    # Courses
    def addCourse(self, data):
        return self.reader_query(self.path_addCourse, "None", True, params=data)

    def addUserCourse(self, data):

        return self.reader_query(self.path_addUserCourse, "None", True, params=data)

    def deleteUserCourse(self, data):
        return self.reader_query(self.path_deleteUserCourse, "None", True, params=data)

    def getUserCourse(self, data):
        return self.reader_query(self.path_getUserCourse, "all", False, params=data)

    # Review
    def addReview(self, data):
        res = self.reader_query(self.path_addReview, "one", True, params=data)
        self.check_and_upgrade_level(data.get("idAuthor"))
        return res

    # Shop
    def buyObject(self, data):
        userPoints = int(self.getPoints(data).get("Points"))
        cout = int(data.get("cost"))
        if userPoints < cout:
            print("Solde Insuffisant")
            return {"success": False, "msg": "Solde Insuffisant"}

        try:
            # Adding objet to users list
            with open(self.path_buyObjet, "r", encoding="utf-8") as fichier:
                sql_addObject = fichier.read()

            # debit points
            with open(self.path_debitPoints, "r", encoding="utf-8") as f:
                sql_debitPoints = f.read()

            with open(self.path_addTransaction, "r", encoding="utf-8") as f:
                sql_addTransaction = f.read()

            self.cursor.execute(sql_addObject, data)
            self.cursor.execute(sql_debitPoints, data)
            self.cursor.execute(sql_addTransaction, data)
            self.conn.commit()
            return {"success": True, "msg": "Achat Réussi!"}
        except Exception as e:
            print(e)
            return {"success": False, "msg": "Erreur lors de l'achat."}

        # return self.reader_query(self.path_buyObjet, "one", True, params=data)

    def getPoints(self, data):
        return self.reader_query(self.path_getPoints, "one", False, params=data)

    def getTransactionHistory(self, data):
        return self.reader_query(
            self.path_getTransactionHistory, "all", False, params=data
        )

    def getObjectInfo(self, data):
        return self.reader_query(self.path_getObjectInfo, "all", False, params=data)

    def getStore(self, data):
        return self.reader_query(self.path_getStore, "all", False, params=data)

    # Summaries
    def addSummary(self, data):
        res = self.reader_query(self.path_addSummary, "one", True, params=data)
        self.check_and_upgrade_level(data.get("idAuthor"))
        return res

    def checkSummary(self, data):
        return self.reader_query(self.path_checkSummary, "all", False, params=data)

    def checkSummaries(self, data):
        return self.reader_query(self.path_checkSummaries, "all", False, params=data)

    def deleteSummary(self, data):
        return self.reader_query(self.path_deleteSummary, "one", True, params=data)

    def getSummAverage(self, data):
        return self.reader_query(self.path_getSummAverage, "one", False, params=data)

    def getEvaluations(self, data):
        return self.reader_query(self.path_getEvaluations, "all", False, params=data)

    def getEval(self, data):
        return self.reader_query(self.path_getEval, "one", False, params=data)

    # User
    def changeStateObj(self, data):
        return self.reader_query(self.path_changeStateObj, "one", True, params=data)

    def getProfile(self, data):
        return self.reader_query(self.path_getProfile, "one", False, params=data)

    def getUserObjet(self, data):
        return self.reader_query(self.path_getUserObject, "all", False, params=data)

    # Statistic
    def checkLeaderBoard(self, data):
        return self.reader_query(self.path_checkLeaderBoard, "all", False, params=data)

    def getObRanking(self, data):
        return self.reader_query(self.path_getObRanking, "all", False, params=data)

    def getSpenderRanking(self, data):
        return self.reader_query(self.path_getSpenderRanking, "all", False, params=data)

    def getMostSummCours(self, data):
        return self.reader_query(self.path_getMostSummCours, "all", False, params=data)

    def getSummInAtLeastThreeCourse(self, data):
        return self.reader_query(
            self.path_getSummInAtLeastThreeCours, "all", False, params=data
        )

    def getBestTenUsers(self, data):
        return self.reader_query(self.path_getBestTenUsers, "all", False, params=data)
