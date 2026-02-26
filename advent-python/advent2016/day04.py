from collections import Counter
from typing import Tuple

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"

def sort_key(pair: Tuple[str, int]) -> Tuple[int, int]:
    return pair[1], -ord(pair[0])

def check_real_room(room: str) -> bool:
    checksum: str = room[-6:-1]
    name:str = room[:room.rindex('-')]
    name_letters = [x for x in name if x in LOWERCASE]
    counter = Counter(name_letters)
    sorted_counter = sorted(counter.items(), key=sort_key, reverse=True)
    computed_checksum = "".join([pair[0] for pair in sorted_counter[:5]])
    return computed_checksum == checksum

def shift_char(char: str, shift_dist: int) -> str:
    return chr((ord(char) - ord('a') + shift_dist) % 26 + ord('a')) if char != '-' else '-'

def shift(string: str, shift_dist: int) -> str:
    return "".join([shift_char(char, shift_dist) for char in string])

real_counter:int = 0
with open("input-04.txt") as f:
    for line in f:
        line = line.strip()
        if check_real_room(line):
            room_id = int(line[-10:-7])
            real_room_name = shift(line[:-11], room_id)
            if 'north' in real_room_name:
                print(f"{room_id}: {real_room_name}")
            real_counter += room_id
print(real_counter)