from math import prod

class Monkey:
    def __init__(self: Monkey, operation: str, operand: str, test_divisor: int, true_target: Monkey|None = None, false_target: Monkey|None = None):
        self.operation: str = operation
        self.operand: str = operand
        self.test_divisor: int = test_divisor
        self.true_target: Monkey = true_target or self
        self.false_target: Monkey = false_target or self
        self.queue: list[int] = []
        self.inspection_count: int = 0

    def inspect(self: Monkey, worry_decay: bool = True, mod: int = 0):
        next: int = self.queue.pop(0)
        if self.operand == "old":
            operand: int = next
        else:
            operand: int = int(self.operand)
        if self.operation == "+":
            next = next + operand
        else:
            next = next * operand
        if worry_decay:
            next = next // 3
        if mod != 0:
            next = next % mod
        if next % self.test_divisor == 0:
            self.true_target.queue.append(next)
        else:
            self.false_target.queue.append(next)
        self.inspection_count += 1
    
    def take_turn(self: Monkey, worry_decay: bool = True, mod: int = 0):
        while len(self.queue) > 0:
            self.inspect(worry_decay, mod)

    def __str__(self: Monkey) -> str:
        return f"Monkey op: {self.operation}, operand: {self.operand}, divisor: {self.test_divisor}"

def parse_monkeys(data: list[str]) -> list[Monkey]:
    monkeys: list[Monkey] = []
    targets: list[tuple[int, int]] = []
    index: int = 0
    while index < len(data):
        #Monkeys are listed in order, so skip id line
        #Process starting items
        index += 1
        items_str: str = data[index][data[index].index(":")+2:]
        items: list[int] = [int(x) for x in items_str.split(", ")]
        #Process monkey operation
        index += 1
        op_list: list[str] = data[index].split()
        operation: str = op_list[-2]
        operand: str = op_list[-1]
        #Process test
        index += 1
        divisor: int = int(data[index].split()[-1])
        #Process true target
        index += 1
        true_target: int = int(data[index].split()[-1])
        #Process false target
        index += 1
        false_target: int = int(data[index].split()[-1])
        #advance to next monkey
        index += 2
        #Add monkey and targets to lists
        monkeys.append(Monkey(operation, operand, divisor))
        monkeys[-1].queue = items
        targets.append((true_target, false_target))
    for i, (true_target, false_target) in enumerate(targets):
        monkeys[i].true_target = monkeys[true_target]
        monkeys[i].false_target = monkeys[false_target]
    return monkeys

with open("input-11.txt") as f:
    data: list[str] = [line.strip() for line in f]

monkeys: list[Monkey] = parse_monkeys(data)

#Part 1
for _ in range(20):
    for monkey in monkeys:
        monkey.take_turn()

inspection_counts: list[int] = [monkey.inspection_count for monkey in monkeys]
inspection_counts.sort(reverse=True)
print(inspection_counts[0] * inspection_counts[1])

#Reset monkeys
monkeys = parse_monkeys(data)

modulus = prod(monkey.test_divisor for monkey in monkeys)

#Part 2
for turn in range(10000):
    print(f"Turn {turn+1} of 10000")
    for monkey in monkeys:
        #Cap worry values - mod by product of monkey divisors to preserve remainders
        monkey.take_turn(False, modulus)

inspection_counts: list[int] = [monkey.inspection_count for monkey in monkeys]
inspection_counts.sort(reverse=True)
print(inspection_counts[0] * inspection_counts[1])