with open("input-03.txt") as f:
    data: list[str] = [line.strip() for line in f]

def count_trees(grid: list[str], x_delta: int, y_delta: int) -> int:
    x_pos: int = x_delta % len(grid[0])
    y_pos: int = y_delta
    tree_count: int = 0
    while y_pos < len(grid):
        if grid[y_pos][x_pos] == "#":
            tree_count += 1
        x_pos = (x_pos + x_delta) % len(grid[0])
        y_pos += y_delta
    return tree_count
#Part 1
print(count_trees(data, 3, 1))

#Part 2
print(count_trees(data, 1, 1) * count_trees(data, 3, 1) * count_trees(data, 5, 1) * count_trees(data, 7, 1) * count_trees(data, 1, 2))