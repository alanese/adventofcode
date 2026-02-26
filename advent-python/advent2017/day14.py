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

def knot_hash(data: bytes) -> bytes:
    skip: int = 0
    position: int = 0
    ords: list[int] = list(data) + [17, 31, 73, 47, 23]
    current_list: list[int] = list(range(256))
    for _ in range(64):
        current_list, position, skip = knot_round(current_list, ords, position, skip)
    
    return bytes([xor_block(block) for block in batched(current_list, n=16)])

def bytes_popcount(data: bytes) -> int:
    return sum([x.bit_count() for x in data])

def to_binary_string(data: bytes) -> str:
    return "".join([f"{x:08b}" for x in data])

key: str = "hwlqcszp"
#key: str = "flqrgnkx"

total_popcount: int = 0
one_positions: set[tuple[int, int]] = set()
for x in range(128):
    subkey: bytes = bytes(key + "-" + str(x), encoding='ascii')
    hash: bytes = knot_hash(subkey)
    for i, char in enumerate(to_binary_string(hash)):
        if char == "1":
            one_positions.add((i, x))
            total_popcount += 1

print(total_popcount)

region_count: int = 0
positions_to_check: list[tuple[int, int]] = []
current_group: set[tuple[int, int]] = set()
while len(one_positions) > 0:
    region_count += 1
    first_position: tuple[int, int] = one_positions.pop()
    positions_to_check.append(first_position)
    current_group.add(first_position)

    curr_x: int
    curr_y: int
    for curr_x, curr_y in positions_to_check:
        for check_x, check_y in [ (curr_x+1, curr_y), (curr_x-1, curr_y), (curr_x, curr_y+1), (curr_x, curr_y-1)]:
            if (check_x, check_y) in one_positions and (check_x, check_y) not in positions_to_check:
                one_positions.remove((check_x, check_y))
                positions_to_check.append((check_x, check_y))
            
    positions_to_check = []
    current_group = set()
print(region_count)