from collections import Counter
from typing import NamedTuple

class HexCoord(NamedTuple):
    q: int
    r: int

    def neighbors(self: HexCoord) -> tuple[HexCoord, ...]:
        return (HexCoord(self.q, self.r-1), HexCoord(self.q+1, self.r-1),
                HexCoord(self.q-1, self.r), HexCoord(self.q+1, self.r),
                HexCoord(self.q-1, self.r+1), HexCoord(self.q, self.r+1))

def parse_directions(directions: str) -> list[str]:
    res: list[str] = []
    while len(directions) > 0:
        if directions[0] in ["e", "w"]:
            res.append(directions[0])
            directions = directions[1:]
        elif directions[:2] in ["se", "sw", "ne", "nw"]:
            res.append(directions[:2])
            directions = directions[2:]
        else:
            raise ValueError(f"Invalid start token {directions}")
    return res

def find_coordinate(directions: list[str]) -> HexCoord:
    q: int = 0
    r: int = 0
    for step in directions:
        match step:
            case "e":
                q += 1
            case "w":
                q -= 1
            case "ne":
                q += 1
                r -= 1
            case "nw":
                r -= 1
            case "se":
                r += 1
            case "sw":
                q -= 1
                r += 1
            case _:
                raise ValueError("Invalid step: {step}")
    return HexCoord(q,r)

with open("input-24.txt") as f:
    data: list[str] = [line.strip() for line in f]

flips: dict[HexCoord, int] = Counter()

#Part 1
for line in data:
    coord: HexCoord = find_coordinate(parse_directions(line))
    flips[coord] += 1

black_tiles: set[HexCoord] = {coord for coord in flips if flips[coord]%2 != 0}
print(len(black_tiles))

#Part 2
for _ in range(100):
    neighbor_count: dict[HexCoord, int] = Counter()
    for tile in black_tiles:
        if tile not in neighbor_count:
            neighbor_count[tile] = 0
        for neighbor in tile.neighbors():
            neighbor_count[neighbor] += 1

    old_black_tiles: set[HexCoord] = black_tiles
    black_tiles = set()
    for tile, count in neighbor_count.items():
        if tile not in old_black_tiles and count == 2:
            black_tiles.add(tile)
        elif tile in old_black_tiles and (count == 1 or count == 2):
            black_tiles.add(tile)

print(len(black_tiles))
