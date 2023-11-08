class SuperHero:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.slug = data["slug"]

# Exemple d'utilisation de la classe SuperHero
# Supposons que vous ayez le JSON sous forme de dictionnaire
data = {
    "id": 0,
    "name": "",
    "slug": "",
}
SuperHero = SuperHero(data)



class powerstats:
    def __init__(self, data):
        self.intelligence = data["intelligence"]
        self.strength = data["strength"]
        self.speed = data["speed"]
        self.durability = data["durability"]
        self.power = data["power"]
        self.combat = data["combat"]

# Exemple d'utilisation de la classe Appearance
# Supposons que vous ayez le JSON sous forme de dictionnaire
data = {
    "intelligence": 0,
    "strength": 0,
    "speed": 0,
    "durability": 0,
    "power": 0,
    "combat": 0
}

# Créez une instance de Appearance en utilisant les données JSON
powerstats_data = powerstats(data)




class Appearance:
    def __init__(self, data):
        self.gender = data["gender"]
        self.race = data["race"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.eyeColor = data["eyeColor"]
        self.hairColor = data["hairColor"]

# Exemple d'utilisation de la classe Appearance
# Supposons que vous ayez le JSON sous forme de dictionnaire
data = {
    "gender": "",
    "race": "",
    "height": ["0'0", "0 cm"],
    "weight": ["0 lb", "0 kg"],
    "eyeColor": "",
    "hairColor": ""
}







class Biography:
    def __init__(self, data):
        self.fullName = data["fullName"]
        self.alterEgos = data["alterEgos"]
        self.aliases = data["aliases"]
        self.placeOfBirth = data["placeOfBirth"]
        self.firstAppearance = data["firstAppearance"]
        self.publisher = data["publisher"]
        self.alignment = data["alignment"]

# Exemple d'utilisation de la classe Biography
# Supposons que vous ayez le JSON sous forme de dictionnaire
data = {
    "fullName": "",
    "alterEgos": "",
    "aliases": [""],
    "placeOfBirth": "",
    "firstAppearance": "",
    "publisher": "",
    "alignment": ""
}

# Créez une instance de Biography en utilisant les données JSON
biography_data = Biography(data)





class Work:
    def __init__(self, data):
        self.occupation = data["occupation"]
        self.base = data["base"]

# Exemple d'utilisation de la classe Work
# Supposons que vous ayez le JSON sous forme de dictionnaire
data = {
    "occupation": "",
    "base": ""
}

# Créez une instance de Work en utilisant les données JSON
work_data = Work(data)





class Connections:
    def __init__(self, data):
        self.groupAffiliation = data["groupAffiliation"]
        self.relatives = data["relatives"]

# Exemple d'utilisation de la classe Connections
# Supposons que vous ayez le JSON sous forme de dictionnaire
data = {
    "groupAffiliation": "",
    "relatives": ""
}

# Créez une instance de Connections en utilisant les données JSON
connections_data = Connections(data)





class Images:
    def __init__(self, data):
        self.xs = data["xs"]
        self.sm = data["sm"]
        self.md = data["md"]
        self.lg = data["lg"]

# Exemple d'utilisation de la classe Images
# Supposons que vous ayez le JSON sous forme de dictionnaire
data = {
    "xs": "",
    "sm": "",
    "md": "",
    "lg": ""
}

# Créez une instance de Images en utilisant les données JSON
images_data = Images(data)
