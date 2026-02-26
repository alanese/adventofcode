def decode_seat(seat: str) -> tuple[int, int]:
    row: int = 0
    col: int = 0
    for i in range(7):
        if seat[6-i] == "B":
            row += 1<<i
    for i in range(3):
        if seat[9-i] == "R":
            col += 1<<i
    return row, col

with open("input-05.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
max_id: int = -1
row: int = -1
col: int = -1
for line in data:
    row, col = decode_seat(line)
    id: int = 8*row + col
    max_id = max(max_id, id)
print(max_id)

#Part 2
max_id = -1
min_id: int = 127*8+7 + 1
seen_ids: set[int] = set()
for line in data:
    row, col = decode_seat(line)
    id = 8*row + col
    seen_ids.add(id)
    max_id = max(max_id, id)
    min_id = min(min_id, id)

for id in range(min_id+1, max_id):
    if id-1 in seen_ids and id+1 in seen_ids and id not in seen_ids:
        print(id)