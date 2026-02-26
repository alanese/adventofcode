from collections import Counter

with open("input-01.txt") as f:
    left: list[int] = []
    right: list[int] = []
    for line in f:
        l, _, r = line.strip().partition("   ")
        left.append(int(l))
        right.append(int(r))

#Part 1
left.sort()
right.sort()
print(sum(abs(x-y) for x,y in zip(left, right)))

#Part 2
counter: dict[int, int] = Counter(right)
print(sum(x*counter[x] for x in left))