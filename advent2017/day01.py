def captcha(sequence: str, offset: int) -> int:
    total: int = 0
    for i, chr in enumerate(sequence):
        if chr == sequence[(i+offset)%len(sequence)]:
            total += int(chr)
    return total


with open("input-01.txt") as f:
    sequence: str = f.read().strip()


total: int = 0
for i, char in enumerate(sequence[:-1]):
    if char == sequence[i+1]:
        total += int(char)
if sequence[-1] == sequence[0]:
    total += int(sequence[0])

print(captcha(sequence, 1))
print(captcha(sequence, len(sequence)//2))