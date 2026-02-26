with open("input-07.txt") as f:
    rows = [list(line.strip()) for line in f.readlines()]

split_count = 0
for i, row in enumerate(rows[1:], start=1):
    row = rows[i]
    for j in range(len(row)):
        if rows[i-1][j] == "S":
            row[j] = "|"
        elif rows[i-1][j] == "|":
            if row[j] == "." or row[j] == "|":
                row[j] = "|"
            elif row[j] == "^":
                split_count += 1
                row[j-1] = "|"
                row[j+1] = "|"

print(split_count)

#-------

with open("input-07.txt") as f:
    rows = [list(line.strip()) for line in f.readlines()]

paths_at = {}

for x, entry in enumerate(rows[-1]):
    if entry == ".":
        paths_at[(len(rows)-1, x)] = 1
    elif entry == "^":
        paths_at[(len(rows)-1, x)] = 2
    else:
        print(f"unexpected entry {entry}")

for y in range(len(rows)-2, -1, -1):
    for x, entry in enumerate(rows[y]):
        if entry == "." or entry == "S":
            paths_at[(y, x)] = paths_at[(y+1, x)]
        elif entry == "^":
            paths_at[(y,x)] = paths_at[(y+1, x-1)] + paths_at[(y+1, x+1)]

init_x = rows[0].index("S")
print(paths_at[(0, init_x)])