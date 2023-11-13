import tkinter as tk


def cherch():
    pass


# création de la barre de recherche
def barre_recherche(interface):
    # création de la barre de recherche
    entry = tk.Entry(interface)
    entry.pack()
    recherche = entry.get()

    print(f"Recherche en cours... : {recherche}")

    # Création d'un boutton
    bouton_recherche = tk.Button(interface, text="Rechercher", command=cherch)
    bouton_recherche.place(x=690, y=55)
