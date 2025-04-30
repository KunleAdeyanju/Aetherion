from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
import random

db = SQLAlchemy()

class Aetherios(db.Model):
    # building the database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    element1 = db.Column(db.String(64))
    # element2 = db.Column(db.String(64))
    # element3 = db.Column(db.String(64))
    species = db.Column(db.String(64))
    # affinity = db.Column(db.String(64))
    # color_palete = db.Column(db.String(64))
    # home_region = db.Column(db.String(64))
    # height = db.Column(db.Float)
    # weight = db.Column(db.Float)
    # attack = db.Column(db.Integer)
    # defense = db.Column(db.Integer)
    # speed = db.Column(db.Integer)
    #  image_location = db.Column(db.String(64))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'element1': self.element1,
            'species': self.species
        }


    
    fire_name = ['Pyro', 'Flare', 'Solaris', 'Crimson', 'Scarlet', 'Amber', 'Ruby', 'Singe', 'Ingite', 'Inferno', 'Scorch', 'Blaze']
    water_name = ['Aqua', 'Cryo', 'Pulse', 'Tidal', 'Abyssal', 'Azure', 'Cerulean', 'Nautilus', 'Marine', 'Hydro', 'Tsunami', 'Wave', 'Mist']
    earth_name = ['Terra', 'Gaia', 'Gaea', 'Geo', 'Quake', 'Tremor', 'Seismic', 'Granite', 'Basalt', 'Obsidian', 'Ivory', 'Sylva']
    thunder_name = ['Volt', 'Storm', 'Tempest', 'Electro', 'Surge', 'Bolt', 'Static', 'Flash', 'Jolt', 'Boom', 'Rumble', 'Zap']
    poison_name = ['Toxin', 'Venom', 'Decay', 'Corrupt', 'Blight', 'Contagion', 'Plague', 'Scourge', 'Pestil', 'Nox', 'Septi', 'Viro', 'Tox', 'Rot', 'Decay']
    aura_name = ['Aura', 'Luster', 'Gleam', 'Glimmer', 'Twinkle', 'Sparkle', 'Dazzle', 'Glint', 'Beam', 'Ray', 'Shine', 'Radiant', 'Stardust']
    
    elemental_dict = {
            'Fire' : fire_name,
            'Water' : water_name,
            'Earth' : earth_name,
            'Thunder' : thunder_name,
            'Poison' : poison_name,
            'Aura' : aura_name
    }

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

    flame_locations = [ 'The Obsidian Forge', 'Crimson Expanse', 'Emberwood Grove']
    water_locations = [ 'Obsidian Depths', 'Veridian Mire', 'Sunken City of Thalassa']
    earth_locations = ['Stonehaven Highland', 'The Great Bedrock', 'Terraforged Mines']
    thunder_locations = ['Solara Peaks', 'Skyfire Citadel', 'Voltaic Vales']
    poison_locations = ['Valley of Blight','The Bog', 'Ruins of Miasma']
    aura_locations = ['Astral Abyss', 'Starlit Glades', 'Radiant Forests', 'Luminous Plains']

    demenor = ['Majestic', 'Fierce', 'Calm', 'Laid Back', 'Angry', 'Jealous', 'Cautious', 'Fearful', 'Gentle Protetor', 'Intimidating', 'Cunning']
    def get_key_by_value(my_dict, target_value):
        """
            Returns the first key in the dictionary that matches the target value.
            If no key is found, returns None.
        """
        for key, value in my_dict.items():
            if target_value in value:
                return key
        
    # def __init__(self, name, element1, element2, element3, ):
    #     """
    #         species, affinity, color_palete,  \
    #              home_region, height, weight, attack, defense, speed, image_location
    #     """
    #     self.name = name
    #     self.element1 = element1
    #     self.element2 = element2
    #     self.element3 = element3
    #     # self.species = species
    #     # self.affinity = affinity
    #     # self.color_palete = color_palete
    #     # self.home_region = home_region
    #     # self.height = height
    #     # self.weight = weight
    #     # self.attack = attack
    #     # self.defense = defense
    #     # self.speed = speed
    #     # self.image_location = image_location

    # defining getters and setters      

    def generate_name(self):
        """
            Generates a random aetherios.
        """
        prefixes = self.fire_name + self.water_name + self.earth_name + self.thunder_name + self.poison_name + self.aura_name
        suffixes = self.wolf_name + self.cat_name + self.drake_name + self.fox_name + self.golem_name + self.spider_name + \
            self.bird_name + self.griffin_name + self.unicorn_name + self.shark_name + self.fairy_name + self.goblin_name
        
        # Check if name already exists in the database
        while True:
            prefix = random.choice(prefixes)
            suffix = random.choice(suffixes)
            name = prefix + suffix
            if Aetherios.query.filter_by(name=name).first() is not None:
                self.name = name
                return (prefix, suffix)
    
    def determine_element(self, name_prefix):
        """
            Determines the element of the aetherios.
        """
        # Every aetherios has at least one element
        # 40% chance of having 2 elements
        # 20% chance of having 3 elements
        if random.random() < 0.4:
            num_elm = 2
            if random.random() < 0.2:
                num_elm = 3
        else:
            num_elm = 1

        first_element = self.get_key_by_value(self.elemental_dict, name_prefix)
        unique_elements = random.sample(self.elements.remove(first_element), num_elm-1)

        if num_elm == 1:
            
            self.element1 = first_element
            self.element2 = None
            self.element3 = None
        elif num_elm == 2:
            
            self.element1 = first_element
            self.element2 = unique_elements[0]
            self.element3 = None
        else:   
            self.element1 = first_element
            self.element2 = unique_elements[0]
            self.element3 = unique_elements[1]

        
        elements = [self.element1, self.element2, self.element3]
        return elements
    

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
    
    # def get_username(self):
    #     return self.username
    # def set_username(self, username):
    #     self.username = username
    # def get_email(self):
    #     return self.email
    # def set_email(self, email):
    #     self.email = email
    # def get_password_hash(self):
    #     return self.password_hash
    # def set_password_hash(self, password_hash):
    #     self.password_hash = password_hash
    