def first_nonzero(xs):
    for i, x in enumerate(xs):
        if x != 0:
            return i
    return -1

def flipped_y(grid):
    return [row for row in grid[::-1]]

def flipped_x(grid):
    return [ [ x for x in row[::-1]] for row in grid ]

def transpose(grid):
    return [ [row[i] for row in grid] for i in range(len(grid[0]))]

def translate(squares, x_offset, y_offset):
    return set([(x+x_offset, y+y_offset) for x,y in squares])

def locations_of(grid, char):
    r = set()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == char:
                r.add((x, y))
    return r

def get_orientations(grid):
    r = []

    for y in (True, False):
        for x in (True, False):
            for t in (True, False):
                next = grid
                if y:
                    next = flipped_y(next)
                if x:
                    next = flipped_x(next)
                if t:
                    next = transpose(next)
                r.append(next)
    return r

def parse_piece(piece):
    index = int(piece[0][:-1])
    grid = [list(row) for row in piece[1:]]
    orientations = get_orientations(grid)
    location_orientations = []
    for o in orientations:
        o = locations_of(o, "#")
        if o not in location_orientations:
            location_orientations.append(o)

    return index, location_orientations

def parse_region(region):
    x_pos = region.index("x")
    colon_pos = region.index(":")
    x = int(region[:x_pos])
    y = int(region[x_pos+1:colon_pos])
    present_counts = [int(c) for c in region[colon_pos+2:].split()]
    return x, y, present_counts

def fits(free, piece):
    for x,y in piece:
        if (x,y) not in free:
            return False
    return True

def presents_fit(free_squares, max_x, max_y, shapes, required):
    if all([rest == 0 for rest in required]):
        return True
    next_index = first_nonzero(required)
    next_piece = shapes[next_index]
    required_after = required.copy()
    required_after[next_index] -= 1
    for shape in next_piece:
        for x in range(max_x):
            for y in range(max_y):
                offset_piece = translate(shape, x, y)
                if fits(free_squares, offset_piece):
                    if presents_fit(free_squares - offset_piece, max_x, max_y, shapes, required_after):
                        return True
                
    return False

with open("input-12.txt") as r:
    lines = [line.strip() for line in r.readlines()]

pieces = []
while "" in lines:
    blank = lines.index("")
    _, ps = parse_piece(lines[:blank])
    pieces.append(ps)
    lines = lines[blank+1:]

sizes = [len(piece[0]) for piece in pieces]

valid_count = 0
for index, line in enumerate(lines, start=1):
    region = parse_region(line)
    empty_region = {(x,y) for x in range(region[0]) for y in range(region[1])}
    if sum([x * y for x,y in zip(sizes, region[2])]) > region[0] * region[1]:
        continue
    elif presents_fit(empty_region, region[0]-1, region[1]-1, pieces, region[2]):
        valid_count += 1

print(valid_count)
