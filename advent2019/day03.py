def get_all_points(directions: list[str]) -> dict[tuple[int, int], int]:
    distances: dict[tuple[int, int], int] = {}
    x = 0
    y = 0

    x_delta: int = 0
    y_delta: int = 0
    steps: int = 0

    for step in directions:
        match step[0]:
            case "L":
                x_delta = -1
                y_delta = 0
            case "R":
                x_delta = 1
                y_delta = 0
            case "U":
                x_delta = 0
                y_delta = 1
            case "D":
                x_delta = 0
                y_delta = -1
        for _ in range(int(step[1:])):
            steps += 1
            x += x_delta
            y += y_delta
            if (x,y) not in distances:
                distances[(x,y)] = steps
    return distances

with open("input-03.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
instructions_1: list[str] = data[0].split(",")
instructions_2: list[str] = data[1].split(",")
distances_1: dict[tuple[int, int], int] = get_all_points(instructions_1)
distances_2: dict[tuple[int, int], int] = get_all_points(instructions_2)
intersections: set[tuple[int, int]] = set(distances_1.keys()) & set(distances_2.keys())
closest: int = min([abs(x) + abs(y) for (x,y) in intersections])
print(closest)

#Part 2
instructions_1 = data[0].split(",")
instructions_2 = data[1].split(",")
distances_1 = get_all_points(instructions_1)
distances_2 = get_all_points(instructions_2)
intersections = set(distances_1.keys()) & set(distances_2.keys())
closest = min([distances_1[pt] + distances_2[pt] for pt in intersections])
print(closest)