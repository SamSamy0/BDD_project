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

    def setAllCourse(self, courses: dict):
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
