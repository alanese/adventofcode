SUBJECT_NUMBER: int = 7

def transform(value: int, subject: int) -> int:
    return (value * subject) % 20201227

def find_loop(public_key: int) -> int:
    value: int = 1
    loop: int = 0
    while value != public_key:
        loop += 1
        value = transform(value, SUBJECT_NUMBER)
    return loop

with open("input-25.txt") as f:
    card_pk: int = int(f.readline().strip())
    door_pk: int = int(f.readline())

door_loop: int = find_loop(door_pk)
value: int = 1
for _ in range(door_loop):
    value = transform(value, card_pk)
print(value)
