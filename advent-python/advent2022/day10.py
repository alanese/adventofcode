with open("input-10.txt") as f:
    data: list[str] = [line.strip() for line in f]

values: list[int] = [1]
current_val: int = 1
for op in data:
    if op == "noop":
        values.append(current_val)
    else:
        addend: int = int(op.split()[-1])
        values += [current_val]*2
        current_val += addend

#Part 1
times: list[int] = [20, 60, 100, 140, 180, 220]
print(sum(i * values[i] for i in times))

#Part 2
for y in range(6):
    for x in range(1, 41):
        if abs((x-1)-values[y*40+x]) <= 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()