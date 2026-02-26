from collections import defaultdict
from enum import Enum

class ProgramState(Enum):
    RUNNING = 1
    TERMINATED = 2
    BLOCKED = 3


def get_register_or_literal(value: str, state: dict[str, int]) -> int:
    if value.isalpha():
        return state[value]
    else:
        return int(value)

def execute_instruction(program: list[str], state: dict[str, int], send_queue: list[int], receive_queue: list[int]) -> ProgramState:
    if state["PC"] < 0 or state["PC"] >= len(program):
        return ProgramState.TERMINATED
    instruction: list[str] = program[state["PC"]].split()
    match instruction[0]:
        case "snd":
            send_queue.append(get_register_or_literal(instruction[1], state))
            state["TIMES_SENT"] += 1
            state["PC"] += 1
        case "set":
            state[instruction[1]] = get_register_or_literal(instruction[2], state)
            state["PC"] += 1
        case "add":
            state[instruction[1]] += get_register_or_literal(instruction[2], state)
            state["PC"] += 1
        case "mul":
            state[instruction[1]] *= get_register_or_literal(instruction[2], state)
            state["PC"] += 1
        case "mod":
            state[instruction[1]] %= get_register_or_literal(instruction[2], state)
            state["PC"] += 1
        case "rcv":
            if len(receive_queue) == 0:
                return ProgramState.BLOCKED
            state[instruction[1]] = receive_queue.pop(0)
            state["PC"] += 1
        case "jgz":
            if get_register_or_literal(instruction[1], state) > 0:
                state["PC"] += get_register_or_literal(instruction[2], state)
            else:
                state["PC"] += 1

    return ProgramState.RUNNING

with open("input-18.txt") as f:
    data: list[str] = [line.strip() for line in f]

registers: dict[str, int] = defaultdict(int)
send_queue: list[int] = []
current_state: ProgramState = ProgramState.RUNNING
while current_state == ProgramState.RUNNING:
    receive_queue: list[int]
    current_state = execute_instruction(data, registers, send_queue, [])
print(send_queue[-1])

#---------------

registers_0: dict[str, int] = defaultdict(int)
registers_1: dict[str, int] = defaultdict(int)
registers_1["p"] = 1
send_queue_0: list[int] = []
send_queue_1: list[int] = []
state_0 = ProgramState.RUNNING
state_1 = ProgramState.RUNNING
while not (state_0 == ProgramState.TERMINATED or state_0 == ProgramState.BLOCKED and len(send_queue_1) == 0) or not (state_1 == ProgramState.TERMINATED or state_1 == ProgramState.BLOCKED and len(send_queue_0) == 0):
    state_0 = execute_instruction(data, registers_0, send_queue_0, send_queue_1)
    while state_0 == ProgramState.RUNNING:
        state_0 = execute_instruction(data, registers_0, send_queue_0, send_queue_1)
    state_1 = execute_instruction(data, registers_1, send_queue_1, send_queue_0)
    while state_1 == ProgramState.RUNNING:
        state_1 = execute_instruction(data, registers_1, send_queue_1, send_queue_0)
print(registers_1["TIMES_SENT"])

