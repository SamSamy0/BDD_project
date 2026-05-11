from View import View, TypeView

class LoginView(View):
    def __init__(self, window):
        super().__init__(window)
        self.type = TypeView.LOGIN
        self.initView()

    def initView(self):
        self.window['-LOGIN-'].update(visible=True)

