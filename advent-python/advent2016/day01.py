from typing import Set, Tuple
from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def right_turn(self: Direction) -> Direction:
        return Direction((self.value + 1) % 4)
    def left_turn(self: Direction) -> Direction:
        return Direction((self.value - 1) % 4)
    
def move(direction: Direction, x: int, y: int, distance: int=1) -> Tuple[int, int]:
    match direction:
        case Direction.NORTH:
            return x, y+distance
        case Direction.EAST:
            return x+distance, y
        case Direction.SOUTH:
            return x, y-distance
        case Direction.WEST:
            return x-distance, y

def handle_instruction(instruction: str, direction: Direction, x: int, y: int) -> Tuple[Direction, int, int]:
    distance = int(instruction[1:])
    if instruction[0] == "R":
        direction = direction.right_turn()
    elif instruction[0] == "L":
        direction = direction.left_turn()
    else:
        print(f"Error: Illegal command {instruction}")
    x,y = move(direction, x, y, distance)
    return direction, x, y


x: int = 0
y: int = 0
direction: Direction = Direction.NORTH
with open("input-01.txt") as f:
    commands = f.read()

for command in commands.split(", "):
    direction, x, y = handle_instruction(command, direction, x, y)

print(abs(x) + abs(y))

#----------

orders = []
for command in commands.split(", "):
    orders.append(command[0])
    orders += ["G"] * int(command[1:])

print(orders)

x = 0
y = 0
direction = Direction.NORTH
seen: Set[Tuple[int, int]] = set()
seen.add((x,y))
for order in orders:
    match order:
        case "L":
            direction = direction.left_turn()
        case "R":
            direction = direction.right_turn()
        case "G":
            x,y = move(direction, x, y)
            if (x,y) in seen:
                break
            seen.add((x,y))

print(abs(x) + abs(y))