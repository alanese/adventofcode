floor = 0
with open("input-01.txt") as f:
    for line in f:
        floor += line.count("(")
        floor -= line.count(")")

print(floor)

#-------------

floor = 0
with open("input-01.txt") as f:
    line = f.readline()
    for i, char in enumerate(line, start=1):
        if char == "(":
            floor += 1
        if char == ")":
            floor -= 1
            if floor == -1:
                print(i)
                break