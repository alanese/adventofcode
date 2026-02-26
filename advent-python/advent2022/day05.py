with open("input-05.txt") as f:
    data: list[str] = [line.strip("\n") for line in f]

delim: int = data.index("")
tower_str: list[str] = data[:delim][::-1]
moves: list[str] = data[delim+1:]

towers: dict[str, list[str]] = {}
for i, char in enumerate(tower_str[0]):
    if char != " ":
        towers[char] = [line[i] for line in tower_str[1:] if line[i] != " "]

#Part 1
for move in moves:
    split: list[str] = move.split()
    count: int = int(split[1])
    from_: str = split[3]
    to: str = split[5]
    for _ in range(count):
        towers[to].append(towers[from_].pop())

print("".join(stack[-1] for _,stack in sorted(towers.items())))

#Reset towers
towers = {}
for i, char in enumerate(tower_str[0]):
    if char != " ":
        towers[char] = [line[i] for line in tower_str[1:] if line[i] != " "]

#Part 2
for move in moves:
    tmp: list[str] = []
    split: list[str] = move.split()
    count: int = int(split[1])
    from_: str = split[3]
    to: str = split[5]
    for _ in range(count):
        tmp.append(towers[from_].pop())
    for _ in range(count):
        towers[to].append(tmp.pop())

print("".join(stack[-1] for _,stack in sorted(towers.items())))