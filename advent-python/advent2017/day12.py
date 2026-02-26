def parse_line(line: str) -> tuple[int, list[int]]:
    split_line: list[str] = line.split(" ", maxsplit=2)
    return int(split_line[0]), [int(x) for x in split_line[2].split(", ")]

def connected_group(program: int, connections: dict[int, list[int]]) -> set[int]:
    connected: set[int] = set([program])
    to_check: list[int] = [program]
    while len(to_check) > 0:
        next_check: int = to_check.pop(0)
        for connection in connections[next_check]:
            if connection not in connected:
                to_check.append(connection)
                connected.add(connection)
    return connected

network: dict[int, list[int]] = {}
programs: list[int] = []
with open("input-12.txt") as f:
    program: int
    connections: list[int]
    for line in f:
        program, connections = parse_line(line.strip())
        network[program] = connections
        programs.append(program)

print(len(connected_group(0, network)))

#------

group_count: int = 0
while len(programs) > 0:
    group_count += 1
    program: int = programs[0]
    for connected_program in connected_group(program, network):
        programs.remove(connected_program)
print(group_count)