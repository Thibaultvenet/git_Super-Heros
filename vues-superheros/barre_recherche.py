import tkinter as tk

# création de la barre de recherche
def barre_recherche(interface):

    # création de la barre de recherche
    entry = tk.Entry(interface, width=90)
    entry.pack()
    recherche = entry.get()

    print(f"Recherche en cours... : {recherche}")

    # Création d'un boutton
    bouton_recherche = tk.Button(interface, text="Rechercher")
    bouton_recherche.pack()
