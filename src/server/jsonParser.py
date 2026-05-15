import json

def parseEval():
    with open("../data/commentaires.json", "r", encoding="utf-8") as f:
        d = json.load(f)
        return d["evaluations"]
