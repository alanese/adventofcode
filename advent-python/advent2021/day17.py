def sign(x: int) -> int:
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1
    
def max_x_distance(x_velocity: int) -> int:
    return x_velocity * (x_velocity+1) // 2

def target_area(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    line = line[13:]
    x_part, _, y_part = line.partition(", ")
    x_part = x_part[2:]
    y_part = y_part[2:]
    min_x, _, max_x = x_part.partition("..")
    min_y, _, max_y = y_part.partition("..")
    return (int(min_x), int(max_x)), (int(min_y), int(max_y))

def check_path(v_x: int, v_y: int, min_x: int, max_x: int, min_y: int, max_y: int) -> tuple[bool, int]:
    peak_y: int = 0
    x_pos: int = 0
    y_pos: int = 0
    while y_pos >= min_y:
        x_pos += v_x
        y_pos += v_y
        v_x -= sign(v_x)
        v_y -= 1
        if v_y == 0:
            peak_y = y_pos
        if min_x <= x_pos <= max_x and min_y <= y_pos <= max_y:
            return True, peak_y
    return False, peak_y

with open("input-17.txt") as f:
    data: str = f.read().strip()

#Parts 1 and 2
(min_x, max_x), (min_y, max_y) = target_area(data)

min_v_x: int = 0
while max_x_distance(min_v_x) < min_x:
    min_v_x += 1

peak_y: int = 0
hit_count: int = 0
for v_x in range(min_v_x, max_x+1):
    for v_y in range(min_y,2-min_y):
        ok, peak = check_path(v_x, v_y, min_x, max_x, min_y, max_y)
        if ok:
            hit_count += 1
            if peak > peak_y:
                peak_y = peak
print(peak_y)
print(hit_count)