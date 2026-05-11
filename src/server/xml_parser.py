import xml.etree.ElementTree as ET


def parseUser():
    res = []
    tree = ET.parse("../data/utilisateurs")
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
            "evaluationsRecues": [],
        }
        resumes_node = user.find("resumes")
        if resumes_node is not None:
            for resum in resumes_node.findall("resume"):
                data["resumes"].append(
                    {
                        "cours": resum.findtext("cours"),
                        "titre": resum.findtext("titre"),
                        "datePublication": resum.findtext("datePublication"),
                        "noteMoyenne": resum.findtext("noteMoyenne"),
                    }
                )
        achats = user.find("achats")
        if achats is not None:
            for obj in achats.findall("objet"):
                data["achats"].append(obj.text)
        evaluations = user.find("evaluationsRecues")
        if evaluations is not None:
            for eval in evaluations.findall("evaluation"):
                data["evaluationsRecues"].append(
                    {
                        "note": eval.findtext("note"),
                        "commentaire": eval.findtext("commentaire"),
                    }
                )
        res.append(data)
    return res


def parseReward():
    catalogue = []
    tree = ET.parse("../data/recompenses.xml")
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
