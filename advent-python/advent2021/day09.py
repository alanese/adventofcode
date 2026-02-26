from collections import Counter
from math import prod

def low_neighbor(x: int, y: int, heightmap: dict[tuple[int, int], int]) -> tuple[int, int]:
    return min((x,y), (x+1,y), (x-1,y), (x,y+1), (x,y-1), key = lambda pt: heightmap.get(pt, 10))

def get_basin(x: int, y: int, heightmap: dict[tuple[int, int], int], known_basins: dict[tuple[int, int], tuple[int, int]]) -> tuple[int, int]:
    if (x,y) in known_basins:
        return known_basins[(x,y)]
    elif heightmap[(x,y)] == 9:
        return -1,-1
    else:
        low_x, low_y = low_neighbor(x,y, heightmap)
        if (low_x, low_y) == (x,y):
            known_basins[(x,y)] = (x,y)
            return x,y
        else:
            return get_basin(low_x, low_y, heightmap, known_basins)
        
with open("input-09.txt") as f:
    data: list[str] = [line.strip() for line in f]
                 
heightmap: dict[tuple[int, int], int] = {}
for y, line in enumerate(data):
    for x, digit in enumerate(line):
        heightmap[(x,y)] = int(digit)

#Part 1
low_risk: int = 0
for (x,y), value in heightmap.items():
    if value == 9:
        continue
    low = low_neighbor(x, y, heightmap)
    if (x,y) == low:
        low_risk += value+1

print(low_risk)

#Part 2
known_basins: dict[tuple[int, int], tuple[int, int]] = {}
for x,y in heightmap:
    known_basins[(x,y)] = get_basin(x, y, heightmap, known_basins)
basin_sizes: dict[tuple[int, int], int] = Counter(known_basins.values())
del basin_sizes[(-1,-1)]
three_max: list[int] = sorted(list(basin_sizes.values()))[-3:]
print(prod(three_max))