from itertools import pairwise, permutations

with open("input-09.txt") as f:
    data: list[str] = [line.strip() for line in f]


#Part 1
distances = {}
locations = set()
min_length = 0
for line in data:
    line = line.split()
    distances[(line[0], line[2])] = int(line[4])
    distances[(line[2], line[0])] = int(line[4])
    locations.add(line[0])
    locations.add(line[2])
    min_length += int(line[4])

for order in permutations(locations):
    route_length = 0
    for pair in pairwise(order):
        route_length += distances[pair]
    if route_length < min_length:
        min_length = route_length
print(min_length)

#Part 2
distances = {}
locations = set()
for line in data:
    line = line.split()
    distances[(line[0], line[2])] = int(line[4])
    distances[(line[2], line[0])] = int(line[4])
    locations.add(line[0])
    locations.add(line[2])

max_length = -1
for order in permutations(locations):
    route_length = 0
    for pair in pairwise(order):
        route_length += distances[pair]
    if route_length > max_length:
        max_length = route_length
print(max_length)