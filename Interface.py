def menu():
    print("Que souhaitez vous faire à présent ?\n")
    print("1 - Afficher tout les super-héros.")
    print("2 - Ajouter un super-héros.")
    print("3 - Modifier un super-héros.")
    print("4 - Supprimer un super-héros.")
    print("5 - Rechercher un super-héros.\n")
    choix = input("Votre choix : ")
    while not choix.isdigit() or choix < "1" or choix > "5":
        print("Erreur : choix invalide")
        choix = input("Votre choix : ")
    if choix == "1":
        # Affichertout
        menu()
    elif choix == "2":
        # Ajouter
        menu()
    elif choix == "3":
        # Modifier
        menu()
    elif choix == "4":
        # Supprimer
        menu()
    elif choix == "5":
        # Rechercher
        menu()


menu()
