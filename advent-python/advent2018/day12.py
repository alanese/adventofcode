def parse_condition(condition: str) -> tuple[tuple[bool, ...], bool]:
    return tuple([char == "#" for char in condition[:5]]), condition[-1] == "#"

with open("input-12.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
initial_state: str = data[0][15:]

initial_lower = 0
initial_upper = len(initial_state)

live_prestates: set[tuple[bool, ...]] = set()
for line in data[2:]:
    prestate, live = parse_condition(line)
    if live:
        live_prestates.add(prestate)

current_state: set[int] = set()
for i, char in enumerate(initial_state):
    if char == "#":
        current_state.add(i)
prev_state: set[int]

for generation in range(1, 21):
    prev_state = current_state
    current_state = set()
    for i in range(initial_lower - 2*generation, initial_upper + 2*generation):
        prestate: tuple[bool, ...] = tuple(x in prev_state for x in range(i-2, i+3))
        if prestate in live_prestates:
            current_state.add(i)

print(sum(current_state))

#Part 2
live_prestates: set[tuple[bool, ...]] = set()
for line in data[2:]:
    prestate, live = parse_condition(line)
    if live:
        live_prestates.add(prestate)

current_state: set[int] = set()
for i, char in enumerate(initial_state):
    if char == "#":
        current_state.add(i)
prev_state: set[int]

cur_sum: int = 0
prev_sum: int = 0
for generation in range(1, 10001):
    print(generation)
    prev_state = current_state
    prev_sum = cur_sum
    current_state = set()
    lower: int = min(prev_state)
    upper: int = max(prev_state)
    for i in range(lower-2, upper+3):
        prestate: tuple[bool, ...] = tuple(x in prev_state for x in range(i-2, i+3))
        if prestate in live_prestates:
            current_state.add(i)
    cur_sum = sum(current_state)

print(cur_sum + (50000000000 - 10000) * (cur_sum - prev_sum))