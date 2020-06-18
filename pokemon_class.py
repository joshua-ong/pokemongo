import numpy as np
import csv
import json


###
# pokemon includes
# self.name = name of pokemon
# self.type = type of pokemon, this will affect how vulnerable this pokemon is to type attack
# self.health = hit points until faint
# self.qm = quick move that a pokemon uses every turn. A pokemon can only have one move.
# self.cm = charge move that pokemon can use energy to use. A pokemon can have two moves.
###
class pokemon():
    # default constructor
    def __init__(self, path):
        """CSV FILE"""
        # with open(path, newline='') as csvfile:
        #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #     count = 0
        #     for row in spamreader:
        #         row = row[0][:-1]  # gets rid of the comma
        #         if(count == 0):
        #             self.name = row
        #         if (count == 1):
        #             self.name = row
        #         print(', '.join(row))
        #         count += 1
        with open(path) as f:
            data = json.load(f)
            print(data)
        self.name = data["name"]
        self.type = data["type"]
        self.health = data["health"]
        self.qm = data["qm"]
        self.cm = data["cm"]
        self.energy = 0

    # a method for printing data members
    def damage_update(self, qm, debug=False):
        dmg = qm[0][2]
        if (debug):
            print(self.health)
        self.health = self.health - dmg
        if (debug):
            print(self.health)

    def energy_update(self, debug=False):
        eng = self.qm[0][1]
        if (debug):
            print("energy: " + self.energy)
        self.energy = self.energy + eng
        if (debug):
            print("energy: " + self.energy)

# path = "pokemon/3.json"
# a = pokemon(path)
# print("caveman")
