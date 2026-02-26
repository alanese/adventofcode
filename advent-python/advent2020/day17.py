from collections import Counter

def get_neighbors(x: int, y: int, z: int) -> set[tuple[int, int, int]]:
    return {(nx, ny, nz) for nx in range(x-1, x+2) for ny in range(y-1, y+2) for nz in range(z-1, z+2) if (nx,ny,nz) != (x,y,z)}

def get_neighbors_4d(x: int, y: int, z: int, w: int) -> set[tuple[int, int, int, int]]:
    return {(nx, ny, nz, nw) for nx in range(x-1, x+2) for ny in range(y-1, y+2) for nz in range(z-1, z+2) for nw in range(w-1, w+2) if (nx, ny, nz, nw) != (x,y,z,w)}

def iterate(current: set[tuple[int, int, int]], survive: list[int] = [2,3], awaken: list[int] = [3]) -> set[tuple[int, int, int]]:
    neighbor_counts: dict[tuple[int, int, int], int] = Counter()
    next: set[tuple[int, int, int]] = set()
    for x,y,z in current:
        for neighbor in get_neighbors(x,y,z):
            neighbor_counts[neighbor] += 1
    for (x,y,z), count in neighbor_counts.items():
        if (x,y,z) in current and count in survive or (x,y,z) not in current and count in awaken:
            next.add((x,y,z))
    return next

def iterate_4d(current: set[tuple[int, int, int, int]], survive: list[int] = [2,3], awaken: list[int] = [3]) -> set[tuple[int, int, int, int]]:
    neighbor_counts: dict[tuple[int, int, int, int], int] = Counter()
    next: set[tuple[int, int, int, int]] = set()
    for x,y,z,w in current:
        for neighbor in get_neighbors_4d(x,y,z,w):
            neighbor_counts[neighbor] += 1
    for (x,y,z,w), count in neighbor_counts.items():
        if (x,y,z,w) in current and count in survive or (x,y,z,w) not in current and count in awaken:
            next.add((x,y,z,w))
    return next
    
with open("input-17.txt") as f:
    data: list[str] = [line.strip() for line in f]

live_cells: set[tuple[int, int, int]] = set()
live_cells_4d: set[tuple[int, int, int, int]] = set()
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "#":
            live_cells.add((x, y, 0))
            live_cells_4d.add((x,y,0,0))

#Part 1
for _ in range(6):
    live_cells = iterate(live_cells)
print(len(live_cells))

#Part 2
for _ in range(6):
    live_cells_4d = iterate_4d(live_cells_4d)
print(len(live_cells_4d))