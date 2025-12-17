from typing import TypeVar
from itertools import batched

T = TypeVar('T')
def rotate_left(xs: list[T], distance: int) -> list[T]:
    if len(xs) <= 1:
        return xs
    else:
        distance = distance % len(xs)
        return xs[distance:] + xs[:distance]
    

def knot(xs: list[T], position: int, length: int) -> list[T]:
    if length > len(xs):
        return xs
    xs = rotate_left(xs, position)
    xs[:length] = reversed(xs[:length])
    xs = rotate_left(xs, len(xs) - position)
    return xs

def knot_round(xs: list[T], lengths: list[int], position: int=0, skip: int=0) -> tuple[list[T], int, int]:
    for length in lengths:
        xs = knot(xs, position, length)
        position = (position+length+skip) % len(xs)
        skip += 1
    return xs, position, skip

def xor_block(chars: tuple[int, ...]) -> int:
    val: int = 0
    for char in chars:
        val ^= char
    return val

skip_size: int = 0
position: int = 0
current_list = list(range(256))
with open("input-10.txt") as f:
    init_data: str = f.read().strip()

data: list[int] = [int(x) for x in init_data.split(",")]

current_list, position, skip_size = knot_round(current_list, data, position, skip_size)

print(current_list[0] * current_list[1])

#-----------

current_list = list(range(256))
lengths: list[int] = [ord(x) for x in init_data] + [17, 31, 73, 47, 23]


skip_size = 0
position = 0
for _ in range(64):
    current_list, position, skip_size = knot_round(current_list, lengths, position, skip_size)

hash: str = ""
for block in batched(current_list, n=16):
    hash += f"{xor_block(block):02x}"

print(hash)