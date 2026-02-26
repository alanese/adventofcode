def is_visible(x: int, y: int, grid: list[list[int]]) -> bool:
    value: int = grid[y][x]
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        next_x: int = x+dx
        next_y: int = y+dy
        visible: bool = True
        while 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
            if grid[next_y][next_x] >= value:
                visible = False
                break
            next_x += dx
            next_y += dy
        if visible:
            return True
    return False

def scenic_score(x: int, y: int, grid: list[list[int]]) -> int:
    value: int = grid[y][x]
    score: int = 1
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        next_x: int = x+dx
        next_y: int = y+dy
        direction_score: int = 0
        while 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
            direction_score += 1
            if grid[next_y][next_x] >= value:
                break
            next_x += dx
            next_y += dy
        score *= direction_score
    return score

with open("input-08.txt") as f:
    data: list[list[int]] = [[int(x) for x in line.strip()] for line in f]

#Parts 1, 2
visible_count: int = 0
max_score: int = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if is_visible(x, y, data):
            visible_count += 1
        score: int = scenic_score(x, y, data)
        if score > max_score:
            max_score = score
print(visible_count)
print(max_score)