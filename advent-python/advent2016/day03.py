from itertools import batched

def valid_triangle(side1: int, side2: int, side3: int) -> bool:
    total = side1 + side2 + side3
    biggest = max(side1, side2, side3)
    return total - biggest > biggest

valid = 0
with open("input-03.txt") as f:
    lines = [ [int(x) for x in line.split()] for line in f]

for line in lines:
    if valid_triangle(*[int(x) for x in line]):
        valid += 1
print(valid)

valid = 0
for triple in batched(lines, 3):
    for i in range(len(triple[0])):
        if valid_triangle(triple[0][i], triple[1][i], triple[2][i]):
            valid += 1

print(valid)