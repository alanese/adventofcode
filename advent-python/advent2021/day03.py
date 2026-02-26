from collections import Counter

#Returns most and least common bits in the list of "1" or "0"; returns "1", "0" if tied
def most_least_common(bits: list[str]) -> tuple[str, str]:
    counter: dict[str, int] = Counter(bits)
    if counter["1"] >= counter["0"]:
        return "1", "0"
    else:
        return "0", "1"
    
with open("input-03.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
gamma: str = ""
epsilon: str = ""
for i in range(len(data[0])):
    most, least = most_least_common([x[i] for x in data])
    gamma += most
    epsilon += least

print(int(gamma, base=2) * int(epsilon, base=2))

#Part 2

i: int = 0
working_data: list[str] = data[:]
while len(working_data) > 1 and i < len(working_data[0]):
    most, _ = most_least_common([x[i] for x in working_data])
    working_data = [x for x in working_data if x[i] == most]
    i += 1
oxygen_rating: int = int(working_data[0], base=2)

i = 0
working_data = data[:]
while len(working_data) > 1 and i < len(working_data[0]):
    _, least = most_least_common([x[i] for x in working_data])
    working_data = [x for x in working_data if x[i] == least]
    i += 1
scrubber_rating: int = int(working_data[0], base=2)

print(oxygen_rating * scrubber_rating)
