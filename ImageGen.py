

class ImageGen:
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
    

