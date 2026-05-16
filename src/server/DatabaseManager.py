
import mysql.connector


class DatabaseManager:
    def __init__(self,cursor):
        self.cursor = cursor
        self.path_signin = "../DB/queries/users/signin.sql"
        self.path_signup = "../DB/queries/users/signup.sql"

    def reader_query(self,path,params=None):
        with open(path, 'r', encoding='utf-8') as fichier:

            script_sql = fichier.read()
            if params:
                script_sql = script_sql.format(**params)
            try:
                # Exécution des requêtes multiples
                iterator = self.cursor.execute(script_sql, multi=True)

                results = []

                #  Parcourir l'itérateur pour vider le flux MySQL
                for statement in iterator:
                    if statement.with_rows:
                        results.append(statement.fetchall())
                self.cursor.connection.commit() #valider les modification
                return results

            except mysql.connector.Error as erreur:
                print(f"Erreur d'exécution : {erreur}")



    def signin(self,data):

       return self.reader_query(self.path_signin,params=data)


    def signup(self,data):
        return self.reader_query(self.path_signup,params=data)




