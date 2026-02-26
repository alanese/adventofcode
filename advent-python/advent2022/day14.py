from typing import NamedTuple

class Coordinate(NamedTuple):
    x: int
    y: int

def sign(n: int) -> int:
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1

def parse_pair(pair: str) -> Coordinate:
    x, y = pair.split(",")
    return Coordinate(int(x), int(y))

def points_to_line(p1: Coordinate, p2: Coordinate) -> set[Coordinate]:
    line: set[Coordinate] = set()
    line.add(p1)
    line.add(p2)
    dx: int = sign(p2.x - p1.x)
    dy: int = sign(p2.y - p1.y)
    next: Coordinate = Coordinate(p1.x + dx, p1.y+dy)
    while next not in line:
        line.add(next)
        next = Coordinate(next.x+dx, next.y+dy)
    return line

def parse_path(path_str: str) -> set[Coordinate]:
    path: list[Coordinate] = [parse_pair(pair) for pair in path_str.split(" -> ")]
    coords: set[Coordinate] = set()
    for i in range(len(path)-1):
        coords |= points_to_line(path[i], path[i+1])
    return coords

#Attempts to drop sand into the field from source coordinate
#Returns True if the sand came to rest, False if it fell out of bounds or failed to enter
#floor determines whether a floor exists at y = max_y+2
def drop_sand(source: Coordinate, blocked: set[Coordinate], max_y: int, floor: bool = False) -> bool:
    if source in blocked:
        return False
    else:
        sand: Coordinate = source
        while sand.y <= max_y:
            if Coordinate(sand.x, sand.y+1) not in blocked:
                sand = Coordinate(sand.x, sand.y+1)
            elif Coordinate(sand.x-1, sand.y+1) not in blocked:
                sand = Coordinate(sand.x-1, sand.y+1)
            elif Coordinate(sand.x+1, sand.y+1) not in blocked:
                sand = Coordinate(sand.x+1, sand.y+1)
            else:
                blocked.add(sand)
                return True
    if not floor:
        return False
    else:
        blocked.add(sand)
        return True

SOURCE: Coordinate = Coordinate(500, 0)

with open("input-14.txt") as f:
    data: list[str] = [line.strip() for line in f]

blocks: set[Coordinate] = set()
for line in data:
    blocks |= parse_path(line)

max_y = max(block.y for block in blocks)

#Part 1
sand_count: int = 0
while drop_sand(SOURCE, blocks, max_y):
    sand_count += 1

print(sand_count)

#Reset field
blocks = set()
for line in data:
    blocks |= parse_path(line)

#Part 2
sand_count: int = 0
while drop_sand(SOURCE, blocks, max_y, True):
    sand_count += 1
print(sand_count)