from collections import defaultdict

def parse_condition(register: str, comparison: str, value: int, registers: dict[str, int]) -> bool:
    match comparison:
        case ">":
            return registers[register] > value
        case "<":
            return registers[register] < value
        case ">=":
            return registers[register] >= value
        case "<=":
            return registers[register] <= value
        case "==":
            return registers[register] == value
        case "!=":
            return registers[register] != value
        case _:
            raise ValueError(f"Invalid comparison {comparison}")
        
registers: dict[str, int] = defaultdict(int)
highest_seen = 0

with open("input-08.txt") as f:
    for line in f:
        line_split: list[str] = line.split()
        register: str = line_split[0]
        inc_value = int(line_split[2])
        if line_split[1] == "dec":
            inc_value = -inc_value
        if parse_condition(line_split[4], line_split[5], int(line_split[6]), registers):
            registers[register] += inc_value
            if registers[register] > highest_seen:
                highest_seen = registers[register]

print(max(registers.values()))
print(highest_seen)