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
    affinity = db.Column(db.String(64))
    color_palete = db.Column(db.String(64))
    home_region = db.Column(db.String(64))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    #  image_location = db.Column(db.String(64))


    
    fire_name = ['Pyro', 'Flare', 'Solaris', 'Crimson', 'Sclarlet', 'Amber', 'Ruby', 'Singe', 'Ingite', 'Inferno', 'Scorch', 'Blaze']
    water_name = ['Aqua', 'Cryo', 'Pluse', 'Tidal', 'Abyssal', 'Azure', 'Cerulean', 'Nautilus', 'Marine', 'Hydro', 'Tusunami', 'Wave', 'Mist']
    earth_name = ['Terra', 'Gaia', 'Gaea', 'Geo', 'Quake', 'Tremor', 'Seismic', 'Granite', 'Basalt', 'Obsidian', 'Ivory', 'Sylva']
    thunder_name = ['Volt', 'Storm', 'Tempest', 'Electro', 'Surge', 'Bolt', 'Static', 'Flash', 'Jolt', 'Boom', 'Rumble', 'Zap']
    poison_name = ['Toxin', 'Venom', 'Decay', 'Corrupt', 'Blight', 'Contagion', 'Plague', 'Scourge', 'Pestil', 'Nox', 'Septi', 'Viro', 'Tox', 'Rot', 'Decay']
    aura_name = ['Aura', 'Luster', 'Gleam', 'Glimmer', 'Twinkle', 'Sparkle', 'Dazzle', 'Glint', 'Beam', 'Ray', 'Shine', 'Radiant', 'Stardust']
    
    
    elements = ['Fire', 'Water', 'Earth', 'Thunder', 'Poison', 'Aura']
    affinity = ['Celestial', 'Deva', 'Etheral', 'Astral', 'Void', 'Nether', None]
    speices = ['Goblin', 'Fox', 'Wolf', 'Cat', 'Bird', 'Drake', 'Shark', 'Fairy', 'Golem', 'Spider', 'Griffin', 'Unicorn']

    
    wolf_name = ['fenris', 'lupin', 'lycan', 'warg', 'kin', 'fang', 'lobo']
    cat_name = ['felis','lynx', 'saber','purr', 'paw', 'patch', 'streak']
    drake_name = ['draco', 'serpent', 'wyrm', 'breath', 'scale', 'gorge']
    fox_name = ['kitsune', 'vulpes', 'renard', 'gumiho', 'fuchsi', 'huli']
    golem_name = ['maton', 'droid', 'borg', 'mech', 'bot']
    spider_name = ['weaver', 'spinner', 'crawler', 'stalker', 'lurker','widow', 'legs']
    bird_name = ['talon', 'feather', 'sparrow', 'crest', 'reign', 'claw']
    griffin_name = ['sphinx', 'chimaera', 'gaze', 'soar', 'guard', 'strike', 'wingbeast', 'aerie']
    unicorn_name = ['pegasus', 'alicorn', 'horn', 'steed', 'hoof', 'mane']
    shark_name = ['fin', 'gill', 'hide', 'hammerhead', 'orca', 'maw']
    fairy_name = ['pixie', 'dew', 'twinkle', 'veil' 'sprite', 'nymph', ]
    goblin_name = ['snag', 'itch', 'ling', 'rascal', 'gremlin', 'imp', 'tooth']
            


    def __init__(self, name, element1, element2, element3, species, affinity, color_palete,  \
                 home_region, height, weight, attack, defense, speed, image_location):
        self.name = name
        self.element1 = element1
        self.element2 = element2
        self.element3 = element3
        self.species = species
        self.affinity = affinity
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

    def generate_name(self):
        """
            Generates a random aetherios.
        """
        prefixes = self.fire_name + self.water_name + self.earth_name + self.thunder_name + self.poison_name + self.aura_name
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
    

