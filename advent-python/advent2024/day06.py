from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def right_turn(self: Direction) -> Direction:
        return Direction((self.value + 1) % 4)
    
    def delta(self: Direction) -> tuple[int, int]:
        match self:
            case Direction.NORTH:
                return (0,-1)
            case Direction.EAST:
                return (1,0)
            case Direction.SOUTH:
                return (0,1)
            case Direction.WEST:
                return (-1,0)

def step(guard_x: int, guard_y: int, current_direction: Direction, obstacles: set[tuple[int, int]]) -> tuple[int, int, Direction]:
    dx, dy = current_direction.delta()
    if (guard_x+dx, guard_y+dy) in obstacles:
        return guard_x, guard_y, current_direction.right_turn()
    else:
        return guard_x+dx, guard_y+dy, current_direction
    
def check_loop(x: int, y: int, max_x: int, max_y: int, direction: Direction, obstacles: set[tuple[int, int]]) -> bool:
    seen_states: set[tuple[int, int, Direction]] = set()
    while 0 <= x <= max_x and 0 <= y <= max_y:
        if (x,y,direction) in seen_states:
            return True
        else:
            seen_states.add((x,y,direction))
            x, y, direction = step(x, y, direction, obstacles)
    return False


with open("input-06.txt") as f:
    data: list[str] = [line.strip() for line in f]

max_x: int = len(data[0])-1
max_y: int = len(data)-1
init_x: int = -1
init_y: int = -1
obstacles: set[tuple[int, int]] = set()
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "^":
            init_x, init_y = x,y
        elif char == "#":
            obstacles.add((x,y))

start_direction: Direction = Direction.NORTH

#Part 1
guard_x: int = init_x
guard_y: int = init_y
current_direction: Direction = start_direction
visited: set[tuple[int, int]] = set()
while 0 <= guard_x <= max_x and 0 <= guard_y <= max_y:
    visited.add((guard_x, guard_y))
    guard_x, guard_y, current_direction = step(guard_x, guard_y, current_direction, obstacles)
print(len(visited))

#Part 2
count: int = 0
for x in range(max_x+1):
    for y in range(max_y+1):
        if (x,y) not in obstacles and (x,y) != (guard_x, guard_y) and check_loop(init_x, init_y, max_x, max_y, Direction.NORTH, obstacles | {(x,y)}):
            count += 1

print(count)