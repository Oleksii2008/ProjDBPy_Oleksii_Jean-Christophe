'''
Nom    : python_display.py
Auteur : Jean-Christophe Serrano, Oleksii Kamarali
Date   : 19.12.2025
'''

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Page1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Canvas pour le fond
        self.canvas = tk.Canvas(self, width=700, height=467, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Image de fond
        self.canvas.create_image(0, 0, image=master.bg_image1, anchor="nw")

        # Titre "MENU" directement sur l'image (transparent)
        self.canvas.create_text(350, 30,
                                text="MENU",
                                font=("Impact", 30, "bold"),
                                fill="white")

        # Boutons
        btn1 = tk.Button(self, text="Ajouter un joueur",
                         command=master.afficher_page2,
                         bg="green", fg="white",
                         font=("Arial", 15, "bold"),
                         padx=25, pady=10)
        self.canvas.create_window(350, 95, window=btn1)

        btn2 = tk.Button(self, text="Supprimer un joueur",
                         command=master.afficher_page3,
                         bg="red", fg="white",
                         font=("Arial", 15, "bold"),
                         padx=10, pady=10)
        self.canvas.create_window(350, 160, window=btn2)

        btn_contest = tk.Button(self, text="Créer un concours",
                         command=master.afficher_page4,
                         bg="blue", fg="white",
                         font=("Arial", 15, "bold"),
                         padx=19, pady=10)
        self.canvas.create_window(350, 225, window=btn_contest)

        btn_launch = tk.Button(self, text="Lancer un concours",
                               command=master.afficher_page5,  # ← AJOUTER CETTE LIGNE
                               bg="orange", fg="white",
                               font=("Arial", 15, "bold"),
                               padx=13, pady=10)
        self.canvas.create_window(350, 290, window=btn_launch)

class Page2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Canvas pour le fond
        self.canvas = tk.Canvas(self, width=700, height=467, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Image de fond
        self.canvas.create_image(0, 0, image=master.bg_image2, anchor="nw")

        self.canvas.create_text(350, 30,
                                text="Ajouter un joueur",
                                font=("Impact", 30, "bold"),
                                fill="white")
        btn3 = tk.Button(self, text="Retour au menu",
                         command=master.afficher_page1,
                         bg="grey",
                         fg="white",
                         font=("Arial", 12, "bold"))
        self.canvas.create_window(350, 75, window=btn3)

        self.canvas.create_text(100, 120,
                                text="Prénom du joueur :",
                                font=("Arial", 12, "bold"),
                                fill="white")
        self.txt_firstname = Entry(self, font=("Arial", 12))
        self.canvas.create_window(118, 142, window=self.txt_firstname)

        self.canvas.create_text(320, 120,
                                text="Nom du joueur :",
                                font=("Arial", 12, "bold"),
                                fill="white")
        self.txt_lastname = Entry(self, font=("Arial", 12))
        self.canvas.create_window(350, 142, window=self.txt_lastname)

        self.canvas.create_text(578, 110,
                                text=f"Nom de l'équipe \n(laisser vide si aucune) :",
                                font=("Arial", 12, "bold"),
                                fill="white")
        self.txt_team = Entry(self, font=("Arial", 12))
        self.canvas.create_window(580, 142, window=self.txt_team)

        self.canvas.create_text(120, 240,
                                text=f"Taille du joueur \n(laisser vide si inconnue) :",
                                font=("Arial", 12, "bold"),
                                fill="white")
        self.txt_height = Entry(self, font=("Arial", 12))
        self.canvas.create_window(115, 272, window=self.txt_height)

        self.canvas.create_text(545, 240,
                                text=f"Nom du Dunk :",
                                font=("Arial", 12, "bold"),
                                fill="white")

        # Récupérer les dunks depuis la base de données
        self.dunks_data = master.db.get_all_dunks()

        # Créer un dictionnaire {nom_dunk: id_dunk}
        self.dunks_dict = {name: id for id, name in self.dunks_data}

        # Liste des noms de dunks pour la Combobox
        listeDunks = ["Aucun"] + [name for id, name in self.dunks_data]

        self.liste_dunks = ttk.Combobox(self, font=("Arial", 12), values=listeDunks)
        self.canvas.create_window(590, 270, window=self.liste_dunks)

        btn4 = tk.Button(self, text="Ajouter le joueur",
                         command=self.soumettre,
                         bg="green",
                         fg="white",
                         font=("Arial", 20, "bold"))
        self.canvas.create_window(350, 350, window=btn4)

    def soumettre(self):
        """Récupère les données et les envoie à la base de données"""
        # Récupérer les valeurs des champs
        firstname = self.txt_firstname.get().strip()
        lastname = self.txt_lastname.get().strip()
        team = self.txt_team.get().strip()
        height = self.txt_height.get().strip()

        # Récupérer l'ID du dunk sélectionné
        selected_dunk = self.liste_dunks.get()
        dunk_id = None
        if selected_dunk != "Aucun":
            dunk_id = self.dunks_dict.get(selected_dunk)

        # Ajouter le joueur dans la base de données
        success = self.master.db.add_player(firstname, lastname, team, height, dunk_id)

        # Si l'ajout a réussi, vider les champs
        if success:
            self.txt_firstname.delete(0, END)
            self.txt_lastname.delete(0, END)
            self.txt_team.delete(0, END)
            self.txt_height.delete(0, END)
            self.liste_dunks.set("Aucun")

class Page3(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Canvas pour le fond
        self.canvas = tk.Canvas(self, width=700, height=467, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Image de fond
        self.canvas.create_image(0, 0, image=master.bg_image3, anchor="nw")

        self.canvas.create_text(350, 30,
                                text="Supprimer un joueur",
                                font=("Impact", 30, "bold"),
                                fill="white")
        btn5 = tk.Button(self, text="Retour au menu",
                         command=master.afficher_page1,
                         bg="grey",
                         fg="white",
                         font=("Arial", 12, "bold"))
        self.canvas.create_window(350, 75, window=btn5)

        self.canvas.create_text(115, 168,
                                text=f"Sélectionnez le \njoueur à supprimer :",
                                font=("Arial", 12, "bold"),
                                fill="white")

        # Charger les joueurs
        self.load_players()

        self.liste_players = ttk.Combobox(self, font=("Arial", 12), values=self.listePlayers)
        self.liste_players.set("Aucun")
        self.canvas.create_window(140, 200, window=self.liste_players)

        btn_delete = tk.Button(self, text="Supprimer le joueur sélectionné",
                               command=self.supprimer_joueur,
                               bg="red",
                               fg="white",
                               font=("Arial", 18, "bold"))
        self.canvas.create_window(350, 420, window=btn_delete)

        # Bouton Actualiser la liste
        btn_refresh = tk.Button(self, text="Actualiser la liste",
                                command=self.refresh,
                                bg="blue", fg="white",
                                font=("Arial", 12, "bold"),
                                padx=20, pady=8)
        self.canvas.create_window(350, 320, window=btn_refresh)

    def load_players(self):
        """Charge tous les joueurs depuis la base de données"""
        # Récupérer les données
        self.players_data = self.master.db.get_all_players()

        # Créer le dictionnaire et la liste
        self.players_dict = {}
        self.listePlayers = ["Aucun"]

        # Parcourir tous les joueurs
        for player in self.players_data:
            id_player = player[0]
            firstname = player[1]
            lastname = player[2]
            team = player[3] if len(player) > 3 else None

            # Créer le nom d'affichage
            if team:
                display_name = f"{firstname} {lastname} ({team})"
            else:
                display_name = f"{firstname} {lastname}"

            # Ajouter au dictionnaire et à la liste
            self.players_dict[display_name] = id_player
            self.listePlayers.append(display_name)

    def refresh(self):
        """Actualise la liste des joueurs"""
        # Recharger les données
        self.load_players()

        # Mettre à jour la Combobox
        self.liste_players['values'] = self.listePlayers
        self.liste_players.set("Aucun")

        messagebox.showinfo("Actualisation", "Liste des joueurs actualisée !")

    def supprimer_joueur(self):
        """Supprime le joueur sélectionné"""
        # Récupérer le joueur sélectionné
        selected_player = self.liste_players.get()

        # Vérifier qu'un joueur est sélectionné
        if selected_player == "Aucun":
            messagebox.showwarning("Attention", "Veuillez sélectionner un joueur à supprimer")
            return

        # Demander confirmation
        confirmation = messagebox.askyesno(
            "Confirmation",
            f"Êtes-vous sûr de vouloir supprimer {selected_player} ?"
        )

        if confirmation:
            # Récupérer l'ID du joueur
            player_id = self.players_dict[selected_player]

            # Supprimer de la base de données
            success = self.master.db.delete_player(player_id)

            if success:
                # Actualiser la liste
                self.refresh()

class Page4(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Canvas pour le fond
        self.canvas = tk.Canvas(self, width=700, height=467, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Image de fond
        self.canvas.create_image(0, 0, image=master.bg_image4, anchor="nw")

        self.canvas.create_text(350, 30,
                                text="Créer un concours",
                                font=("Impact", 30, "bold"),
                                fill="white")

        btn5 = tk.Button(self, text="Retour au menu",
                         command=master.afficher_page1,
                         bg="grey",
                         fg="white",
                         font=("Arial", 12, "bold"))
        self.canvas.create_window(350, 75, window=btn5)

        self.canvas.create_text(48, 130,
                                text="Année :",
                                font=("Arial", 12, "bold"),
                                fill="white")
        self.txt_year = Entry(self, font=("Arial", 12))
        self.canvas.create_window(110, 150, window=self.txt_year)

        self.canvas.create_text(290, 130,
                                text="Lieu :",
                                font=("Arial", 12, "bold"),
                                fill="white")
        self.txt_location = Entry(self, font=("Arial", 12))
        self.canvas.create_window(360, 150, window=self.txt_location)

        self.canvas.create_text(575, 130,
                                text="Date (AAAA-MM-JJ) :",
                                font=("Arial", 12, "bold"),
                                fill="white")
        self.txt_date = Entry(self, font=("Arial", 12))
        self.canvas.create_window(590, 150, window=self.txt_date)

        self.canvas.create_text(108, 200,
                                text="Sélectionner 4 joueurs :",
                                font=("Arial", 12, "bold"),
                                fill="white")

        # Récupérer les données
        self.players_data = self.master.db.get_all_players()

        # Créer le dictionnaire et la liste
        self.players_dict = {}
        self.listePlayers = []

        # 4 Combobox pour les joueurs
        self.player_combos = []
        positions = [
            (118, 240, "Joueur 1 :"),
            (118, 290, "Joueur 2 :"),
            (118, 340, "Joueur 3 :"),
            (118, 390, "Joueur 4 :")
        ]

        for player in self.players_data:
            id_player = player[0]
            firstname = player[1]
            lastname = player[2]
            team = player[3] if len(player) > 3 else None

            # Créer le nom d'affichage
            if team:
                display_name = f"{firstname} {lastname} ({team})"
            else:
                display_name = f"{firstname} {lastname}"

            self.players_dict[display_name] = id_player
            self.listePlayers.append(display_name)



        for x, y, label in positions:
            self.canvas.create_text(x, y - 20,
                                    text=label,
                                    font=("Arial", 10, "bold"),
                                    fill="white")
            combo = ttk.Combobox(self, values=self.listePlayers,
                                 font=("Arial", 9),
                                 state="readonly",
                                 width=25)
            combo.set("Sélectionner...")
            self.canvas.create_window(x, y, window=combo)
            self.player_combos.append(combo)

            self.canvas.create_text(350, 200,
                                    text="Sélectionner 2 juges :",
                                    font=("Arial", 12, "bold"),
                                    fill="white")

            # Récupérer les données
            self.judges_data = self.master.db.get_all_judges()

            # Créer le dictionnaire et la liste
            self.judges_dict = {}
            self.listeJudges = []

            for judge in self.judges_data:
                id_judge = judge[0]
                firstname = judge[1]
                lastname = judge[2]
                status = judge[3] if len(judge) > 3 else None

                # Créer le nom d'affichage
                if status:
                    display_name = f"{firstname} {lastname}"
                else:
                    display_name = f"{firstname} {lastname}"

                self.judges_dict[display_name] = id_judge
                self.listeJudges.append(display_name)

                # 2 Combobox pour les juges
            self.judge_combos = []
            judge_positions = [
                (350, 240, "Juge 1 :"),
                (350, 290, "Juge 2 :"),
            ]

            for x, y, label in judge_positions:
                self.canvas.create_text(x, y - 20,
                                        text=label,
                                        font=("Arial", 10, "bold"),
                                        fill="white")
                combo = ttk.Combobox(self, values=self.listeJudges,
                                     font=("Arial", 9),
                                     state="readonly",
                                     width=20)
                combo.set("Sélectionner...")
                self.canvas.create_window(x, y, window=combo)
                self.judge_combos.append(combo)

            btn_create = tk.Button(self, text="Créer le concours",
                                   command=self.creer_concours,
                                   bg="green", fg="white",
                                   font=("Arial", 14, "bold"),
                                   padx=20, pady=10)
            self.canvas.create_window(570, 405, window=btn_create)

    def creer_concours(self):
        """Crée le concours avec les informations saisies"""

        # Récupérer les informations
        year = self.txt_year.get().strip()
        location = self.txt_location.get().strip()
        contest_date = self.txt_date.get().strip()

        # Vérifications
        if not year or not location or not contest_date:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires !")
            return

        # Vérifier l'année
        try:
            year = int(year)
        except ValueError:
            messagebox.showerror("Erreur", "L'année doit être un nombre !")
            return

        # Récupérer les joueurs sélectionnés
        selected_players = []
        for i, combo in enumerate(self.player_combos, 1):
            player_name = combo.get()
            if player_name == "Sélectionner...":
                messagebox.showerror("Erreur", f"Veuillez sélectionner le joueur {i} !")
                return
            id_player = self.players_dict.get(player_name)
            selected_players.append((id_player, i))

        # Vérifier qu'il n'y a pas de doublons
        player_ids = [p[0] for p in selected_players]
        if len(player_ids) != len(set(player_ids)):
            messagebox.showerror("Erreur", "Vous ne pouvez pas sélectionner le même joueur plusieurs fois !")
            return

        # Récupérer les juges sélectionnés
        selected_judges = []
        for i, combo in enumerate(self.judge_combos, 1):
            judge_name = combo.get()
            if judge_name == "Sélectionner...":
                messagebox.showerror("Erreur", f"Veuillez sélectionner le juge {i} !")
                return
            id_judge = self.judges_dict.get(judge_name)
            selected_judges.append(id_judge)

        # Vérifier qu'il n'y a pas de doublons
        if len(selected_judges) != len(set(selected_judges)):
            messagebox.showerror("Erreur", "Vous ne pouvez pas sélectionner le même juge plusieurs fois !")
            return

        # Créer le concours
        id_contest = self.master.db.create_contest(year, location, contest_date)

        if id_contest:
            # Ajouter les joueurs
            for id_player, position in selected_players:
                self.master.db.add_player_to_contest(id_contest, id_player, position)

            # Ajouter les juges
            for id_judge in selected_judges:
                self.master.db.add_judge_to_contest(id_contest, id_judge)

            # Message de succès
            messagebox.showinfo("Succès",
                                f"✅ Concours créé avec succès !\n\n"
                                f"ID: {id_contest}\n"
                                f"4 joueurs et 2 juges ajoutés\n\n"
                                f"Vous pouvez maintenant lancer le concours !"
                                )

            # Vider les champs
            self.txt_year.delete(0, END)
            self.txt_location.delete(0, END)
            self.txt_date.delete(0, END)

            for combo in self.player_combos:
                combo.set("Sélectionner...")
            for combo in self.judge_combos:
                combo.set("Sélectionner...")

class Page5(tk.Frame):
    """Page 5 - Sélectionner et lancer un concours"""

    def __init__(self, master):
        super().__init__(master)

        # Canvas pour le fond
        self.canvas = tk.Canvas(self, width=700, height=467, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Image de fond
        self.canvas.create_image(0, 0, image=master.bg_image2, anchor="nw")

        # Titre
        self.canvas.create_text(350, 25,
                                text="Gérer un concours",
                                font=("Impact", 28, "bold"),
                                fill="white")

        # Bouton retour
        btn_retour = tk.Button(self, text="Retour au menu",
                               command=master.afficher_page1,
                               bg="grey", fg="white",
                               font=("Arial", 12, "bold"))
        self.canvas.create_window(90, 30, window=btn_retour)

        # Label instruction
        self.canvas.create_text(350, 70,
                                text="Sélectionnez un concours à lancer :",
                                font=("Arial", 13, "bold"),
                                fill="white")

        # Charger les concours
        self.load_contests()

        # Combobox pour sélectionner un concours
        self.combo_contests = ttk.Combobox(self,
                                           values=self.contest_names,
                                           font=("Arial", 12),
                                           state="readonly",
                                           width=50)
        self.combo_contests.set("Sélectionner un concours...")
        self.canvas.create_window(350, 110, window=self.combo_contests)

        # Bind pour afficher les détails quand on sélectionne
        self.combo_contests.bind("<<ComboboxSelected>>", self.afficher_details)

        # Zone d'affichage des détails
        self.details_frame = tk.Frame(self, bg="white", relief="solid", bd=2)
        self.canvas.create_window(350, 265, window=self.details_frame, width=650, height=265)

        # Label pour les détails (sera mis à jour)
        self.lbl_details = tk.Label(self.details_frame,
                                    text="Sélectionnez un concours pour voir les détails",
                                    font=("Arial", 11),
                                    bg="white",
                                    justify="left")
        self.lbl_details.pack(pady=20, padx=20)

        # Bouton lancer le concours
        self.btn_lancer = tk.Button(self, text="LANCER LE CONCOURS",
                                    command=self.lancer_concours,
                                    bg="green", fg="white",
                                    font=("Arial", 16, "bold"),
                                    padx=20, pady=10,
                                    state="disabled")
        self.canvas.create_window(350, 430, window=self.btn_lancer)

    def load_contests(self):
        """Charge tous les concours depuis la base de données"""
        contests = self.master.db.get_all_contests()

        self.contests_dict = {}
        self.contest_names = []

        for contest in contests:
            id_contest = contest[0]
            name = contest[1] if len(contest) > 1 else f"Concours {id_contest}"
            year = contest[2] if len(contest) > 2 else ""
            location = contest[3] if len(contest) > 3 else ""

            display_name = f"{name} - {location} {year}"
            self.contests_dict[display_name] = id_contest
            self.contest_names.append(display_name)

    def afficher_details(self, event=None):
        """Affiche les détails du concours sélectionné"""
        selected = self.combo_contests.get()

        if selected == "Sélectionner un concours...":
            return

        id_contest = self.contests_dict[selected]

        # Récupérer les joueurs
        players = self.master.db.get_contest_players(id_contest)

        # Récupérer les juges
        judges = self.master.db.get_contest_judges(id_contest)

        # Construire le texte des détails
        details = f"DÉTAILS DU CONCOURS\n\n"

        details += f"JOUEURS ({len(players)}/4) :\n"
        if players:
            for player in players:
                id_player, firstname, lastname, position = player
                details += f"   {position}. {firstname} {lastname}\n"
        else:
            details += "   Aucun joueur inscrit\n"

        details += f"\nJUGES ({len(judges)}/2) :\n"
        if judges:
            for judge in judges:
                id_judge, firstname, lastname = judge
                details += f"   • {firstname} {lastname}\n"
        else:
            details += "   Aucun juge assigné\n"

        # Vérifier si le concours peut être lancé
        if len(players) == 4 and len(judges) == 2:
            details += f"\n✅ Le concours est prêt à être lancé !"
            self.btn_lancer.config(state="normal")
            self.selected_contest_id = id_contest
        else:
            details += f"\n⚠️ Impossible de lancer :"
            if len(players) != 4:
                details += f"\n   - Il faut exactement 4 joueurs (vous en avez {len(players)})"
            if len(judges) != 2:
                details += f"\n   - Il faut exactement 2 juges (vous en avez {len(judges)})"
            self.btn_lancer.config(state="disabled")

        self.lbl_details.config(text=details)

    def lancer_concours(self):
        """Lance le concours sélectionné"""
        if not hasattr(self, 'selected_contest_id'):
            return

        confirmation = messagebox.askyesno(
            "Confirmation",
            "Êtes-vous prêt à lancer ce concours ?\n\n"
            "Le Round 1 (Demi-finales) va commencer.\n"
            "4 joueurs × 2 essais chacun."
        )

        if confirmation:
            # Stocker l'ID du concours actif
            self.master.current_contest_id = self.selected_contest_id

            # Aller à la page du Round 1
            self.master.afficher_page6()

class Page6(tk.Frame):
    """Page 6 - Round 1 (Demi-finales)"""

    def __init__(self, master):
        super().__init__(master)

        self.current_player_index = 0
        self.current_attempt = 1

        # Canvas pour le fond
        self.canvas = tk.Canvas(self, width=700, height=467, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Image de fond
        self.canvas.create_image(0, 0, image=master.bg_image5, anchor="nw")

        # Titre
        self.title_text = self.canvas.create_text(350, 30,
                                                  text="ROUND 1 - DEMI-FINALES",
                                                  font=("Impact", 26, "bold"),
                                                  fill="white")

        # Informations joueur actuel
        self.lbl_player = tk.Label(self,
                                   text="rsh",
                                   font=("Arial", 18, "bold"),
                                   bg="#1a1a1a", fg="orange",
                                   padx=20, pady=10)
        self.canvas.create_window(350, 80, window=self.lbl_player)

        # Numéro d'essai
        self.lbl_attempt = tk.Label(self,
                                    text="rsth",
                                    font=("Arial", 14, "bold"),
                                    bg="#1a1a1a", fg="white")
        self.canvas.create_window(350, 120, window=self.lbl_attempt)

        # Sélection du type de dunk
        self.canvas.create_text(350, 160,
                                text="Type de dunk effectué :",
                                font=("Arial", 12, "bold"),
                                fill="white")

        # Charger les dunks
        dunks_data = master.db.get_all_dunks()
        self.dunks_dict = {name: id for id, name in dunks_data}
        dunk_names = [name for id, name in dunks_data]

        self.combo_dunk = ttk.Combobox(self,
                                       values=dunk_names,
                                       font=("Arial", 11),
                                       state="readonly",
                                       width=30)
        self.combo_dunk.set("Sélectionner un dunk...")
        self.canvas.create_window(350, 190, window=self.combo_dunk)

        # Notes des juges
        self.canvas.create_text(350, 230,
                                text="NOTES DES JUGES",
                                font=("Arial", 14, "bold"),
                                fill="orange")

        # Juge 1
        self.lbl_judge1 = tk.Label(self, text="Juge 1 :",
                                   font=("Arial", 11, "bold"),
                                   bg="#1a1a1a", fg="white")
        self.canvas.create_window(200, 270, window=self.lbl_judge1)

        self.spin_score1 = tk.Spinbox(self, from_=0, to=10, increment=0.5,
                                      font=("Arial", 14, "bold"),
                                      width=6)
        self.spin_score1.delete(0, END)
        self.spin_score1.insert(0, "0.0")
        self.canvas.create_window(300, 270, window=self.spin_score1)

        # Juge 2
        self.lbl_judge2 = tk.Label(self, text="Juge 2 :",
                                   font=("Arial", 11, "bold"),
                                   bg="#1a1a1a", fg="white")
        self.canvas.create_window(400, 270, window=self.lbl_judge2)

        self.spin_score2 = tk.Spinbox(self, from_=0, to=10, increment=0.5,
                                      font=("Arial", 14, "bold"),
                                      width=6)
        self.spin_score2.delete(0, END)
        self.spin_score2.insert(0, "0.0")
        self.canvas.create_window(500, 270, window=self.spin_score2)

        # Moyenne
        self.lbl_average = tk.Label(self,
                                    text="Moyenne : 0.0",
                                    font=("Arial", 16, "bold"),
                                    bg="#1a1a1a", fg="yellow")
        self.canvas.create_window(350, 320, window=self.lbl_average)

        # Bouton calculer moyenne
        btn_calc = tk.Button(self, text="Calculer la moyenne",
                             command=self.calculer_moyenne,
                             bg="blue", fg="white",
                             font=("Arial", 11, "bold"))
        self.canvas.create_window(350, 360, window=btn_calc)

        # Bouton valider l'essai
        self.btn_valider = tk.Button(self, text="✅ VALIDER CET ESSAI",
                                     command=self.valider_essai,
                                     bg="green", fg="white",
                                     font=("Arial", 14, "bold"),
                                     padx=30, pady=10)
        self.canvas.create_window(350, 415, window=self.btn_valider)

        # Progression
        self.lbl_progress = tk.Label(self,
                                     text="",
                                     font=("Arial", 10),
                                     bg="#1a1a1a", fg="lightgray")
        self.canvas.create_window(350, 450, window=self.lbl_progress)

    def refresh_display(self):
        """Met à jour l'affichage pour le joueur et l'essai courant"""
        if not hasattr(self.master, 'current_contest_id'):
            messagebox.showerror("Erreur", "Aucun concours sélectionné")
            self.master.afficher_page5()
            return

        # Charger les joueurs et juges
        if not hasattr(self, 'players'):
            self.players = self.master.db.get_contest_players(self.master.current_contest_id)
            self.judges = self.master.db.get_contest_judges(self.master.current_contest_id)

            if len(self.players) != 4 or len(self.judges) != 2:
                messagebox.showerror("Erreur", "Le concours n'est pas correctement configuré")
                self.master.afficher_page5()
                return

        # Joueur actuel
        player = self.players[self.current_player_index]
        player_id, firstname, lastname, position = player

        self.lbl_player.config(text=f"{firstname} {lastname}")
        self.lbl_attempt.config(text=f"Essai {self.current_attempt}/2")

        # Afficher les noms des juges
        judge1 = self.judges[0]
        judge2 = self.judges[1]
        self.lbl_judge1.config(text=f"{judge1[1]} {judge1[2]} :")
        self.lbl_judge2.config(text=f"{judge2[1]} {judge2[2]} :")

        # Progression
        total_attempts = 4 * 2  # 4 joueurs × 2 essais
        current = self.current_player_index * 2 + self.current_attempt
        self.lbl_progress.config(text=f"Progression : {current}/{total_attempts} essais")

        # Réinitialiser les champs
        self.combo_dunk.set("Sélectionner un dunk...")
        self.spin_score1.delete(0, END)
        self.spin_score1.insert(0, "0.0")
        self.spin_score2.delete(0, END)
        self.spin_score2.insert(0, "0.0")
        self.lbl_average.config(text="Moyenne : 0.0")

    def calculer_moyenne(self):
        """Calcule et affiche la moyenne des deux notes"""
        try:
            score1 = float(self.spin_score1.get())
            score2 = float(self.spin_score2.get())

            if score1 < 0 or score1 > 10 or score2 < 0 or score2 > 10:
                messagebox.showerror("Erreur", "Les notes doivent être entre 0 et 10")
                return

            average = (score1 + score2) / 2
            self.lbl_average.config(text=f"Moyenne : {average:.1f}")

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des notes valides")

    def valider_essai(self):
        """Valide l'essai et enregistre dans la base de données"""
        # Vérifications
        selected_dunk = self.combo_dunk.get()
        if selected_dunk == "Sélectionner un dunk...":
            messagebox.showwarning("Attention", "Veuillez sélectionner un type de dunk")
            return

        try:
            score1 = float(self.spin_score1.get())
            score2 = float(self.spin_score2.get())

            if score1 < 0 or score1 > 10 or score2 < 0 or score2 > 10:
                messagebox.showerror("Erreur", "Les notes doivent être entre 0 et 10")
                return

            average = (score1 + score2) / 2

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des notes valides")
            return

        # Récupérer les infos
        player = self.players[self.current_player_index]
        player_id = player[0]
        dunk_id = self.dunks_dict[selected_dunk]

        # Enregistrer l'essai
        attempt_id = self.master.db.add_attempt(
            self.master.current_contest_id,
            player_id,
            1,  # Round 1
            self.current_attempt,
            dunk_id,
            average
        )

        if attempt_id:
            # Enregistrer les notes des juges
            judge1_id = self.judges[0][0]
            judge2_id = self.judges[1][0]

            self.master.db.add_score(attempt_id, judge1_id, score1)
            self.master.db.add_score(attempt_id, judge2_id, score2)

            messagebox.showinfo("✅ Validé", f"Essai enregistré !\nMoyenne : {average:.1f}/10")

            # Passer au suivant
            self.next_attempt()

    def next_attempt(self):
        """Passe au prochain essai ou joueur"""
        if self.current_attempt == 1:
            # Passer au 2ème essai du même joueur
            self.current_attempt = 2
            self.refresh_display()
        else:
            # Passer au joueur suivant
            self.current_attempt = 1
            self.current_player_index += 1

            if self.current_player_index >= 4:
                # Round 1 terminé, calculer les qualifiés
                self.terminer_round1()
            else:
                self.refresh_display()

    def terminer_round1(self):
        """Termine le Round 1 et sélectionne les 2 finalistes"""
        messagebox.showinfo("🎉 Round 1 terminé !",
                            "Calcul des résultats en cours...")

        # Calculer les moyennes totales de chaque joueur
        results = self.master.db.get_round1_results(self.master.current_contest_id)

        # results = [(player_id, firstname, lastname, average_total), ...]
        if len(results) >= 2:
            # Les 2 meilleurs
            finalist1 = results[0]
            finalist2 = results[1]

            # Mettre à jour qualified_for_final
            self.master.db.qualify_player(self.master.current_contest_id, finalist1[0])
            self.master.db.qualify_player(self.master.current_contest_id, finalist2[0])

            messagebox.showinfo("🏆 FINALISTES",
                                f"Les 2 finalistes sont :\n\n"
                                f"1️⃣ {finalist1[1]} {finalist1[2]} - {finalist1[3]:.2f}/10\n"
                                f"2️⃣ {finalist2[1]} {finalist2[2]} - {finalist2[3]:.2f}/10\n\n"
                                f"Prêt pour la FINALE ?")

            # Aller au Round 2
            self.master.afficher_page7()
        else:
            messagebox.showerror("Erreur", "Impossible de calculer les résultats")


class Page7(tk.Frame):
    """Page 7 - Round 2 (Finale)"""

    def __init__(self, master):
        super().__init__(master)

        self.current_player_index = 0
        self.current_attempt = 1

        # Canvas pour le fond
        self.canvas = tk.Canvas(self, width=700, height=467, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Image de fond
        self.canvas.create_image(0, 0, image=master.bg_image3, anchor="nw")

        # Titre
        self.canvas.create_text(350, 30,
                                text="🏆 FINALE - ROUND 2 🏆",
                                font=("Impact", 26, "bold"),
                                fill="gold")

        # Informations joueur actuel
        self.lbl_player = tk.Label(self,
                                   text="",
                                   font=("Arial", 18, "bold"),
                                   bg="#1a1a1a", fg="gold",
                                   padx=20, pady=10)
        self.canvas.create_window(350, 80, window=self.lbl_player)

        # Numéro d'essai
        self.lbl_attempt = tk.Label(self,
                                    text="",
                                    font=("Arial", 14, "bold"),
                                    bg="#1a1a1a", fg="white")
        self.canvas.create_window(350, 120, window=self.lbl_attempt)

        # Sélection du type de dunk
        self.canvas.create_text(350, 160,
                                text="Type de dunk effectué :",
                                font=("Arial", 12, "bold"),
                                fill="white")

        # Charger les dunks
        dunks_data = master.db.get_all_dunks()
        self.dunks_dict = {name: id for id, name in dunks_data}
        dunk_names = [name for id, name in dunks_data]

        self.combo_dunk = ttk.Combobox(self,
                                       values=dunk_names,
                                       font=("Arial", 11),
                                       state="readonly",
                                       width=30)
        self.combo_dunk.set("Sélectionner un dunk...")
        self.canvas.create_window(350, 190, window=self.combo_dunk)

        # Notes des juges
        self.canvas.create_text(350, 230,
                                text="NOTES DES JUGES",
                                font=("Arial", 14, "bold"),
                                fill="gold")

        # Juge 1
        self.lbl_judge1 = tk.Label(self, text="Juge 1 :",
                                   font=("Arial", 11, "bold"),
                                   bg="#1a1a1a", fg="white")
        self.canvas.create_window(200, 270, window=self.lbl_judge1)

        self.spin_score1 = tk.Spinbox(self, from_=0, to=10, increment=0.5,
                                      font=("Arial", 14, "bold"),
                                      width=6)
        self.spin_score1.delete(0, END)
        self.spin_score1.insert(0, "0.0")
        self.canvas.create_window(300, 270, window=self.spin_score1)

        # Juge 2
        self.lbl_judge2 = tk.Label(self, text="Juge 2 :",
                                   font=("Arial", 11, "bold"),
                                   bg="#1a1a1a", fg="white")
        self.canvas.create_window(400, 270, window=self.lbl_judge2)

        self.spin_score2 = tk.Spinbox(self, from_=0, to=10, increment=0.5,
                                      font=("Arial", 14, "bold"),
                                      width=6)
        self.spin_score2.delete(0, END)
        self.spin_score2.insert(0, "0.0")
        self.canvas.create_window(500, 270, window=self.spin_score2)

        # Moyenne
        self.lbl_average = tk.Label(self,
                                    text="Moyenne : 0.0",
                                    font=("Arial", 16, "bold"),
                                    bg="#1a1a1a", fg="yellow")
        self.canvas.create_window(350, 320, window=self.lbl_average)

        # Bouton calculer moyenne
        btn_calc = tk.Button(self, text="Calculer la moyenne",
                             command=self.calculer_moyenne,
                             bg="blue", fg="white",
                             font=("Arial", 11, "bold"))
        self.canvas.create_window(350, 360, window=btn_calc)

        # Bouton valider l'essai
        self.btn_valider = tk.Button(self, text="✅ VALIDER CET ESSAI",
                                     command=self.valider_essai,
                                     bg="green", fg="white",
                                     font=("Arial", 14, "bold"),
                                     padx=30, pady=10)
        self.canvas.create_window(350, 415, window=self.btn_valider)

        # Progression
        self.lbl_progress = tk.Label(self,
                                     text="",
                                     font=("Arial", 10),
                                     bg="#1a1a1a", fg="lightgray")
        self.canvas.create_window(350, 450, window=self.lbl_progress)

    def refresh_display(self):
        """Met à jour l'affichage pour le joueur et l'essai courant"""
        print("🔍 Page7 - refresh_display() appelé")

        if not hasattr(self.master, 'current_contest_id'):
            print("❌ Pas de current_contest_id")
            messagebox.showerror("Erreur", "Aucun concours sélectionné")
            self.master.afficher_page5()
            return

        print(f"✅ Contest ID: {self.master.current_contest_id}")

        # Charger les finalistes et juges
        if not hasattr(self, 'finalists'):
            print("📥 Chargement des finalistes...")
            self.finalists = self.master.db.get_finalists(self.master.current_contest_id)
            self.judges = self.master.db.get_contest_judges(self.master.current_contest_id)

            print(f"✅ {len(self.finalists)} finalistes chargés")
            print(f"✅ {len(self.judges)} juges chargés")

            if len(self.finalists) != 2:
                print(f"❌ Nombre de finalistes invalide: {len(self.finalists)}")
                messagebox.showerror("Erreur",
                                     f"Il faut exactement 2 finalistes.\n"
                                     f"Actuellement : {len(self.finalists)} finaliste(s).\n\n"
                                     f"Le Round 1 n'a peut-être pas été terminé correctement.")
                self.master.afficher_page5()
                return

            if len(self.judges) != 2:
                print(f"❌ Nombre de juges invalide: {len(self.judges)}")
                messagebox.showerror("Erreur", "Le concours doit avoir exactement 2 juges")
                self.master.afficher_page5()
                return

        # Joueur actuel (finaliste)
        player = self.finalists[self.current_player_index]
        player_id, firstname, lastname = player[:3]

        print(f"👤 Finaliste actuel: {firstname} {lastname}")
        print(f"📝 Essai: {self.current_attempt}/2")

        self.lbl_player.config(text=f"🏀 {firstname} {lastname}")
        self.lbl_attempt.config(text=f"Essai {self.current_attempt}/2")

        # Afficher les noms des juges
        judge1 = self.judges[0]
        judge2 = self.judges[1]

        print(f"👨‍⚖️ Juge 1: {judge1[1]} {judge1[2]}")
        print(f"👨‍⚖️ Juge 2: {judge2[1]} {judge2[2]}")

        self.lbl_judge1.config(text=f"{judge1[1]} {judge1[2]} :")
        self.lbl_judge2.config(text=f"{judge2[1]} {judge2[2]} :")

        # Progression
        total_attempts = 2 * 2  # 2 finalistes × 2 essais
        current = self.current_player_index * 2 + self.current_attempt
        self.lbl_progress.config(text=f"🏆 Finale : {current}/{total_attempts} essais")

        # Réinitialiser les champs
        self.combo_dunk.set("Sélectionner un dunk...")
        self.spin_score1.delete(0, END)
        self.spin_score1.insert(0, "0.0")
        self.spin_score2.delete(0, END)
        self.spin_score2.insert(0, "0.0")
        self.lbl_average.config(text="Moyenne : 0.0")

        print("✅ Affichage mis à jour")

    def calculer_moyenne(self):
        """Calcule et affiche la moyenne des deux notes"""
        try:
            score1 = float(self.spin_score1.get())
            score2 = float(self.spin_score2.get())

            if score1 < 0 or score1 > 10 or score2 < 0 or score2 > 10:
                messagebox.showerror("Erreur", "Les notes doivent être entre 0 et 10")
                return

            average = (score1 + score2) / 2
            self.lbl_average.config(text=f"Moyenne : {average:.1f}")

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des notes valides")

    def valider_essai(self):
        """Valide l'essai et enregistre dans la base de données"""
        print("🔍 Validation de l'essai...")

        # Vérifications
        selected_dunk = self.combo_dunk.get()
        if selected_dunk == "Sélectionner un dunk...":
            messagebox.showwarning("Attention", "Veuillez sélectionner un type de dunk")
            return

        try:
            score1 = float(self.spin_score1.get())
            score2 = float(self.spin_score2.get())

            if score1 < 0 or score1 > 10 or score2 < 0 or score2 > 10:
                messagebox.showerror("Erreur", "Les notes doivent être entre 0 et 10")
                return

            average = (score1 + score2) / 2

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des notes valides")
            return

        # Récupérer les infos
        player = self.finalists[self.current_player_index]
        player_id = player[0]
        dunk_id = self.dunks_dict[selected_dunk]

        print(f"💾 Enregistrement: Player {player_id}, Round 2, Essai {self.current_attempt}")

        # Enregistrer l'essai
        attempt_id = self.master.db.add_attempt(
            self.master.current_contest_id,
            player_id,
            2,  # Round 2 (Finale)
            self.current_attempt,
            dunk_id,
            average
        )

        if attempt_id:
            print(f"✅ Essai enregistré avec ID: {attempt_id}")

            # Enregistrer les notes des juges
            judge1_id = self.judges[0][0]
            judge2_id = self.judges[1][0]

            self.master.db.add_score(attempt_id, judge1_id, score1)
            self.master.db.add_score(attempt_id, judge2_id, score2)

            print(f"✅ Notes enregistrées: {score1} et {score2}")

            messagebox.showinfo("✅ Validé", f"Essai enregistré !\nMoyenne : {average:.1f}/10")

            # Passer au suivant
            self.next_attempt()
        else:
            print("❌ Échec de l'enregistrement de l'essai")

    def next_attempt(self):
        """Passe au prochain essai ou joueur"""
        print(f"🔄 next_attempt() - Player {self.current_player_index}, Attempt {self.current_attempt}")

        if self.current_attempt == 1:
            # Passer au 2ème essai du même finaliste
            self.current_attempt = 2
            print("➡️ Passage à l'essai 2 du même joueur")
            self.refresh_display()
        else:
            # Passer au finaliste suivant
            self.current_attempt = 1
            self.current_player_index += 1

            print(f"➡️ Passage au joueur suivant (index: {self.current_player_index})")

            if self.current_player_index >= 2:
                # Round 2 terminé, calculer le gagnant
                print("🎉 Finale terminée ! Calcul du gagnant...")
                self.terminer_finale()
            else:
                self.refresh_display()

    def terminer_finale(self):
        """Termine la finale et détermine le gagnant"""
        print("🏆 Calcul des résultats finaux...")

        messagebox.showinfo("🎉 Finale terminée !",
                            "Calcul du classement final en cours...")

        # Calculer les moyennes finales
        results = self.master.db.get_round2_results(self.master.current_contest_id)

        print(f"📊 Résultats Round 2: {results}")

        if len(results) >= 2:
            # Le gagnant et le second
            winner = results[0]
            second = results[1]

            print(f"🥇 Gagnant: {winner[1]} {winner[2]} - {winner[3]:.2f}")
            print(f"🥈 Second: {second[1]} {second[2]} - {second[3]:.2f}")

            # Mettre à jour les classements finaux
            self.master.db.set_final_ranks(self.master.current_contest_id, winner[0], 1)
            self.master.db.set_final_ranks(self.master.current_contest_id, second[0], 2)

            # Récupérer les 2 autres joueurs (éliminés en demi)
            all_players = self.master.db.get_contest_players(self.master.current_contest_id)
            round1_results = self.master.db.get_round1_results(self.master.current_contest_id)

            # Trouver les 2 éliminés et leur assigner les rangs 3 et 4
            rank = 3
            for player in round1_results:
                player_id = player[0]
                # Si le joueur n'est pas dans les 2 premiers
                if player_id not in [winner[0], second[0]]:
                    self.master.db.set_final_ranks(self.master.current_contest_id, player_id, rank)
                    rank += 1

            # Afficher le podium
            self.afficher_podium(winner, second, round1_results)

        else:
            print("❌ Impossible de calculer les résultats")
            messagebox.showerror("Erreur", "Impossible de calculer les résultats de la finale")

    def afficher_podium(self, winner, second, all_results):
        """Affiche le podium final"""

        # Trouver les 3ème et 4ème
        third = None
        fourth = None

        for player in all_results:
            player_id = player[0]
            if player_id not in [winner[0], second[0]]:
                if third is None:
                    third = player
                else:
                    fourth = player

        # Message du podium
        podium_msg = "🏆 CLASSEMENT FINAL 🏆\n\n"
        podium_msg += f"🥇 1ER : {winner[1]} {winner[2]}\n"
        podium_msg += f"   Moyenne finale : {winner[3]:.2f}/10\n\n"

        podium_msg += f"🥈 2ÈME : {second[1]} {second[2]}\n"
        podium_msg += f"   Moyenne finale : {second[3]:.2f}/10\n\n"

        if third:
            podium_msg += f"🥉 3ÈME : {third[1]} {third[2]}\n"
            podium_msg += f"   Moyenne Round 1 : {third[3]:.2f}/10\n\n"

        if fourth:
            podium_msg += f"4ÈME : {fourth[1]} {fourth[2]}\n"
            podium_msg += f"   Moyenne Round 1 : {fourth[3]:.2f}/10\n\n"

        podium_msg += f"\n🎊 Félicitations à {winner[1]} {winner[2]} ! 🎊"

        # Afficher le podium
        result = messagebox.askquestion("🏆 CONCOURS TERMINÉ",
                                        podium_msg + "\n\nRetourner au menu principal ?",
                                        icon='info')

        if result == 'yes':
            # Réinitialiser la page
            if hasattr(self, 'finalists'):
                delattr(self, 'finalists')
            if hasattr(self, 'judges'):
                delattr(self, 'judges')

            self.current_player_index = 0
            self.current_attempt = 1

            # Retourner au menu
            self.master.afficher_page1()
        else:
            # Rester sur cette page (afficher les stats ?)
            messagebox.showinfo("Statistiques",
                                "Fonctionnalité à venir :\n"
                                "- Voir tous les essais\n"
                                "- Meilleur dunk du concours\n"
                                "- Export des résultats")
            self.master.afficher_page1()
