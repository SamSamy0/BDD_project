from View import View, TypeView

class LoginView(View):
    def __init__(self, window):
        super().__init__(window)
        self.type = TypeView.LOGIN

    def initView(self):
        
        pass
