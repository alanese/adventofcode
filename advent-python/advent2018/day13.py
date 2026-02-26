from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Train:
    next_id: int = 0
    def __init__(self: Train, x: int, y: int, direction: Direction):
        self.x: int = x
        self.y: int = y
        self.direction: Direction = direction
        self.next_intersection: int = 0
        self.id: int = Train.next_id
        Train.next_id += 1

    def move(self: Train):
        match self.direction:
            case Direction.NORTH:
                self.y -= 1
            case Direction.EAST:
                self.x += 1
            case Direction.SOUTH:
                self.y += 1
            case Direction.WEST:
                self.x -= 1

    def turn_left(self: Train):
        match self.direction:
            case Direction.NORTH:
                self.direction = Direction.WEST
            case Direction.EAST:
                self.direction = Direction.NORTH
            case Direction.SOUTH:
                self.direction = Direction.EAST
            case Direction.WEST:
                self.direction = Direction.SOUTH

    def turn_right(self: Train):
        match self.direction:
            case Direction.NORTH:
                self.direction = Direction.EAST
            case Direction.EAST:
                self.direction = Direction.SOUTH
            case Direction.SOUTH:
                self.direction = Direction.WEST
            case Direction.WEST:
                self.direction = Direction.NORTH

    def handle_turn(self: Train, rail: str):
        if rail == "|" or rail == "-":
            return
        elif rail == "\\":
            if self.direction in (Direction.NORTH, Direction.SOUTH):
                self.turn_left()
            else:
                self.turn_right()
        elif rail == "/":
            if self.direction in (Direction.NORTH, Direction.SOUTH):
                self.turn_right()
            else:
                self.turn_left()
        elif rail == "+":
            match self.next_intersection:
                case 0:
                    self.turn_left()
                case 1:
                    pass #go straight
                case 2:
                    self.turn_right()
            self.next_intersection = (self.next_intersection + 1) % 3


def collision(train: Train, others: list[Train]) -> tuple[bool, int]:
    for other in others:
        if train.id != other.id and train.x == other.x and train.y == other.y:
            return True, other.id
    return False, -1


with open("input-13.txt") as f:
    data: list[list[str]] = [list(line.strip("\n")) for line in f]

#Part 1

rails = [list(line) for line in data]
trains: list[Train] = []

for y, line in enumerate(rails):
    for x, char in enumerate(line):
        if char == "^":
            trains.append(Train(x, y, Direction.NORTH))
            line[x] = "|"
        elif char == ">":
            trains.append(Train(x, y, Direction.EAST))
            line[x] = "-"
        elif char == "v":
            trains.append(Train(x, y, Direction.SOUTH))
            line[x] = "|"
        elif char == "<":
            trains.append(Train(x, y, Direction.WEST))
            line[x] = "-"


collision_coords: tuple[int, int] = 0, 0
crashed: bool = False
while not crashed:
    trains.sort(key = lambda train: (train.y, train.x))
    for train in trains:
        train.move()
        #print(f"Moved {train.direction} to {train.x},{train.y}")
        if collision(train, trains)[0]:
            collision_coords = train.x, train.y
            crashed = True
            break

        train.handle_turn(rails[train.y][train.x])
        #print(f"Rail is {rails[train.y][train.x]}, turning to {train.direction}")

print(collision_coords)

#Part 2

rails = [list(line) for line in data]
trains: list[Train] = []
trains_by_id: list[Train] = []
Train.next_id = 0
for y, line in enumerate(rails):
    for x, char in enumerate(line):
        if char == "^":
            trains.append(Train(x, y, Direction.NORTH))
            trains_by_id.append(trains[-1])
            line[x] = "|"
        elif char == ">":
            trains.append(Train(x, y, Direction.EAST))
            trains_by_id.append(trains[-1])
            line[x] = "-"
        elif char == "v":
            trains.append(Train(x, y, Direction.SOUTH))
            trains_by_id.append(trains[-1])
            line[x] = "|"
        elif char == "<":
            trains.append(Train(x, y, Direction.WEST))
            trains_by_id.append(trains[-1])
            line[x] = "-"

running_trains: set[int] = set([train.id for train in trains])

crashed: bool = False
while len(running_trains) > 1:
    trains.sort(key = lambda train: (train.y, train.x))
    for train in trains:
        if train.id not in running_trains:
            continue
        train.move()
        #print(f"Moved {train.direction} to {train.x},{train.y}")
        collided, other = collision(train, [trains_by_id[i] for i in running_trains])
        if collided:
            #print(f"CRASH! Removing {train.id}, {other}")
            running_trains.remove(train.id)
            running_trains.remove(other)

        train.handle_turn(rails[train.y][train.x])
        #print(f"Rail is {rails[train.y][train.x]}, turning to {train.direction}")

#print(running_trains)
last_train: Train = trains_by_id[running_trains.pop()]
print(f"{last_train.x},{last_train.y}")