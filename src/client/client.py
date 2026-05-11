import FreeSimpleGUI as sg
from LoginView import LoginView


class Client:

    def __init__(self):
        sg.theme("DarkAmber")  # Add a touch of color
        self.window = self.createWindow()
        view = LoginView(self.window)


    def createWindow(self):
        # All the stuff inside your window.
        layout = [
            [sg.Text("Some text on Row 1")],
            [sg.Text("Enter something on Row 2"), sg.InputText()],
            [sg.Button("Ok"), sg.Button("Cancel")],

        ]
        # Create the Window
        return sg.Window("Window Title", layout)


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
