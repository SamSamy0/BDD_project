import csv
import json

import mysql.connector
from jsonParser import parseEval
from xml_parser import parseReward, parseUser


def getUserId(mycursor, auteur):
    getUserIdSql = """
    SELECT u.ID
    FROM Utilisateur u
    WHERE u.Nom = %s
    """
    mycursor.execute(getUserIdSql, (auteur,))
    res = mycursor.fetchone()
    if res:
        auteur_id = res[0]
        print(f"L'id de l'auteur est : {auteur_id}")
        return auteur_id
    else:
        print("L'auteur n'est pas dans la bdd")


def getResumeId(mycursor, title, mnemo):
    getResumeId = """
    SELECT r.ID
    FROM Resume r
    WHERE r.Titre = %s AND r.Mnemonique = %s
    """
    mycursor.execute(getResumeId, (title.strip(), mnemo.strip()))
    res = mycursor.fetchone()
    if res:
        resume_id = res[0]
        print(f"L'id du résumé est:  {resume_id}")
        return resume_id
    else:
        print("on a pas su fetch")


def initCours(myCursor):
    insertCourseSql = """
    INSERT INTO Cours
    (Mnemonique, Nom, Fac, Credits,Annee)
    VALUES (%s, %s, %s, %s, %s)
    """
    with open("data/cours.csv", "r") as csv_file:
        annee_academique = 2025
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for line in csv_reader:
            mnemo = line[0]
            nom = line[1]
            fac = line[2]
            utc = line[3]
            val = (mnemo, nom, fac, utc, annee_academique)
            myCursor.execute(insertCourseSql, val)


def initUser(mycursor):
    utilisateurs = parseUser()
    insertUserSql = """INSERT INTO Utilisateur
                    (ID, Nom, Email, Inscription, Niveau, Points )
                    VALUES (%s, %s, %s, %s, %s, %s)"""

    insertResumeSql = """INSERT INTO Resume
                        (Titre, Description, Publication, Version, Visibilite, Moyenne, Mnemonique, IdUtilisateur)
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
            except Exception as e:
                print("ERROR: ", e)
                continue


def initEval(mycursor):
    raw_eval = parseEval()
    initEval = """
    INSERT INTO Evaluation
    (Note, Commentaire, IdUtilisateur, IdResume)
    VALUES(%s,%s,%s,%s)
    """
    for elem in raw_eval:
        author = elem["auteur"]
        course = elem["resume"]["cours"]
        title = elem["resume"]["titre"]
        note = elem["note"]
        comment = elem["commentaire"]
        auteur_id = getUserId(mycursor, author)
        resume_id = getResumeId(mycursor, title, course)
        # try:
        print("title: ", title)
        if auteur_id is not None and resume_id is not None:
            mycursor.execute(initEval, (note, comment, auteur_id, resume_id))
        else:
            print(f"Donnée incohérente => ignoré")


def initRew(myCursor):
    rew = parseReward()
    initRew = """
    INSERT INTO ObjetCosmetique
    (ID, Nom, TypeObjet, Prix, Description)
    VALUES(%s, %s, %s, %s, %s)
    """
    for r in rew:
        id = r["id"]
        name = r["nom"]
        typeObj = r["type"]
        prix = r["prix"]
        desc = r["description"]
        try:
            myCursor.execute(initRew, (id, name, typeObj, prix, desc))
        except Exception as e:
            print("SOMETHING WRONG: ", e)


def initCoursUtilisateur(mycursor):
    utilisateurs = parseUser()
    insertCoursUtilisateur = """
    INSERT IGNORE INTO CoursUtilisateur
    (Mnemonique, IdUtilisateur)
    VALUES(%s,%s)
    """
    with open("data/cours.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            mnemo = line[0]
            for user in utilisateurs:
                iduser = user["id"]
                for res in user["resumes"]:
                    if not res["cours"]:
                        continue
                    try:
                        if res["cours"] == mnemo:
                            val = (mnemo, iduser)
                            mycursor.execute(insertCoursUtilisateur, val)
                    except Exception as e:
                        print("ERROR:", e)
                        continue


def initUtilisateurObjet(mycursor):
    utilisateurs = parseUser()
    rew = parseReward()

    mapping_object = dict()
    for r in rew:
        mapping_object[r["nom"]] = r["id"]

    insertUtilisateurObjet = """
    INSERT IGNORE INTO UtilisateurObjet
    (Idutilisateur, IdObjet, EstActif)
    VALUES(%s,%s,%s)
    """
    for user in utilisateurs:
        iduser = user["id"]
        title_activate = user["titreActif"]
        objects = user["achats"]

        if not objects:
            continue

        for obj in objects:
            if obj not in mapping_object:
                continue

            if title_activate and title_activate == obj:
                is_active = True
            else:
                is_active = False
            val = (iduser, mapping_object[obj], is_active)
            try:
                mycursor.execute(insertUtilisateurObjet, val)

            except Exception as e:
                print(
                    f"Erreur lors de l'insertion de l'objet {obj} pour l'utilisateur {iduser} : {e}"
                )


def load_json():
    with open("DB/config.json", "r") as jsonfile:
        data = json.load(jsonfile)

    return data


def connect_mySql():
    connection = None
    init = load_json()
    connection = mysql.connector.connect(
        host=init["host"],
        port=init["port"],
        user=init["user"],
        password=init["password"],
        database=init["database"],
    )
    print("MySQL Database connection successful")
    return connection


if __name__ == "__main__":
    connexion = connect_mySql()
    cursor = connexion.cursor()
    initCours(cursor)
    initUser(cursor)
    initEval(cursor)
    initRew(cursor)
    initUtilisateurObjet(cursor)
    connexion.commit()
    cursor.close()
    connexion.close()
