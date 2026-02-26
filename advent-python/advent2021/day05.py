from collections import Counter, namedtuple

Coordinate = namedtuple("Coordinate", ["x", "y"])

def parse_line(line: str) -> tuple[Coordinate, Coordinate]:
    left, _, right = line.partition(" -> ")
    x1, _, y1 = left.partition(",")
    coord_1: Coordinate = Coordinate(int(x1), int(y1))
    x2, _, y2 = right.partition(",")
    coord_2: Coordinate = Coordinate(int(x2), int(y2))
    return coord_1, coord_2

def sign(num: int) -> int:
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

def get_line_coords(p1: Coordinate, p2: Coordinate) -> set[Coordinate]:
    dx: int = sign(p2.x - p1.x)
    dy: int = sign(p2.y - p1.y)
    next_coord = p1
    line_set: set[Coordinate] = set()
    while next_coord != p2:
        line_set.add(next_coord)
        next_coord = Coordinate(next_coord.x + dx, next_coord.y + dy)
    line_set.add(next_coord)
    return line_set

with open("input-05.txt") as f:
    data: list[str] = [line.strip() for line in f]

lines: list[tuple[Coordinate, Coordinate]] = [parse_line(line) for line in data]

#Part 1
vent_count: dict[Coordinate, int] = Counter()
for p1, p2 in lines:
    if p1.x == p2.x or p1.y == p2.y:
        for vent in get_line_coords(p1, p2):
            vent_count[vent] += 1
print(len([x for x in vent_count if vent_count[x] > 1]))

#Part 2
vent_count = Counter()
for p1, p2 in lines:
    for vent in get_line_coords(p1, p2):
        vent_count[vent] += 1
print(len([x for x in vent_count if vent_count[x] > 1]))