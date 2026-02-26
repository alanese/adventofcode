from collections import defaultdict
from dataclasses import dataclass
import heapq

@dataclass
class Elf:
    task: str
    time_remaining: int

def parse_data(data: list[str]) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    allows: dict[str, set[str]] = defaultdict(set)
    prerequisites: dict[str, set[str]] = defaultdict(set)
    for line in data:
        line_split: list[str] = line.split()
        first = line_split[1]
        second = line_split[7]
        allows[first].add(second)
        prerequisites[second].add(first)
    return allows, prerequisites


with open("input-07.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
allows: dict[str, set[str]]
prerequisites: dict[str, set[str]]
allows, prerequisites = parse_data(data)

done: list[str] = []
todo: list[str] = []
for task in allows:
    if len(prerequisites[task]) == 0:
        heapq.heappush(todo, task)

while len(todo) > 0:
    next_task: str = heapq.heappop(todo)
    done.append(next_task)
    for future_task in allows[next_task]:
        prerequisites[future_task].remove(next_task)
        if len(prerequisites[future_task]) == 0:
            heapq.heappush(todo, future_task)

print("".join(done))

#Part 2
allows, prerequisites = parse_data(data)
todo = []
for task in allows:
    if len(prerequisites[task]) == 0:
        heapq.heappush(todo, task)

ADDED_COSTS: str = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE_COST: int = 60
ELF_COUNT = 5

elves: list[Elf] = []
for i in range(ELF_COUNT):
    elves.append(Elf("_", 0))
    if len(todo) > 0:
        elves[i].task = heapq.heappop(todo)
        elves[i].time_remaining = BASE_COST + ADDED_COSTS.index(elves[i].task)

seconds: int = 0
while not all([elf.task == "_" for elf in elves]):
    seconds += 1
    for elf in elves:
        if elf.task != "_":
            elf.time_remaining -= 1
            if elf.time_remaining == 0:
                for future_task in allows[elf.task]:
                    prerequisites[future_task].remove(elf.task)
                    if len(prerequisites[future_task]) == 0:
                        heapq.heappush(todo, future_task)
                elf.task = "_"
    for elf in elves:
        if elf.task == "_" and len(todo) > 0:
            elf.task = heapq.heappop(todo)
            elf.time_remaining = BASE_COST + ADDED_COSTS.index(elf.task)

print(seconds)