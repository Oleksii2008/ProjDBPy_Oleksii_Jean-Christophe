# show_table.py
# Programme simple pour :
# 1) se connecter à la base MySQL "mydb"
# 2) demander le nom d'une table
# 3) vérifier si la table existe
# 4) afficher le contenu de la table si elle existe

import mysql.connector
from mysql.connector import Error

# -----------------------------
# Connexion à la base de données
# -----------------------------
def get_connection():
    """Ouvre une connexion à la base mydb."""
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",   # comme dans HeidiSQL
            user="root",        # utilisateur
            password="root",    # mot de passe
            database="mydb",    # nom du schéma
            port=3306
        )
        return conn
    except Error as e:
        print("Erreur de connexion à MySQL :", e)
        return None

# -----------------------------
# Vérifier si la table existe
# -----------------------------
def table_exists(conn, table_name):
    """Retourne True si la table existe dans le schéma mydb."""
    sql = """
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_schema = %s
          AND table_name = %s
    """
    cur = conn.cursor()
    cur.execute(sql, ("mydb", table_name))
    (count,) = cur.fetchone()
    cur.close()
    return count == 1

# -----------------------------
# Afficher le contenu de la table
# -----------------------------
def show_table(conn, table_name):
    """Affiche toutes les lignes de la table."""
    cur = conn.cursor()
    # ATTENTION : ici on insère le nom de table directement dans la requête
    # (ok pour un petit exercice en local)
    cur.execute(f"SELECT * FROM {table_name}")

    # noms des colonnes
    column_names = [desc[0] for desc in cur.description]
    print(" | ".join(column_names))

    # lignes
    for row in cur.fetchall():
        # convertir tous les champs en string pour l'affichage
        print(" | ".join(str(v) for v in row))

    cur.close()

# -----------------------------
# Programme principal
# -----------------------------
def main():
    conn = get_connection()
    if conn is None:
        return

    print('Connexion réussie à "mydb".')
    print('Tape le nom de la table à afficher (par ex. Dunks, Players, Judges).')
    print('Écris "quit" pour sortir.\n')

    while True:
        table_name = input("Nom de la table: ").strip()
        if table_name.lower() in ("quit", "exit"):
            print("Au revoir.")
            break

        if not table_name:
            continue

        if not table_exists(conn, table_name):
            print(f'La table "{table_name}" n’existe pas dans mydb.\n')
        else:
            print(f'\nContenu de la table "{table_name}":')
            show_table(conn, table_name)
            print()  # ligne vide pour lisibilité

    conn.close()

if __name__ == "__main__":
    main()