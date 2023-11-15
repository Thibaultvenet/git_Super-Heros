import json
import sys


json_file_path = "api/all.json"  # Chemin du fichier .JSON dont on se sert


# Definition de la structure de données sous forme de dictionnaire
class SuperHero:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.slug = data["slug"]
        self.powerstats = PowerStats(data["powerstats"])
        self.appearance = Appearance(data["appearance"])
        self.biography = Biography(data["biography"])
        self.work = Work(data["work"])
        self.connections = Connections(data["connections"])
        self.images = Images(data["images"])

class PowerStats:
    def __init__(self, data):
        self.intelligence = data["intelligence"]
        self.strength = data["strength"]
        self.speed = data["speed"]
        self.durability = data["durability"]
        self.power = data["power"]
        self.combat = data["combat"]

class Appearance:
    def __init__(self, data):
        self.gender = data["gender"]
        self.race = data["race"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.eyeColor = data["eyeColor"]
        self.hairColor = data["hairColor"]

class Biography:
    def __init__(self, data):
        self.fullName = data["fullName"]
        self.alterEgos = data["alterEgos"]
        self.aliases = data["aliases"]
        self.placeOfBirth = data["placeOfBirth"]
        self.firstAppearance = data["firstAppearance"]
        self.publisher = data["publisher"]
        self.alignment = data["alignment"]

class Work:
    def __init__(self, data):
        self.occupation = data["occupation"]
        self.base = data["base"]

class Connections:
    def __init__(self, data):
        self.groupAffiliation = data["groupAffiliation"]
        self.relatives = data["relatives"]

class Images:
    def __init__(self, data):
        self.xs = data["xs"]
        self.sm = data["sm"]
        self.md = data["md"]
        self.lg = data["lg"]


# Définition de l'objet liste de super héros, permettant d'y inclure une fonction pour ajouter
# un super Héro dans une liste
class SuperHeroList:
    def __init__(self):
        self.superheroes = []

    def add_superhero(self, superhero):
        self.superheroes.append(superhero)


# Définition du sous programme pour lire les données du fichier JSON avec plusieurs vérifications pour
# éviter les erreurs de chargement du fichier ainsi que des vérifications sur la structure des données
# dans le fichier JSON

def load_superheroes_from_json(file_path):
    try:
        # Lecture du fichier JSON
        with open(file_path, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        # Si le prgramme ne trouve pas de fichier dans le chemin indiqué
        print(f"Erreur : Fichier '{file_path}' introuvable.")
        return None

    except json.JSONDecodeError:
        #Format incorrect
        print(f"Erreur : Format JSON invalide dans le fichier '{file_path}'.")
        return None

    except Exception as e:
        # Erreur inconnue
        print(f"Erreur : Une erreur inattendu s'est produite - {e}.")
        return None

    if not isinstance(data, list):
        # Les données ne sont pas sous la forme d'un dictionnaire
        print("Erreur : Les données JSON devraient être une liste de super héros.")
        return None

    # Si toutes les vérifications sont passées, création de la liste de super héros
    superhero_list = SuperHeroList()

    for superhero_data in data:
        if not isinstance(superhero_data, dict):
            print("Erreur : Chaque données d'un super héro devraient être un dictionnaire.")
            return None

        try:
            superhero = SuperHero(superhero_data)
            superhero_list.add_superhero(superhero)

        except KeyError as ke:
            print(f"Erreur: Clé manquante {ke} dans les données du super héro.")
            return None

        except Exception as e:
            print(f"Erreur : Une erreur inattendu s'est produite - {e}.")
            return None

        # Valider la structure des données pour chaque super-héros
        if not all(key in superhero_data for key in ["id", "name", "slug", "powerstats", "appearance", "biography", "work", "connections", "images"]):
            print("Erreur: La structure de données du super héro est incomplète.")
            return None

    return superhero_list

def show_superhero(superhero_list):
    for superhero in superhero_list.superheroes:
        # Affiche le nom de tous les super héros
        print(superhero.name)


# Exemple d'utilisation :
superhero_list = load_superheroes_from_json(json_file_path)

if superhero_list is not None:
    # Les données ont été chargées avec succès
    print("Les données ont été chargées avec succès, voici le nom de tous les super héros :")

    # Affiche le nom de tous les super héros
    show_superhero(superhero_list)

    pass
else:
    # Il y a eu une erreur lors du chargement des données
    sys.exit(1)
    pass

def modify_superhero(json_file_path):

    superhero_name = input("Entrez le nom du super héros à modifier : ")

    # Lecture du fichier JSON
    with open(json_file_path, "r") as file:
        data = json.load(file)

    superhero_found = False  # Indicateur pour vérifier si le super-héros a été trouvé

    for superhero_data in data:
        if superhero_data["name"] == superhero_name:
            superhero_found = True  # Marquer que le super-héros a été trouvé
            print(f"Modification des données pour {superhero_name}")
            field_path = input("Entrez le chemin du champ (exemple, 'name' or 'powerstats.speed') : ")

            # Divise les champs imbriqués en champs individuels
            field_path_list = field_path.split('.')
            current_data = superhero_data

            # Parcoure les structures imbriqués pour savoir si le champ souhaité existe, exemple si on veut modifier
            # powerstats.speed
            for field in field_path_list[:-1]:
                if field in current_data:
                    current_data = current_data[field]
                else:
                    print(f"{field} n'est pas un champ valide pour {superhero_name}")
                    return

            # Vérifies si le champ souhaité à modifier existe bien dans la structure de données d'un super héro
            last_field = field_path_list[-1]
            if last_field not in current_data:
                print(f"Erreur: {last_field} n'est pas un champ valide pour {superhero_name}.")
                return

            # Modifies l'information souhaitée dans les données du super héro
            new_value = input(f"Entrez la nouvelle valeur pour {last_field} : ")

            # Convertie la nouvelle en int si la valeur originale était aussi un int
            if isinstance(current_data[last_field], int):
                new_value = int(new_value)

            current_data[last_field] = new_value
            print(f"{last_field} a été modifié par {new_value}")

    if not superhero_found:
        print(f"Erreur: Aucun super héro trouvé avec le nom {superhero_name}.")

    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=2)



def add_superhero(json_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)

    # Vérifier l'unicité de l'ID
    while True:
        new_id = int(input("Entrez l'ID du super héros (0 pour quitter) : "))

        if new_id == 0:
            print("Opération annulée. Aucun super héros n'a été ajouté.")
            return

        existing_ids = {superhero["id"] for superhero in data}
        if new_id not in existing_ids:
            break
        else:
            print("Erreur: Cet ID existe déjà pour un super héros. Veuillez choisir un ID unique.")

    new_superhero = {
        "id": new_id,
        "name": input("Entrez le nom du super héros (0 pour quitter) : "),
        "slug": input("Entrez le slug du super héros (0 pour quitter) : "),
        "powerstats": {
            "intelligence": int(input("Entrez l'intelligence : ")),
            "strength": int(input("Entrez la force : ")),
            "speed": int(input("Entrez la vitesse : ")),
            "durability": int(input("Entrez la durabilité : ")),
            "power": int(input("Entrez la puissance : ")),
            "combat": int(input("Entrez le combat : ")),
        },
        "appearance": {
            "gender": input("Entrez le genre : "),
            "race": input("Entrez la race : "),
            "height": [input("Entrez la hauteur en feet : "), input("Entrez la hauteur en cm : ")],
            "weight": [input("Entrez le poids en lb : "), input("Entrez le poids en kg : ")],
            "eyeColor": input("Entrez la couleur des yeux : "),
            "hairColor": input("Entrez la couleur des cheveux : "),
        },
        "biography": {
            "fullName": input("Entrez le nom complet : "),
            "alterEgos": input("Entrez les alter egos : "),
            "aliases": [input("Entrez les alias (séparés par des virgules) : ")],
            "placeOfBirth": input("Entrez le lieu de naissance : "),
            "firstAppearance": input("Entrez la première apparition : "),
            "publisher": input("Entrez le éditeur : "),
            "alignment": input("Entrez l'alignement : "),
        },
        "work": {
            "occupation": input("Entrez l'occupation : "),
            "base": input("Entrez la base : "),
        },
        "connections": {
            "groupAffiliation": input("Entrez l'affiliation au groupe : "),
            "relatives": input("Entrez les relations : "),
        },
        "images": {
            "xs": input("Entrez le chemin de l'image XS : "),
            "sm": input("Entrez le chemin de l'image SM : "),
            "md": input("Entrez le chemin de l'image MD : "),
            "lg": input("Entrez le chemin de l'image LG : "),
        },
    }

    data.append(new_superhero)

    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=2)

    print(f"Le super héros {new_superhero['name']} a été ajouté avec succès.")



