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

        classView.after(0, lambda: classView.displayCourses(courses))


    def displayStore(self, store: dict):
        self.app.show_view("SHOP")
        shopView = self.app.frames["SHOP"]
        shopView.after(0, lambda: shopView.displayStore(store))

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

    def showUserObject(self, data: dict):
        # self.app.show_view("SHOP")
        shopView = self.app.frames["SHOP"]
        shopView.after(0, lambda: shopView.saveBoughtObject(data))
        shopView.after(0, lambda: shopView.showUserObject(data))

    def isBought(self, data: dict):
        shopView = self.app.frames["SHOP"]
        shopView.buy(data)


    def addCourse(self, data: dict):
        if data is not None:
            print("Cours enregistré avec succès: ", data)
        else:
            # TODO: Pop-up cours existe déjà
            classView = self.app.frames["CLASS"]
            classView.rollback_course()


    def checkLeaderboard(self, data: list[dict]):
        leaderView = self.app.frames["LEADERBOARD"]
        leaderView.leaderboard = []
        for user in data:
            leaderView.leaderboard.append(tuple(user.values()))
        self.app.show_view("LEADERBOARD")
        leaderView.displayLeaderboard()


    def updatePointsInShop(self, data):
        shopView = self.app.frames["SHOP"]
        shopView.after(0, lambda: shopView.updatePoints(data))
        
    def addCourse(self, data: dict):
        classView = self.app.frames["CLASS"]
        if data is not None:
           classView.after(0, lambda: classView.confirmedAdd(data))
           print("Cours enregistré avec succès: ",data)
        else:
            #TODO: Pop-up cours existe déjà
            classView = self.app.frames["CLASS"]
            classView.after(0, lambda: classView.refusedAdd(data))


    def getUserCourse(self,data):
        if data is not None:
            self.app.show_view("MYCLASS")
            myClassView = self.app.frames["MYCLASS"]
            myClassView.after(0, lambda: myClassView.displayCourses(data))


    def addUserCourse(self,data):
        self.app.show_view("MYCLASS")
        myClassView = self.app.frames["MYCLASS"]
        if data is not None:
            myClassView.after(0, lambda: myClassView.confirmedAdd(data))
        else:
            myClassView.after(0, lambda: myClassView.refusedAdd(data))

    def deleteUserCourse(self,data):
        self.app.show_view("MYCLASS")
        myClassView = self.app.frames["MYCLASS"]
        if data is not None:
            myClassView.after(0, lambda: myClassView.confirmedDelete(data))



    def checkSummaries(self, data: list[dict]):
        view = self.app.frames["SUMMARY"]
        view.summaries = []
        summaries = view.summaries
        for summary in data:
            temp = (summary["Titre"],summary["Nom"],summary["Moyenne"])
            summaries.append(temp)

        self.app.show_view("SUMMARY")
        view.after(0, lambda: view.displaySummaries())

    def addSummary(self,data):
        view = self.app.frames["SUMMARY"]
        view.after(0, lambda: view.displaySummaries())
