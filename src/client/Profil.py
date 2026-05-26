class Profile:
    def __init__(self, id=None, title=None, name=None, points=None):
        self.idUser = id
        self.title = title
        self.name = name
        self.points = points

    def initData(self, data: dict):
        self.idUser = data.get("ID")
        self.points = data.get("Points")
        self.name = data.get("Nom")


    def getName(self):
        return self.name
