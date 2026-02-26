NUM_REGISTERS: int = 4

def valid_registers(*args: int) -> bool:
    for arg in args:
        if not 0<=arg<NUM_REGISTERS:
            return False
    return True

def parse_list(data: str) -> list[int]:
    return [int(x) for x in data[1:-1].split(", ")]

def handle_addr(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_B, operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = rv[operand_A]+rv[operand_B]
        return rv

def handle_addi(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = rv[operand_A] + operand_B
        return rv
    
def handle_mulr(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_B, operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = rv[operand_A] * rv[operand_B]
        return rv

def handle_muli(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = rv[operand_A] * operand_B
        return rv
    
def handle_banr(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_B, operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = rv[operand_A] & rv[operand_B]
        return rv
    
def handle_bani(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = rv[operand_A] & operand_B
        return rv
    
def handle_borr(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_B, operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = rv[operand_A] | rv[operand_B]
        return rv
    
def handle_bori(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = rv[operand_A] | operand_B
        return rv
    
def handle_setr(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = rv[operand_A]
        return rv
    
def handle_seti(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_C):
        return []
    else:
        rv = list(registers)
        rv[operand_C] = operand_A
        return rv
    
def handle_gtir(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_B, operand_C):
        return []
    else:
        rv = list(registers)
        if operand_A > rv[operand_B]:
            rv[operand_C] = 1
        else:
            rv[operand_C] = 0
        return rv
    
def handle_gtri(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_C):
        return []
    else:
        rv = list(registers)
        if rv[operand_A] > operand_B:
            rv[operand_C] = 1
        else:
            rv[operand_C] = 0
        return rv
    
def handle_gtrr(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_B, operand_C):
        return []
    else:
        rv = list(registers)
        if rv[operand_A] > rv[operand_B]:
            rv[operand_C] = 1
        else:
            rv[operand_C] = 0
        return rv
    
def handle_eqir(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_B, operand_C):
        return []
    else:
        rv = list(registers)
        if operand_A == rv[operand_B]:
            rv[operand_C] = 1
        else:
            rv[operand_C] = 0
        return rv
    
def handle_eqri(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_C):
        return []
    else:
        rv = list(registers)
        if rv[operand_A] == operand_B:
            rv[operand_C] = 1
        else:
            rv[operand_C] = 0
        return rv
    
def handle_eqrr(operand_A: int, operand_B: int, operand_C: int, registers: list[int]) -> list[int]:
    if not valid_registers(operand_A, operand_B, operand_C):
        return []
    else:
        rv = list(registers)
        if rv[operand_A] == rv[operand_B]:
            rv[operand_C] = 1
        else:
            rv[operand_C] = 0
        return rv
    
opcodes: dict = {"addr": handle_addr, "addi": handle_addi,
                 "mult": handle_mulr, "muli": handle_muli,
                 "banr": handle_banr, "bani": handle_bani,
                 "borr": handle_borr, "bori": handle_bori,
                 "setr": handle_setr, "seti": handle_seti,
                 "gtir": handle_gtir, "gtri": handle_gtri, "gtrr": handle_gtrr,
                 "eqir": handle_eqir, "eqri": handle_eqri, "eqrr": handle_eqrr}

with open("input-16-p1.txt") as f:
    data: list[str] = [line.strip() for line in f]

threeplus: int = 0
samples: list[str] = list(data)
while len(samples) > 0:
    before_str: str = samples.pop(0)
    before: list[int] = parse_list(before_str[before_str.index("["):])
    command: list[int] = [int(x) for x in samples.pop(0).split()]
    after_str: str = samples.pop(0)
    after: list[int] = parse_list(after_str[after_str.index("["):])
    ok_count: int = 0
    for func in opcodes.values():
        check_after: list[str] = func(command[1], command[2], command[3], before)
        if check_after == after:
            ok_count += 1
    if ok_count >= 3:
        threeplus += 1
    if len(samples) > 0:
        samples.pop(0)

print(threeplus)

#Part 2

with open("input-16-p2.txt") as f:
    program: list[str] = [line.strip() for line in f]

samples = list(data)
possible_opcodes: dict[int, set[str]] = {i: set(opcodes.keys()) for i in range (len(opcodes))}

while len(samples) > 0:
    before_str: str = samples.pop(0)
    before: list[int] = parse_list(before_str[before_str.index("["):])
    command: list[int] = [int(x) for x in samples.pop(0).split()]
    after_str: str = samples.pop(0)
    after: list[int] = parse_list(after_str[after_str.index("["):])
    for opcode, opfunc in opcodes.items():
        if opfunc(command[1], command[2], command[3], before) != after:
            if opcode in possible_opcodes[command[0]]:
                possible_opcodes[command[0]].remove(opcode)
    if len(samples) > 0:
        samples.pop(0)

found_opcodes: dict[int, str] = {}
while len(found_opcodes) < 16:
    for num, opcode_set in list(possible_opcodes.items()):
        if len(opcode_set) == 1:
            found_opcodes[num] = opcode_set.pop()
            del possible_opcodes[num]
            for possible_opcode_set in possible_opcodes.values():
                if found_opcodes[num] in possible_opcode_set:
                    possible_opcode_set.remove(found_opcodes[num])
            break

registers: list[int] = [0, 0, 0, 0]
for line in program:
    command: list[int] = [int(x) for x in line.split()]
    registers = opcodes[found_opcodes[command[0]]](command[1], command[2], command[3], registers)

print(registers)