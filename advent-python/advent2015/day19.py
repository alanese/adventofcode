from typing import Dict, Generator, List, Optional, Set, Tuple
from collections import defaultdict
from string import ascii_uppercase

class Rule:
    next_id:int = 1

    def __init__(self:Rule, source:str, to: Tuple[str, str], weight: int=1):
        self.source = source
        self.to = to
        self.weight = weight

    def __str__(self):
        return f"{self.source} => {self.to} ({self.weight})"
    def __repr__(self):
        return str(self)
    @classmethod
    def binarize(cls, source: str, to: List[str]) -> List[Rule]:
        if len(to) < 2:
            return []
        elif len(to) == 2:
            return [Rule(source, (to[0], to[1]), 1)]
        else:
            inter = "INTER" + str(cls.next_id)
            cls.next_id += 1
            r1 = Rule(source, (to[0], inter), 0)
            rest = cls.binarize(inter, to[1:])
            return [r1] + rest



def parse_sequence(sequence: str) -> List[str]:
    if len(sequence) == 0:
        return []
    atoms: List[str] = []
    cur_atom:str = sequence[0]
    for i, char in enumerate(sequence[1:]):
        if char in ascii_uppercase:
            atoms.append(cur_atom)
            cur_atom = char
        else:
            cur_atom += char
    atoms.append(cur_atom)
    return atoms

def parse_rule(line: str) -> Tuple[str, List[str]]:
    line_split = line.split()
    return line_split[0], parse_sequence(line_split[2])

#This was a tricky one! I'm pretty sure this is a version of the CYK algorithm
def short_parse(word: List[str], start: str, rules: Dict[str, List[Rule]], seen: Dict[Tuple[str, str], Optional[int]] = {}) -> Optional[int]:
    word_str = "".join(word)
    if [start] == word:
        return 0
    
    if (word_str, start) in seen:
        return seen[(word_str, start)]
    
    shortest_path = None
    for i in range(1, len(word)):
        left = word[:i]
        right = word[i:]
        for rule in rules[start]:
            left_dist = short_parse(left, rule.to[0], rules, seen)
            if left_dist is None:
                continue
            right_dist = short_parse(right, rule.to[1], rules, seen)
            if right_dist is None:
                continue
            split_short = rule.weight + left_dist + right_dist
            if shortest_path is None or shortest_path > split_short:
                shortest_path = split_short

    print(f"Shortest path {shortest_path} from {start} => {word_str}")
    seen[(word_str, start)] = shortest_path
    return shortest_path

with open("input-19.txt") as f:
    lines: List[str] = f.readlines()
    lines = [line.strip() for line in lines]

rules: Dict[str, List[List[str]]] = defaultdict(list)
binary_rules: Dict[str, List[Rule]] = defaultdict(list)

for rule in lines[:-2]:
    src, target = parse_rule(rule)
    rules[src].append(target)
    for binary_rule in Rule.binarize(src, target):
        binary_rules[binary_rule.source].append(binary_rule)
start_sequence = parse_sequence(lines[-1])

found_sequences: Set[str] = set()
for i, atom in enumerate(start_sequence):
    for replacement in rules[atom]:
        found_sequences.add("".join(start_sequence[:i] + replacement + start_sequence[i+1:]))

print(len(found_sequences))
print(short_parse(start_sequence, "e", binary_rules))