import liste_super_heros
import barre_recherche
import tkinter as tk
from tkinter import ttk

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))



interface = tk.Tk()
interface.title("Grilles avec Défilement")

width= interface.winfo_screenwidth()
height= interface.winfo_screenheight()

interface.geometry("%dx%d" % (width, height))


# Créer une barre de défilement vertical
scrollbar = ttk.Scrollbar(interface, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Créer un canevas pour le contenu
canvas = tk.Canvas(interface, yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
canvas.bind("<Configure>", on_canvas_configure)

# Configurer la barre de défilement pour contrôler le canevas
scrollbar.config(command=canvas.yview)


def on_mouse_scroll(event):
    if event.delta:
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    elif event.num == 5:
        canvas.yview_scroll(1, "units")
    elif event.num == 4:
        canvas.yview_scroll(-1, "units")



# Créer un cadre pour contenir les grilles
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")


barre_recherche.barre_recherche(frame)
liste_super_heros.superHeroesListFrame(frame)


# Configurer la gestion de la taille du canevas
interface.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
canvas.bind("<MouseWheel>", on_mouse_scroll)  # Utilisation de "<MouseWheel>" pour Windows
canvas.bind("<Button-4>", on_mouse_scroll)  # Utilisation de "<Button-4>" pour Linux
canvas.bind("<Button-5>", on_mouse_scroll) 

interface.mainloop()
