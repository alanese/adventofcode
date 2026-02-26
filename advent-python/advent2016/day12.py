#Part 2 needs work - took an hour to run with this code
registers: dict[str, int] = {"a": 0,
                             "b": 0,
                             "c": 1,
                             "d": 0}

with open("input-12.txt") as f:
    program: list[list[str]] = [line.split() for line in f]

pc = 0
while 0 <= pc < len(program):
    command: list[str] = program[pc]
    print(f"{pc}: {command} | {registers}")
    match command[0]:
        case "cpy":
            if command[1].isnumeric():
                registers[command[2]] = int(command[1])
            else:
                registers[command[2]] = registers[command[1]]
            pc += 1
        case "inc":
            registers[command[1]] += 1
            pc += 1
        case "dec":
            registers[command[1]] -= 1
            pc += 1
        case "jnz":
            check_val:int = -1
            if command[1].isnumeric():
                check_val = int(command[1])
            else:
                check_val = registers[command[1]]
            if check_val != 0:
                pc += int(command[2])
            else:
                pc += 1
        case _:
            print("ERROR")
            break

print(registers["a"])