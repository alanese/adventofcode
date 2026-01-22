from collections import defaultdict

def parse_rule(rule: str) -> tuple[int, int]:
    first, _, second = rule.partition("|")
    return int(first), int(second)

def update_valid(update: list[int], rules: list[tuple[int, int]]):
    for first, second in rules:
        if first in update and second in update and update.index(first) > update.index(second):
            return False
    return True

def topo_sort(update: list[int], rules: list[tuple[int, int]]) -> list[int]:
    predecessors: dict[int, set[int]] = defaultdict(set)
    successors: dict[int, set[int]] = defaultdict(set)
    for first, second in rules:
        if first in update and second in update:
            predecessors[second].add(first)
            successors[first].add(second)

    res: list[int] = []
    remaining: set[int] = set()
    for num in update:
        if len(predecessors[num]) == 0:
            remaining.add(num)
    while len(remaining) > 0:
        res.append(remaining.pop())
        for successor in successors[res[-1]]:
            predecessors[successor].remove(res[-1])
            if len(predecessors[successor]) == 0:
                remaining.add(successor)
    return res

with open("input-05.txt") as f:
    data: list[str] = [line.strip() for line in f]

delim: int = data.index("")
rules: list[tuple[int, int]] = [parse_rule(rule) for rule in data[:delim]]
updates: list[list[int]] = [ [int(x) for x in line.split(",")] for line in data[delim+1:]]

#Part 1
invalid_updates: list[list[int]] = []
middle_sum: int = 0
for update in updates:
    if update_valid(update, rules):
        middle_sum += update[len(update)//2]
    else:
        invalid_updates.append(update)
print(middle_sum)

#Part 2
sorted_middle_sum: int = 0
for invalid in invalid_updates:
    sorted_update: list[int] = topo_sort(invalid, rules)
    sorted_middle_sum += sorted_update[len(sorted_update)//2]
print(sorted_middle_sum)