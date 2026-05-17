import mysql.connector


class DatabaseManager:
    def __init__(self, cursor):
        self.cursor = cursor.cursor(dictionary=True)
        self.conn = cursor
        self.path_signin = "DB/queries/users/signin.sql"
        self.path_signup = "DB/queries/users/signup.sql"
        self.path_getAllCourses = "DB/queries/courses/list_courses.sql"
        self.path_getBestTenUsers = "DB/queries/stats/ranking_ten_users_points.sql"
        self.path_getSummInAtLeastThreeCours = "DB/queries/stats/at_least_three_differents.sql"
        self.path_getMostSummCours = "DB/queries/stats/most_summarize_course.sql"
        self.path_getSpenderRanking = "DB/queries/stats/ranking_spender.sql"
        self.path_getObRanking = "DB/queries/stats/ranking_object.sql"


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

    def getAllCourses(self, data):
        return self.reader_query(self.path_getAllCourses, "all", False, params=data)
    

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
