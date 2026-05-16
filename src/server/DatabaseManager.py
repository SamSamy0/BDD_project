
import mysql.connector


class DatabaseManager:
    def __init__(self,cursor):
        self.cursor = cursor.cursor()
        self.db_c2 = cursor
        self.path_signin = "DB/queries/users/signin.sql"
        self.path_signup = "DB/queries/users/signup.sql"

    def reader_query(self,path,params=None):
        with open(path, 'r', encoding='utf-8') as fichier:

            script_sql = fichier.read()
            #if params:
            #   script_sql = script_sql.format(**params)
            try:
                """iterator = self.cursor.execute(script_sql,params)
                results = []
                results.append(iterator.fetchall())
                self.cursor.connection.commit() #valider les modification
                return results"""
                self.cursor.execute(script_sql, params)

                # Récupérer les résultats directement depuis le curseur
                results = self.cursor.fetchone()
                print(results)

                # Valider les modifications (utile seulement pour INSERT/UPDATE/DELETE)
                self.db_c2.commit()

                # Retourne sous forme de liste de liste si c'est ce qu'attendait le reste du code
                return results

            except mysql.connector.Error as erreur:
                print(f"Erreur d'exécution : {erreur}")



    def signin(self,data):
        print("DM")
        return self.reader_query(self.path_signin,params=data)


    def signup(self,data):
        return self.reader_query(self.path_signup,params=data)




