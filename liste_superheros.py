import tkinter as tk
from tkinter import Button, Entry, Scrollbar, Canvas

def afficher_liste_superheros(fenetre, logo, rechercher_superheros, recherche_avancee_superheros):
    # Détruire les widgets actuels (sauf le logo)
    for widget in fenetre.winfo_children():
        if widget != logo:
            widget.destroy()

    # Afficher le logo et le titre
    label_logo = tk.Label(fenetre, image=logo, bg="#FFC13B")
    label_logo.photo = logo
    label_logo.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    # Ajouter un titre
    titre_label = tk.Label(fenetre, text="Liste des Super Héros", font=("Helvetica", 18), bg="#FFC13B", fg="black")
    titre_label.grid(row=0, column=1, pady=10, sticky="w")

    # Créer un cadre pour regrouper la barre de recherche, le bouton de recherche et le bouton de recherche avancée
    cadre_recherche = tk.Frame(fenetre, bg="#FFC13B")
    cadre_recherche.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")

    # Ajouter une barre de recherche
    recherche_entry = Entry(cadre_recherche, width=40)
    recherche_entry.grid(row=0, column=0, padx=10, pady=10)

    # Ajouter un bouton de recherche
    bouton_rechercher = Button(cadre_recherche, text="Rechercher", width=20, height=2, bg="#1E3D59", fg="white", bd=0, relief="solid", command=rechercher_superheros)
    bouton_rechercher.grid(row=0, column=1, padx=10, pady=10)

    # Ajouter un bouton de recherche avancée
    bouton_recherche_avancee = Button(cadre_recherche, text="Recherche Avancée", width=20, height=2, bg="#1E3D59", fg="white", bd=0, relief="solid", command=recherche_avancee_superheros)
    bouton_recherche_avancee.grid(row=0, column=2, padx=10, pady=10)

    # Liste de super-héros (nom, image de profil)
    liste_superheros = [
        {"nom": "Superman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        {"nom": "Batman", "image": "profil_heros_test.png"},
        # Ajoutez d'autres super-héros selon vos besoins
    ]

    # Cadre pour afficher la liste de super-héros avec une barre de défilement
    cadre_superheros = tk.Frame(fenetre, bg="white")
    cadre_superheros.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Barre de défilement verticale
    scrollbar = Scrollbar(cadre_superheros, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    # Canvas pour afficher les super-héros avec la barre de défilement
    canvas_superheros = Canvas(cadre_superheros, bg="white", yscrollcommand=scrollbar.set)
    canvas_superheros.pack(side="left", fill="both", expand=True)

    # Configuration de la barre de défilement
    scrollbar.config(command=canvas_superheros.yview)

    # Cadre à l'intérieur du canvas
    cadre_interieur = tk.Frame(canvas_superheros, bg="white")
    canvas_superheros.create_window((0, 0), window=cadre_interieur, anchor="nw")

    # Tri de la liste des super-héros par ordre alphabétique
    liste_superheros = sorted(liste_superheros, key=lambda x: x["nom"])

    # Affichage des super-héros dans des carrés
    for i, superheros in enumerate(liste_superheros):
        nom = superheros["nom"]
        image_path = superheros["image"]

        # Charger l'image (assurez-vous que les fichiers image sont dans le même répertoire que le script)
        image = tk.PhotoImage(file=image_path).subsample(5,5)  # Ajustez le facteur de sous-échantillonnage selon vos besoins

        # Créer un label pour afficher l'image
        label_image = tk.Label(cadre_interieur, image=image, text=nom, compound=tk.BOTTOM)
        label_image.photo = image
        label_image.grid(row=i // 6, column=i % 6, padx=10, pady=10)

    # Configuration du Canvas pour qu'il suive la taille du cadre interieur
    cadre_interieur.update_idletasks()
    canvas_superheros.config(scrollregion=canvas_superheros.bbox("all"))

