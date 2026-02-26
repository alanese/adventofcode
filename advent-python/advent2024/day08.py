from collections import defaultdict

with open("input-08.txt") as f:
    data: list[str] = [line.strip() for line in f]

antennas: dict[str, list[tuple[int, int]]] = defaultdict(list)

max_x = len(data[0]) - 1
max_y = len(data) - 1

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != ".":
            antennas[char].append((x,y))

#Part 1
antinodes: set[tuple[int, int]] = set()

for frequency in antennas:
    for i, (x1, y1) in enumerate(antennas[frequency]):
        for (x2,y2) in antennas[frequency][i+1:]:
            x_a1, y_a1 = x2 + (x2-x1), y2 + (y2-y1)
            x_a2, y_a2 = x1 + (x1-x2), y1 + (y1-y2)
            if 0 <= x_a1 <= max_x and 0 <= y_a1 <= max_y:
                antinodes.add( (x2 + (x2-x1), y2 + (y2-y1)) )
            if 0 <= x_a2 <= max_x and 0 <= y_a2 <= max_y:
                antinodes.add( (x1 + (x1-x2), y1 + (y1-y2)) )

print(len(antinodes))

antinodes = set()
for frequency in antennas:
    for i, (x1, y1) in enumerate(antennas[frequency]):
        for x2,y2 in antennas[frequency][i+1:]:
            dx: int = x2 - x1
            dy: int = y2 - y1
            new_x: int = x1
            new_y: int = y1
            while 0 <= new_x <= max_x and 0 <= new_y <= max_y:
                antinodes.add((new_x, new_y))
                new_x += dx
                new_y += dy
            new_x = x1 - dx
            new_y = y1 - dy
            while 0 <= new_x <= max_x and 0 <= new_y <= max_y:
                antinodes.add((new_x, new_y))
                new_x -= dx
                new_y -= dy
print(len(antinodes))