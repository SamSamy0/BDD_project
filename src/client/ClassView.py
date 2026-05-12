from View import View
import customtkinter as ctk



class ClassView(View):

    def initView(self):
        self.title_label = ctk.CTkLabel(self, text="Cours", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=1, column=0, padx=20, pady=20)

    def back_action(self):
        self.controller.show_view("MENU")
