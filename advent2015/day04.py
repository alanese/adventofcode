import hashlib

def find_zeroes(secret: bytes, count: int):
    i = 0
    while True:
        i += 1
        input_data = secret + bytes(str(i), 'ascii')
        digest = hashlib.md5(input_data).hexdigest()
        if digest[:count] == "0"*count:
            return i


with open("input-04.txt", 'rb') as f:
    data = f.read()

#Part 1
print(find_zeroes(data, 5))

#Part 2
print(find_zeroes(data, 6))