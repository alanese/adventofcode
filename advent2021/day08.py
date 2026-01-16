def parse_pattern(line: str) -> tuple[list[set[str]], list[set[str]]]:
    inputs, _, output = line.partition(" | ")
    input_sets: list[set[str]] = [set(x) for x in inputs.split()]
    output_patterns: list[set[str]] = [ set(x) for x in output.split()]
    return input_sets, output_patterns

def id_patterns(patterns: list[set[str]]) -> list[set[str]]:
    if len(patterns) != 10:
        raise ValueError(f"Improper parameter length {len(patterns)}")
    res: list[set[str]] = [set()]*10

    #ID unique lengths
    for pattern in patterns:
        match len(pattern):
            case 2:
                res[1] = pattern
            case 3:
                res[7] = pattern
            case 4:
                res[4] = pattern
            case 7:
                res[8] = pattern
            case _:
                continue
    
    #ID remainder
    for pattern in patterns:
        if len(pattern) == 5:
            if len(pattern & res[4]) == 2:
                res[2] = pattern
            elif res[1] < pattern:
                res[3] = pattern
            else:
                res[5] = pattern
        elif len(pattern) == 6:
            if not res[7] < pattern:
                res[6] = pattern
            elif res[4] < pattern:
                res[9] = pattern
            else:
                res[0] = pattern
    return res
            

with open("input-08.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Parts 1&2
count_1478: int = 0
result_sum: int = 0
for line in data:
    inputs, output = parse_pattern(line)
    numbers: list[set[str]] = id_patterns(inputs)
    result: int = int("".join(str(numbers.index(digit)) for digit in output))
    result_sum += result
    for pattern in output:
        if numbers.index(pattern) in (1,4,7,8):
            count_1478 += 1
print(count_1478)
print(result_sum)