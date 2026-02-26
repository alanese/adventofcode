buffer: list[int] = [0]

STEP_COUNT: int = 359

curr_ptr: int = 0
for x in range(2017):
    curr_ptr = (curr_ptr + STEP_COUNT) % len(buffer)
    buffer.insert(curr_ptr + 1, x+1)
    curr_ptr += 1

print(buffer[curr_ptr+1])

#-----------

curr_zeroindex: int = 0
curr_ptr = 0
for curr_length in range(1, 50000001):
    curr_ptr = (curr_ptr + STEP_COUNT) % curr_length
    if curr_ptr == 0:
        curr_zeroindex = curr_length
    curr_ptr += 1

print(curr_zeroindex)