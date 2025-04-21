

class Aetherion:
    def __init__(self, name, type1, type2, type3, species, element, color_palete,  \
                 region, height, weight, attack, defense, speed):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3
        self.species = species
        self.element = element
        self.color_palete = color_palete
        self.region = region
        self.height = height
        self.weight = weight
        self.attack = attack
        self.defense = defense
        self.speed = speed


    def get_name(self):
        return self.name
    
    