from itertools import product

with open("input-02.txt") as f:
    data: str = f.read().strip()

#Part 1
program: list[int] = [int(x) for x in data.split(",")]
program[1] = 12
program[2] = 2
pc: int = 0

while 0 <= pc < len(program):
    match program[pc]:
        case 1:
            program[program[pc+3]] = program[program[pc+1]] + program[program[pc+2]]
            pc += 4
        case 2:
            program[program[pc+3]] = program[program[pc+1]] * program[program[pc+2]]
            pc += 4
        case 99:
            break


print(program[0])

#Part 2
TARGET_INPUT: int = 19690720

for noun, verb in product(range(100), repeat=2):
    program = [int(x) for x in data.split(",")]
    program[1] = noun
    program[2] = verb
    pc = 0
    while 0 <= pc < len(program):
        match program[pc]:
            case 1:
                program[program[pc+3]] = program[program[pc+1]] + program[program[pc+2]]
                pc += 4
            case 2:
                program[program[pc+3]] = program[program[pc+1]] * program[program[pc+2]]
                pc += 4
            case 99:
                break
        if program[0] == TARGET_INPUT:
            print(100*noun + verb)
            break