def delete_superhero(json_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)

    while True:
        superhero_identifier = input("Entrez le nom ou l'ID du super héros que vous souhaitez supprimer (0 pour quitter) : ")

        # Vérifier si l'utilisateur souhaite quitter
        if superhero_identifier == "0":
            print("Opération annulée. Aucun super héros n'a été supprimé.")
            break

        # Vérifier si l'identifiant est un nombre (ID) ou une chaîne de caractères (nom)
        if superhero_identifier.isdigit():
            superhero_identifier = int(superhero_identifier)
            field = "id"
        else:
            field = "name"

        # Rechercher le super-héros dans la liste
        found_superhero = None
        for superhero in data:
            if superhero[field] == superhero_identifier:
                found_superhero = superhero
                break

        # Si le super-héros est trouvé, le supprimer
        if found_superhero:
            data.remove(found_superhero)
            with open(json_file_path, "w") as file:
                json.dump(data, file, indent=2)
            print(f"Le super héros {found_superhero['name']} a été supprimé avec succès.")
            break
        else:
            print(f"Aucun super héros trouvé avec {field} : {superhero_identifier}. Veuillez réessayer.")


# Exemple d'utilisation :


#modify_superhero(json_file_path)
#add_superhero(json_file_path)
#delete_superhero(json_file_path)