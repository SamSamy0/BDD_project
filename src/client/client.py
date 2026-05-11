import FreeSimpleGUI as sg
from LoginView import LoginView


class Client:

    def __init__(self):
        sg.theme("DarkAmber")  # Add a touch of color
        self.window = self.createWindow()
        view = LoginView(self.window)


    def createWindow(self):
        # All the stuff inside your window.
        login_layout = [
            [sg.Text("Authentification")],
            [sg.Text("Identifiant"),sg.InputText()],
            [sg.Text("Mot de passe"),sg.InputText()],
            [sg.Button("Log in"), sg.Button("Register")]
        ]

        menu_layout = []
        profil_layout = []
        class_layout = []
        leaderboard_layout = []
        layout = [
            [sg.Column(login_layout, key='-LOGIN-',visible=True),sg.Column(menu_layout, key ='-MENU-',visible=False),
             sg.Column(profil_layout,key ='-PROFIL-',visible=False),sg.Column(leaderboard_layout,key='-LEADERBOARD-',visible=False),
             sg.Column(class_layout,key='-CLASS-',visible=False),]

        ]
        # Create the Window
        return sg.Window("Window Title", layout,finalize=True)


    def run (self):
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = self.window.read()
            if (
                event == sg.WIN_CLOSED or event == "Cancel"
            ):  # if user closes window or clicks cancel
                break
            print("You entered ", values[0])

        self.window.close()



if __name__ == "__main__":
    client = Client()
    client.run()
