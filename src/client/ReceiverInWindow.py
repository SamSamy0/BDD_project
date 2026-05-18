from Gui import Gui


class ReceiverInWindow:
    def __init__(self, app: Gui):
        # Gui
        self.app = app
        pass

    def isAcceptedLogin(self, connect: bool):
        if connect:
            self.app.show_view("MENU")
        else:
            # app.showLoginError("Identifiants incorrect")
            pass

    def setAllCourse(self, courses: list[dict]):
        self.app.show_view("CLASS")
        classView = self.app.frames["CLASS"]
        classView.displayCourses(courses)



    def displayStore(self, store: dict):
        self.app.show_view("SHOP")
        shopView = self.app.frames["SHOP"]
        shopView.displayStore(store)

    def bestTenUser(self, top: dict):
        self.app.show_view("LEADERBOARD")
        leaderView = self.app.frames["LEADERBOARD"]
        leaderView.displayTop10(top)

    def mostSummCours(self, best: dict):
        self.app.show_view("LEADERBOARD")
        leaderView = self.app.frames["LEADERBOARD"]
        leaderView.displayMostSumCours(best)

    def SumInAtLeastThree(self, data: dict):
        self.app.show_view("LEADERBOARD")
        leaderView = self.app.frames["LEADERBOARD"]
        leaderView.SumInMoreThanThree(data)

    def showProfile(self, data: dict):
        self.app.show_view("PROFIL")
        profilView = self.app.frames["PROFIL"]
        profilView.displayStats(data)

    def isBought(self, data: dict):
        shopView = self.app.frames["SHOP"]
        shopView.buy(data)

    def addCourse(self, data: dict):
        if data is not None:
           print("Cours enregistré avec succès: ",data)
        else:
            #TODO: Pop-up cours existe déjà
            classView = self.app.frames["CLASS"]
            classView.rollback_course()


    def checkLeaderboard(self, data: list[dict]):
        leaderView = self.app.frames["LEADERBOARD"]
        leaderView.leaderboard = []
        for user in data:
            leaderView.leaderboard.append(tuple(user.values()))
        self.app.show_view("LEADERBOARD")
        leaderView.displayLeaderboard()

    def deleteCourse(self,data,iduser):
        if data is not None:
            classView = self.app.frames["CLASS"]
            classView.deleteCourse(data,iduser)
            classView.after(0, classView.refresh)

    def getUserCourse(self,data):
        pass


