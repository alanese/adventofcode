from itertools import chain

def has_empty(disk: list[tuple[int, int]]) -> bool:
    for _, val in disk:
        if val == -1:
            return True
    return False

with open("input-09.txt") as f:
    data: list[int] = [int(x) for x in f.read().strip()]

data_block: bool = True
disk: list[int] = []
disk_chunks: list[tuple[int, int]] = []
next_id: int = 0
for num in data:
    if data_block:
        disk += [next_id]*num
        disk_chunks.append((num, next_id))
        next_id += 1
    else:
        disk += [-1]*num
        disk_chunks.append((num, -1))
    data_block = not data_block

#Part 1
working_disk: list[int] = disk[:]
remaining_empty: int = working_disk.count(-1)
while -1 in working_disk:
    last: int = working_disk.pop()
    if last != -1:
        working_disk[working_disk.index(-1)] = last
    remaining_empty -= 1

checksum: int = sum(i*val for i,val in enumerate(working_disk))
print(checksum)

#Part 2
working_chunks: list[tuple[int, int]] = disk_chunks[:]
rest: list[tuple[int, int]] = []
while has_empty(working_chunks):
    length, val = working_chunks.pop()
    if val == -1:
        rest = [(length, val)] + rest
        continue
    else:
        moved: bool = False
        for i, (search_length, search_val) in enumerate(working_chunks):
            if search_val != -1 or search_length < length:
                continue
            elif search_length == length:
                working_chunks[i] = (length, val)
                rest = [(length, -1)] + rest
                moved = True
                break
            else:
                working_chunks[i] = (length, val)
                working_chunks.insert(i+1, (search_length-length, -1))
                rest = [(length, -1)] + rest
                moved = True
                break
        if not moved:
            rest = [(length, val)] + rest

working_chunks = working_chunks + rest
blocks = chain.from_iterable( [val]*length for length,val in working_chunks)
checksum = 0
for i, block in enumerate(blocks):
    if block != -1:
        checksum += i*block
print(checksum)