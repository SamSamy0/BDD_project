from View import View, TypeView

class AppView(View):
    def __init__(self, window):
        super().__init__(window)
        self.type = TypeView.APP

    def initView(self):
        pass
