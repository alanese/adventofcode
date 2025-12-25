def get_neighbors(x: int, y: int, max_x: int, max_y: int) -> list[tuple[int, int]]:
    neighbors: list[tuple[int, int]] = []
    for new_x in range(max(x-1, 0), min(x+2, max_x+1)):
        for new_y in range(max(y-1, 0), min(y+2, max_y+1)):
            neighbors.append((new_x,new_y))
    neighbors.remove((x,y))
    return neighbors

DIRECTIONS: list[tuple[int, int]] = [ (-1,-1), (0,-1), (1,-1),
                                      (-1, 0),         (1, 0),
                                      (-1, 1), (0, 1), (1, 1)]
def get_visible_seats(x: int, y: int, grid: list[list[str]]) -> list[tuple[int, int]]:
    visible_seats: list[tuple[int, int]] = []
    for dx, dy in DIRECTIONS:
        cur_x: int = x+dx
        cur_y: int = y+dy
        while 0 <= cur_x < len(grid[0]) and 0 <= cur_y < len(grid):
            if grid[cur_y][cur_x] in ["#", "L"]:
                visible_seats.append((cur_x, cur_y))
                break
            cur_x += dx
            cur_y += dy
    return visible_seats

def step_p1(grid: list[list[str]]) -> list[list[str]]:
    new_grid: list[list[str]] = [["."] * len(grid[0]) for _ in range(len(grid))]
    for y in range(len(new_grid)):
        for x in range(len(new_grid[0])):
            if grid[y][x] == ".":
                continue
            neighbors: list[tuple[int, int]] = get_neighbors(x, y, len(new_grid[0])-1, len(new_grid)-1)
            occupied_count: int = 0
            for n_x, n_y in neighbors:
                if grid[n_y][n_x] == "#":
                    occupied_count += 1
            if grid[y][x] == "L":
                if occupied_count == 0:
                    new_grid[y][x] = "#"
                else:
                    new_grid[y][x] = "L"
            elif grid[y][x] == "#":
                if occupied_count >= 4:
                    new_grid[y][x] = "L"
                else:
                    new_grid[y][x] = "#"
    return new_grid

def step_p2(grid: list[list[str]]) -> list[list[str]]:
    new_grid: list[list[str]] = [["."] * len(grid[0]) for _ in range(len(grid))]
    for y in range(len(new_grid)):
        for x in range(len(new_grid[0])):
            if grid[y][x] == ".":
                continue
            neighbors: list[tuple[int, int]] = get_visible_seats(x, y, grid)
            occupied_count: int = 0
            for n_x, n_y in neighbors:
                if grid[n_y][n_x] == "#":
                    occupied_count += 1
            if grid[y][x] == "L":
                if occupied_count == 0:
                    new_grid[y][x] = "#"
                else:
                    new_grid[y][x] = "L"
            elif grid[y][x] == "#":
                if occupied_count >= 5:
                    new_grid[y][x] = "L"
                else:
                    new_grid[y][x] = "#"
    return new_grid

with open("input-11.txt") as f:
    grid: list[list[str]] = [list(line.strip()) for line in f]

prev_grid: list[list[str]] = []
curr_grid = grid

while prev_grid != curr_grid:
    prev_grid = curr_grid
    curr_grid = step_p1(prev_grid)

occupied_count: int = 0
for row in curr_grid:
    occupied_count += row.count("#")
print(occupied_count)

#Part 2
prev_grid = []
curr_grid = grid
while prev_grid != curr_grid:
    prev_grid = curr_grid
    curr_grid = step_p2(prev_grid)

occupied_count: int = 0
for row in curr_grid:
    occupied_count += row.count("#")
print(occupied_count)