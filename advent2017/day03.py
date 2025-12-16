from collections import defaultdict

def ulam_coord_square_x(index: int) -> int:
    index = index - 1
    if index % 2 == 0:
        return index // 2
    else:
        return -(index // 2)
    
def ulam_coords(i: int) -> tuple[int, int]:
    sqrt_floor: int = int(i**(1/2))
    square_floor: int = sqrt_floor ** 2
    square_floor_x: int
    square_floor_y: int
    square_floor_x, square_floor_y = ulam_coord_square_x(sqrt_floor), ulam_coord_square_x(sqrt_floor + 1)
    if square_floor == i:
        return square_floor_x, square_floor_y
    elif sqrt_floor % 2 == 0:
        if i - square_floor <= sqrt_floor + 1:
            return square_floor_x - 1, square_floor_y - (i - (square_floor+1))
        else:
            return square_floor_x - 1 + i - (square_floor + sqrt_floor + 1), square_floor_y - sqrt_floor
    else:
        if i - square_floor <= sqrt_floor + 1:
            return square_floor_x + 1, square_floor_y + (i - (square_floor + 1))
        else:
            return square_floor_x + 1 - (i - (square_floor + sqrt_floor + 1)), square_floor_y + sqrt_floor
        
def sum_neighbors(grid: dict[tuple[int, int], int], x: int, y: int) -> int:
    total = 0
    for x_offset in (-1, 0, 1):
        for y_offset in (-1, 0, 1):
            if x_offset != 0 or y_offset != 0:
                total += grid[(x+x_offset, y+y_offset)]
    return total

PUZZLE_INPUT = 312051
ulam_x: int
ulam_y: int
ulam_x, ulam_y = ulam_coords(PUZZLE_INPUT)
print(abs(ulam_x) + abs(ulam_y))

##part 2
new_ulam: defaultdict[tuple[int, int], int] = defaultdict(int)

i = 1
next_value = 1
ulam_x, ulam_y = 0,0
while next_value <= PUZZLE_INPUT:
    new_ulam[(ulam_x, ulam_y)] = next_value
    i += 1
    ulam_x, ulam_y = ulam_coords(i)
    next_value = sum_neighbors(new_ulam, ulam_x, ulam_y)
    print(f"({ulam_x}, {ulam_y}): {next_value}")

print(next_value)