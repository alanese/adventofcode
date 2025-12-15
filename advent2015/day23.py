from typing import Dict, List

def run(program: List[List[str]], init_a: int, init_b:int) -> Dict[str, int]:
    registers = {'a': init_a, 'b': init_b}
    program_counter = 0
    while 0 <= program_counter < len(program):
        instruction = program[program_counter]
        match instruction[0]:
            case "hlf":
                registers[instruction[1]] //= 2
                program_counter += 1
            case "tpl":
                registers[instruction[1]] *= 3
                program_counter += 1
            case "inc":
                registers[instruction[1]] += 1
                program_counter += 1
            case "jmp":
                program_counter += int(instruction[1])
            case "jie":
                if registers[instruction[1][0]] % 2 == 0:
                    program_counter += int(instruction[2])
                else:
                    program_counter += 1
            case "jio":
                if registers[instruction[1][0]] == 1:
                    program_counter += int(instruction[2])
                else:
                    program_counter += 1
    return registers


with open("input-23.txt") as f:
    program = [line.strip().split() for line in f]

print(run(program, 0, 0))
print(run(program, 1, 0))