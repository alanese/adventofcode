#Executes the given step, returns new values for (pc, a, b, c, output (if any))
def step(program: list[int], pc: int, a: int, b:int, c: int) -> tuple[int, int, int, int, int|None]:
    opcode: int = program[pc]
    literal_op: int = program[pc+1]
    combo_op: int = program[pc+1]
    if combo_op == 4:
        combo_op = a
    elif combo_op == 5:
        combo_op = b
    elif combo_op == 6:
        combo_op = c

    output: int | None = None
    next_pc: int = pc+2
    match opcode:
        case 0:
            a = a//(2**combo_op)
        case 1:
            b = b^literal_op
        case 2:
            b = combo_op%8
        case 3:
            if a != 0:
                next_pc = literal_op
        case 4:
            b = b^c
        case 5:
            output = combo_op%8
        case 6:
            b = a//(2**combo_op)
        case 7:
            c = a//(2**combo_op)
    return next_pc, a, b, c, output

def run_program(program: list[int], a: int, b: int, c: int) -> list[int]:
    #seen_states: set[tuple[int, int, int, int]]= set()
    output: list[int] = []
    pc: int = 0
    while 0 <= pc < len(program):
        pc, a, b, c, next_output = step(program, pc, a, b, c)
        if next_output is not None:
            output.append(next_output)
    return output

#Return largest n such that l_1[:n] == l_2[:n]
def prefix_size(l_1: list[int], l_2: list[int]) -> int:
    for i, (num_1, num_2) in enumerate(zip(l_1, l_2)):
        if num_1 != num_2:
            return i
    return min(len(l_1), len(l_2))


with open("input-17.txt") as f:
    data: list[str] = [line.strip() for line in f]

a: int = int(data[0][12:])
b: int = int(data[1][12:])
c: int = int(data[2][12:])

program: list[int] = [int(x) for x in data[4][9:].split(",")]

print(",".join(str(x) for x in run_program(program, a, b, c)))