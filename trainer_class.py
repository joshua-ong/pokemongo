import pokemon_class

class trainer():
    # default constructor
    def __init__(self, pokemon1, pokemon2, pokemon3):
       self.p1 = pokemon1
       self.p2 = pokemon2
       self.p3 = pokemon3
       self.lost = False
       self.pokemoninplay = pokemon1

    def damage_update(self, qm):
        self.pokemoninplay.damage_update(qm)

    def energy_update(self):
        self.pokemoninplay.energy_update()