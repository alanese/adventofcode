#Octopus at x,y flashes; return total number of flashes, including current and any induced
def process_flash(x: int, y: int, grid: list[list[int]], threshold: int = 10) -> int:
    flash_count: int = 1
    for next_x in range(max(x-1, 0), min(len(grid[y])-1, x+1)+1):
        for next_y in range(max(y-1, 0), min(len(grid)-1, y+1)+1):
            if (x,y) != (next_x, next_y):
                grid[next_y][next_x] += 1
                if grid[next_y][next_x] == threshold:
                    flash_count += process_flash(next_x, next_y, grid, threshold)
    return flash_count

FLASH_THRESHOLD: int = 10
with open("input-11.txt") as f:
    data: list[list[int]] = [ [int(x) for x in line.strip()] for line in f]

working_data: list[list[int]] = [line[:] for line in data]

#Part 1
flash_count: int = 0
step: int = 0
while step < 100:
    step += 1
    for y in range(len(working_data)):
        for x in range(len(working_data[y])):
            working_data[y][x] += 1
            if working_data[y][x] == FLASH_THRESHOLD:
                flash_count += process_flash(x, y, working_data, FLASH_THRESHOLD)
    for y in range(len(working_data)):
        for x in range(len(working_data[y])):
            if working_data[y][x] >= FLASH_THRESHOLD:
                working_data[y][x] = 0

print(flash_count)

#Part 2
all_flash: bool = False
while not all_flash:
    all_flash = True
    step += 1
    for y in range(len(working_data)):
        for x in range(len(working_data[y])):
            working_data[y][x] += 1
            if working_data[y][x] == FLASH_THRESHOLD:
                process_flash(x, y, working_data, FLASH_THRESHOLD)
    for y in range(len(working_data)):
        for x in range(len(working_data[y])):
            if working_data[y][x] >= FLASH_THRESHOLD:
                working_data[y][x] = 0
            else:
                all_flash = False
print(step)