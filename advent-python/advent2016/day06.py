from collections import Counter
from typing import List, Tuple

def most_least_common_in_column(grid: List[str], column: int) -> Tuple[str, str]:
    counter = Counter(line[column] for line in grid)
    sorted_column = sorted(counter.items(), key=lambda pair: pair[1])
    most_common = sorted_column[-1][0]
    least_common = sorted_column[0][0]
    return most_common, least_common

with open("input-06.txt") as f:
    lines = [line.strip() for line in f]

pairs = []
for i in range(len(lines[0])):
    pairs.append(most_least_common_in_column(lines, i))
print("".join([pair[0] for pair in pairs]))
print("".join([pair[1] for pair in pairs]))