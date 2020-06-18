import numpy as np
import trainer_class as t_c
import pokemon_class as p_c

a = p_c.pokemon("pokemon/3.json")
b = p_c.pokemon("pokemon/6.json")
c = p_c.pokemon("pokemon/9.json")
t1 = t_c.trainer(a, b, c)
