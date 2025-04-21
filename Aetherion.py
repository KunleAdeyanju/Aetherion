

class Aetherion:
    def __init__(self, name, type1, type2, type3, species, element, color_palete,  \
                 region, height, weight, attack, defense, speed, image_location):
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
        self.image_location = image_location


    def get_name(self):
        return self.name
    
    def get_types(self):
        return (self.type1, self.type2, self.type3)
    
    def get_species(self):
        return self.species
    
    def get_element(self):
        return self.element
    
    def get_color_palete(self):
        return self.color_palete
    
    def get_region(self):
        return self.region
    
    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight 
    
    def get_attack(self):
        return self.attack
    
    def get_defence(self):
        return self.speed
    
    def get_image_location(self):
        pass