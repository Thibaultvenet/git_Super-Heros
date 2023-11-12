"""
Ce module represente les grilles permettant d'afficher visuellement les super héros
Auteur : Toudjani Soumana - Abdoul Majid

"""

import tkinter as tk


class Grille :
    def __init__(self,largeur,hauteur,image_couverture,nom_hero,indice_description):
        """
        La liste des super héros est affichées sous forme de grilles visuelles
        Cette permet de créer des grilles  visuelles avec Tkinter.
        Une grille comprend une image de couverture (l'image du super héro), le nom du super héro
        et un boutton permettant d'afficher la description détaillé du super héro
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.couverture = image_couverture
        self.nom_hero = nom_hero
        self.indice = indice_description

    
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
    
    
    def placer(self,frame,positionX,positionY):
        """
        Permet de plader une grille au sein d'un frame à une position donnée
        param positionX : la position X ou placer la grille
        param positionY : la position Y ou placer la grille
        """
        grid_frame = tk.Frame(frame,width=self.largeur,height=self.hauteur,bg="red")
        grid_frame.place(x=positionX, y=positionY)
        
        hero_image_frame = tk.Frame(grid_frame,width=350,height=250,bg="blue")
        hero_image_frame.place(x=0,y=0)
        
        hero_name_frame = tk.Frame(grid_frame,width=350,height=100,bg="yellow")
        hero_name_frame.place(x=0,y=250)
        
        hero_button_frame = tk.Frame(grid_frame,width=350,height=100,bg="gray")
        hero_button_frame.place(x=0,y=350)
        
