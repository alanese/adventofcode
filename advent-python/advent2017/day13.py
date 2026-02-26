def compute_severity(firewall: list[tuple[int, int]], start_time: int) -> int:
    severity: int = 0
    for (depth, range) in firewall:
        if (depth + start_time) % (2*range - 2) == 0:
            severity += depth * range
    return severity

def caught(firewall: list[tuple[int, int]], start_time: int) -> bool:
    for (depth, range) in firewall:
        if (depth + start_time) % (2*range - 2) == 0:
            return True
    return False

severity: int = 0
firewall: list[tuple[int, int]] = []

with open("input-13.txt") as f:
    for line in f:
        line = line.strip()
        colon: int = line.index(":")
        depth = int(line[:colon])
        range = int(line[colon+2:])
        firewall.append((depth, range))


start: int = -1
severity: int = -1
while caught(firewall, start):
    start += 1

print(start)