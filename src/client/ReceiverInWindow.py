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

    def showProfile(self, connect: bool, data: dict):
        if connect:
            self.app.show_view("MENU")
        else:
            # app.showLoginError("Identifiants incorrect")
            pass

    def setAllCourse(self, courses: dict):
        self.app.show_view("CLASS")
        classView = self.app.frames["CLASS"]
        classView.displayCourses(courses)
