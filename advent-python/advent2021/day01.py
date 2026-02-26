with open("input-01.txt") as f:
    data: list[int] = [int(line.strip()) for line in f]

#Part 1
increase_count: int = 0
for i in range(len(data)-1):
    if data[i+1] > data[i]:
        increase_count += 1
print(increase_count)

#Part 2
WINDOW_SIZE: int = 3
increase_count: int = 0
for i in range(len(data)-WINDOW_SIZE):
    if sum(data[i:i+WINDOW_SIZE]) < sum(data[i+1:i+1+WINDOW_SIZE]):
        increase_count += 1
print(increase_count)