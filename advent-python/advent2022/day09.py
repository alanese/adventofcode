from typing import NamedTuple

def sign(n: int) -> int:
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1
    
class Vector2D(NamedTuple):
    x: int
    y: int

    def distance_to(self: Vector2D, other: Vector2D) -> int:
        return max(abs(other.x-self.x), abs(other.y-self.y))
    
    def step_towards(self: Vector2D, other: Vector2D) -> Vector2D:
        return Vector2D(self.x+sign(other.x-self.x), self.y+sign(other.y-self.y))
    
    def __add__(self: Vector2D, other: object) -> Vector2D:
        if isinstance(other, Vector2D):
            return Vector2D(self.x+other.x, self.y+other.y)
        return NotImplemented
    

DIRECTIONS: dict[str, Vector2D] = {"U": Vector2D(0, 1),
                                   "R": Vector2D(1, 0),
                                   "D": Vector2D(0,-1),
                                   "L": Vector2D(-1,0)}
with open("input-09.txt") as f:
    data: list[str] = [line.strip() for line in f]

step_sequence: list[str] = []

for line in data:
    dir, steps = line.split(maxsplit=1)
    step_sequence += [dir] * int(steps)

#Part 1
head: Vector2D = Vector2D(0,0)
tail: Vector2D = Vector2D(0,0)
tail_spaces: set[Vector2D] = {tail}
for step in step_sequence:
    head = head + DIRECTIONS[step]
    if tail.distance_to(head) > 1:
        tail = tail.step_towards(head)
        tail_spaces.add(tail)

print(len(tail_spaces))

#Part 1
rope: list[Vector2D] = [Vector2D(0,0) for _ in range(10)]
tail_spaces = {rope[-1]}
for step in step_sequence:
    rope[0] = rope[0] + DIRECTIONS[step]
    for i in range(len(rope)-1):
        if rope[i+1].distance_to(rope[i]) > 1:
            rope[i+1] = rope[i+1].step_towards(rope[i])
        else:
            break
    tail_spaces.add(rope[-1])

print(len(tail_spaces))