with open("input-01.txt") as f:
    data: list[str] = [line.strip() for line in f]


def total_fuel(mass: int) -> int:
    total: int = 0
    mass = mass//3 - 2
    while mass > 0:
        total += mass
        mass = mass//3 - 2
    return total

#Part 1
print(sum([int(x)//3 - 2 for x in data]))

#Part 2
print(sum([total_fuel(int(x)) for x in data]))