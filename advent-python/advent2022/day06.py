def id_marker(stream: str, length: int) -> int:
    for i in range(length-1, len(stream)):
        possible_marker: str = stream[i-(length-1):i+1]
        if len(set(possible_marker)) == len(possible_marker):
            return i+1
    return -1

with open("input-06.txt") as f:
    stream: str = f.read().strip()

print(id_marker(stream, 4))

print(id_marker(stream, 14))