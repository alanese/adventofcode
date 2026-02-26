from collections import defaultdict

def count_routes(end: str, path: list[str], tunnels: dict[str, list[str]], small_twice_ok: bool = False) -> int:
    if path[-1] == end:
        return 1
    else:
        route_count: int = 0
        for next in tunnels[path[-1]]:
            if not (next.islower() and next in path):
                route_count += count_routes(end, path+[next], tunnels, small_twice_ok)
            elif small_twice_ok and next != "start" and next.islower() and next in path:
                route_count += count_routes(end, path+[next], tunnels, False)
        return route_count

tunnels: dict[str, list[str]] = defaultdict(list)
with open("input-12.txt") as f:
    for line in f:
        c1, _, c2 = line.strip().partition("-")
        tunnels[c1].append(c2)
        tunnels[c2].append(c1)

#Part 1
print(count_routes("end", ["start"], tunnels, False))

#Part 2
print(count_routes("end", ["start"], tunnels, True))