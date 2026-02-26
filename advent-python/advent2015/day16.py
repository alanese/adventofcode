from typing import Dict, List, Tuple

def is_subdict(dict1: Dict, dict2: Dict) -> bool:
    for k, v in dict1.items():
        if k not in dict2 or dict2[k] != v:
            return False
    return True

def valid_sue(sue: Dict[str, int], known_sue:Dict[str, int], gt_keys: List[str], lt_keys: List[str], eq_keys: List[str]) -> bool:
    for key in gt_keys:
        if key in sue and (key not in known_sue or sue[key] <= known_sue[key]):
            return False
    for key in lt_keys:
        if key in sue and (key not in known_sue or sue[key] >= known_sue[key]):
            return False
    for key in eq_keys:
        if key in sue and (key not in known_sue or sue[key] != known_sue[key]):
            return False
    return True


def parse_sue(sue: str) -> Tuple[int, Dict[str, int]]:
    sue_split = sue.split(maxsplit=2)
    sue_number = int(sue_split[1][:-1])
    new_sue: Dict[str, int] = {}
    for entry in sue_split[2].split(","):
        keyval = entry.strip().split(":")
        key = keyval[0].strip()
        val = int(keyval[1].strip())
        new_sue[key] = val
    return sue_number, new_sue

known_sue: Dict[str, int] = {'children': 3,
                             'cats': 7,
                             'samoyeds': 2,
                             'pomeranians': 3,
                             'akitas': 0,
                             'vizslas': 0,
                             'goldfish': 5,
                             'trees': 3,
                             'cars': 2,
                             'perfumes': 1}

GT_KEYS = ['cats', 'trees']
LT_KEYS = ['pomeranians', 'goldfish']
EQ_KEYS = ['children', 'samoyeds', 'akitas', 'vizslas', 'cars', 'perfumes']

with open("input-16.txt") as f:
    for line in f:
        number, sue = parse_sue(line)
        if is_subdict(sue, known_sue):
            print(f"Part 1: {number}")
        if valid_sue(sue, known_sue, GT_KEYS, LT_KEYS, EQ_KEYS):
            print(f"Part 2: {number}")