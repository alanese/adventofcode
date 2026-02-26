from collections import Counter

with open("input-02.txt") as f:
    data: list[str] = [line.strip("\n") for line in f]

#Part 1
two_count: int = 0
three_count: int = 0
for line in data:
    letters: Counter = Counter(line)
    if 2 in letters.values():
        two_count += 1
    if 3 in letters.values():
        three_count += 1
print(two_count * three_count)

#Part 2
i: int = 0
found: bool = False
found_1: str = "NONE"
found_2: str = "NONE"
while i < len(data) and not found:
    line_1: str = data[i]
    for line_2 in data[i+1:]:
        diff_count: int = 0
        for char_1, char_2 in zip(line_1, line_2):
            if char_1 != char_2:
                diff_count += 1
        if diff_count == 1:
            found = True
            found_1 = line_1
            found_2 = line_2
            break
    i += 1
print(f"First: {found_1}")
print(f"Second:{found_2}")
i = 0
while i < len(data):
    if found_1[i] != found_2[i]:
        break
    i += 1
print(f"Common: {found_1[:i] + found_1[i+1:]}")