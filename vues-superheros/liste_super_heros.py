import tkinter as tk


def superHeroesListFrame(interface):
    """
    Crée la vue principale de l'affichage des super héros
    """
    label = tk.Label(interface, text = "Liste des super héros")
    label.place(x=25,y=125)
    