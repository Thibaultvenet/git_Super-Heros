import tkinter as tk
from tkinter import Button
from tkinter import ttk

class VotreApplication:
    def __init__(self):
        fenetre = tk.Tk()
        fenetre.title("Accueil")
        fenetre.geometry("1280x720")
        fenetre.configure(bg="#FFC13B")  # Changer la couleur du fond de la fenêtre
        
        logo = tk.PhotoImage(file="logo.png").subsample(6)
        label_logo = tk.Label(fenetre, image=logo, bg="#FFC13B")  # Ajout de la couleur de fond
        label_logo.photo = logo
        label_logo.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        titre_label = tk.Label(fenetre, text="Accueil", font=("Helvetica", 24), bg="#FFC13B", fg="black")  # Ajout de la couleur de fond et de la couleur du texte
        titre_label.grid(row=0, column=1, pady=10, sticky="w")

        self.bouton_liste = Button(fenetre, text="Liste des super héros", width=40, height=3, bg="#1E3D59", fg="white", bd=0, relief="solid", command=self.afficher_liste_superheros)
        self.bouton_liste.grid(row=1, column=0, padx=10, pady=10)

        self.bouton_recherche = Button(fenetre, text="Rechercher un super héros", width=40, height=3, bg="#1E3D59", fg="white", bd=0, relief="solid", command=self.rechercher_superheros)
        self.bouton_recherche.grid(row=1, column=1, padx=10, pady=10)

        cadre_classement = tk.Frame(fenetre, bg="white", height=150)
        cadre_classement.grid(row=2, column=0, columnspan=2, sticky="nsew")

        titre_classement = tk.Label(cadre_classement, text="Classement", font=("Helvetica", 18), bg="white")
        titre_classement.pack(pady=10)

        fenetre.grid_rowconfigure(2, weight=1)
        fenetre.grid_columnconfigure(0, weight=1)
        fenetre.grid_columnconfigure(1, weight=1)

        fenetre.mainloop()

    def afficher_liste_superheros(self):
        # Ajoutez le code nécessaire pour afficher la liste des super héros ici
        pass

    def rechercher_superheros(self):
        # Ajoutez le code nécessaire pour rechercher un super héros ici
        pass

VotreApplication()
