def streaks(digits: str) -> list[tuple[str, int]]:
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

def streak_to_str(streak: tuple[str, int], cache: dict) -> str:
    if streak not in cache:
        cache[streak] = str(streak[1]) + streak[0]
    return cache[streak]

def lookandsay(digits: str, cache: dict) -> str:
    return "".join([streak_to_str(streak, cache) for streak in streaks(digits)])

with open("input-10.txt") as f:
    data:str = f.read()

#Part 1
cache: dict = {}
new_digits: str = data
for _ in range(40):
    new_digits = lookandsay(new_digits, cache)

print(len(new_digits))

#Part 2
cache = {}
new_digits = data
for _ in range(50):
    new_digits = lookandsay(new_digits, cache)

print(len(new_digits))
