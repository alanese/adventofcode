joltage_sum = 0
with open("input-03.txt") as f:
    for bank in f:
        bank = bank.strip()
        max_joltage = 0
        for i, batt_1 in enumerate(bank):
            for batt_2 in bank[i+1:]:
                curr_joltage = 10*int(batt_1) + int(batt_2)
                if curr_joltage > max_joltage:
                    max_joltage = curr_joltage
        joltage_sum += max_joltage
print(joltage_sum)


def construct_largest(digits, length):
    if length == 1:
        return max(digits)
    else:
        max_seen = -1
        max_index = -1
        for i, v in enumerate(digits[:1-length]):
            if v > max_seen:
                max_seen = v
                max_index = i
                if max_seen == 9:
                    break
        return (10**(length-1))*max_seen + construct_largest(digits[max_index+1:], length-1)
    
joltage_sum = 0
with open("input-03.txt") as f:
    for bank in f:
        bank_digits = [int(x) for x in bank.strip()]
        joltage_sum += construct_largest(bank_digits, 12)
print(joltage_sum)

