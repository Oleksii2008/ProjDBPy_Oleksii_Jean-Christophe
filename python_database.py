'''
Nom    : python_database.py
Auteur : Jean-Christophe Serrano, Oleksii Kamarali
Date   : 19.12.2025
'''

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

    def add_attempt(self, contest_id, player_id, round_number, attempt_number, dunk_id, average_score):
        """Enregistre un essai de dunk"""
        try:
            query = """
                    INSERT INTO attempts (id_contest, id_player, Round_number, Attempt_number, id_dunk, Average_score)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
            values = (contest_id, player_id, round_number, attempt_number, dunk_id, average_score)

            self.cursor.execute(query, values)
            self.connection.commit()

            # Retourner l'ID de l'essai créé
            return self.cursor.lastrowid

        except Error as e:
            print(f"❌ Erreur add_attempt : {e}")
            messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement de l'essai : {e}")
            return None

    def add_score(self, attempt_id, judge_id, score):
        """Enregistre la note d'un juge pour un essai"""
        try:
            query = """
                    INSERT INTO scores (id_attempt, id_judge, Score)
                    VALUES (%s, %s, %s)
                    """
            values = (attempt_id, judge_id, score)

            self.cursor.execute(query, values)
            self.connection.commit()

            return True

        except Error as e:
            print(f"❌ Erreur add_score : {e}")
            return False

    def get_round1_results(self, contest_id):
        """Calcule les résultats du Round 1 et retourne les joueurs triés par moyenne"""
        try:
            query = """
                    SELECT p.id,
                           p.Firstname,
                           p.Lastname,
                           AVG(a.Average_score) as total_average
                    FROM Players p
                             JOIN attempts a ON p.id = a.id_player
                    WHERE a.id_contest = %s
                      AND a.Round_number = 1
                    GROUP BY p.id, p.Firstname, p.Lastname
                    ORDER BY total_average DESC
                    """

            self.cursor.execute(query, (contest_id,))
            results = self.cursor.fetchall()

            return results

        except Error as e:
            print(f"❌ Erreur get_round1_results : {e}")
            return []

    def get_round1_results(self, contest_id):
        """Calcule les résultats du Round 1 et retourne les joueurs triés par moyenne"""
        try:
            query = """
            SELECT 
                p.id,
                p.Firstname,
                p.Lastname,
                AVG(a.Average_score) as total_average
            FROM Players p
            JOIN attempts a ON p.id = a.id_player
            WHERE a.id_contest = %s AND a.Round_number = 1
            GROUP BY p.id, p.Firstname, p.Lastname
            ORDER BY total_average DESC
            """

            self.cursor.execute(query, (contest_id,))
            results = self.cursor.fetchall()

            return results

        except Error as e:
            print(f"❌ Erreur get_round1_results : {e}")
            return []

    def qualify_player(self, contest_id, player_id):
        """Marque un joueur comme qualifié pour la finale"""
        try:
            query = """
            UPDATE contest_players 
            SET Qualified_for_final = TRUE
            WHERE id_contest = %s AND id_player = %s
            """

            self.cursor.execute(query, (contest_id, player_id))
            self.connection.commit()

            return True

        except Error as e:
            print(f"❌ Erreur qualify_player : {e}")
            return False

    def get_finalists(self, contest_id):
        """Récupère les 2 joueurs qualifiés pour la finale"""
        try:
            query = """
            SELECT p.id, p.Firstname, p.Lastname
            FROM Players p
            JOIN contest_players cp ON p.id = cp.id_player
            WHERE cp.id_contest = %s AND cp.Qualified_for_final = TRUE
            ORDER BY cp.Position
            """

            self.cursor.execute(query, (contest_id,))
            return self.cursor.fetchall()

        except Error as e:
            print(f"❌ Erreur get_finalists : {e}")
            return []

    def get_round2_results(self, contest_id):
        """Calcule les résultats du Round 2 (Finale)"""
        try:
            query = """
            SELECT 
                p.id,
                p.Firstname,
                p.Lastname,
                AVG(a.Average_score) as final_average
            FROM Players p
            JOIN attempts a ON p.id = a.id_player
            WHERE a.id_contest = %s AND a.Round_number = 2
            GROUP BY p.id, p.Firstname, p.Lastname
            ORDER BY final_average DESC
            """

            self.cursor.execute(query, (contest_id,))
            return self.cursor.fetchall()

        except Error as e:
            print(f"❌ Erreur get_round2_results : {e}")
            return []

    def set_final_ranks(self, contest_id, player_id, rank):
        """Définit le classement final d'un joueur"""
        try:
            query = """
            UPDATE contest_players 
            SET Final_rank = %s
            WHERE id_contest = %s AND id_player = %s
            """

            self.cursor.execute(query, (rank, contest_id, player_id))
            self.connection.commit()

            return True

        except Error as e:
            print(f"❌ Erreur set_final_ranks : {e}")
            return False

    def get_contest_summary(self, contest_id):
        """Récupère un résumé complet du concours"""
        try:
            # Informations générales du concours
            query_contest = """
            SELECT id, Year, Location, Contest_date
            FROM contests
            WHERE id = %s
            """
            self.cursor.execute(query_contest, (contest_id,))
            contest_info = self.cursor.fetchone()

            # Classement final
            query_ranking = """
            SELECT 
                p.Firstname,
                p.Lastname,
                cp.Final_rank,
                cp.Qualified_for_final
            FROM Players p
            JOIN contest_players cp ON p.id = cp.id_player
            WHERE cp.id_contest = %s
            ORDER BY cp.Final_rank
            """
            self.cursor.execute(query_ranking, (contest_id,))
            ranking = self.cursor.fetchall()

            return {
                'contest_info': contest_info,
                'ranking': ranking
            }

        except Error as e:
            print(f"❌ Erreur get_contest_summary : {e}")
            return None

    def update_contest_status(self, contest_id, status):
        """Met à jour le statut d'un concours"""
        try:
            query = """
            UPDATE contests 
            SET status = %s
            WHERE id = %s
            """

            self.cursor.execute(query, (status, contest_id))
            self.connection.commit()

            return True

        except Error as e:
            print(f"❌ Erreur update_contest_status : {e}")
            return False

    def get_all_attempts(self, contest_id):
        """Récupère tous les essais d'un concours"""
        try:
            query = """
            SELECT 
                a.id,
                p.Firstname,
                p.Lastname,
                a.Round_number,
                a.Attempt_number,
                d.Name as dunk_name,
                a.Average_score
            FROM attempts a
            JOIN Players p ON a.id_player = p.id
            LEFT JOIN Dunks d ON a.id_dunk = d.id
            WHERE a.id_contest = %s
            ORDER BY a.Round_number, a.id_player, a.Attempt_number
            """

            self.cursor.execute(query, (contest_id,))
            return self.cursor.fetchall()

        except Error as e:
            print(f"❌ Erreur get_all_attempts : {e}")
            return []

    def get_player_attempts(self, contest_id, player_id):
        """Récupère tous les essais d'un joueur dans un concours"""
        try:
            query = """
            SELECT 
                a.Round_number,
                a.Attempt_number,
                d.Name as dunk_name,
                a.Average_score
            FROM attempts a
            LEFT JOIN Dunks d ON a.id_dunk = d.id
            WHERE a.id_contest = %s AND a.id_player = %s
            ORDER BY a.Round_number, a.Attempt_number
            """

            self.cursor.execute(query, (contest_id, player_id))
            return self.cursor.fetchall()

        except Error as e:
            print(f"❌ Erreur get_player_attempts : {e}")
            return []

    def get_best_dunk(self, contest_id):
        """Trouve le meilleur dunk du concours"""
        try:
            query = """
            SELECT 
                p.Firstname,
                p.Lastname,
                d.Name as dunk_name,
                a.Average_score,
                a.Round_number,
                a.Attempt_number
            FROM attempts a
            JOIN Players p ON a.id_player = p.id
            LEFT JOIN Dunks d ON a.id_dunk = d.id
            WHERE a.id_contest = %s
            ORDER BY a.Average_score DESC
            LIMIT 1
            """

            self.cursor.execute(query, (contest_id,))
            return self.cursor.fetchone()

        except Error as e:
            print(f"❌ Erreur get_best_dunk : {e}")
            return None

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
