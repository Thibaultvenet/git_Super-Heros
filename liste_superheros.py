# liste_superheros.py

import tkinter as tk
from tkinter import Button, Entry

def afficher_liste_superheros(fenetre, logo, rechercher_superheros, recherche_avancee_superheros):
    # Détruire les widgets actuels (sauf le logo)
    for widget in fenetre.winfo_children():
        if widget != logo:
            widget.destroy()

    # Afficher le logo
    label_logo = tk.Label(fenetre, image=logo, bg="#FFC13B")
    label_logo.photo = logo
    label_logo.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    # Ajouter une barre de recherche
    recherche_entry = Entry(fenetre, width=40)
    recherche_entry.grid(row=1, column=0, padx=10, pady=10)

    # Ajouter un bouton de recherche
    bouton_rechercher = Button(fenetre, text="Rechercher", width=20, height=2, bg="#1E3D59", fg="white", bd=0, relief="solid", command=rechercher_superheros)
    bouton_rechercher.grid(row=1, column=1, padx=10, pady=10)

    # Ajouter un bouton de recherche avancée
    bouton_recherche_avancee = Button(fenetre, text="Recherche Avancée", width=20, height=2, bg="#1E3D59", fg="white", bd=0, relief="solid", command=recherche_avancee_superheros)
    bouton_recherche_avancee.grid(row=1, column=2, padx=10, pady=10)
