def cost_p2(crabs: list[int], point: int) -> int:
    cost: int = 0
    for crab in crabs:
        distance: int = abs(crab-point)
        cost += distance*(distance+1)//2
    return cost

with open("input-07.txt") as f:
    data: list[int] = [int(x) for x in f.read().strip().split(",")]

#Part 1
min_cost: int = sum(data)
for x in range(max(data)+1):
    min_cost = min(min_cost, sum(abs(x-point) for point in data))
print(min_cost)

#Part 2
min_cost = cost_p2(data, 0)
for point in range(1, max(data)+1):
    min_cost = min(min_cost, cost_p2(data, point))
print(min_cost)

