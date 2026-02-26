from itertools import batched

PRIORITIES: dict[str, int] = {char: i for i, char in enumerate("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}

def shared_item(rucksack: str) -> str:
    left: str = rucksack[:len(rucksack)//2]
    right: set = set(rucksack[len(rucksack)//2:])
    for char in left:
        if char in right:
            return char
    return "_"

def shared_p2(r1: str, r2: str, r3: str) -> str:
    r2_set: set[str] = set(r2)
    r3_set: set[str] = set(r3)
    for char in r1:
        if char in r2_set and char in r3_set:
            return char
    return "_"

with open("input-03.txt") as f:
    data: list[str] = [line.strip() for line in f]

total: int = 0
for rucksack in data:
    total += PRIORITIES[shared_item(rucksack)]
print(total)

total = 0
for r1, r2, r3 in batched(data, 3):
    total += PRIORITIES[shared_p2(r1, r2, r3)]
print(total)