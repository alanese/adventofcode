with open("input-02.txt") as f:
    data = f.read()

r = data.split(",")
invalid_sum = 0
for nums in r:
    bounds = nums.split("-")
    start = int(bounds[0])
    end = int(bounds[1])
    for i in range(start, end+1):
        i_str = str(i)
        i_length = len(i_str)
        if i_length % 2 != 0:
            continue
        if i_str[:i_length//2] == i_str[i_length//2:]:
            invalid_sum += i

print(invalid_sum)

def is_n_dupes(num, n):
    num_str = str(num)
    num_len = len(num_str)
    if num_len % n != 0:
        return False
    part_length = num_len // n
    first_part = num_str[:part_length]
    for i in range(1, n):
        if first_part != num_str[i*part_length:(i+1)*part_length]:
            return False
    return True

def is_any_dupes(num):
    num_len = len(str(num))
    for i in range(2,num_len+1):
        if num_len % i == 0 and is_n_dupes(num, i):
            return True
    return False


invalid_sum = 0
for nums in r:
    bounds = nums.split("-")
    start = int(bounds[0])
    end = int(bounds[1])
    for i in range(start, end+1):
        if is_any_dupes(i):
            invalid_sum += i

print(invalid_sum)
