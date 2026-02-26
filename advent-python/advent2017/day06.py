def redistribute(state: list[int]) -> None:
    max_val: int = -1
    max_index: int = 0
    for i, val in enumerate(state):
        if val > max_val:
            max_val = val
            max_index = i
    
    redist = state[max_index]
    state[max_index] = 0
    cur_index: int = (max_index + 1) % len(state)
    while redist > 0:
        state[cur_index] += 1
        redist -= 1
        cur_index = (cur_index + 1) % len(state)

with open("input-06.txt") as f:
    state: list[int] = [int(x) for x in f.read().split()]

seen: dict[tuple[int, ...], int] = {}

cycles: int = 0
while tuple(state) not in seen:
    seen[tuple(state)] = cycles
    redistribute(state)
    cycles += 1

print(cycles)
print(cycles - seen[tuple(state)])