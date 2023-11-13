import json
import sys


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

class SuperHeroList:
    def __init__(self):
        self.superheroes = []

    def add_superhero(self, superhero):
        self.superheroes.append(superhero)

def load_superheroes_from_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}.")
        return None

    if not isinstance(data, list):
        print("Error: JSON data should be a list of superheroes.")
        return None

    superhero_list = SuperHeroList()

    for superhero_data in data:
        if not isinstance(superhero_data, dict):
            print("Error: Each superhero data should be a dictionary.")
            return None

        try:
            superhero = SuperHero(superhero_data)
            superhero_list.add_superhero(superhero)
        except KeyError as ke:
            print(f"Error: Missing key {ke} in superhero data.")
            return None
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}.")
            return None

        # Valider la structure des données pour chaque super-héros
        if not all(key in superhero_data for key in ["id", "name", "slug", "powerstats", "appearance", "biography", "work", "connections", "images"]):
            print("Error: Incomplete superhero data structure.")
            return None

        # Ajoutez des validations supplémentaires pour chaque section (powerstats, appearance, etc.) si nécessaire.

    return superhero_list


# Exemple d'utilisation :
json_file_path = "api/all.json"
superhero_list = load_superheroes_from_json(json_file_path)

if superhero_list is not None:
    # Les données ont été chargées avec succès
    # Accéder à la liste de super-héros
    print("Les données ont été chargées avec succès, voici le nom de tous les super héros :")
    for superhero in superhero_list.superheroes:
        print(superhero.name)
    pass
else:
    # Il y a eu une erreur lors du chargement des données
    sys.exit(1)
    pass

def modify_superhero(json_file_path):
    superhero_name = input("Entrez le nom du super héros à modifier : ")

    with open(json_file_path, "r") as file:
        data = json.load(file)

    superhero_found = False  # Indicateur pour vérifier si le super-héros a été trouvé

    for superhero_data in data:
        if superhero_data["name"] == superhero_name:
            superhero_found = True  # Marquer que le super-héros a été trouvé
            print(f"Modification des données pour {superhero_name}")
            field_path = input("Entrez le chemin du champ (exemple, 'name' or 'powerstats.speed') : ")

            # Split the field path into individual fields
            field_path_list = field_path.split('.')
            current_data = superhero_data

            # Traverse the nested structure to find the target field
            for field in field_path_list[:-1]:
                if field in current_data:
                    current_data = current_data[field]
                else:
                    print(f"{field} n'est pas un champ valide pour {superhero_name}")
                    return

            # Check if the last field in the path exists in the current_data
            last_field = field_path_list[-1]
            if last_field not in current_data:
                print(f"Erreur: {last_field} n'est pas un champ valide pour {superhero_name}.")
                return

            # Modify the final field (except for the last field in the path)
            new_value = input(f"Entrez la nouvelle valeur pour {last_field} : ")

            # Convert new value to integer if the original field is an integer
            if isinstance(current_data[last_field], int):
                new_value = int(new_value)

            current_data[last_field] = new_value
            print(f"{last_field} a été modifié par {new_value}")

    if not superhero_found:
        print(f"Erreur: Aucun super héros trouvé avec le nom {superhero_name}.")

    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=2)


# Exemple d'utilisation :
modify_superhero(json_file_path)

