import tkinter as tk
import interface_global


label = tk.Label(interface_global.interface, text = "Liste des super héros")
label.place(x=25,y=50)

def superHeroesListFrame():
    """
    Crée la vue principale de l'affichage des super héros
    """
    label = tk.Label(interface_global.interface, text = "Liste des super héros")
    label.place(x=25,y=50)
    
superHeroesListFrame()