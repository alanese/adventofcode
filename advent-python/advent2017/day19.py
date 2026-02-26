from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

def step(x: int, y: int, direction: Direction) -> tuple[int, int]:
    match direction:
        case Direction.NORTH:
            return x, y-1
        case Direction.SOUTH:
            return x, y+1
        case Direction.EAST:
            return x+1, y
        case Direction.WEST:
            return x-1, y
        
def turn(x: int, y: int, start_direction: Direction, grid: list[str]) -> Direction:
    if start_direction == Direction.NORTH or start_direction == Direction.SOUTH:
        if grid[y][x-1] == " ":
            return Direction.EAST
        else:
            return Direction.WEST
    else:
        if grid[y-1][x] == " ":
            return Direction.SOUTH
        else:
            return Direction.NORTH

with open("input-19.txt") as f:
    data: list[str] = [line.strip("\n") for line in f]

CAPITALS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VALID_SYMBOLS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-|+"

x: int = data[0].index("|")
y: int = 0
direction: Direction = Direction.SOUTH
seen: str = ""
steps: int = 0

while data[y][x] != " ":
    steps += 1
    x, y = step(x, y, direction)
    if data[y][x] == "+":
        direction = turn(x, y, direction, data)
    elif data[y][x] in CAPITALS:
        seen += data[y][x]
print(seen)
print(steps)