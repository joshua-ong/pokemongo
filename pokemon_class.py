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
    def __init__(self,path):
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
        self.energy = 0

    # a method for printing data members
    def print_Geek(self):
        print("lame")

# path = "pokemon/3.json"
# a = pokemon(path)
# print("caveman")
