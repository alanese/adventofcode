def execute_instruction(acc: int, pc: int, program:list[tuple[str, int]]) -> tuple[int, int]:
    """
    Executes a single instruction in the computer
    
    :param acc: Accumulator value
    :type acc: int
    :param pc: Program counter
    :type pc: int
    :param program: The program instructions
    :type program: list[tuple[str, int]]
    :return: The new accumulator and program counter
    :rtype: tuple[int, int]
    """
    operator: str
    operand: int
    operator, operand = program[pc]
    match operator:
        case "acc":
            acc += operand
            pc += 1
        case "jmp":
            pc += operand
        case "nop":
            pc += 1

    return acc, pc

def run_program(program: list[tuple[str, int]]) -> tuple[int, int]:
    """
    Docstring for run_program
    
    :param program: The program instructions
    :type program: list[tuple[str, int]]
    :return: The final accumulator and pc values
    :rtype: tuple[int, int]
    """

    pc: int = 0
    acc: int = 0
    seen: set[int] = set()
    while pc not in seen and 0 <= pc < len(program):
        seen.add(pc)
        acc, pc = execute_instruction(acc, pc, program)


    return acc, pc

def parse_instructions(instructions: list[str]) -> list[tuple[str, int]]:
    program: list[tuple[str, int]] = []
    for line in instructions:
        boundary: int = line.index(" ")
        program.append((line[:boundary], int(line[boundary+1:])))
    return program

with open("input-08.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
program: list[tuple[str, int]] = parse_instructions(data)

seen: set[int] = set()
acc: int = 0
pc: int = 0
while pc not in seen:
    seen.add(pc)
    acc, pc = execute_instruction(acc, pc, program)

print(acc)

#Part 2
program = parse_instructions(data)
jumps: list[int] = [i for i in range(len(program)) if program[i][0] == "jmp"]
print(jumps)
for jump in jumps:
    working_program = list(program)
    working_program[jump] = ("nop", 0)
    acc, pc = run_program(working_program)
    if pc < 0 or pc >= len(program):
        print(acc)
        break