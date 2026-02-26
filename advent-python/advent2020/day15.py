from collections import defaultdict

INPUT_DATA: list[int] = [16,11,15,0,1,7]

#For part 1
#LIMIT: int = 2020
#For part 2
LIMIT: int = 30000000

last_spoken: dict[int, list[int]] = defaultdict(list)

numbers: list[int] = INPUT_DATA[:]
for i, num in enumerate(INPUT_DATA):
    last_spoken[num].append(i+1)

while len(numbers) < LIMIT:
    if len(numbers) % 1000 == 0:
        print(len(numbers))
    last_history: list[int] = last_spoken[numbers[-1]]
    if len(last_history) == 1:
        next_num: int = 0
    else:
        next_num: int = last_history[-1] - last_history[-2]
    numbers.append(next_num)
    last_spoken[next_num].append(len(numbers))

print(numbers[-1])