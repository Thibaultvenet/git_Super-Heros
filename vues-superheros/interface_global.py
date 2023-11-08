import tkinter as tk
import liste_super_heros
import barre_recherche

interface = tk.Tk()


width= interface.winfo_screenwidth()
height= interface.winfo_screenheight()

interface.geometry("%dx%d" % (width, height))

liste_super_heros.superHeroesListFrame(interface)
barre_recherche.barre_recherche(interface)


interface.mainloop()