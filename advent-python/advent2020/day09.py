def is_subset_sum(target: int, summands: list[int]) -> bool:
    for i in range(len(summands)):
        for j in range(i+1, len(summands)):
            if summands[i] + summands[j] == target:
                return True
    return False

LOOKBACK_LENGTH: int = 25

with open("input-09.txt") as f:
    data: list[int] = [int(line.strip()) for line in f]

#Part 1
weakness: int = -1
for i in range(LOOKBACK_LENGTH, len(data)):
    if not is_subset_sum(data[i], data[i-LOOKBACK_LENGTH:i]):
        weakness = data[i]
        break

print(weakness)

#Part 2
lower_bound: int = -1
upper_bound: int = -1
for i in range(len(data)+1):
    for j in range(i+2, len(data)+1):
        range_sum = sum(data[i:j])
        if range_sum == weakness:
            lower_bound = i
            upper_bound = j
        elif range_sum > weakness:
            break
print(max(data[lower_bound:upper_bound]) + min(data[lower_bound:upper_bound]))
        
