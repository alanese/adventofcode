def parsed_length(line: str) -> int:
    count: int = 0

    line = line[1:-1]
    while len(line) > 0:
        count += 1
        if not line[0] == "\\":
            line = line[1:]
        elif line[1] == "\"" or line[1] == "\\":
            line = line[2:]
        elif line[1] == "x":
            line = line[4:]

    return count


with open("input-08.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
raw_total: int = 0
parsed_total: int = 0
for line in data:
    raw_total += len(line)
    parsed_total += parsed_length(line)
print(raw_total - parsed_total)

#Part 2
increase_count: int = 0
for line in data:
    for char in line:
        if char in ["\"", "\\"]:
            increase_count += 1
    increase_count += 2 #count starting and ending quotes
print(increase_count)