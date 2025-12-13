from typing import List, Tuple

def on_neighbors(x: int, y: int, grid: List[List[bool]]) -> int:
    count = -1 if grid[x][y] else 0 #compensate for if (x,y) is on
    for check_x in range(max(0, x-1), min(x+2, len(grid))):
        for check_y in range(max(0, y-1), min(y+2, len(grid[check_x]))):
            if grid[check_x][check_y]:
                count += 1
    return count

def new_value(x: int, y: int, grid: List[List[bool]], stay_on: List[int], turn_on: List[int]) -> bool:
    neighbors = on_neighbors(x, y, grid)
    current = grid[x][y]
    return (current and neighbors in stay_on) or (not current and neighbors in turn_on)

def step(grid: List[List[bool]], stay_on: List[int], turn_on: List[int]) -> List[List[bool]]:
    new_grid: List[List[bool]] = []
    for x in range(len(grid)):
        next_line: List[bool] = []
        for y in range(len(grid[x])):
            next_line.append(new_value(x, y, grid, stay_on, turn_on))
        new_grid.append(next_line)
    return new_grid

def print_grid(grid: List[List[bool]], true: str = "#", false: str = "."):
    for line in grid:
        for entry in line:
            print(true if entry else false, end='')
        print()

STAY_ON: List[int] = [2,3]
TURN_ON: List[int] = [3]

with open("input-18.txt") as f:
    grid_p1: List[List[bool]] = []
    grid_p2: List[List[bool]] = []
    for line in f:
        grid_p1.append([x == "#" for x in line.strip()])
        grid_p2.append([x == "#" for x in line.strip()])

max_x: int = len(grid_p1)-1
max_y: int = len(grid_p1[0])-1
stuck_on: List[Tuple[int, int]] = [ (0, 0), (0, max_y), (max_x, 0), (max_x, max_y)]
for x, y in stuck_on:
    grid_p2[x][y] = True
for i in range(100):
    grid_p1 = step(grid_p1, STAY_ON, TURN_ON)
    grid_p2 = step(grid_p2, STAY_ON, TURN_ON)
    for x,y in stuck_on:
        grid_p2[x][y] = True

print(sum([x for line in grid_p1 for x in line]))
print(sum([x for line in grid_p2 for x in line]))
