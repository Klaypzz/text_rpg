#from entity import Entity

#class Human(Entity):
#    def __init__(self):
#        pass
##(Import and inherit class)##

class Entity:
    def __init__(self, name, race, role):
        self.name = name
        self.race = race
        self.role = role

    ### Global Variables ###
    races = [
        'Human',
        'Elf',
        'Dwarf',
    ]
    roles =  [
        'Knight',
        'Mage',
        'Archer'
    ]