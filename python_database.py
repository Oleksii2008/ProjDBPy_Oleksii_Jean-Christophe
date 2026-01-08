import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class Database:
    def __init__(self, config):
        self.config = config
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Ouvre une connexion à la base ProjDBPy."""
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
            print("✅ Connexion à MySQL réussie")

        except Error as e:
            print("Erreur de connexion à MySQL :", e)
            return None

    def get_all_dunks(self):
        """Récupère tous les types de dunks"""
        try:
            query = "SELECT id, Name FROM dunks ORDER BY Name"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Erreur récupération dunks : {e}")
            return []

    def get_all_players(self):
        """Récupère tous les types de dunks"""
        try:
            query = "SELECT * FROM players"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Erreur récupération dunks : {e}")
            return []

    def get_all_judges(self):
        """Récupère tous les types de dunks"""
        try:
            query = "SELECT * FROM judges ORDER BY lastname"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Erreur récupération dunks : {e}")
            return []

    def add_player(self, firstname, lastname, team, height, id_dunk):
        """Ajoute un joueur dans la base de données"""
        try:
            # Vérification des champs obligatoires
            if not firstname or not lastname:
                messagebox.showerror("Erreur", "Le prénom et le nom sont obligatoires !")
                return False

            # Requête SQL d'insertion
            query = """
            INSERT INTO players (firstname, lastname, team, height, id_dunk)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                firstname,
                lastname,
                team if team else None,
                height if height else None,
                id_dunk
            )

            # Exécution de la requête
            self.cursor.execute(query, values)
            self.connection.commit()

            messagebox.showinfo("Succès", f"✅ Joueur {firstname} {lastname} ajouté avec succès !")
            print(f"✅ Joueur ajouté : {firstname} {lastname}")
            return True

        except Error as e:
            messagebox.showerror("Erreur", f"❌ Erreur lors de l'ajout :\n{e}")
            print(f"❌ Erreur : {e}")
            return False

    def delete_player(self, id_player):
        """Ajoute un joueur dans la base de données"""
        try:
            # Requête SQL d'insertion
            query = "DELETE FROM players WHERE id = %s"

            # Exécution de la requête
            params = (id_player,)  # La virgule est ESSENTIELLE
            self.cursor.execute(query, params)
            self.connection.commit()

            messagebox.showinfo("Succès", "Joueur supprimé avec succès !")
            print(f"✅ Joueur ID {id_player} supprimé")
            return True


        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de la suppression : {e}")
            print(f"❌ Erreur : {e}")
            return False

    def create_contest(self, year, location, contest_date):
        """Crée un nouveau concours"""
        try:
            # Requête SQL d'insertion
            query = """
            INSERT INTO contests (year, location, contest_date)
            VALUES (%s, %s, %s)
            """

            self.cursor.execute(query, (year, location, contest_date))
            self.connection.commit()

            # Récupérer l'ID du concours créé
            id_contest = self.cursor.lastrowid
            messagebox.showinfo("Succès", f"✅ Concours créé avec l'ID {id_contest} !")
            return id_contest

        except Error as e:
            messagebox.showerror("Erreur", f"❌ Erreur : {e}")
            return None

    def add_player_to_contest(self, id_contest, id_player, position):
        """Ajoute un joueur au concours"""
        try:
            query = """
            INSERT INTO contest_players (id_contest, id_player, position)
            VALUES (%s, %s, %s)
            """
            self.cursor.execute(query, (id_contest, id_player, position))
            self.connection.commit()
            return True
        except Error as e:
            print(f"❌ Erreur : {e}")
            return False

    def add_judge_to_contest(self, id_contest, id_judge):
        """Ajoute un juge au concours"""
        try:
            query = """
            INSERT INTO contest_judges (id_contest, id_judge)
            VALUES (%s, %s)
            """
            self.cursor.execute(query, (id_contest, id_judge))
            self.connection.commit()
            return True
        except Error as e:
            print(f"❌ Erreur : {e}")
            return False

    def get_all_contests(self):
        """Récupère tous les concours"""
        try:
            query = "SELECT * FROM contests ORDER BY contest_date DESC"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Erreur : {e}")
            return []

    def get_contest_players(self, id_contest):
        """Récupère les joueurs d'un concours"""
        try:
            query = """
            SELECT p.id, p.firstname, p.lastname, cp.position
            FROM players p
            INNER JOIN contest_players cp ON p.id = cp.id_player
            WHERE cp.id_contest = %s
            ORDER BY cp.position
            """
            self.cursor.execute(query, (id_contest,))
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Erreur : {e}")
            return []

    def get_contest_judges(self, id_contest):
        """Récupère les juges d'un concours"""
        try:
            query = """
            SELECT j.id, j.firstname, j.lastname
            FROM judges j
            JOIN contest_judges cj ON j.id = cj.id_judge
            WHERE cj.id_contest = %s
            """
            self.cursor.execute(query, (id_contest,))
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Erreur : {e}")
            return []

    def close(self):
        """Ferme la connexion à MySQL"""
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection and self.connection.is_connected():
                self.connection.close()
                print("✅ Connexion MySQL fermée")
        except Error as e:
            print(f"❌ Erreur fermeture : {e}")
