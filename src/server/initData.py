import csv

from xml_parser import parseReward, parseUser

utilisateurs = parseUser()
rew = parseReward()

# for x in utilisateurs:
#     print(x["points"])


def initCours(myCursor):
    insertCourseSql = """
    INSERT INTO Cours
    (Mnemonique, Nom, Fac, Credits,Annee) 
    VALUES (%s, %s, %s, %s, %s)
    """
    with open("../data/cours.csv", "r") as csv_file:
        annee_academique = 2025
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for line in csv_reader:
            mnemo = line[0]
            nom = line[1]
            fac = line[2]
            utc = line[3]
            val = (mnemo, nom, fac, utc, annee_academique)
            print(nom)
            myCursor.execute(insertCourseSql, val)


def initUser(mycursor):
    insertUserSql = """INSERT INTO Utilisateur 
                    (Id, Name, Email, Inscription, Niveau, Points )
                    VALUES (%s, %s, %s, %s, %s, %s)"""

    insertResumeSql = """INSERT INTO Resume
                        (Title, Description, Publication, Version, Visibilite, Moyenne, Mnemonique, IdUser)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    for user in utilisateurs:
        niveau = user["niveau"] if user["niveau"] else 0
        points = user["points"] if user["points"] else 0
        val = (
            user["id"],
            user["nomUtilisateur"],
            user["email"],
            user["dateInscription"],
            niveau,
            points,
        )
        print(user["nomUtilisateur"])
        mycursor.execute(insertUserSql, val)

        for res in user["resumes"]:
            if not res["cours"]:
                continue
            description = res["description"] if res["description"] else None
            version = res["version"] if res["version"] else 1
            visibilite = res["visibilite"] if res["visibilite"] else 1
            val = (
                res["titre"],
                description,
                res["datePublication"],
                version,
                visibilite,
                res["noteMoyenne"],
                res["cours"],
                user["id"],
            )
            try:
                mycursor.execute(insertResumeSql, val)
            except:
                continue
