with open("input-05.txt") as f:
    data: str = f.read().strip()

def react(polymer: list[str]):
    i: int = 0
    while i < len(polymer)-1:
        if abs(ord(polymer[i]) - ord(polymer[i+1])) == ord('a') - ord('A'):
            polymer.pop(i)
            polymer.pop(i)
            i = max(i-1, 0)
        else:
            i += 1

#Part 1
polymer: list[str] = list(data)
react(polymer)
print(len(polymer))

#Part 2
min_length = len(data)
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    polymer = list(data)
    lower_letter = chr(ord(letter) + (ord('a') - ord('A')))
    if letter not in polymer and lower_letter not in polymer:
        continue
    while letter in polymer:
        polymer.remove(letter)
    while lower_letter in polymer:
        polymer.remove(lower_letter)
    react(polymer)
    if len(polymer) < min_length:
        min_length = len(polymer)

print(min_length)