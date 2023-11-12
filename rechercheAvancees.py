import tkinter as tk
import json

def rechercher():
    critere = {
        "nom": entry_nom.get(),
        "genre": genre_var.get(),
        "race": race_var.get(),
        "puissance_min": entry_puissance_min.get(),
        "puissance_max": entry_puissance_max.get(),
        "intelligent": intelligent_var.get(),
        "rapide": rapide_var.get(),
        "durabilite": durabilite_var.get(),
        "pouvoir": pouvoir_var.get(),
        "combat": combat_var.get()
    }

    with open('all.json', 'r') as json_file:
        superheros = json.load(json_file)

    resultats = []

    for superheros in superheros:
        if critere["nom"] and critere["nom"].lower() not in superheros["name"].lower():
            continue
        if critere["genre"] and critere["genre"] != superheros["appearance"]["gender"]:
            continue
        if critere["race"] and critere["race"] != superheros["appearance"]["race"]:
            continue
        if critere["puissance_min"] and critere["puissance_min"] > superheros["powerstats"]["strength"]:
            continue
        if critere["puissance_max"] and critere["puissance_max"] < superheros["powerstats"]["strength"]:
            continue

        # Vérifier les critères supplémentaires
        if critere["intelligent"] and superheros["powerstats"]["intelligence"] < 50:
            continue
        if critere["rapide"] and superheros["powerstats"]["speed"] < 50:
            continue
        if critere["durabilite"] and superheros["powerstats"]["durability"] < 50:
            continue
        if critere["pouvoir"] and superheros["powerstats"]["power"] < 50:
            continue
        if critere["combat"] and superheros["powerstats"]["combat"] < 50:
            continue

        resultats.append(superheros)

    # Afficher les résultats dans une zone de texte
    resultat_text.config(state=tk.NORMAL)
    resultat_text.delete('1.0', tk.END)
    for resultat in resultats:
        resultat_text.insert(tk.END, f"Nom: {resultat['name']}, Genre: {resultat['appearance']['gender']}, Race: {resultat['appearance']['race']}, Puissance: {resultat['powerstats']['strength']}\n")
    resultat_text.config(state=tk.DISABLED)

def afficher_filtres_supplementaires():
    frame_filtres_supplementaires.pack()
    button_filtres.config(text="Masquer les filtres")

def cacher_filtres_supplementaires():
    frame_filtres_supplementaires.pack_forget()
    button_filtres.config(text="Plus de filtres")

# Créer la fenêtre principale
window = tk.Tk()
window.title("Recherche de Superhéros")

# Créer des champs de texte et des étiquettes pour la recherche
label_nom = tk.Label(window, text="Nom:")
entry_nom = tk.Entry(window)
label_genre = tk.Label(window, text="Genre:")
genre_var = tk.StringVar()
genre_var.set("")  # Valeur par défaut
genre_optionmenu = tk.OptionMenu(window, genre_var, "", "Male", "Female")
label_race = tk.Label(window, text="Race:")
race_var = tk.StringVar()
race_var.set("")  # Valeur par défaut
race_optionmenu = tk.OptionMenu(window, race_var, "", "Human", "Icthyo Sapien", "Ungaran", "Human / Radiation", "Cosmic Entity")
label_puissance_min = tk.Label(window, text="Puissance minimale:")
entry_puissance_min = tk.Entry(window)
label_puissance_max = tk.Label(window, text="Puissance maximale:")
entry_puissance_max = tk.Entry(window)
button_filtres = tk.Button(window, text="Plus de filtres", command=afficher_filtres_supplementaires)

# Créer un bouton pour la recherche
button_rechercher = tk.Button(window, text="Rechercher", command=rechercher)

# Créer une zone de texte pour afficher les résultats
resultat_text = tk.Text(window, state=tk.DISABLED)

# Créer un cadre pour les filtres supplémentaires
frame_filtres_supplementaires = tk.Frame(window)

# Ajouter des critères supplémentaires au cadre
label_critere_supplementaire = tk.Label(frame_filtres_supplementaires, text="Critères supplémentaires:")
label_critere_supplementaire.pack()

# Exemple de critère supplémentaire : Une case à cocher pour les superhéros avec une intelligence élevée
intelligent_var = tk.IntVar()
checkbox_intelligent = tk.Checkbutton(frame_filtres_supplementaires, text="Intelligent", variable=intelligent_var)
checkbox_intelligent.pack()

# Exemple de critère supplémentaire : Une case à cocher pour les superhéros avec une vitesse élevée
rapide_var = tk.IntVar()
checkbox_rapide = tk.Checkbutton(frame_filtres_supplementaires, text="Rapide", variable=rapide_var)
checkbox_rapide.pack()

# Exemple de critère supplémentaire : Une case à cocher pour les superhéros avec une durabilité élevée
durabilite_var = tk.IntVar()
checkbox_durabilite = tk.Checkbutton(frame_filtres_supplementaires, text="Durabilité élevée", variable=durabilite_var)
checkbox_durabilite.pack()

# Exemple de critère supplémentaire : Une case à cocher pour les superhéros avec un pouvoir élevé
pouvoir_var = tk.IntVar()
checkbox_pouvoir = tk.Checkbutton(frame_filtres_supplementaires, text="Pouvoir élevé", variable=pouvoir_var)
checkbox_pouvoir.pack()

# Exemple de critère supplémentaire : Une case à cocher pour les superhéros avec un combat élevé
combat_var = tk.IntVar()
checkbox_combat = tk.Checkbutton(frame_filtres_supplementaires, text="Combat élevé", variable=combat_var)
checkbox_combat.pack()

# Placer les éléments dans la fenêtre
label_nom.pack()
entry_nom.pack()
label_genre.pack()
genre_optionmenu.pack()
label_race.pack()
race_optionmenu.pack()
label_puissance_min.pack()
entry_puissance_min.pack()
label_puissance_max.pack()
entry_puissance_max.pack()
button_rechercher.pack()
button_filtres.pack()
resultat_text.pack()

window.mainloop()
