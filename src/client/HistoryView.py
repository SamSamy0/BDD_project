import customtkinter as ctk
from View import View

class HistoryView(View):
    def initView(self):
        self.label = ctk.CTkLabel(
            self, text="Historique des Transactions", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label.pack(pady=20)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=600, height=400)
        self.scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.back_button = ctk.CTkButton(
            self, text="Retour au Menu", command=self.back_action
        )
        self.back_button.pack(pady=20)

    def back_action(self):
        self.controller.show_view("MENU")

    def update_history(self, transactions: dict):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not transactions:
            no_data_label = ctk.CTkLabel(self.scrollable_frame, text="Aucune transaction trouvée.")
            no_data_label.pack(pady=20)
            return

        for trans in transactions:
            date = trans.get("Date", "Date inconnue")
            montant = trans.get("Montant", 0)
            type_trans = trans.get("TypeTransaction", "Inconnu")

            signe = "+" if montant > 0 else ""
            color = "#2ecc71" if montant > 0 else "#e74c3c"
            text_trans = f"{date}   |   {type_trans.capitalize()}   |   {signe}{montant} pts"
            trans_label = ctk.CTkLabel(
                self.scrollable_frame, 
                text=text_trans, 
                text_color=color, 
                font=ctk.CTkFont(size=14, weight="bold")
            )
            trans_label.pack(pady=10, anchor="w", padx=20)
