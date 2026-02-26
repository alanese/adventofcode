from collections import Counter

with open("input-20.txt") as f:
    target = int(f.read())

presents = Counter()

for elf in range(1, target//10):
    print(f"Elf {elf} delivering . . .")
    for house in range(elf, target//10+1, elf):
        presents[house] += 10*elf
    if presents[elf] >= target:
        print(f"House {elf} gets {presents[elf]} presents")
        break

presents_2 = Counter()
for elf in range(1, target//11):
    print(f"Elf {elf} delivering . . .")
    for house in range(1, 51):
        presents_2[elf * house] += 11*elf
    if presents_2[elf] >= target:
        print(f"House {elf} gets {presents_2[elf]} presents")
        break
