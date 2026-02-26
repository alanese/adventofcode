with open("input-02.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
valid_count: int = 0
for line in data:
    line_split: list[str] = line.split()
    lower_bound: int = int(line_split[0][:line_split[0].index("-")])
    upper_bound: int = int(line_split[0][line_split[0].index("-")+1:])
    char: str = line_split[1][0]
    if lower_bound <= line_split[2].count(char) <= upper_bound:
        valid_count += 1

print(valid_count)

#Part 2
valid_count = 0
for line in data:
    line_split: list[str] = line.split()
    index_1: int = int(line_split[0][:line_split[0].index("-")]) - 1
    index_2: int = int(line_split[0][line_split[0].index("-") + 1:]) - 1
    char = line_split[1][0]
    if (line_split[2][index_1] == char) ^ (line_split[2][index_2] == char):
        valid_count += 1
    
print(valid_count)