from collections import Counter

def valid_passphrase_v1(phrase: str) -> bool:
    phrase_split: list[str] = phrase.split()
    for i, word1 in enumerate(phrase_split):
        for word2 in phrase_split[i+1:]:
            if word1 == word2:
                return False
    return True

def valid_passphrase_v2(phrase: str) -> bool:
    phrase_counters: list[Counter] = [Counter(x) for x in phrase.split()]
    for i, word1 in enumerate(phrase_counters):
        for word2 in phrase_counters[i+1:]:
            if word1 == word2:
                return False
    return True

valid_v1_counter: int = 0
valid_v2_counter: int = 0
with open("input-04.txt") as f:
    for line in f:
        if valid_passphrase_v1(line.strip()):
            valid_v1_counter += 1
        if valid_passphrase_v2(line.strip()):
            valid_v2_counter += 1

print(valid_v1_counter)
print(valid_v2_counter)