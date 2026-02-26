with open("input-01.txt") as f:
    data = f.read()

#Part 1
floor = data.count("(") - data.count(")")
print(floor)

#Part 2
floor = 0
for i, char in enumerate(data, start=1):
    if char == "(":
        floor += 1
    if char == ")":
        floor -= 1
        if floor == -1:
            print(i)
            break