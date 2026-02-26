#Utility functions
def rotate_list(start: list, distance: int) -> list:
    if len(start) <= 1:
        return start
    distance = len(start) - (distance % len(start)) # I think? to rotate right?
    return start[distance:] + start[:distance]

def show_grid(grid: list[list[bool]], on: str = "#", off: str = "."):
    for row in grid:
        print("".join([on if pixel else off for pixel in row]))

# Functions to execute operations
def handle_rect(grid: list[list[bool]], x_size: int, y_size: int):
    for x in range(x_size):
        for y in range(y_size):
            grid[y][x] = True

def handle_rotate_row(grid: list[list], row: int, distance:int):
    if len(grid) == 0:
        return
    distance = distance % len(grid[0])
    grid[row] = rotate_list(grid[row], distance)

def handle_rotate_column(grid: list[list], col: int, distance: int):
    col_list = rotate_list([row[col] for row in grid], distance)
    for i in range(len(grid)):
        grid[i][col] = col_list[i]

#Functions to parse commands
def parse_rect(command: str) -> tuple[int, int]:
    coords = command.split('x')
    return int(coords[0]), int(coords[1])

def parse_rotate(command:list[str]) -> tuple[int, int]:
    rowcol = int(command[0][2:])
    distance = int(command[-1])
    return rowcol, distance

ROWS = 6
COLUMNS = 50

grid: list[list[bool]] = []
for _ in range(ROWS):
    grid.append([False] * COLUMNS)

with open("input-08.txt") as f:
    for command in f:
        command = command.strip().split()
        if command[0] == "rect":
            x, y = parse_rect(command[1])
            handle_rect(grid, x, y)
        elif command[1] == "row":
            row, dist = parse_rotate(command[2:])
            handle_rotate_row(grid, row, dist)
        elif command[1] == "column":
            col, dist = parse_rotate(command[2:])
            handle_rotate_column(grid, col, dist)

on = sum([sum(row) for row in grid])
print(on)
show_grid(grid)