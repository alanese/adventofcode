zero_count = 0
current_pos = 50
with open("input-01-1.txt") as f:
    for line in f:
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            current_pos = (current_pos - distance) % 100
        else:
            current_pos = (current_pos + distance) % 100
        
        if current_pos == 0:
            zero_count += 1
print(zero_count)

zero_count = 0
current_pos = 50

with open("input-01-1.txt") as f:
    for line in f:
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            delta = -1
        else:
            delta = 1
        for _ in range(distance):
            current_pos = (current_pos + delta) % 100
            if current_pos == 0:
                zero_count += 1
print(zero_count)