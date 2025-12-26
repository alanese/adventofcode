from dataclasses import dataclass

@dataclass
class Wire:
    source: str
    value: int | None

def parse_argument(argument: str, network: dict[str, Wire]) -> int:
    if argument.isnumeric():
        return int(argument)
    else:
        if network[argument].value is None:
            network[argument].value = retrieve_value(argument, network)
        return network[argument].value

def parse_not(argument:str, network: dict[str, Wire]) -> int:
    return (~parse_argument(argument, network)) % 65536

def parse_and(arg1: str, arg2: str, network: dict[str, Wire]) -> int:
    arg1_int = parse_argument(arg1, network)
    arg2_int = parse_argument(arg2, network)
    return arg1_int & arg2_int

def parse_or(arg1: str, arg2: str, network: dict[str, Wire]) -> int:
    arg1_int = parse_argument(arg1, network)
    arg2_int = parse_argument(arg2, network)
    return arg1_int | arg2_int

def parse_lshift(arg1: str, arg2: str, network: dict[str, Wire]) -> int:
    arg1_int = parse_argument(arg1, network)
    arg2_int = parse_argument(arg2, network)
    return (arg1_int << arg2_int) % 65536

def parse_rshift(arg1: str, arg2: str, network: dict[str, Wire]) -> int:
    arg1_int = parse_argument(arg1, network)
    arg2_int = parse_argument(arg2, network)
    return (arg1_int >> arg2_int) % 65536

def retrieve_value(wire: str, network: dict[str, Wire]) -> int:
    if network[wire].value is not None:
        return network[wire].value
    
    signal = network[wire].source.split()

    if len(signal) == 1:
        network[wire].value = parse_argument(signal[0], network)
    elif signal[0] == "NOT":
        network[wire].value = parse_not(signal[1], network)
    elif signal[1] == "AND":
        network[wire].value = parse_and(signal[0], signal[2], network)
    elif signal[1] == "OR":
        network[wire].value = parse_or(signal[0], signal[2], network)
    elif signal[1] == "LSHIFT":
        network[wire].value = parse_lshift(signal[0], signal[2], network)
    elif signal[1] == "RSHIFT":
        network[wire].value = parse_rshift(signal[0], signal[2], network)
    else:
        print(f"Unrecognized source {signal}")

    return network[wire].value

with open("input-07.txt") as f:
    data = [line.strip().split(" -> ") for line in f]


#Part 1
network = {}

for line in data:
    network[line[1]] = Wire(line[0], None)

a_value = retrieve_value("a", network)
print(a_value)

#Part 2
network = {}
for line in data:
    network[line[1]] = Wire(line[0], None)
network["b"].source = str(a_value)

print(retrieve_value("a", network))