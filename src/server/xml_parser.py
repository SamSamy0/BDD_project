import xml.etree.ElementTree as ET
from enum import Enum

from getUserLevel import getUserLevel


def parseUser():
    res = []
    tree = ET.parse("data/utilisateurs")
    root = tree.getroot()
    for user in root.findall("utilisateur"):
        str_points = user.findtext("points")
        str_level = user.findtext("niveau")
        points = int(str_points) if str_points else None
        level = int(str_level) if str_level else None
        # If we have level but not points
        if points is None and level is not None:
            default_points = {
                1: 150,
                2: 400,
                3: 650,
                4: 1000,
                5: 1300,
                6: 1700,
                7: 2200,
                8: 2600,
                9: 3000,
            }
            points = default_points.get(level, 0)

        if level is None and points is not None:
            level = getUserLevel(points)

        data = {
            "id": user.get("id"),
            "nomUtilisateur": user.findtext("nomUtilisateur"),
            "email": user.findtext("email"),
            "dateInscription": user.findtext("dateInscription"),
            "points": points,
            "niveau": level,
            "titreActif": user.findtext("titreActif"),
            "resumes": [],
            "achats": [],
        }
        resumes_node = user.find("resumes")
        if resumes_node is not None:
            for resum in resumes_node.findall("resume"):
                data["resumes"].append(
                    {
                        "titre": resum.findtext("titre"),
                        "description": resum.findtext("description"),
                        "datePublication": resum.findtext("datePublication"),
                        "version": resum.findtext("version"),
                        "visibilite": resum.findtext("visibilite"),
                        "noteMoyenne": resum.findtext("noteMoyenne"),
                        "cours": resum.findtext("cours"),
                    }
                )
        achats = user.find("achats")
        if achats is not None:
            for obj in achats.findall("objet"):
                data["achats"].append(obj.text)

        # We don't parse evalutaions bc they're in commentiares.json
        res.append(data)
    return res


def parseReward():
    catalogue = []
    tree = ET.parse("data/recompenses.xml")
    root = tree.getroot()

    for cosmetics in root.findall("objet"):
        obj = {
            "id": cosmetics.get("id"),
            "nom": cosmetics.findtext("nom"),
            "type": cosmetics.findtext("type"),
            "description": cosmetics.findtext("description"),
            "prix": cosmetics.findtext("prix"),
        }
        catalogue.append(obj)
    return catalogue
