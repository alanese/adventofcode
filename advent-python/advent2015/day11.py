VALID_CHARS = "abcdefghjkmnpqrstuvwxyz"
def increment_char(char: str) -> str:
    index = (VALID_CHARS.index(char) + 1) % len(VALID_CHARS)
    return VALID_CHARS[index]

def increment_list(chars: list[str]) -> list[str]:
    if len(chars) == 0:
        return chars
    last = increment_char(chars[-1])
    if last != 'a':
        return chars[:-1] + [last]
    else:
        return increment_list(chars[:-1]) + [last]

def check_password(chars: list[str]) -> bool:
    pairs = set()
    for char in chars:
        if char not in VALID_CHARS:
            return False
    for i in range(len(chars) - 1):
        if chars[i] == chars[i+1]:
            pairs.add(chars[i] + chars[i+1])
    if len(pairs) < 2:
        return False
    
    for i in range(len(chars) - 2):
        if ord(chars[i+1]) == ord(chars[i]) + 1 and ord(chars[i+2]) == ord(chars[i]) + 2:
            return True
    return False


with open("input-11.txt") as f:
    password = list(f.read())

#Part 1
while not check_password(password):
    password = increment_list(password)

print("".join(password))

#Part 2
password = increment_list(password)
while not check_password(password):
    password = increment_list(password)

print("".join(password))