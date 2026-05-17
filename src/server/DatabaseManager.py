import mysql.connector


class DatabaseManager:
    def __init__(self, cursor):
        self.cursor = cursor.cursor(dictionary=True)
        self.conn = cursor
        self.path_signin = "DB/queries/users/signin.sql"
        self.path_signup = "DB/queries/users/signup.sql"
        # Courses

        self.path_getAllCourses = "DB/queries/courses/list_courses.sql"
        self.path_addCourse = "DB/queries/courses/add_course.sql"
        self.path_deleteUserCourse = "DB/queries/users/delete_user_course.sql"
        self.path_getUserCourse = "DB/queries/courses/list_user_cours.sql"
        # Review
        self.path_addReview = "DB/queries/review/add_evaluation.sql"
        # Shop
        self.path_buyObjet = "DB/queries/shop/add_object_to_users.sql"
        self.path_getPoints = "DB/queries/shop/check_points.sql"
        self.path_getTransactionHistory = (
            "DB/queries/shop/check_transaction_history.sql"
        )
        self.path_getObjectInfo = "DB/queries/shop/inspect_object.sql"
        # Summaries
        self.path_addSummary = "DB/queries/summaries/add_summary.sql"
        self.path_checkSummary = "DB/queries/summaries/check_summary.sql"
        self.path_deleteSummary = "DB/queries/summaries/delete_summary.sql"
        self.path_getSummAverage = "DB/queries/stats/summary_average.sql"
        # User
        self.path_changeStateObj = "DB/queries/users/changeStataeObj"
        self.path_getProfile = "DB/queries/check_profile"
        # Statistic
        self.path_checkLeaderBoard = "DB/queries/stats/check_leaderboard.sql"
        self.path_getObRanking = "DB/queries/stats/ranking_object.sql"
        self.path_getSpenderRanking = "DB/queries/stats/ranking_spender.sql"
        self.path_getMostSummCours = "DB/queries/stats/most_summarize_course.sql"
        self.path_getSummInAtLeastThreeCours = "DB/queries/stats/at_least_three_differents.sql"
        self.path_getBestTenUsers = "DB/queries/stats/ranking_ten_users_points.sql"

    def reader_query(self, path, fetch="all", insert=False, params=None):
        with open(path, "r", encoding="utf-8") as fichier:

            script_sql = fichier.read()
            # if params:
            #   script_sql = script_sql.format(**params)
            try:
                """iterator = self.cursor.execute(script_sql,params)
                results = []
                results.append(iterator.fetchall())
                self.cursor.connection.commit() #valider les modification
                return results"""
                self.cursor.execute(script_sql, params)

                # Valider les modifications (utile seulement pour INSERT/UPDATE/DELETE)
                if insert:
                    self.conn.commit()

                # Récupérer les résultats directement depuis le curseur
                if fetch == "one":
                    results = self.cursor.fetchone()
                elif fetch == "all":
                    results = self.cursor.fetchall()
                print("results in DM", results)

                # Retourne sous forme de liste de liste si c'est ce qu'attendait le reste du code
                return results

            except mysql.connector.Error as erreur:
                print(f"Erreur d'exécution : {erreur}")

    def signin(self, data):
        print("DM")
        return self.reader_query(self.path_signin, "one", False, params=data)

    def signup(self, data):
        return self.reader_query(self.path_signup, "one", True, params=data)

    #Courses
    def getAllCourses(self, data):
        return self.reader_query(self.path_getAllCourses, "all", False, params=data)

    # Courses
    def addCourse(self, data):
        return self.reader_query(self.path_addCourse, "one", True, params=data)

    def deleteUserCourse(self, data):
        return self.reader_query(self.path_deleteUserCourse, "one", True, params=data)

    def getUserCourse(self, data):
        return self.reader_query(self.path_getUserCourse, "all", False, params=data)

    # Review
    def addReview(self, data):
        return self.reader_query(self.path_addReview, "one", True, params=data)

    # Shop
    def buyObject(self, data):
        return self.reader_query(self.path_buyObjet, "one", True, params=data)

    def getPoints(self, data):
        return self.reader_query(self.path_getPoints, "one", False, params=data)

    def getTransactionHistory(self, data):
        return self.reader_query(
            self.path_getTransactionHistory, "all", False, params=data
        )

    def getObjectInfo(self, data):
        return self.reader_query(self.path_getObjectInfo, "all", False, params=data)

    # Summaries
    def addSummary(self, data):
        return self.reader_query(self.path_addSummary, "one", True, params=data)

    def checkSummary(self, data):
        return self.reader_query(self.path_checkSummary, "all", False, params=data)

    def deleteSummary(self, data):
        return self.reader_query(self.path_deleteSummary, "one", True, params=data)

    def getSummAverage(self, data):
        return self.reader_query(self.path_getSummAverage, "one", False, params=data)

    # User
    def changeStateObj(self, data):
        return self.reader_query(self.path_changeStateObj, "one", False, params=data)

    def getProfile(self,data):
        return self.reader_query(self.path_getProfile,"one",False,params=data)

    #Statistic
    def checkLeaderBoard(self,data):
        self.reader_query(self.path_checkLeaderBoard,"all",False,params=data)

    def getObRanking(self,data):
        return self.reader_query(self.path_getObRanking,"all",False,params=data)

    def getSpenderRanking(self,data):
        return self.reader_query(self.path_getSpenderRanking,"all",False,params=data)

    def getMostSummCours(self,data):
        return self.reader_query(self.path_getMostSummCours,"one",False,params=data)

    def getSummInAtLeastThreeCourse(self,data):
        return self.reader_query(self.path_getSummInAtLeastThreeCours,"all",False,params=data)

    def getBestTenUsers(self,data):
        return self.reader_query(self.path_getBestTenUsers,"all",False,params=data)
