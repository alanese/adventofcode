import re

def eval_mul(instruction: str) -> int:
    a, _, b = instruction[4:-1].partition(",")
    return int(a) * int(b)

with open("input-03.txt") as f:
    data: str = f.read()
exp = re.compile(r'mul\(\d+,\d+\)')
print(sum(eval_mul(match) for match in exp.findall(data)))

enabled: bool = True
total: int = 0
while len(data) > 0:
    if enabled:
        chunk, _, data = data.partition("don't()")
        total += sum(eval_mul(match) for match in exp.findall(chunk))
    else:
        chunk, _, data = data.partition("do()")
    enabled = not enabled
print(total)