from collections import defaultdict

class Rule():
    _next_id: int = 0

    def __init__(self, source: str, output: list[str]):
        self.source: str = source
        self.output: list[str] = output
    
    def __repr__(self) -> str:
        return f"{self.source} -> {" ".join(self.output)}"

    @classmethod
    def binarize(cls, source: str, output: list[str])  -> list[Rule]:
        if len(output) <= 2:
            return [Rule(source, output)]
        else:
            inter: str = f"INTER{Rule._next_id}"
            Rule._next_id += 1
            first: list[Rule] = [Rule(source, [output[0], inter])]
            rest: list[Rule] = cls.binarize(inter, output[1:])
            return first+rest


def parse_rules(line: str) -> list[Rule]:
    source, _, rest = line.partition(" ")
    source = source[:-1]
    outputs: list[str] = rest.split(" | ")
    res: list[Rule] = []
    for output in outputs:
        if output[0] == "\"":
            res.append(Rule(source, [output[1:-1]]))
        else:
            res += Rule.binarize(source, output.split())
    return res

def match(target: str, start: str, rules: dict[str, list[Rule]], seen: dict[tuple[str, str], bool] = {}) -> bool:
    if (start,target) in seen:
        return seen[(start,target)]
    if len(target) == 0:
        return False
    else:
        for rule in rules[start]:
            if len(rule.output) == 1:
                if rule.output[0] == target or match(target, rule.output[0], rules, seen):
                    return True
            else:
                for divider in range(1, len(target)):
                    first: str = target[:divider]
                    second: str = target[divider:]
                    if match(first, rule.output[0], rules, seen) and match(second, rule.output[1], rules, seen):
                        seen[(start, target)] = True
                        return True
        seen[(start, target)] = False
        return False

with open("input-19.txt") as f:
    data: list[str] = [line.strip() for line in f]

delim: int = data.index("")
messages: list[str] = data[delim+1:]
rules: dict[str, list[Rule]] = defaultdict(list)
for line in data[:delim]:
    for rule in parse_rules(line):
        rules[rule.source].append(rule)

#Part 1
match_count: int = 0
for i, message in enumerate(messages):
    if match(message, "0", rules, seen={}):
        match_count += 1
print(match_count)

#Part 2
rules['8'] = parse_rules('8: 42 | 42 8')
new_11 = parse_rules('11: 42 31 | 42 11 31')
rules['11'] = []
for rule in new_11:
    rules[rule.source].append(rule)

match_count: int = 0
for i, message in enumerate(messages):
    if match(message, "0", rules, seen = {}):
        match_count += 1
print(match_count)