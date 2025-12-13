from typing import List, Tuple, Dict


def streaks(digits: str) -> List[Tuple[str, int]]:
    if len(digits) == 0:
        return []
    
    s = []
    cur_char = digits[0]
    cur_length = 1
    i = 1
    for digit in digits[1:]:
        if digit == cur_char:
            cur_length += 1
        else:
            s.append((cur_char, cur_length))
            cur_char = digit
            cur_length = 1

    s.append((cur_char, cur_length))
    return s

def streak_to_str(streak: Tuple[str, int], cache: Dict) -> str:
    if streak not in cache:
        cache[streak] = str(streak[1]) + streak[0]
    return cache[streak]

def lookandsay(digits: str, cache: Dict) -> str:
    return "".join([streak_to_str(streak, cache) for streak in streaks(digits)])

with open("input-10.txt") as f:
    digits = f.read()

cache = {}
for _ in range(40):
    digits = lookandsay(digits, cache)

print(len(digits))

#-------
for _ in range(10):
    digits = lookandsay(digits, cache)

print(len(digits))
