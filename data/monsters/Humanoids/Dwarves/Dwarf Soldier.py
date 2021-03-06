dwarf_soldier = genMonster("Dwarf Soldier", 71, 6014)
dwarf_soldier.health(135, healthmax=135)
dwarf_soldier.type("blood")
dwarf_soldier.defense(armor=9, fire=1.05, earth=0.9, energy=1, ice=1, holy=1, death=1.05, physical=1, drown=1)
dwarf_soldier.experience(70)
dwarf_soldier.speed(170)
dwarf_soldier.behavior(summonable=360, hostile=True, illusionable=True, convinceable=360, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
dwarf_soldier.walkAround(energy=1, fire=1, poison=1)
dwarf_soldier.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
dwarf_soldier.voices("Hail Durin!")
dwarf_soldier.melee(70)
dwarf_soldier.distance(60, ANIMATION_BOLT, chance(21))
dwarf_soldier.loot( ("soldier helmet", 11.5), ("white mushroom", 60.5, 2), ("shovel", 10.0), ("chain armor", 7.25), (2148, 100, 12), ("bolt", 100, 7), ("dwarven shield", 3.0), ("crossbow", 3.25), ("piercing bolt", 7.5, 3), ("battle axe", 2.5), ("axe ring", 0.25), ("iron ore", 0.25, 3) )