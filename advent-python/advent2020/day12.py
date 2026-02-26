import math

instructions: list[tuple[str, int]] = []
with open("input-12.txt") as f:
    for line in f:
        line = line.strip()
        command: str = line[0]
        distance: int = int(line[1:])
        instructions.append((command, distance))

#Part 1
cur_x: int = 0
cur_y: int = 0
cur_bearing: int = 0

for command, distance in instructions:
    match command:
        case "N":
            cur_y += distance
        case "S":
            cur_y -= distance
        case "E":
            cur_x += distance
        case "W":
            cur_x -= distance
        case "L":
            cur_bearing = (cur_bearing + distance) % 360
        case "R":
            cur_bearing = (cur_bearing - distance) % 360
        case "F":
            cur_x += round(distance * math.cos(math.radians(cur_bearing)))
            cur_y += round(distance * math.sin(math.radians(cur_bearing)))
    
print(abs(cur_x) + abs(cur_y))

#Part 2
cur_x = 0
cur_y = 0
waypoint_x: int = 10
waypoint_y: int = 1
for command, distance in instructions:
    match command:
        case "N":
            waypoint_y += distance
        case "S":
            waypoint_y -= distance
        case "E":
            waypoint_x += distance
        case "W":
            waypoint_x -= distance
        case "L":
            new_wp_x: int = round(waypoint_x * math.cos(math.radians(distance)) - waypoint_y * math.sin(math.radians(distance)))
            new_wp_y: int = round(waypoint_x * math.sin(math.radians(distance)) + waypoint_y * math.cos(math.radians(distance)))
            waypoint_x, waypoint_y = new_wp_x, new_wp_y
        case "R":
            new_wp_x: int = round(waypoint_x * math.cos(math.radians(-distance)) - waypoint_y * math.sin(math.radians(-distance)))
            new_wp_y: int = round(waypoint_x * math.sin(math.radians(-distance)) + waypoint_y * math.cos(math.radians(-distance)))
            waypoint_x, waypoint_y = new_wp_x, new_wp_y
        case "F":
            cur_x += distance * waypoint_x
            cur_y += distance * waypoint_y

print(abs(cur_x) + abs(cur_y))