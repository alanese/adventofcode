with open("input-01.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
print(sum([int(x) for x in data]))

#Part 2
seen: set[int] = set()
index: int = 0
curr_freq = 0
while curr_freq not in seen:
    seen.add(curr_freq)
    curr_freq += int(data[index])
    index = (index + 1) % len(data)
print(curr_freq)