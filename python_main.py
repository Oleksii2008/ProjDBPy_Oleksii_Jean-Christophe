'''
Nom    : python_main.py
Auteur : Jean-Christophe Serrano, Oleksii Kamarali
Date   : 19.12.2025
'''

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from python_display import Page1, Page2, Page3, Page4, Page5, Page6, Page7
from python_database import Database
import os

DB_config = {
            "host": "127.0.0.1",
            "user": "root",
            "password": os.getenv("DB_password"),
            "database": "dunk_contest",
            "port": 3306
        }

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Événement NBA")

        window_width = 700
        window_height = 467

        self.geometry(f"{window_width}x{window_height}")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_left = int(screen_width / 2 - window_width / 2)
        y_top = int(screen_height / 2 - window_height / 2)
        self.geometry("+{}+{}".format(x_left, y_top))

        self.db = Database(DB_config)

        self.bg_image1 = ImageTk.PhotoImage(Image.open("slamdunk_0.png"))

        bg_image2 = Image.open("1_7OmCmTMBu1adOhD6vP9BFw.jpg")
        bg_image2 = bg_image2.resize((700, 467), Image.LANCZOS)  # Redimensionner
        self.bg_image2 = ImageTk.PhotoImage(bg_image2)

        bg_image3 = Image.open("north-americas-all-time-best-nba-players.jpg")
        bg_image3 = bg_image3.resize((700, 467), Image.LANCZOS)  # Redimensionner
        self.bg_image3 = ImageTk.PhotoImage(bg_image3)

        bg_image4 = Image.open("360_F_346562502_uyFXtYg06IOPPtlhiHyeBlI3SBCgOSz8.jpg")
        bg_image4 = bg_image4.resize((700, 467), Image.LANCZOS)  # Redimensionner
        self.bg_image4 = ImageTk.PhotoImage(bg_image4)

        bg_image5 = Image.open("R.jpg")
        bg_image5 = bg_image5.resize((700, 467), Image.LANCZOS)  # Redimensionner
        self.bg_image5 = ImageTk.PhotoImage(bg_image5)

        self.page1 = Page1(self)
        self.page2 = Page2(self)
        self.page3 = Page3(self)
        self.page4 = Page4(self)
        self.page5 = Page5(self)
        self.page6 = Page6(self)
        self.page7 = Page7(self)

        self.page1.pack(fill="both", expand=True)

    def afficher_page7(self):
        self.page6.pack_forget()
        self.page7.pack(fill="both", expand=True)
        self.page7.refresh_display()

    def afficher_page6(self):
        self.page5.pack_forget()
        self.page6.pack(fill="both", expand=True)
        self.page6.refresh_display()

    def afficher_page5(self):
        self.page1.pack_forget()
        self.page5.pack(fill="both", expand=True)
        self.page5.load_contests()

    def afficher_page4(self):
        self.page1.pack_forget()
        self.page4.pack(fill="both", expand=True)

    def afficher_page3(self):
        self.page1.pack_forget()
        self.page3.pack(fill="both", expand=True)

    def afficher_page2(self):
        self.page1.pack_forget()
        self.page2.pack(fill="both", expand=True)

    def afficher_page1(self):
        self.page5.pack_forget()
        self.page4.pack_forget()
        self.page3.pack_forget()
        self.page2.pack_forget()
        self.page1.pack(fill="both", expand=True)

    def on_closing(self):
        """Ferme proprement la connexion MySQL"""
        self.db.close()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()

