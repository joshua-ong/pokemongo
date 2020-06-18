import pokemon_class as p_c
import trainer_class as t_c

a = p_c.pokemon("pokemon/3.json")
b = p_c.pokemon("pokemon/6.json")
c = p_c.pokemon("pokemon/9.json")
t1 = t_c.trainer(a, b, c)
t2 = t_c.trainer(a, b, c)

count = 0
while (t1.lost == False and t2.lost == False and count <= 240):
    # update damage and energy
    t1.damage_update(t2.pokemoninplay.qm)
    t1.energy_update()
    t2.damage_update(t1.pokemoninplay.qm)
    t2.energy_update()

    # charge moves

    # switch pokemon

    count = count + 1  # 240 turns/seconds
