# show_table.py
# Programme pour gérer la base ProjDBPy :
# - afficher contenu d'une table
# - ajouter un joueur
# - supprimer un joueur

import mysql.connector
from mysql.connector import Error

# -----------------------------
# Connexion à la base
# -----------------------------
def get_connection():
    """Ouvre une connexion à la base ProjDBPy."""
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="ProjDBPy",
            port=3306
        )
        return conn
    except Error as e:
        print("Erreur de connexion à MySQL :", e)
        return None


# -----------------------------
# Vérifie si une table existe
# -----------------------------
def table_exists(conn, table_name):
    sql = """
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_schema = %s
          AND table_name = %s
    """
    cur = conn.cursor()
    cur.execute(sql, ("ProjDBPy", table_name))
    (count,) = cur.fetchone()
    cur.close()
    return count == 1


# -----------------------------
# Afficher contenu d’une table
# -----------------------------
def show_table(conn, table_name):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")

    column_names = [desc[0] for desc in cur.description]
    print("\n" + " | ".join(column_names))

    for row in cur.fetchall():
        print(" | ".join(str(v) for v in row))

    cur.close()


# -----------------------------
# Ajouter un joueur
# -----------------------------
def add_player(conn):
    """Ajoute un nouveau joueur dans la table Players."""
    cur = conn.cursor()

    print("\n=== AJOUTER UN JOUEUR ===")

    firstname = input("Prénom : ").strip()
    lastname = input("Nom : ").strip()
    team = input("Équipe (laisser vide si aucune) : ").strip() or None

    height_input = input("Taille en mètres (ex: 1.95, laisser vide si inconnu) : ").strip()
    height = float(height_input) if height_input else None

    # Afficher liste des dunks
    cur.execute("SELECT id, Description FROM Dunks")
    dunks = cur.fetchall()

    if not dunks:
        print("⚠ Aucun dunk disponible. Ajoutez d'abord un dunk.")
        cur.close()
        return

    print("\nDunks disponibles :")
    for d in dunks:
        print(f"{d[0]} : {d[1]}")

    dunk_id_input = input("ID du dunk choisi : ").strip()
    try:
        dunk_id = int(dunk_id_input)
    except ValueError:
        print("ID invalide.")
        cur.close()
        return

    # Insérer le joueur
    sql = """
        INSERT INTO Players (Firstname, Lastname, Team, Height, Dunks_id)
        VALUES (%s, %s, %s, %s, %s)
    """

    try:
        cur.execute(sql, (firstname, lastname, team, height, dunk_id))
        conn.commit()
        print(f"\n✔ Joueur {firstname} {lastname} ajouté avec succès !\n")
    except Exception as e:
        print("Erreur lors de l'ajout :", e)
        conn.rollback()

    cur.close()


# -----------------------------
# Supprimer un joueur
# -----------------------------
def delete_player(conn):
    """Supprime un joueur via son ID."""
    cur = conn.cursor()

    print("\n=== SUPPRIMER UN JOUEUR ===")

    # Afficher joueurs
    cur.execute("SELECT id, Firstname, Lastname FROM Players")
    players = cur.fetchall()

    if not players:
        print("⚠ Aucun joueur trouvé.")
        cur.close()
        return

    print("\nListe des joueurs :")
    for p in players:
        print(f"ID: {p[0]}  -  {p[1]} {p[2]}")

    # ID du joueur
    player_id_input = input("\nID du joueur à supprimer : ").strip()

    try:
        player_id = int(player_id_input)
    except ValueError:
        print("ID invalide.")
        cur.close()
        return

    # Vérifier existence
    cur.execute("SELECT COUNT(*) FROM Players WHERE id = %s", (player_id,))
    (count,) = cur.fetchone()

    if count == 0:
        print("⚠ Aucun joueur avec cet ID.")
        cur.close()
        return

    confirm = input("Confirmer suppression ? (oui/non) : ").strip().lower()
    if confirm not in ("oui", "o", "yes", "y"):
        print("Suppression annulée.")
        cur.close()
        return

    # Suppression
    try:
        cur.execute("DELETE FROM Players WHERE id = %s", (player_id,))
        conn.commit()
        print("✔ Joueur supprimé avec succès !")
    except Exception as e:
        print("Erreur :", e)
        conn.rollback()

    cur.close()


# -----------------------------
# PROGRAMME PRINCIPAL
# -----------------------------
def main():
    conn = get_connection()
    if conn is None:
        return

    print('\nConnexion réussie à "ProjDBPy".\n')

    while True:
        print("=== MENU ===")
        print("1 - Afficher une table")
        print("2 - Ajouter un joueur")
        print("3 - Supprimer un joueur")
        print("4 - Quitter")

        choice = input("\nChoix : ").strip()

        if choice == "1":
            table_name = input("Nom de la table : ").strip()
            if table_exists(conn, table_name):
                show_table(conn, table_name)
            else:
                print("Table inexistante.\n")

        elif choice == "2":
            add_player(conn)

        elif choice == "3":
            delete_player(conn)

        elif choice == "4":
            print("Au revoir.")
            break

        else:
            print("Choix invalide.\n")

    conn.close()


if __name__ == "__main__":
    main()
