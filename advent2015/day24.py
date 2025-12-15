from typing import Generator, List

def list_diff(x1: List, x2: List) -> List:
    return list(set(x1) - set(x2))

def product(xs: List[int]) -> int:
    total = 1
    for x in xs:
        total *= x
    return total
    
def sum_subsets(xs: List[int], target: int) -> Generator:
    if target == 0:
        yield []
    elif len(xs) > 0:
        if xs[0] <= target:
            for rest in sum_subsets(xs[1:], target - xs[0]):
                yield [xs[0]] + rest
        for rest in sum_subsets(xs[1:], target):
            yield rest

def equal_sums(xs: List[int], subsets: int) -> Generator:
    if subsets == 1:
        yield [xs]
    elif sum(xs) % subsets != 0:
        yield []
    else:
        target = sum(xs) // subsets
        for first in sum_subsets(xs, target):
            remaining = list_diff(xs, first)
            for rest in equal_sums(remaining, subsets-1):
                yield [first] + rest

def minimum_quantum(presents: List[int], subsets: int) -> int:
    target_size = sum(presents) // subsets
    min_size = len(presents)
    min_quantum = product(presents)
    for subset in sum_subsets(presents, target_size):
        if len(subset) < min_size:
            min_size = len(subset)
            min_quantum = product(subset)
            print(f"New smallest: {subset}, size={min_size}, quantum={min_quantum}, CHECK: sum {sum(subset)} == {target_size}")
        elif len(subset) == min_size and product(subset) < min_quantum:
            min_quantum = product(subset)
            print(f"New smallest: {subset}, size={min_size}, quantum={min_quantum}, CHECK: sum {sum(subset)} == {target_size}")
    return min_quantum

with open("input-24.txt") as f:
    presents = [int(x) for x in f]

print(minimum_quantum(presents, 3))
print(minimum_quantum(presents, 4))
