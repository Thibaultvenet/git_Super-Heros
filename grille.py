"""
Ce module represente les grilles permettant d'afficher visuellement les super héros
Auteur : Toudjani Soumana - Abdoul Majid

"""

import tkinter as tk

from PIL import Image
from PIL import ImageTk


class Grille :
    def __init__(self,largeur,hauteur,hero):
        """
        La liste des super héros est affichées sous forme de grilles visuelles
        Cette permet de créer des grilles  visuelles avec Tkinter.
        Une grille comprend une image de couverture (l'image du super héro), le nom du super héro
        et un boutton permettant d'afficher la description détaillé du super héro
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.hero = hero 

    
    def getLargeurr(self):
        """
        Renvoie la largeur de la grille
        """
        return self.largeur
    
    def getHauteur(self):
        """
        Renvoi la hauteur de la grille
        """
        return self.hauteur
    
    
    def placer(self,parentFrame,ligne,colonne):
        """
        Permet de plader une grille au sein d'un frame à une position donnée
        param positionX : la position X ou placer la grille
        param positionY : la position Y ou placer la grille
        """
        
        print("api/images/"+self.hero.images.xs)
        original_image = Image.open("api/images/"+self.hero.images.xs)
        resized_image = original_image.resize((350, 250), Image.ANTIALIAS)  # Ajuster la taille selon tes besoins
        image = ImageTk.PhotoImage(resized_image)

        # Créer un label avec l'image comme fond
        
        grid_frame = tk.Frame(parentFrame,width=self.largeur,height=self.hauteur,bg="red")
        grid_frame.grid(row = ligne, column = colonne,padx=10, pady=10) # placement de la grille à la ligne et à la colonne souhaité
        
        hero_image_frame = tk.Frame(grid_frame,width=350,height=250)
        hero_image_frame.place(x=0,y=0)
        
        
        image_label = tk.Label(hero_image_frame, image=image)
        image_label.place(x=0,y=0,relwidth=1, relheight=1)
        
        
        hero_name_frame = tk.Frame(grid_frame,width=350,height=100,bg="yellow")
        hero_name_frame.place(x=0,y=250)
        
        hero_button_frame = tk.Frame(grid_frame,width=350,height=100,bg="gray")
        hero_button_frame.place(x=0,y=350)
        
