with open("input-10.txt") as f:
    data: list[int] = [int(line.strip()) for line in f]

#Part 1
data.sort()
data = [0] + data + [data[-1]+3]
differences: dict[int, int] = {1: 0, 2: 0, 3: 0}
for i in range(len(data)-1):
    differences[data[i+1]-data[i]] += 1

print(differences[1] * differences[3])

#Part 2
routes_from: dict[int, int] = {len(data) - 1: 1}
for i in reversed(range(len(data)-1)):
    routes_from[i] = 0
    if data[i+1] - data[i] <= 3:
        routes_from[i] += routes_from[i+1]
        if i+2 in routes_from and data[i+2] - data[i] <= 3:
            routes_from[i] += routes_from[i+2]
            if i+3 in routes_from and data[i+3] - data[i] <= 3:
                routes_from[i] += routes_from[i+3]
print(routes_from[0])