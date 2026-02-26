from collections import Counter

def step(fish_counts: dict[int, int]):
    new_fish: int = fish_counts[0]
    for i in range(8):
        fish_counts[i] = fish_counts[i+1]
    fish_counts[6] += new_fish
    fish_counts[8] = new_fish

with open("input-06.txt") as f:
    data: list[int] = [int(x) for x in f.read().strip().split(",")]

#Part 1
fish: Counter = Counter(data)

for _ in range(80):
    step(fish)
print(fish.total())

#Part 2
for _ in range(256-80):
    step(fish)
print(fish.total())