from typing import NamedTuple

class Ingredient(NamedTuple):
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

def partitions(n: int, length: int):
    if length == 1:
        yield [n]
    else:
        for i in range(0, n+1):
            for partition in partitions(n-i, length-1):
                yield [i] + partition

def cookie_value(ingredients: list[Ingredient], counts: list[int]) -> int:
    if len(ingredients) != len(counts):
        return -1
    capacity: int = 0
    durability: int = 0
    flavor: int = 0
    texture: int = 0

    for ing, count in zip(ingredients, counts):
        capacity += ing.capacity*count
        durability += ing.durability*count
        flavor += ing.flavor*count
        texture += ing.texture*count

    return max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)

def calorie_count(ingredients: list[Ingredient], counts: list[int]) -> int:
    if len(ingredients) != len(counts):
        return -1
    
    return sum([ing.calories * count for ing, count in zip(ingredients, counts)])
    

def parse_line(line: str) -> Ingredient:
    line_split:list[str] = line.strip().split()
    ingredient = Ingredient(capacity=int(line_split[2][:-1]),
                            durability=int(line_split[4][:-1]),
                            flavor=int(line_split[6][:-1]),
                            texture=int(line_split[8][:-1]),
                            calories=int(line_split[10]))
    return ingredient

with open("input-15.txt") as f:
    ingredients: list[Ingredient] = [parse_line(line) for line in f]

#Part 1
max_score = 0

for partition in partitions(100, len(ingredients)):
    score = cookie_value(ingredients, partition)
    max_score = max(score, max_score)

print(max_score)

#Part 2
max_500cal_score = 0
for partition in partitions(100, len(ingredients)):
    score = cookie_value(ingredients, partition)
    if calorie_count(ingredients, partition) == 500:
        max_500cal_score = max(max_500cal_score, score)
print(max_500cal_score)