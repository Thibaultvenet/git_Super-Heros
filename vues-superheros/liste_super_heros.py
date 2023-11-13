import tkinter as tk
import grille


# Nombre de grilles par ligne
grids_per_row = 3

# Dimensions d'une grille
grid_width = 350
grid_height = 450

# Nombre total de grilles
total_grids = 9  # Vous pouvez ajuster cela en fonction de vos besoins


def superHeroesListFrame(interface):
    """
    Crée la vue principale de l'affichage des super héros
    """
    
    for i in range(total_grids):
        grid_frame = tk.Frame(interface, width=grid_width, height=grid_height, bg="red", relief="solid", borderwidth=1)
        grid_frame.grid(row=i // grids_per_row, column=i % grids_per_row, padx=10, pady=10)
    
    
    #g = grille.Grille(350,450,"test.png","test",0)
    #g.placer(interface,25,75)