class Profile:
    def __init__(self, id=None, title=None, name=None, points=None):
        self.idUser = id
        self.title = title
        self.name = name
        self.points = points

    def initData(self, data: dict):
        self.idUser = data.get("ID")
        # self.title = data.get("")
        self.points = data.get("Points")
        print("pointso", self.points)
