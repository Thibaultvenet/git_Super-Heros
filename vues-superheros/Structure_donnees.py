import json

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
    superhero_list = SuperHeroList()

    with open(file_path, "r") as file:
        data = json.load(file)
        for superhero_data in data:
            superhero = SuperHero(superhero_data)
            superhero_list.add_superhero(superhero)

    return superhero_list

# Exemple d'utilisation :
json_file_path = "all.json"
superhero_list = load_superheroes_from_json(json_file_path)

# Accéder à la liste de super-héros
for superhero in superhero_list.superheroes:
    print(superhero.images.xs)
