GRID_SERIAL_NUMBER: int = 7403
GRID_SIZE = 300

def compute_power_level(x: int, y: int) -> int:
    rack_id: int = x+10
    power_level: int = rack_id * y
    power_level += GRID_SERIAL_NUMBER
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    return power_level

#Part 1
max_square_power: int = -45
max_power_x: int = -1
max_power_y: int = -1

for x in range(1, GRID_SIZE-1):
    for y in range(1, GRID_SIZE-1):
        square_power: int = sum([compute_power_level(i, j) for i in range(x, x+3) for j in range(y, y+3)])
        if square_power > max_square_power:
            max_square_power = square_power
            max_power_x = x
            max_power_y = y

print(f"{max_power_x},{max_power_y}")

#Part 2
max_square_power = GRID_SIZE * GRID_SIZE * -5
max_power_x: int = -1
max_power_y: int = -1
max_power_size: int = -1

for x in range(1, GRID_SIZE+1):
    for y in range(1, GRID_SIZE+1):
        square_power: int = compute_power_level(x, y)
        if square_power > max_square_power:
            max_square_power = square_power
            max_power_x = x
            max_power_y = y
            max_power_size = 1
        for size in range(2, GRID_SIZE-max(x,y)):
            for i in range(x, x+size):
                square_power += compute_power_level(i, y+size-1)
            for j in range(y, y+size-1):
                square_power += compute_power_level(x+size-1, j)
            if square_power > max_square_power:
                max_square_power = square_power
                max_power_x = x
                max_power_y = y
                max_power_size = size

print(f"{max_power_x},{max_power_y},{max_power_size}")