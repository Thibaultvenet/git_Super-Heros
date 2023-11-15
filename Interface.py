import vues-superheros.interface_global
import rechercheAvancees
import Structure_donnees

def menu():
    print("Que souhaitez vous faire à présent ?\n")
    print("1 - Afficher tout les super-héros.")
    print("2 - Ajouter un super-héros.")
    print("3 - Modifier un super-héros.")
    print("4 - Supprimer un super-héros.")
    print("5 - Rechercher un super-héros.\n")
    print("6 - Quitter.\n")
    choix = input("Votre choix : ")
    while not choix.isdigit() or choix < "1" or choix > "6":
        print("Erreur : choix invalide")
        choix = input("Votre choix : ")
    if choix == "1":
        Structure_donnees.show_superhero(Structure_donnees.load_superheroes_from_json('api/all.json'))
        menu()
    elif choix == "2":
        Structure_donnees.add_superhero('api/all.json')
        menu()
    elif choix == "3":
        Structure_donnees.modify_superhero('api/all.json')
        menu()
    elif choix == "4":
        Structure_donnees.delete_superhero('api/all.json')
        menu()
    elif choix == "5":
        rechercheAvancees.rechercher()
        menu()


menu()
