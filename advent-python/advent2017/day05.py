with open("input-05.txt") as f:
    offsets_p1: list[int] = ([int(line) for line in f])
    offsets_p2: list[int] = [i for i in offsets_p1]

i: int = 0
steps: int = 0
while 0 <= i < len(offsets_p1):
    offsets_p1[i] += 1
    i += (offsets_p1[i] - 1)
    steps += 1
print(steps)

i = 0
steps = 0
while 0 <= i < len(offsets_p2):
    steps += 1
    if offsets_p2[i] >= 3:
        offsets_p2[i] -= 1
        i += offsets_p2[i] + 1
    else:
        offsets_p2[i] += 1
        i += offsets_p2[i] - 1
print(steps)