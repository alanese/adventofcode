def min_max(nums: list[int]) -> tuple[int, int]:
    cur_min: int = nums[0]
    cur_max: int = nums[0]
    for val in nums[1:]:
        if val < cur_min:
            cur_min = val
        if val > cur_max:
            cur_max = val
    return cur_min, cur_max

def even_divide(nums: list[int]) -> int:
    for p in nums:
        for q in nums:
            if p != q and p%q == 0:
                return p//q
    return 0

with open("input-02.txt") as f:
    lines: list[list[int]] = []
    for line in f:
        lines.append([int(x) for x in line.strip().split()])

total: int = 0
for row in lines:
    row_min, row_max = min_max(row)
    total += row_max - row_min
print(total)

print(sum([even_divide(row) for row in lines]))
