from collections import defaultdict
from enum import Enum
from functools import total_ordering
import heapq

@total_ordering
class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __lt__(self: Direction, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def left_turn(self: Direction) -> Direction:
        match self:
            case Direction.NORTH:
                return Direction.WEST
            case Direction.EAST:
                return Direction.NORTH
            case Direction.SOUTH:
                return Direction.EAST
            case Direction.WEST:
                return Direction.SOUTH
    
    def right_turn(self: Direction) -> Direction:
        match self:
            case Direction.NORTH:
                return Direction.EAST
            case Direction.EAST:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.WEST
            case Direction.WEST:
                return Direction.NORTH
            
    def vector(self: Direction) -> tuple[int, int]:
        match self:
            case Direction.NORTH:
                return 0, -1
            case Direction.EAST:
                return 1, 0
            case Direction.SOUTH:
                return 0, 1
            case Direction.WEST:
                return -1, 0

#Find the length of the shortest path from start to end, via Dijkstra's algorithm
def shortest_path(start: tuple[int, int, Direction], end: tuple[int, int, Direction], edges: dict[tuple[int, int, Direction], list[tuple[int, tuple[int, int, Direction]]]]) -> int:
    visited: dict[tuple[int, int, Direction], int] = {}
    to_visit: list[tuple[int, tuple[int, int, Direction]]] = [(0, start)]
    while end not in visited and len(to_visit) > 0:
        next_wt, next = heapq.heappop(to_visit)
        if next not in visited:
            for edge_wt, neighbor in edges[next]:
                if neighbor not in visited:
                    heapq.heappush(to_visit, (next_wt+edge_wt, neighbor))
            visited[next] = next_wt
    return visited.get(end, -1)




with open("input-16.txt") as f:
    data: list[str] = [line.strip() for line in f]

neighbors: dict[tuple[int, int, Direction], list[tuple[int, tuple[int, int, Direction]]]] = defaultdict(list)
start_x: int = -1
start_y: int = -1
end_x: int = -1
end_y: int = -1

for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "#":
            continue
        else:
            if char == "S":
                start_x = x
                start_y = y
            elif char == "E":
                end_x = x
                end_y = y
            for direction in [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]:
                neighbors[(x,y,direction)].append((1000, (x,y,direction.left_turn())))
                neighbors[(x,y,direction)].append((1000, (x,y,direction.right_turn())))
                dx, dy = direction.vector()
                if 0 <= x+dx < len(row) and 0 <= y+dy < len(data) and data[y+dy][x+dx] != "#":
                    neighbors[(x,y,direction)].append((1, (x+dx, y+dy, direction)))

start: tuple[int, int, Direction] = start_x, start_y, Direction.EAST
end: tuple[int, int, Direction] = -1, -1, Direction.EAST
for direction in Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST:
    neighbors[(end_x, end_y, direction)].append((0, end))

#Part 1
shortest: int = shortest_path(start, end, neighbors)
print(shortest)

#Part 2
#Should I be using Bellman-Ford here? Yes. Obvious room for improvement
points_on_path: set[tuple[int, int]] = set()

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != "#":
            print(f"Checking {x},{y} of {len(line)-1},{len(data)-1}")
            for direction in [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]:
                short_to: int = shortest_path(start, (x,y,direction), neighbors)
                if short_to <= shortest and short_to + shortest_path((x,y,direction), end, neighbors) == shortest:
                    points_on_path.add((x,y))
                    break
print(len(points_on_path))

