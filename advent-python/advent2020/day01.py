with open("input-01.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if int(data[i]) + int(data[j]) == 2020:
            print(int(data[i]) * int(data[j]))

#Part 2
for i in range(len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)):
            if int(data[i]) + int(data[j]) + int(data[k]) == 2020:
                print(int(data[i]) * int(data[j]) * int(data[k]))