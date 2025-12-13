from collections import defaultdict
def parse_command(command: str) -> tuple[str, tuple[int, int], tuple[int, int]] | None:
    match command[:7]:
        case "turn on":
            cmd = "on"
            rest = command[8:]
        case "turn of":
            cmd = "off"
            rest = command[9:]
        case "toggle ":
            cmd = "toggle"
            rest = command[7:]
        case _:
            return None

    tmp = rest.split()
    coords_1 = tuple([int(x) for x in tmp[0].split(",")])
    coords_2 = tuple([int(x) for x in tmp[2].split(",")])
    
    return cmd, coords_1, coords_2

grid_p1 = defaultdict(lambda: False)
grid_p2 = defaultdict(lambda: 0)

with open("input-06.txt") as f:
    for line in f:
        cmd, start, end = parse_command(line.strip())
        match cmd:
            case "on":
                cmd_func_1 = lambda x: True
                cmd_func_2 = lambda x: x+1
            case "off":
                cmd_func_1 = lambda x: False
                cmd_func_2 = lambda x: max(0, x-1)
            case "toggle":
                cmd_func_1 = lambda x: not x
                cmd_func_2 = lambda x: x+2
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid_p1[(x,y)] = cmd_func_1(grid_p1[(x,y)])
                grid_p2[(x,y)] = cmd_func_2(grid_p2[(x,y)])

on_count = 0
for pair in grid_p1:
    if grid_p1[pair]:
        on_count += 1

print(on_count)

total = 0
for pair in grid_p2:
    total += grid_p2[pair]

print(total)
