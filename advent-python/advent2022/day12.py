from collections import defaultdict
from typing import TypeVar
import heapq

T = TypeVar('T')

HEIGHTS: dict[str, int] = {x: ord(x)-ord('a')+1 for x in "abcdefghijklmnopqrstuvwxyz"}
HEIGHTS['S'] = HEIGHTS['a']
HEIGHTS['E'] = HEIGHTS['z']

#Find the shortest path from start to any element of end, using a variant of Dijkstra's algorithm
def shortest_to_any(start: T, end: set[T], edges: dict[T, list[T]]) -> int:
    visited: dict[T, int] = {}
    to_visit: list[tuple[int, T]] = [(0, start)]
    next: T = start
    while next not in end and len(to_visit) > 0:
        next_dist, next = heapq.heappop(to_visit)
        if next not in visited:
            visited[next] = next_dist
            for neighbor in edges[next]:
                if neighbor not in visited:
                    heapq.heappush(to_visit, (next_dist+1, neighbor))
    if next in end:
        return visited[next]
    else:
        return -1

with open("input-12.txt") as f:
    data: list[str] = [line.strip() for line in f]

edges: dict[tuple[int, int], list[tuple[int, int]]] = {}
down_edges: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
a_coords: set[tuple[int, int]] = set()
start_x: int = -1
start_y: int = -1
end_x: int = -1
end_y: int = -1
for y, row in enumerate(data):
    for x, char in enumerate(row):
        edges[(x,y)] = []
        if char == "S":
            start_x, start_y = x,y
            a_coords.add((x,y))
        elif char == "a":
            a_coords.add((x,y))
        elif char == "E":
            end_x, end_y = x,y
        for n_x,n_y in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if 0 <= n_x < len(row) and 0 <= n_y < len(data) and\
               HEIGHTS[char] + 1 >= HEIGHTS[data[n_y][n_x]]:
                edges[(x,y)].append((n_x,n_y))
                down_edges[(n_x, n_y)].append((x,y))

#Part 1
print(shortest_to_any((start_x, start_y), {(end_x, end_y)}, edges))

#Part 2
print(shortest_to_any((end_x, end_y), a_coords, down_edges))