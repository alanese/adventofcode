from math import atan2

def taxicab_distance(p1: tuple[int, int], p2: tuple[int, int]):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

with open("input-06.txt") as f:
    data = [line.strip() for line in f]

#Part 1
points: list[tuple[int, int]] = []

for line in data:
    split_line: list[str] = line.split(", ")
    points.append( (int(split_line[0]), int(split_line[1])) )

min_x: int = points[0][0]
max_x: int = points[0][0]
min_y: int = points[0][1]
max_y: int = points[0][1]
for point in points:
    min_x = min(min_x, point[0])
    max_x = max(max_x, point[0])
    min_y = min(min_y, point[1])
    max_y = max(max_y, point[1])

init_min_distance: int = 10*(max_x - min_x) + 10*(max_y - min_y)
edge_closest: set[tuple[int, int]] = set()
start_x = min_x
finish_x = max_x
start_y = min_y
finish_y = max_y
voronoi_sizes = {point: 0 for point in points}
for check_x in range(start_x, finish_x+1):
    for check_y in range(start_y, finish_y+1):
        min_distance: int = init_min_distance
        min_distance_double: bool = False
        min_point: tuple[int, int] = (-1, -1)
        for point in points:
            check_distance: int = taxicab_distance( (check_x, check_y), point)
            if check_distance < min_distance:
                min_distance = check_distance
                min_point = point
                min_distance_double = False
            elif check_distance == min_distance:
                min_distance_double = True
        if not min_distance_double:
            voronoi_sizes[min_point] += 1
            if check_x == min_x or check_x == max_x or check_y == min_y or check_y == max_y:
                edge_closest.add(min_point)

#Any point that is the closest point to any edge point has an infinite cell (under taxicab)
for point in edge_closest:
    del voronoi_sizes[point]

print(max(voronoi_sizes.values()))


#Part 2

points: list[tuple[int, int]] = []

for line in data:
    split_line: list[str] = line.split(", ")
    points.append( (int(split_line[0]), int(split_line[1])) )

DISTANCE_THRESHOLD: int = 10000

min_x: int = points[0][0]
max_x: int = points[0][0]
min_y: int = points[0][1]
max_y: int = points[0][1]
for point in points:
    min_x = min(min_x, point[0])
    max_x = max(max_x, point[0])
    min_y = min(min_y, point[1])
    max_y = max(max_y, point[1])

start_x = min_x - DISTANCE_THRESHOLD // len(points)
finish_x = max_x + DISTANCE_THRESHOLD // len(points)
start_y = min_y - DISTANCE_THRESHOLD // len(points)
finish_y = max_y + DISTANCE_THRESHOLD // len(points)

close_point_count: int = 0
for check_x in range(start_x, finish_x+1):
    for check_y in range(start_y, finish_y+1):
        total_distance: int = sum([taxicab_distance(point, (check_x, check_y)) for point in points])
        if total_distance < DISTANCE_THRESHOLD:
            close_point_count += 1
print(close_point_count)