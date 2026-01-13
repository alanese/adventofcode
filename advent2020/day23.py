import datetime as dt

class Cup:
    def __init__(self: Cup, value: int):
        self.value = value
        self.next = self

    def add_after(self: Cup, value: int) -> Cup:
        tmp: Cup = Cup(value)
        tmp.next = self.next
        self.next = tmp
        return tmp
    
    def pop_after(self: Cup) -> int:
        tmp: int = self.next.value
        self.next = self.next.next
        return tmp
    
def create_circle(start: list[int]) -> tuple[Cup, dict[int, Cup]]:
    index: dict[int, Cup] = {}
    first: Cup = Cup(start[0])
    index[1] = first
    for i in start[1:][::-1]:
        first.add_after(i)
        index[i] = first.next
    return first, index

def process_moves(start: Cup, moves: int, low: int, high: int, index: dict[int, Cup], announce_interval: int = 0) -> Cup:
    start_time = dt.datetime.now()
    for i in range(moves):
        if announce_interval > 0 and i%announce_interval == 0:
            cur_time = dt.datetime.now()
            print(f"{i} rounds of {moves} complete; elapsed time {cur_time - start_time}")
        next_1: int = start.pop_after()
        next_2: int = start.pop_after()
        next_3: int = start.pop_after()
        dest: int = start.value - 1
        if dest < low:
            dest = high
        while dest in (next_1, next_2, next_3):
            dest -= 1
            if dest < low:
                dest = high
        dest_ptr: Cup = index[dest]
        dest_ptr.add_after(next_3)
        index[next_3] = dest_ptr.next
        dest_ptr.add_after(next_2)
        index[next_2] = dest_ptr.next
        dest_ptr.add_after(next_1)
        index[next_1] = dest_ptr.next
        start = start.next
    return start


INITIAL_ORDER: str = "167248359"

#Part 1
order: list[int] = [int(x) for x in INITIAL_ORDER]
low, high = min(order), max(order)

current: Cup
index: dict[int, Cup]
current, index = create_circle(order)

current = process_moves(current, 100, low, high, index)


while current.value != 1:
    current = current.next

print(current.value, end="")
current = current.next
while current.value != 1:
    print(current.value, end="")
    current = current.next
print()

#Part 2
current, index = create_circle(order + list(range(high+1, 1000001)))
high = 1000000
ptr: Cup = current

current = process_moves(current, 10000000, low, high, index, 1000)
current = index[1]

print(current.next.value * current.next.next.value)