import tkinter as tk

interface = tk.Tk()

width= interface.winfo_screenwidth()
height= interface.winfo_screenheight()

interface.geometry("%dx%d" % (width, height))

interface.mainloop()