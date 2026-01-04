MASK_SIZE: int = 36

def apply_mask(n: int, mask: str) -> int:
    for i in range(len(mask)):
        match mask[-(1+i)]:
            case "X":
                continue
            case "1":
                n |= 2**i
            case "0":
                n &= (2**MASK_SIZE - 1) - 2**i
    return n

def apply_mask_v2(n: int, mask: str) -> list[int]:
    values: list[int] = [n]
    for i in range(len(mask)):
        match mask[-(1+i)]:
            case "0":
                continue
            case "1":
                for j in range(len(values)):
                    values[j] |= 2**i
            case "X":
                val_length: int = len(values)
                for j in range(val_length):
                    values.append(values[j] ^ (2**i))
    return values

#Parse a mem[xxxx] = yyyy string, returning mem address and value
def parse_mem(line: str) -> tuple[int, int]:
    bracket_left: int = line.index("[")
    bracket_right: int = line.index("]")
    eq: int = line.index("=")
    address: int = int(line[bracket_left+1:bracket_right])
    val: int = int(line[eq+2:])
    return address, val


with open("input-14.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
memory: dict[int, int] = {}
mask: str = "X"*MASK_SIZE

for line in data:
    if line[1] == "a":
        mask = line[-36:]
    else:
        address, val = parse_mem(line)
        memory[address] = apply_mask(val, mask)
print(sum(memory.values()))

#Part 2
memory = {}
mask: str = "X"*MASK_SIZE
for line in data:
    if line[1] == "a":
        mask = line[-36:]
    else:
        address, val = parse_mem(line)
        for new_add in apply_mask_v2(address, mask):
            memory[new_add] = val
print(sum(memory.values()))