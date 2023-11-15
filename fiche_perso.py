import tkinter as tk
from tkinter import PhotoImage

class FichePerso:

    def __init__(self, root):
        self.root = root

        # Destruction de la fenêtre d'accueil
        self.root.destroy()

        # Création de la fenêtre d'affichage des personnages
        self.fenetre_perso = tk.Tk()
        self.fenetre_perso.title("Fiche du Héro")
        self.fenetre_perso.geometry("1280x720")

        # Configuration de la couleur de fond
        couleur_fond_jaune = "#FFC13B"
        couleur_fond_beige = "#F5F0E1"
        couleur_fond_noir = "#000000"
        
        # Partie Head
        self.head_frame = tk.Frame(self.fenetre_perso, bg=couleur_fond_jaune)
        self.head_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Ajout de la photo de profil dans la partie Head
        image_profil = PhotoImage(file="pdp_ironman.png").subsample(6)
        label_profil = tk.Label(self.head_frame, image=image_profil, bg=couleur_fond_jaune)
        label_profil.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Ajout du titre avec le nom dans la partie Head
        nom_utilisateur = " Ironman"
        label_titre = tk.Label(self.head_frame, text=nom_utilisateur, font=("Helvetica", 30), bg=couleur_fond_jaune)
        label_titre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Ajout du bouton de retour à droite dans la partie Head
        bouton_retour = tk.Button(self.head_frame, text="Retour", command=None, font=("Helvetica", 12), bg=couleur_fond_jaune, fg="black")
        bouton_retour.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        # Partie Body
        self.body_frame = tk.Frame(self.fenetre_perso, bg=couleur_fond_jaune)
        self.body_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Ajout d'une Frame en dessous de la photo de profil dans la partie Body
        frame_en_dessous = tk.Frame(self.body_frame, bg=couleur_fond_beige)
        frame_en_dessous.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Ajout des informations dans la Frame en dessous
        nom_label = tk.Label(frame_en_dessous, text="Nom:", font=("Helvetica", 12), bg=couleur_fond_beige, fg="black")
        nom_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        taille_label = tk.Label(frame_en_dessous, text="Taille:", font=("Helvetica", 12), bg=couleur_fond_beige, fg="black")
        taille_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        sexe_label = tk.Label(frame_en_dessous, text="Sexe:", font=("Helvetica", 12), bg=couleur_fond_beige, fg="black")
        sexe_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Ajout d'une Frame au milieu de la fenêtre dans la partie Body
        frame_description = tk.Frame(self.body_frame, bg=couleur_fond_beige)
        frame_description.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Ajout d'un texte de description dans la Frame de description
        description_texte = "Ironman est un super-héros de l'univers Marvel, créé par Stan Lee."
        label_description = tk.Label(frame_description, text=description_texte, font=("Helvetica", 14), bg=couleur_fond_beige, fg="black")
        label_description.pack()

        # Ajout de deux nouvelles Frames à droite de la partie Body
        frame_stats = tk.Frame(self.fenetre_perso, bg=couleur_fond_jaune)
        frame_stats.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        frame_connections = tk.Frame(self.fenetre_perso, bg=couleur_fond_jaune)
        frame_connections.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Ajout du texte avec les stats dans la Frame Stats
        stats_texte = "Stats du personnage:\nForce: 100\nAgilité: 80\nIntelligence: 90"
        label_stats = tk.Label(frame_stats, text=stats_texte, font=("Helvetica", 12), bg=couleur_fond_jaune, fg="black")
        label_stats.pack()

        # Ajout du texte avec les connections dans la Frame Connections
        connections_texte = "Connections du personnage:\nAvengers\nS.H.I.E.L.D."
        label_connections = tk.Label(frame_connections, text=connections_texte, font=("Helvetica", 12), bg=couleur_fond_jaune, fg="black")
        label_connections.pack()

        # Redimensionnement de la partie Body pour occuper tout l'espace disponible
        self.fenetre_perso.grid_rowconfigure(1, weight=1)
        self.fenetre_perso.grid_columnconfigure(0, weight=1)
        self.fenetre_perso.grid_columnconfigure(1, weight=1)

        # Boucle principale de la fenêtre
        self.fenetre_perso.mainloop()

# Création de la fenêtre d'accueil
fenetre_accueil = tk.Tk()
fenetre_accueil.title("Accueil")
fenetre_accueil.geometry("800x600")

# Création de l'instance de la classe FichePerso
fiche_perso = FichePerso(fenetre_accueil)
