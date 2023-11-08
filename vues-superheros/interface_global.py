import tkinter as tk
import liste_super_heros


interface = tk.Tk()


width= interface.winfo_screenwidth()
height= interface.winfo_screenheight()

interface.geometry("%dx%d" % (width, height))

liste_super_heros.superHeroesListFrame(interface)

interface.mainloop()