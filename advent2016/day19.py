def josephus(num: int) -> int:
    remaining: list[int] = [True] * num
    i: int = 0
    for _ in range(num-1):
        i = (i+1) % num
        while not remaining[i]:
            i = (i+1) % num
        remaining[i] = False
        while not remaining[i]:
            i = (i+1) % num
    return remaining.index(True) + 1

def across_josephus(num: int) -> int:
    remaining: list[int] = list(range(1, num+1))
    i = 0
    while len(remaining) > 1:
        remove_index: int = (i + len(remaining)//2) % len(remaining)
        remaining.pop(remove_index)
        if i >= len(remaining):
            i = 0
        elif i < remove_index:
            i += 1
    print(remaining)
    return remaining[0]


print(josephus(3005290))
print(across_josephus(3005290))