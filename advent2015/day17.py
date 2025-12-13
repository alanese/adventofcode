from typing import List
from itertools import combinations

def fill_combo_count(eggnog: int, containers: List[int]) -> int:
    if eggnog == 0:
        return 1
    elif len(containers) == 0:
        return 0
    elif eggnog < containers[0]:
        return fill_combo_count(eggnog, containers[1:])
    else:
        return fill_combo_count(eggnog, containers[1:]) + fill_combo_count(eggnog - containers[0], containers[1:])
    

def min_combo_count(eggnog: int, containers: List[int]) -> int:
    count: int = 0
    for i in range(1,len(containers)+1):
        for combo in combinations(containers, i):
            if sum(combo) == eggnog:
                count += 1
        if count != 0:
            return count
    return -1

    
with open("input-17.txt") as f:
    containers = [int(x) for x in f]

print(fill_combo_count(150, containers))
print(min_combo_count(150, containers))