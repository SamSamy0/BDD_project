import xml.etree.ElementTree as ET

MAXLV1 = 300
MAXLV2 = 500
MAXLV3 = 850
MAXLV4 = 1150
MAXLV5 = 1500
MAXLV6 = 2000
MAXLV7 = 2400
MAXLV8 = 2850


def parseUser():
    res = []
    tree = ET.parse("data/utilisateurs")
    root = tree.getroot()
    for user in root.findall("utilisateur"):
        data = {
            "id": user.get("id"),
            "nomUtilisateur": user.findtext("nomUtilisateur"),
            "email": user.findtext("email"),
            "dateInscription": user.findtext("dateInscription"),
            "points": user.findtext("points"),
            "niveau": user.findtext("niveau"),
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
