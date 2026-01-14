with open("input-02.txt") as f:
    data: list[str] = [line.strip() for line in f]

parsed_data: list[tuple[str,int]] = []
for line in data:
    direction, _, distance = line.partition(" ")
    parsed_data.append((direction, int(distance)))

#Part 1
pos: int = 0
depth: int = 0
for direction, distance in parsed_data:
    match direction:
        case "forward":
            pos += distance
        case "down":
            depth += distance
        case "up":
            depth -= distance
        case _:
            print(f"Error - {direction} not a valid direction")

print(pos*depth)

#Part 2
pos = 0
depth = 0
aim: int = 0
for direction, distance in parsed_data:
    match direction:
        case "down":
            aim += distance
        case "up":
            aim -= distance
        case "forward":
            pos += distance
            depth += aim*distance
        case _:
            print(f"Error  - {direction} not a valid direction")
print(pos*depth)