from typing import NamedTuple
from math import isqrt

class Orientation:
    def __init__(self: Orientation, id: int, grid: list[str], orientation: str = "e"):
        self.id: int = id
        self.grid: list[str] = grid
        self.orientation: str = orientation
        self.north: str = self.grid[0]
        self.south: str = self.grid[-1]
        self.east: str = "".join(row[-1] for row in self.grid)
        self.west: str = "".join(row[0] for row in grid)

    #Return copy rotated 90 degrees clockwise
    def r(self: Orientation) -> Orientation:
        return Orientation(self.id, [ "".join([line[i] for line in self.grid])[::-1] for i in range(len(self.grid))], orientation=self.orientation+"r")
    
    #Return copy flipped across vertical axis
    def f(self: Orientation) -> Orientation:
        return Orientation(self.id, [line[::-1] for line in self.grid], self.orientation+"f")
    
class Piece(NamedTuple):
    id: int
    orientations: list[Orientation]

def next_coord(x: int, y: int, row_size: int) -> tuple[int, int]:
    if x < row_size-1:
        return x+1, y
    else:
        return 0, y+1

def parse_tile(tile: list[str]) -> Piece:
    id: int = int(tile[0][:-1].split()[1])
    tile  = tile[1:]
    base: Orientation = Orientation(id, tile)
    return Piece(id, [base, base.r(), base.r().r(), base.r().r().r(), base.f(), base.f().r(), base.f().r().r(), base.f().r().r().r()])

def fill_grid(grid: dict[tuple[int, int], Orientation], x: int, y: int, row_size: int, remaining_pieces: set[int], piece_dict: dict[int, Piece]) -> dict[tuple[int, int], Orientation]:
    if len(remaining_pieces) == 0:
        return grid
    else:
        next_x, next_y = next_coord(x, y, row_size)
        for piece in remaining_pieces:
            for orientation in piece_dict[piece].orientations:
                if (x==0 or orientation.west == grid[x-1,y].east) and (y==0 or orientation.north == grid[x, y-1].south):
                    filled: dict[tuple[int, int], Orientation] = fill_grid(grid | {(x,y): orientation}, next_x, next_y, row_size, remaining_pieces - {piece}, piece_dict)
                    if len(filled) != 0:
                        return filled
        return {}

def locations(grid: list[str], target: str) -> set[tuple[int, int]]:
    res: set[tuple[int, int]] = set()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == target:
                res.add((x,y))
    return res

with open("input-20.txt") as f:
    data: list[str] = [line.strip() for line in f]

SEA_MONSTER: set[tuple[int, int]] = locations(["                  # ",
                                               "#    ##    ##    ###",
                                               " #  #  #  #  #  #   "], "#")


piece_ids: set[int] = set()
piece_dict: dict[int, Piece] = {}
working: list[str] = data[:]
while "" in working:
    next: list[str] = working[:working.index("")]
    working = working[working.index("")+1:]
    next_piece: Piece = parse_tile(next)
    piece_ids.add(next_piece.id)
    piece_dict[next_piece.id] = next_piece
grid_size: int = isqrt(len(piece_dict))
piece_size = len(list(piece_dict.values())[0].orientations[0].grid)

#Part 1
grid: dict[tuple[int, int], Orientation] = fill_grid({}, 0, 0, grid_size, piece_ids, piece_dict)
print(grid[(0,0)].id * grid[(0,grid_size-1)].id * grid[(grid_size-1, 0)].id * grid[(grid_size-1, grid_size-1)].id)

#Part 2
full_grid: list[str] = ["Grid 0:"]
for i in range(grid_size):
    for y in range(1, piece_size-1):
        row: str = ""
        for j in range(grid_size):
            row += grid[(j,i)].grid[y][1:-1]
        full_grid.append(row)

image: Piece = parse_tile(full_grid)
image_size = len(image.orientations[0].grid)
for orientation in image.orientations:
    hashes = locations(orientation.grid, "#")
    working_hashes = hashes.copy()
    for dx in range(image_size):
        for dy in range(image_size):
            serpent: set[tuple[int, int]] = {(x+dx, y+dy) for (x,y) in SEA_MONSTER}
            if serpent <= hashes:
                working_hashes -= serpent
    if working_hashes != hashes:
        print(len(working_hashes))
        break