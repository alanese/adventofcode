def split_list(numbers: list[int], delim: int) -> list[list[int]]:
    sublists: list[list[int]] = []
    while delim in numbers:
        sublists.append(numbers[:numbers.index(delim)])
        numbers = numbers[numbers.index(delim)+1:]
    if len(numbers) > 0:
        sublists.append(numbers)
    return sublists

with open("input-01.txt") as f:
    data: list[str] = [line.strip() for line in f]
data_nums: list[int] = [int(num) if num != "" else -1 for num in data]

elves: list[int] = [sum(nums) for nums in split_list(data_nums, -1)]
elves.sort(reverse=True)
print(elves[0])
print(sum(elves[:3]))