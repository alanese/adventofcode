from collections import Counter

#First return value is the count of pairs, second counts newly-added elements
def step(pairs: dict[str, int], rules: dict[str, str]) -> tuple[dict[str, int], dict[str, int]]:
    res_pairs: dict[str, int] = Counter()
    new_elements: dict[str, int] = Counter()
    for pair, count in pairs.items():
        mid: str = rules[pair]
        res_pairs[pair[0]+mid] += count
        res_pairs[mid+pair[1]] += count
        new_elements[mid] += count
    return res_pairs, new_elements

with open("input-14.txt") as f:
    data: list[str] = [line.strip() for line in f]

rules: dict[str, str] = {}
for line in data[2:]:
    pair, _, insert = line.partition(" -> ")
    rules[pair] = insert

#Part 1
polymer: str = data[0]
pairs: dict[str, int] = Counter()
element_counts: dict[str, int] = Counter(polymer)
for i in range(len(polymer)-1):
    pairs[polymer[i:i+2]] += 1
for _ in range(10):
    pairs, new_counts = step(pairs, rules)
    for elt, count in new_counts.items():
        element_counts[elt] += count

atoms: list[tuple[int, str]] = [(y,x) for (x,y) in element_counts.items()]
atoms.sort()
print(atoms[-1][0] - atoms[0][0])

#Part 2
for _ in range(30):
    pairs, new_counts = step(pairs, rules)
    for elt, count in new_counts.items():
        element_counts[elt] += count

atoms = [(y,x) for (x,y) in element_counts.items()]
atoms.sort()
print(atoms[-1][0] - atoms[0][0])