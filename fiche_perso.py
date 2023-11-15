import tkinter as tk
from tkinter import Button
from tkinter import PhotoImage

class FichePerso:

    def __init__(self,root):
        self.root = root

        # Quitter la fenetre d'acceuil
        self.root.destroy()

        # Creation de la fenetre d'affichage des perso
        self.fenetre_perso = tk.Tk()
        self.fenetre_perso.title("Fiche du Héro")
        self.fenetre_perso.geometry("1280x720")

        # Configuration de la couleur de fond
        couleur_fond_jaune = "#FFC13B"
        self.fenetre_perso.configure(bg=couleur_fond_jaune)

        # Ajout de la photo de profil
        image_profil = PhotoImage(file="pdp_ironman.png").subsample(6)  
        label_profil = tk.Label(self.fenetre_perso, image=image_profil, bg=couleur_fond_jaune)
        label_profil.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Ajout du titre avec le nom
        nom_utilisateur = " Ironman"  
        label_titre = tk.Label(self.fenetre_perso, text=nom_utilisateur, font=("Helvetica", 24), bg=couleur_fond_jaune)
        label_titre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Ajout d'une Frame en dessous de la photo de profil
        couleur_fond_beige = "#F5F0E1"
        couleur_fond_noir = "#000000"
        frame_en_dessous = tk.Frame(self.fenetre_perso, bg=couleur_fond_beige)
        frame_en_dessous.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        # Ajout des informations dans la Frame en dessous
        nom_label = tk.Label(frame_en_dessous, text="Nom:", font=("Helvetica", 12), bg=couleur_fond_noir)
        nom_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        taille_label = tk.Label(frame_en_dessous, text="Taille:", font=("Helvetica", 12), bg=couleur_fond_noir)
        taille_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        sexe_label = tk.Label(frame_en_dessous, text="Sexe:", font=("Helvetica", 12), bg=couleur_fond_noir)
        sexe_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    

        # Boucle principale de la fenêtre
        self.fenetre_perso.mainloop()

un = tk.Tk()
FichePerso(un)
un.mainloop