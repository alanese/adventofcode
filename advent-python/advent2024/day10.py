def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

#Solution via dynamic programming - if height 9, we're already at a peak and can't get to any others
#If not, identify neighbors that are valid next steps and count total reachable peaks from those
def reachable_peaks(x: int, y: int, grid: dict[tuple[int, int], int], known_values: dict[tuple[int, int], set[tuple[int, int]]] ) -> set[tuple[int, int]]:
    if (x,y) not in known_values:
        if grid[(x,y)] == 9:
            known_values[(x,y)] = {(x,y)}
        else:
            reachable: set[tuple[int, int]] = set()
            for n_x, n_y in get_neighbors(x,y):
                if (n_x, n_y) in grid and grid[(n_x, n_y)] - grid[(x, y)] == 1:
                    reachable |= reachable_peaks(n_x, n_y, grid, known_values)
            known_values[(x,y)] = reachable
    return known_values[(x,y)]

def count_trails(x: int, y: int, grid: dict[tuple[int, int], int], known_values: dict[tuple[int, int], int]) -> int:
    if (x,y) not in known_values:
        if grid[(x,y)] == 9:
            known_values[(x,y)] = 1
        else:
            paths: int = 0
            for n_x, n_y in get_neighbors(x,y):
                if (n_x, n_y) in grid and grid[(n_x, n_y)] - grid[(x,y)] == 1:
                    paths += count_trails(n_x, n_y, grid, known_values)
            known_values[(x,y)] = paths
    return known_values[(x,y)]

with open("input-10.txt") as f:
    data: list[list[int]] = [[int(x) for x in line.strip()] for line in f]

trailheads: list[tuple[int, int]] = []
grid: dict[tuple[int, int], int] = {}

for y, line in enumerate(data):
    for x, num in enumerate(line):
        grid[(x,y)] = num
        if num == 0:
            trailheads.append((x,y))

#Part 1
reachable: dict[tuple[int, int], set[tuple[int, int]]] = {}
total_score: int = 0
for x, y in trailheads:
    total_score += len(reachable_peaks(x, y, grid, reachable))
print(total_score)

#Part 2
paths: dict[tuple[int, int], int] = {}
total_score = 0
for x,y in trailheads:
    total_score += count_trails(x, y, grid, paths)
print(total_score)