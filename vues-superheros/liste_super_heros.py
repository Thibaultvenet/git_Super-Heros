import tkinter as tk
import grille


def superHeroesListFrame(interface):
    """
    Crée la vue principale de l'affichage des super héros
    """
    label = tk.Label(interface, text = "Liste des super héros")
    label.place(x=25,y=125)
    
    g = grille.Grille(350,450,"test.png","test",0)
    g.placer(interface,25,75)