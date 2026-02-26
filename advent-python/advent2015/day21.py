from typing import List, NamedTuple, Tuple
from math import ceil
from itertools import chain, combinations
from enum import Enum

class Stats(NamedTuple):
    name:str
    cost:int
    damage:int
    armor:int

weapons: List[Stats] = [Stats("Dagger", 8, 4, 0),
                       Stats("Shortsword", 10, 5, 0),
                       Stats("Warhammer", 25, 6, 0),
                       Stats("Longsword", 40, 7, 0),
                       Stats("Greataxe", 74, 8, 0)]

armors: List[Stats] = [Stats("Leather", 13, 0, 1),
                       Stats("Chainmail", 31, 0, 2),
                       Stats("Splintmail", 53, 0, 3),
                       Stats("Bandedmail", 75, 0, 4),
                       Stats("Platemail", 102, 0, 5)]

rings: List[Stats] = [Stats("Damage +1", 25, 1, 0),
                    Stats("Damage +2", 50, 2, 0),
                    Stats("Damage +3", 100, 3, 0),
                    Stats("Defense +1", 20, 0, 1),
                    Stats("Defense +2", 40, 0, 2),
                    Stats("Defense +3", 80, 0, 3)]

def total_gear(weapon: Stats, armor: Tuple[Stats, ...], rings:Tuple[Stats, ...]) -> Stats:
    total_cost = weapon.cost + sum(a.cost for a in armor) + sum([r.cost for r in rings])
    total_damage = weapon.damage + sum(a.damage for a in armor) + sum([r.damage for r in rings])
    total_armor = weapon.armor + sum(a.armor for a in armor) + sum([r.armor for r in rings])
    return Stats("Total", total_cost, total_damage, total_armor)

def total_any_gear(gear: Tuple[Stats, ...]) -> Stats:
    total_cost = sum([item.cost for item in gear])
    total_damage = sum([item.damage for item in gear])
    total_armor = sum([item.armor for item in gear])
    return Stats("Total", total_cost, total_damage, total_armor)

def subsets(items: List):
    yield ()
    for i, item in enumerate(items):
        for subset in subsets(items[i+1:]):
            yield (item,) + subset

def print_gear_set(gear: Tuple[Stats, ...]):
    print(", ".join([item.name for item in gear]))

def player_wins(player_hp:int, player_gear:Stats, boss_hp:int, boss_gear:Stats) -> bool:
    boss_damage = max(1, boss_gear.damage - player_gear.armor)
    player_damage = max(1, player_gear.damage - boss_gear.armor)
    boss_death_round = ceil(boss_hp / player_damage)
    player_death_round = ceil(player_hp / boss_damage)
    return boss_death_round <= player_death_round

with open("input-21.txt") as f:
    boss_hp: int = int(f.readline().strip().split()[-1])
    boss_damage: int = int(f.readline().strip().split()[-1])
    boss_armor: int = int(f.readline().strip().split()[-1])

boss_gear = Stats("Boss", 0, boss_damage, boss_armor)

min_win_cost:int = sum([w.cost for w in weapons] + [a.cost for a in armors] + [r.cost for r in rings]) + 1
max_lose_cost = -1
for weapon in weapons:
    for armor in chain(combinations(armors, 0), combinations(armors, 1)):
        for ring_set in chain(combinations(rings, 0), combinations(rings, 1), combinations(rings, 2)):
            total = total_gear(weapon, armor, ring_set)
            player_winner: bool = player_wins(100, total, boss_hp, boss_gear)
            if total.cost < min_win_cost and player_winner:
                min_win_cost = total.cost
            if total.cost > max_lose_cost and not player_winner:
                max_lose_cost = total.cost
print(min_win_cost)
print(max_lose_cost)

max_lose_cost = -1
