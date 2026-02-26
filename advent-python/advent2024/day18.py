from collections import defaultdict
import heapq
from typing import TypeVar

T = TypeVar("T")

def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

#Find the length of the shortest path from start to end with the given edges, or -1 if no path exists
#How many times will I be using Dijkstra's algorithm for this year? Apparently a lot!
def shortest_path(start: T, end: T, edges: dict[T, list[T]]) -> int:
    visited: dict[T, int] = {}
    to_visit: list[tuple[int, T]] = [(0, start)]
    while end not in visited and len(to_visit) > 0:
        next_distance, next = heapq.heappop(to_visit)
        if next not in visited:
            visited[next] = next_distance
            for neighbor in edges[next]:
                if neighbor not in visited:
                    heapq.heappush(to_visit, (next_distance+1, neighbor))
    return visited.get(end, -1)

MAX_X: int = 70
MAX_Y: int = 70
BLOCK_COUNT: int = 1024
data: list[tuple[int, int]] = []
with open("input-18.txt") as f:
    for line in f:
        x, y = line.strip().split(",")
        data.append((int(x), int(y)))


blocks: set[tuple[int, int]] = set(data[:BLOCK_COUNT])
nodes: set[tuple[int, int]] = set()
for x in range(MAX_X+1):
    for y in range(MAX_Y+1):
        if (x,y) not in blocks:
            nodes.add((x,y))

edges: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
for node in nodes:
    for neighbor in get_neighbors(*node):
        if neighbor in nodes:
            edges[node].append(neighbor)

#Part 1
print(shortest_path((0,0), (MAX_X,MAX_Y), edges))
#Part 2
for node in data[BLOCK_COUNT:]:
    if node in edges:
        del edges[node]
        for neighbors in edges.values():
            if node in neighbors:
                neighbors.remove(node)
    if shortest_path((0, 0), (MAX_X, MAX_Y), edges) == -1:
        print(node)
        break
