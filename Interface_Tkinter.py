# main.py

import tkinter as tk
from tkinter import Button
from liste_superheros import afficher_liste_superheros


class VotreApplication:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Accueil")
        self.fenetre.geometry("1280x720")
        self.fenetre.configure(bg="#FFC13B")
        self.fenetre.resizable(False, False)  

        self.logo = tk.PhotoImage(file="logo.png").subsample(6)
        label_logo = tk.Label(self.fenetre, image=self.logo, bg="#FFC13B")
        label_logo.photo = self.logo
        label_logo.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        titre_label = tk.Label(self.fenetre, text="Accueil", font=("Helvetica", 24), bg="#FFC13B", fg="black")
        titre_label.grid(row=0, column=1, pady=10, sticky="w")

        self.bouton_liste = Button(self.fenetre, text="Liste des super héros", width=40, height=3, bg="#1E3D59", fg="white", bd=0, relief="solid", command=self.afficher_liste_superheros)
        self.bouton_liste.grid(row=1, column=0, padx=10, pady=10)

        self.bouton_recherche = Button(self.fenetre, text="Rechercher un super héros", width=40, height=3, bg="#1E3D59", fg="white", bd=0, relief="solid", command=self.rechercher_superheros)
        self.bouton_recherche.grid(row=1, column=1, padx=10, pady=10)

        cadre_classement = tk.Frame(self.fenetre, bg="white", height=150)
        cadre_classement.grid(row=2, column=0, columnspan=2, sticky="nsew")

        titre_classement = tk.Label(cadre_classement, text="Classement", font=("Helvetica", 18), bg="white")
        titre_classement.pack(pady=10)

        self.fenetre.grid_rowconfigure(2, weight=1)
        self.fenetre.grid_columnconfigure(0, weight=1)
        self.fenetre.grid_columnconfigure(1, weight=1)

        self.fenetre.mainloop()

    def afficher_liste_superheros(self):
        from liste_superheros import afficher_liste_superheros
        afficher_liste_superheros(self.fenetre, self.logo, self.rechercher_superheros, self.recherche_avancee_superheros)

    def rechercher_superheros(self):
        # Ajoutez le code nécessaire pour rechercher un super héros ici
        pass

    def recherche_avancee_superheros(self):
        # Ajoutez le code nécessaire pour la recherche avancée des super héros ici
        pass

VotreApplication()
