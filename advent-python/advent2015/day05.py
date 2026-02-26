VOWELS = "aeiou"
BAD_PAIRS = (('a', 'b'),
             ('c', 'd'),
             ('p', 'q'),
             ('x', 'y'))

def is_nice_p1(check_string: str) -> bool:
    vowel_count = 0
    double = False
    for i, c in enumerate(check_string[:-1]):
        if (c, check_string[i+1]) in BAD_PAIRS:
            return False
        if c in VOWELS:
            vowel_count += 1
        if (not double) and c == check_string[i+1]:
            double = True
    if check_string[-1] in VOWELS:
        vowel_count += 1
    return (vowel_count >= 3) and double

def is_nice_p2(check_string: str) -> bool:
    double_pair = False
    one_between = False

    for i in range(len(check_string)-2):
        if (not one_between) and check_string[i] == check_string[i+2]:
            one_between = True
        if (not double_pair) and check_string[i:i+2] in check_string[i+2:]:
            double_pair = True

    return one_between and double_pair


with open("input-05.txt") as f:
    data = [line.strip() for line in f]

#Part 1
nice_p1_count = 0
for line in data:
    if is_nice_p1(line):
        nice_p1_count += 1
print(nice_p1_count)

#Part 2
nice_p2_count = 0
for line in data:
    if is_nice_p2(line):
        nice_p2_count += 1
print(nice_p2_count)