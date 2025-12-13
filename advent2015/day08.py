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

raw_total: int = 0
parsed_total: int = 0
increase_count: int = 0
with open("input-08.txt") as f:
    for line in f:
        raw_total += len(line)
        parsed_total += parsed_length(line)
        for char in line:
            if char in ["\"", "\\"]:
                increase_count += 1
        increase_count += 2 #count starting and ending quotes
print(raw_total - parsed_total)
print(increase_count)