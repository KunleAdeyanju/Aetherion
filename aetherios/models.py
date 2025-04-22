from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class Aetherios(db.Model):
    # building the database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    type1 = db.Column(db.String(64))
    type2 = db.Column(db.String(64))
    type3 = db.Column(db.String(64))
    species = db.Column(db.String(64))
    element = db.Column(db.String(64))
    color_palete = db.Column(db.String(64))
    home_region = db.Column(db.String(64))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    #  image_location = db.Column(db.String(64))

    def __init__(self, name, type1, type2, type3, species, element, color_palete,  \
                 home_region, height, weight, attack, defense, speed, image_location):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3
        self.species = species
        self.element = element
        self.color_palete = color_palete
        self.home_region = home_region
        self.height = height
        self.weight = weight
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.image_location = image_location

    # defining getters and setters

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_types(self):
        return (self.type1, self.type2, self.type3)
    
    def set_types(self, types): # types needs to be a tuples
        self.type1 = types[0]
        self.type2 = types[1]
        self.type3 = types[2]

    def get_species(self):
        return self.species
    
    def set_species(self, species):
        self.species = species

    def get_element(self):
        return self.element
    
    def set_element(self, element):
        self.element = element

    def get_color_palete(self):
        return self.color_palete
    
    def set_color_palete(self, colors):
        self.color_palete = colors

    def get_home_region(self):
        return self.home_region
    
    def set_home_region(self, home_region):
        self.home_region = home_region
    
    def get_height(self):
        return self.height
    
    def set_height(self, height):
        self.height = height

    def get_weight(self):
        return self.weight 
    
    def set_weight(self, weight):
        self.weight = weight
    
    def get_attack(self):
        return self.attack
    
    def set_attack(self, attack):
        self.attack = attack
    
    def get_defence(self):
        return self.speed
    
    def set_defence(self, defence):
        self.defense = defence
    
    # def get_image_location(self):
    #     pass

class ImageGen:

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    type1 = db.Column(db.String(64))
    type2 = db.Column(db.String(64))
    type3 = db.Column(db.String(64))
    species = db.Column(db.String(64))
    element = db.Column(db.String(64))
    color_palete = db.Column(db.String(64))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)

    def __init__(self, name, element, type1, type2, type3, species, color_palette, height, weight):
        self.name = name
        self.species = species
        self.element = element
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3
        self.color_palette = color_palette
        self.height = height
        self.weight = weight
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_types(self):
        return (self.type1, self.type2, self.type3)
    
    def get_species(self):
        return self.species
    
    def get_element(self):
        return self.element
    
    def get_color_palete(self):
        return self.color_palete
    
    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight 
    


