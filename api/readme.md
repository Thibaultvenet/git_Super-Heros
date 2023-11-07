
# API

Multiple universes superheroes open-source REST API

## References
- [glossary](glossary.md)

###  url de base
`https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api`



### [routes](#routes-1)
- [`/all.json`](#alljson)
- [`/id`](#id)
- [`/powerstats`](#powerstats)
- [`/appearance`](#appearance)
- [`/biography`](#biography)
- [`/connections`](#connections)
- [`/work`](#work)

### [images](#images-1)

----

## Routes

##### `/all.json`
Tous les superheroes dans un seul fichier JSON

eg. [`/all.json`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/all.json)

##### `/id`
Obtenir toutes les informations d'un superhero à l'aide de son id

eg. [`/id/1.json`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/id/1.json)
```json
{
  "id": 1,
  "name": "A-Bomb",
  "slug": "1-a-bomb",
  "powerstats": {
    "intelligence": 38,
    "strength": 100,
    "speed": 17,
    "durability": 80,
    "power": 24,
    "combat": 64
  },
  "appearance": {
    "gender": "Male",
    "race": "Human",
    "height": [
      "6'8",
      "203 cm"
    ],
    "weight": [
      "980 lb",
      "441 kg"
    ],
    "eyeColor": "Yellow",
    "hairColor": "No Hair"
  },
  "biography": {
    "fullName": "Richard Milhouse Jones",
    "alterEgos": "No alter egos found.",
    "aliases": [
      "Rick Jones"
    ],
    "placeOfBirth": "Scarsdale, Arizona",
    "firstAppearance": "Hulk Vol 2 #2 (April, 2008) (as A-Bomb)",
    "publisher": "Marvel Comics",
    "alignment": "good"
  },
  "work": {
    "occupation": "Musician, adventurer, author; formerly talk show host",
    "base": "-"
  },
  "connections": {
    "groupAffiliation": "Hulk Family; Excelsior (sponsor), Avengers (honorary member); formerly partner of the Hulk, Captain America and Captain Marvel; Teen Brigade; ally of Rom",
    "relatives": "Marlo Chandler-Jones (wife); Polly (aunt); Mrs. Chandler (mother-in-law); Keith Chandler, Ray Chandler, three unidentified others (brothers-in-law); unidentified father (deceased); Jackie Shorr (alleged mother; unconfirmed)"
  },
  "images": {
    "xs": "xs/1-a-bomb.jpg",
    "sm": "sm/1-a-bomb.jpg",
    "md": "md/1-a-bomb.jpg",
    "lg": "lg/1-a-bomb.jpg"
  }
}
```

##### `/powerstats`
Obtenir les __powerstats__ d'un superhero à l'aide de son id


eg. [`/powerstats/1.json`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/powerstats/1.json)
```json
{
  "intelligence": 38,
  "strength": 100,
  "speed": 17,
  "durability": 80,
  "power": 24,
  "combat": 64
}
```

##### `/appearance`
Obtenir __appearance__ d'un superhero à l'aide de son id


eg. [`/appearance/1.json`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/appearance/1.json)
```json
{
  "gender": "Male",
  "race": "Human",
  "height": [
    "6'8",
    "203 cm"
  ],
  "weight": [
    "980 lb",
    "441 kg"
  ],
  "eyeColor": "Yellow",
  "hairColor": "No Hair"
}
```

##### `/biography`
Obtenir __biography__ d'un superhero à l'aide de son id


eg. [`/biography/1.json`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/biography/1.json)
```json
{
  "fullName": "Richard Milhouse Jones",
  "alterEgos": "No alter egos found.",
  "aliases": [
    "Rick Jones"
  ],
  "placeOfBirth": "Scarsdale, Arizona",
  "firstAppearance": "Hulk Vol 2 #2 (April, 2008) (as A-Bomb)",
  "publisher": "Marvel Comics",
  "alignment": "good"
}
```

##### `/connections`
Obtenir __connections__ d'un superhero à l'aide de son id

eg. [`/connections/1.json`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/connections/1.json)
```json
{
  "groupAffiliation": "Hulk Family; Excelsior (sponsor), Avengers (honorary member); formerly partner of the Hulk, Captain America and Captain Marvel; Teen Brigade; ally of Rom",
  "relatives": "Marlo Chandler-Jones (wife); Polly (aunt); Mrs. Chandler (mother-in-law); Keith Chandler, Ray Chandler, three unidentified others (brothers-in-law); unidentified father (deceased); Jackie Shorr (alleged mother; unconfirmed)"
}
```

##### `/work`
Obtenir __work__ d'un superhero à l'aide de son id

eg. [`/work/1.json`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/work/1.json)
```json
{
  "occupation": "Musician, adventurer, author; formerly talk show host",
  "base": "-"
}
```


## Images
Obtenir l'image d'un superhero à l'aide de son id

- Thumb (~32x48)
[`/images/xs/1-a-bomb.jpg`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/xs/1-a-bomb.jpg)

- Small (~160x240)
[`/images/sm/1-a-bomb.jpg`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/sm/1-a-bomb.jpg)

- Medium (~320x480)
[`/images/md/1-a-bomb.jpg`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/md/1-a-bomb.jpg)

- Large (~480x640)
[`/images/lg/1-a-bomb.jpg`](https://raw.githubusercontent.com/INSA-UPHF/git-superhero/master/api/lg/1-a-bomb.jpg)
