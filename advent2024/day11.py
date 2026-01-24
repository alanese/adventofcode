from math import log10

#Find the number of stones after given number of steps, starting from a single stone
#with value x. Seen tracks already-seen (x,steps) combinations
def length_after(x: int, steps: int, seen: dict[tuple[int, int], int] = {}) -> int:
    if (x,steps) not in seen:
        if steps == 0:
            seen[(x, steps)] = 1
        elif x == 0:
            seen[(x, steps)] = length_after(1, steps-1, seen)
        else:
            #Compute the number of digits in x
            length: int = int(log10(x) + 1)
            if length%2 == 0:
                #Extract first half and last half of digits
                left: int = x // 10**(length//2)
                right: int = x % 10**(length//2)
                seen[(x, steps)] = length_after(left, steps-1, seen) + length_after(right, steps-1, seen)
            else:
                seen[(x, steps)] = length_after(x*2024, steps-1, seen)
    return seen[(x, steps)]

with open("input-11.txt") as f:
    data: list[int] = [int(x) for x in f.read().split()]

#Part 1
seen: dict[tuple[int, int], int] = {}
print(sum(length_after(x, 25, seen) for x in data))

#Part 2
print(sum(length_after(x, 75, seen) for x in data))