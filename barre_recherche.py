import tkinter as tk


def cherch():
    pass


# création de la barre de recherche
def barre_recherche(interface):
    # création de la barre de recherche
    
    frame = tk.Frame(interface, width=700, height=175, relief="solid", borderwidth=1)
    frame.grid(row=0,column=1)
    entry = tk.Entry(frame)
    entry.pack()
    recherche = entry.get()

    print(f"Recherche en cours... : {recherche}")

    # Création d'un boutton
    bouton_recherche = tk.Button(frame, text="Rechercher", command=cherch)
    bouton_recherche.pack()
