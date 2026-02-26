import heapq
from collections import defaultdict

#Length of the shortest path from start to end, using Dijkstra's algorithm
def shortest_path(start: tuple[int, int], end: tuple[int, int], edges: dict[tuple[int, int], list[tuple[int, tuple[int, int]]]]) -> int:
    visited: dict[tuple[int, int], int] = {start: 0}
    to_visit: list[tuple[int, tuple[int, int]]] = edges[start][:]
    heapq.heapify(to_visit)
    while end not in visited:
        if len(to_visit) == 0:
            raise ValueError("Start and end not connected")
        distance, vertex = heapq.heappop(to_visit)
        if vertex not in visited:
            visited[vertex] = distance
            for weight, neighbor in edges[vertex]:
                if neighbor not in visited:
                    heapq.heappush(to_visit, (distance+weight, neighbor))
    return visited[end]

def grid_to_edges(grid: list[list[int]]) -> dict[tuple[int, int], list[tuple[int, tuple[int, int]]]]:
    edge_weights: dict[tuple[int, int], list[tuple[int, tuple[int, int]]]] = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if x < len(grid[y])-1:
                edge_weights[(x,y)].append((grid[y][x+1], (x+1,y)))
                edge_weights[(x+1,y)].append((grid[y][x], (x,y)))
            if y < len(grid)-1:
                edge_weights[(x,y)].append((grid[y+1][x], (x,y+1)))
                edge_weights[(x,y+1)].append((grid[y][x], (x,y)))
    return edge_weights


def increment_weight(weight: int, increment: int):
    return (((weight - 1) + increment) % 9) + 1

with open("input-15.txt") as f:
    data: list[list[int]] = [ [int(x) for x in line.strip()] for line in f]

#Part 1
edge_weights: dict[tuple[int, int], list[tuple[int, tuple[int, int]]]] = grid_to_edges(data)
print(shortest_path((0,0), (len(data[0])-1,len(data)-1), edge_weights))

#Part 2
big_grid: list[list[int]] = [row[:] for row in data]
tile_x = len(big_grid[0])
tile_y = len(big_grid)

##tile larger grid
for inc in range(1, 5):
    for row in range(tile_y):
        big_grid[row] += [increment_weight(weight, inc) for weight in big_grid[row][:tile_x]]

for inc in range(1, 5):
    for row in big_grid[:tile_y]:
        big_grid.append([increment_weight(weight, inc) for weight in row])

big_edge_weights: dict[tuple[int, int], list[tuple[int, tuple[int, int]]]] = grid_to_edges(big_grid)
print(shortest_path((0,0), (len(big_grid[0])-1, len(big_grid)-1), big_edge_weights))