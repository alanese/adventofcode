def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

def distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

with open("input-20.txt") as f:
    data: list[str] = [line.strip() for line in f]

nodes: set[tuple[int, int]] = set()
blocks: set[tuple[int, int]] = set()
start_x: int = -1
start_y: int = -1
end_x: int = -1
end_y: int = -1

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "#":
            continue
        if char == "S":
            start_x = x
            start_y = y
        if char == "E":
            end_x = x
            end_y = y
        nodes.add((x,y))

path: list[tuple[int, int]] = [(start_x, start_y)]
while path[-1] != (end_x, end_y):
    for neighbor in get_neighbors(*path[-1]):
        if neighbor in nodes and (len(path) == 1 or neighbor != path[-2]):
            path.append(neighbor)
            break

#Did this with Bellman-Ford until I realized that the "maze" was a single path
#this is . . . faster
from_start: dict[tuple[int, int], int] = {node: index for index, node in enumerate(path)}
to_end: dict[tuple[int, int], int] = {node: index for index, node in enumerate(path[::-1])}

fair_time: int = from_start[(end_x, end_y)]
savings_threshold: int = 100

#Part 1
saved_count: int = 0
for node_1 in nodes:
    for dx in range(-2, 3):
        for dy in range(-(2-abs(dx)), 2-abs(dx)+1):
            node_2 = (node_1[0]+dx, node_1[1]+dy)
            if node_2 in nodes and distance(node_1, node_2) == 2:
                if fair_time - (from_start[node_1] + 2 + to_end[node_2]) >= savings_threshold:
                    saved_count += 1
print(saved_count)

#Part 2
saved_count = 0
for node_1 in nodes:
    for dx in range(-20, 21):
        for dy in range(-(20-abs(dx)), 20-abs(dx)+1):
            node_2 = (node_1[0]+dx, node_1[1]+dy)
            if node_2 in nodes and distance(node_1, node_2) <= 20:
                if fair_time - (from_start[node_1] + distance(node_1, node_2) + to_end[node_2]) >= savings_threshold:
                    saved_count += 1
print(saved_count)