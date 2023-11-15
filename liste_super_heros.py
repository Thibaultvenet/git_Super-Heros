import tkinter as tk
import grille

import Structure_donnees as SD


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
    
    #parcours de la liste des super héros
    for i in range(200):
        g = grille.Grille(350,450,SD. superhero_list.superheroes[i])
        g.placer( interface,(i // grids_per_row)+1, i % grids_per_row)
    
    
    #
    #g.placer(interface,25,75)