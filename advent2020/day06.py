with open("input-06.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
seen: set[str] = set()
total_answered: int = 0
for line in data:
    if line == "":
        total_answered += len(seen)
        seen = set()
    else:
        seen = seen | set(line)
total_answered += len(seen)

print(total_answered)

#Part 2
group: list[str] = []
total_answered: int = 0
for line in data:
    if line == "":
        seen = set(group[0])
        for answers in group[1:]:
            seen &= set(answers)
        total_answered += len(seen)
        group = []
    else:
        group.append(line)
seen = set(group[0])
for answers in group[1:]:
    seen &= set(answers)
total_answered += len(seen)
print(total_answered)