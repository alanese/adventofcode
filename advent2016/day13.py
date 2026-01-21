import heapq
from collections import defaultdict

FAV_NUM: int = 1352
def is_open(x: int, y: int) -> bool:
    if x<0 or y<0:
        return False
    else:
        return (x*x + 3*x + 2*x*y + y + y*y + FAV_NUM).bit_count() % 2 == 0

def shortest_route(start: tuple[int, int], end: tuple[int, int]) -> int:
    visited: dict[tuple[int, int], int] = {}
    to_visit: list[tuple[int, tuple[int, int]]] = [(0, start)]
    while len(to_visit) > 0 and end not in visited:
        distance, (x,y) = heapq.heappop(to_visit)
        if (x,y) not in visited:
            visited[(x,y)] = distance
            for n_x, n_y in ( (x+1,y), (x-1,y), (x,y+1), (x,y-1) ):
                if is_open(n_x, n_y) and (n_x,n_y) not in visited:
                    heapq.heappush(to_visit, (distance+1, (n_x,n_y)))
    return visited[end]

#Part 1
print(shortest_route((1,1), (31,39)))

#Part 2
in_range: dict[int, set[tuple[int, int]]] = defaultdict(set)
in_range[0] = {(1,1)}

for i in range(50):
    for x,y in in_range[i]:
        for n_x, n_y in ( (x+1,y), (x-1,y), (x,y+1), (x,y-1) ):
            if is_open(n_x, n_y):
                in_range[i+1].add((n_x, n_y))

all_range: set[tuple[int, int]] = set()
for points in in_range.values():
    all_range |= points
print(len(all_range))