def execute_command(command: str, data: list[str]) -> list[str]:
    match command[0]:
        case "s":
            spin_dist: int = len(data) - int(command[1:])
            data = data[spin_dist:] + data[:spin_dist]
        case "x":
            pos_1: int = int(command[1:command.index("/")])
            pos_2: int = int(command[command.index("/")+1:])
            data[pos_1], data[pos_2] = data[pos_2], data[pos_1]
        case "p":
            pos_1 = data.index(command[1:command.index("/")])
            pos_2 = data.index(command[command.index("/")+1:])
            data[pos_1], data[pos_2] = data[pos_2], data[pos_1]

    return data

def execute_shuffle(commands: list[str], data: list[str]) -> list[str]:
    for command in commands:
        data = execute_command(command, data)
    return data

LETTERS: list[str] = list("abcdefghijklmnop")

letters: list[str] = LETTERS.copy()

with open("input-16.txt") as f:
    data: str = f.read()

commands: list[str] = data.split(",")
letters = execute_shuffle(commands, letters)

print("".join(letters))

i: int = 1
while letters != LETTERS:
    i += 1
    letters = execute_shuffle(commands, letters)
for _ in range(1000000000 % i):
    letters = execute_shuffle(commands, letters)
print("".join(letters))