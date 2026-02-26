from functools import total_ordering
import re

@total_ordering
class Unit:
    def __init__(self: Unit, value: int|list[Unit]):
        self.value: int|list[Unit] = value

    def __eq__(self: Unit, other: object) -> bool:
        if not isinstance(other, Unit):
            return False
        else:
            return self.value == other.value
    
    def __lt__(self: Unit, other: object) -> bool:
        if not isinstance(other, Unit):
            return NotImplemented
        elif isinstance(self.value, int) and isinstance(other.value, list):
            return Unit([self]) < other
        elif isinstance(self.value, list) and isinstance(other.value, int):
            return self < Unit([other])
        elif isinstance(self.value, int) and isinstance(other.value, int):
            return self.value < other.value
        elif isinstance(self.value, list) and isinstance(other.value, list):
            for s, o in zip(self.value, other.value):
                if s < o:
                    return True
                elif o < s:
                    return False
            return len(self.value) < len(other.value)
        else:
            raise ValueError("Invalid values")
        
REGEX: re.Pattern = re.compile(r"\[|\]|\d+")
def tokenize(packet: str) -> list[str]:
    return REGEX.findall(packet)

def parse_packet(tokens: list[str]) -> Unit:
    stack: list[str|Unit] = []
    for token in tokens:
        if token.isnumeric():
            stack.append(Unit(int(token)))
        elif token == "[":
            stack.append(token)
        elif token == "]":
            sublist: list[Unit] = []
            while isinstance(stack[-1], Unit):
                sublist.insert(0, stack.pop()) #Ignore the typing error, it's guaranteed to work
            stack.pop()
            stack.append(Unit(sublist))
        else:
            raise ValueError(f"Invalid token {token}")
    if isinstance(stack[0], Unit):
        return stack[0]
    raise ValueError("Malformed packet")

with open("input-13.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
index: int = 0
valid_sum: int = 0
while index < len(data):
    if parse_packet(tokenize(data[index])) < parse_packet(tokenize(data[index+1])):
        valid_sum += index//3 + 1
    index += 3
print(valid_sum)

#Part 2
packets: list[Unit] = [parse_packet(tokenize(packet)) for packet in data if packet != ""]
divider_1: Unit = parse_packet(tokenize("[[2]]"))
divider_2: Unit = parse_packet(tokenize("[[6]]"))
packets += [divider_1, divider_2]
packets.sort()
print((packets.index(divider_1)+1)*(packets.index(divider_2)+1))