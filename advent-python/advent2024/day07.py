from itertools import product

def process(nums: list[int], ops: tuple[str, ...]) -> int:
    cur: int = nums[0]
    for op, num in zip(ops, nums[1:]):
        match op:
            case "+":
                cur += num
            case "*":
                cur *= num
            case "||":
                cur = int(str(cur) + str(num))
            case _:
                raise ValueError(f"Invalid operator {op}")
    return cur

def check_valid(target: int, nums: list[int], possible_ops: tuple[str, ...]) -> bool:
    for ops in product(possible_ops, repeat=len(nums)-1):
        if process(nums, ops) == target:
            return True
    return False

with open("input-07.txt") as f:
    data: list[str] = [line.strip() for line in f]

equations: list[tuple[int, list[int]]] = []
for line in data:
    target, _, nums = line.partition(": ")
    equations.append((int(target), [int(num) for num in nums.split()]))

#Part 1
valid_total: int = 0
for target, nums in equations:
    if check_valid(target, nums, ("+", "*")):
        valid_total += target
print(valid_total)

#Part 2
valid_total = 0
for target, nums in equations:
    if check_valid(target, nums, ("+", "*", "||")):
        valid_total += target
print(valid_total)