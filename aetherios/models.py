from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
import random

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

    flame_name = [ ]

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

    def generate_name():
        """
            Generates a random aetherios.
        """
        prefixes = ["Aqua", "Pyro", "Terra", "Electro", "Sylva", "Nocti", "Aero", "Chrono", "Cryo", "Meca", "Fanto", "Lumi", "Umbra", "Soni", "Vibra", "Spectro",
                    "Flare", "Frost", "Storm", "Shadow", "Radiant", "Celestial", "Dusk", "Dawn", "Echo", "Rumble", "Static", "Tempest", "Twilight", "Aurora",
                    "Blitz", "Comet", "Ember", "Gale", "Horizon", "Nebula", "Onyx", "Pulse", "Quasar", "Solaris", "Tidal", "Zenith", "Astral", "Crimson", "Emerald",
                    "Ivory", "Obsidian", "Scarlet", "Violet", "Azure", "Cerulean", "Jade", "Amber", "Opal", "Quartz", "Ruby", "Sapphire", "Topaz"]
        suffixes = ["drake", "wing", "horn", "claw", "tail", "strike", "shade", "beam", "frost", "drive", "geist", "flare", "howl", "pulse", "surge", "nova", "bloom", "shield",
                    "fang", "scale", "talon", "venom", "wisp", "gaze", "roar", "song", "dancer", "weaver", "rider", "walker", "watcher", "warden", "slayer", "bringer",
                    "caller", "shaper", "binder", "breaker", "champion", "conqueror", "defender", "destroyer", "guardian", "herald", "hunter", "knight", "master",
                    "paladin", "ranger", "savior", "sovereign", "titan", "vanquisher", "voyager", "zephyr", "blaze", "cascade", "cyclone", "dusk", "ember", "frostbite",
                    "hurricane", "nightfall", "sunburst", "thunderclap", "twilight"]
        

        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)

        return f"{prefix}{suffix}"  # No number

class ImageGen(db.Model):

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

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64))
    password_hash = db.Column(db.Text)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_password_hash(self):
        return self.password_hash
    def set_password_hash(self, password_hash):
        self.password_hash = password_hash
    

