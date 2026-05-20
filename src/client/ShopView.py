import time

import customtkinter as ctk
from object import Object
from View import View
from tkinter import messagebox


class ShopView(View):

    def initView(self):
        self.allobj = []
        self.buy_buttons = {}
        self.buying = None
        self.catalog_widgets = []
        self.inventory_widgets = []
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="Boutique", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        # Information about the user can't activate several object of same type
        self.info_frame = ctk.CTkFrame(
            self,
            fg_color=("#EAEAEA", "#2E2E2E"),
            border_width=1,
            border_color=("#A0A0A0", "#555555"),
        )
        self.info_frame.grid(
            row=1, column=0, columnspan=2, padx=20, pady=(0, 15), sticky="ew"
        )

        self.info_label = ctk.CTkLabel(
            self.info_frame,
            text="⚠️ Règle d'activation : Vous ne pouvez équiper qu'un seul Titre ou Badge à la fois (l'un exclut l'autre), et un seul Thème à la fois.",
            font=ctk.CTkFont(size=12, slant="italic"),
            text_color=(
                "#D32F2F",
                "#F44336",
            ),
        )
        self.info_label.pack(padx=15, pady=8)

        print("poiiiiint", self.manager.user.points)
        print()
        print()
        self.points_label = ctk.CTkLabel(
            self,
            text=f"Points disponibles :...",
            font=ctk.CTkFont(size=14),
        )
        self.points_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 10))

        self.catalog_frame = ctk.CTkScrollableFrame(self, label_text="Catalogue")
        self.catalog_frame.grid(row=3, column=0, padx=(20, 10), pady=10, sticky="nsew")
        self.catalog_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        ctk.CTkLabel(
            self.catalog_frame, text="Objet", font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(
            self.catalog_frame, text="Type", font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkLabel(
            self.catalog_frame, text="Prix", font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=2, padx=10, pady=5)
        ctk.CTkLabel(
            self.catalog_frame,
            text="",
        ).grid(row=0, column=3, padx=10, pady=5)

        self.inventory_frame = ctk.CTkScrollableFrame(self, label_text="Mes objets")
        self.inventory_frame.grid(
            row=3, column=1, padx=(10, 20), pady=10, sticky="nsew"
        )
        self.inventory_frame.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(
            self.inventory_frame, text="Objet", font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkLabel(
            self.inventory_frame, text="Type", font=ctk.CTkFont(weight="bold")
        ).grid(row=0, column=1, padx=10, pady=5)
        ctk.CTkLabel(
            self.inventory_frame,
            text="",
        ).grid(row=0, column=2, padx=10, pady=5)
        self.actif_states = {}

        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_action)
        self.back_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        self.ranking_button = ctk.CTkButton(
            self, text="L'objet le plus vendu", command=self.objranking
        )
        self.ranking_button.grid(row=4, column=1, columnspan=2, padx=20, pady=20)

    def back_action(self):
        self.controller.show_view("MENU")

    def buy_action(self, o_id, prix, nom):
        self.buying = o_id
        self.manager.buyObject(self.manager.user.idUser, o_id, prix)
        print(f"Demande d'achat envoyée pour {nom} ({prix} points)")
        print(f"Acheter {nom} pour {prix} points - test")

    def toggle_activate(self, obj_name):
        state = self.actif_states[obj_name]
        target_type = state["typ"]

        if state["actif"]:
            state["actif"] = False
            state["btn"].configure(
                text="Activer", fg_color="green", hover_color="darkgreen"
            )
            self.manager.actObject(self.manager.user.idUser, state["o_id"], 0)
            print(f"{obj_name} désactivé")
        else:
            if target_type in ["Titre", "Badge", "titre", "badge"]:
                exclusive_types = ["Titre", "Badge", "titre", "badge"]
            else:
                exclusive_types = [target_type]

            for otherName, otherState in self.actif_states.items():
                if otherState["actif"] and otherState["typ"] in exclusive_types:
                    otherState["actif"] = False
                    otherState["btn"].configure(
                        text="Activer", fg_color="green", hover_color="darkgreen"
                    )
                    self.manager.actObject(
                        self.manager.user.idUser, otherState["o_id"], 0
                    )
                    print(
                        f"Ancien objet '{otherName}' désactivé (remplacé par '{obj_name}')"
                    )

            state["actif"] = True
            state["btn"].configure(
                text="Désactiver", fg_color="gray", hover_color="darkgray"
            )
            self.manager.actObject(self.manager.user.idUser, state["o_id"], 1)
            print(f"{obj_name} activé")

    def displayStore(self, obj: dict):
        self.points_label.configure(
            text=f"Points disponibles : {self.manager.user.points}"
        )

        for widget in self.catalog_widgets:
            widget.destroy()
        self.catalog_widgets.clear()

        lbl_obj = ctk.CTkLabel(
            self.catalog_frame, text="Objet", font=ctk.CTkFont(weight="bold")
        )
        lbl_obj.grid(row=0, column=0, padx=10, pady=5)
        self.catalog_widgets.append(lbl_obj)

        lbl_type = ctk.CTkLabel(
            self.catalog_frame, text="Type", font=ctk.CTkFont(weight="bold")
        )
        lbl_type.grid(row=0, column=1, padx=10, pady=5)
        self.catalog_widgets.append(lbl_type)

        lbl_prix = ctk.CTkLabel(
            self.catalog_frame, text="Prix", font=ctk.CTkFont(weight="bold")
        )
        lbl_prix.grid(row=0, column=2, padx=10, pady=5)
        self.catalog_widgets.append(lbl_prix)

        lbl_vide = ctk.CTkLabel(self.catalog_frame, text="")
        lbl_vide.grid(row=0, column=3, padx=10, pady=5)
        self.catalog_widgets.append(lbl_vide)

        row = 1
        for elem in obj:
            name = elem.get("Nom")
            objId = elem.get("ID")
            typeObj = elem.get("TypeObjet")
            price = elem.get("Prix")
            desc = elem.get("Desc")
            obj_instance = Object(name, objId, typeObj, price, desc)
            self.allobj.append(obj_instance)

            lbl_name = ctk.CTkLabel(self.catalog_frame, text=name)
            lbl_name.grid(row=row, column=0, padx=10, pady=5)
            self.catalog_widgets.append(lbl_name)

            lbl_type_val = ctk.CTkLabel(self.catalog_frame, text=typeObj)
            lbl_type_val.grid(row=row, column=1, padx=10, pady=5)
            self.catalog_widgets.append(lbl_type_val)

            lbl_price = ctk.CTkLabel(self.catalog_frame, text=f"{price} pts")
            lbl_price.grid(row=row, column=2, padx=10, pady=5)
            self.catalog_widgets.append(lbl_price)

            btn = ctk.CTkButton(
                self.catalog_frame,
                text="Acheter",
                width=80,
                command=lambda o=objId, p=price, n=name: self.buy_action(o, p, n),
            )
            btn.grid(row=row, column=3, padx=10, pady=5)
            self.catalog_widgets.append(btn)

            self.buy_buttons[objId] = btn
            if objId in self.manager.objBought:
                btn.configure(text="Acheté", fg_color="gray", state="disabled")

            row += 1

    def buy(self, data: dict):
        if data.get("success"):
            print(f"!!!! {data.get('msg')}")
            if self.buying is not None:
                btn = self.buy_buttons.get(self.buying)
                if btn:
                    btn.configure(
                        text="Acheté",
                        fg_color="gray",
                        state="disabled",
                    )
                if self.buying not in self.manager.objBought:
                    self.manager.objBought.append(self.buying)
                self.buying = None

            self.manager.getUserObject(self.manager.user.idUser)
            self.manager.getPoints(self.manager.user.idUser)

        else:
            print(f"xxxx{data.get('msg')}xxxx")

    def showUserObject(self, data: dict):
        for widget in self.inventory_widgets:
            widget.destroy()
        self.inventory_widgets.clear()

        lbl_obj = ctk.CTkLabel(
            self.inventory_frame, text="Objet", font=ctk.CTkFont(weight="bold")
        )
        lbl_obj.grid(row=0, column=0, padx=10, pady=5)
        self.inventory_widgets.append(lbl_obj)

        lbl_type = ctk.CTkLabel(
            self.inventory_frame, text="Type", font=ctk.CTkFont(weight="bold")
        )
        lbl_type.grid(row=0, column=1, padx=10, pady=5)
        self.inventory_widgets.append(lbl_type)

        lbl_vide = ctk.CTkLabel(self.inventory_frame, text="")
        lbl_vide.grid(row=0, column=2, padx=10, pady=5)
        self.inventory_widgets.append(lbl_vide)

        row = 1
        for elem in data:
            name = elem.get("Nom")
            o_id = elem.get("ID")
            typ = elem.get("TypeObjet")
            state = elem.get("EstActif")
            print("STATETATE", state)

            lbl_name = ctk.CTkLabel(self.inventory_frame, text=name)
            lbl_name.grid(row=row, column=0, padx=10, pady=5)
            self.inventory_widgets.append(lbl_name)

            lbl_type_val = ctk.CTkLabel(self.inventory_frame, text=typ)
            lbl_type_val.grid(row=row, column=1, padx=10, pady=5)
            self.inventory_widgets.append(lbl_type_val)

            self.actif_states[name] = True if state else False

            if state:
                text = "Désactiver"
                fg_color = "gray"
                hover_color = "darkgray"
            else:
                text = "Activer"
                fg_color = "green"
                hover_color = "darkgreen"

            btn = ctk.CTkButton(
                self.inventory_frame,
                text=text,
                width=80,
                fg_color=fg_color,
                hover_color=hover_color,
                command=lambda n=name: self.toggle_activate(n),
            )
            btn.grid(row=row, column=2, padx=10, pady=5)
            self.inventory_widgets.append(btn)

            self.actif_states[name] = {
                "actif": True if state else False,
                "btn": btn,
                "typ": typ,
                "o_id": o_id,
            }
            row += 1

    def saveBoughtObject(self, data):
        print("in save Bought")
        for elem in data:
            o_id = elem.get("ID")
            if not o_id in self.manager.objBought:
                print("elem not saved", elem)
                print("appending : ", o_id)
                self.manager.objBought.append(o_id)
                print("objbought", self.manager.objBought)

    def updatePoints(self, data):
        print("updating")
        print()
        newPoints = data.get("Points")
        print("NOW USER HAVE: ", newPoints)
        if newPoints is not None:
            self.manager.user.points = newPoints
        self.points_label.configure(
            text=f"Points disponibles : {self.manager.user.points}"
        )

    def objranking(self):
        self.manager.getObRanking()

    def showRanking(self,data):

        print(type(data))
        for i in data:
            compteur = str(i.get("compteur"))
            messagebox.showinfo("Objet","L'objet le plus vendu: " + "\n" +i.get("Nom") + "\n")
