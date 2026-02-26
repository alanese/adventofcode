from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Particle:
    pos_x: int
    pos_y: int
    pos_z: int
    v_x: int
    v_y: int
    v_z: int
    a_x: int
    a_y: int
    a_z: int

    def tick(self: Particle):
        self.v_x += self.a_x
        self.v_y += self.a_y
        self.v_z += self.a_z
        self.pos_x += self.v_x
        self.pos_y += self.v_y
        self.pos_z += self.v_z

    def position_after(self: Particle, time: int) -> tuple[int, int, int]:
        x_pos = self.pos_x + time * self.v_x + time * (time+1) * self.a_x // 2
        y_pos = self.pos_y + time * self.v_y + time * (time+1) * self.a_y // 2
        z_pos = self.pos_z + time * self.v_z + time * (time+1) * self.a_z // 2
        return x_pos, y_pos, z_pos
    
    def distance_after(self: Particle, time: int) -> int:
        x_pos, y_pos, z_pos = self.position_after(time)
        return abs(x_pos) + abs(y_pos) + abs(z_pos)
    
    def intersections(self: Particle, other: Particle) -> list[int]:
        a: float = (self.a_x - other.a_x) / 2
        b: float = self.v_x - other.v_x + (self.a_x - other.a_x)/2
        c: float = self.pos_x - other.pos_x
        #print(a, b, c)

        if a == 0:
            if b == 0:
                return []
            if (-c/b).is_integer() and self.position_after(int(-c/b)) == other.position_after(int(-c/b)):
                return [int(-c/b)]
            else:
                return []

        discriminant: float = b*b - 4*a*c
        if discriminant < 0:
            return []
        
        possible_1: float = (-b + discriminant**(1/2))/(2*a)
        possible_2: float = (-b - discriminant**(1/2))/(2*a)
        solutions = []
        if possible_1.is_integer() and self.position_after(int(possible_1)) == other.position_after(int(possible_1)):
            solutions.append(int(possible_1))
        if possible_2.is_integer() and self.position_after(int(possible_2)) == other.position_after(int(possible_2)):
            solutions.append(int(possible_2))

        return solutions
        
def parse_particle(line: str) -> Particle:
    line_split: list[str] = line.split(", ")
    pos_components: list[str] = line_split[0][3:-1].split(",")
    vel_components: list[str] = line_split[1][3:-1].split(",")
    accel_components: list[str] = line_split[2][3:-1].split(",")
    return Particle(int(pos_components[0]), int(pos_components[1]), int(pos_components[2]),
                    int(vel_components[0]), int(vel_components[1]), int(vel_components[2]),
                    int(accel_components[0]), int(accel_components[1]), int(accel_components[2]))

with open("input-20.txt") as f:
    data: list[str] = [line.strip() for line in f]

particles: list[Particle] = [parse_particle(line) for line in data]
max_accel_component: int = 0
max_velo_component: int = 0
max_pos_component: int = 0
for p in particles:
    if p.a_x > max_accel_component:
        max_accel_component = p.a_x
    if p.a_y > max_accel_component:
        max_accel_component = p.a_y
    if p.a_z > max_accel_component:
        max_accel_component = p.a_z
    if p.v_x > max_velo_component:
        max_velo_component = p.v_x
    if p.v_y > max_velo_component:
        max_velo_component = p.v_y
    if p.v_z > max_velo_component:
        max_velo_component = p.v_z
    if p.pos_x > max_pos_component:
        max_pos_component = p.pos_x
    if p.pos_y > max_pos_component:
        max_pos_component = p.pos_y
    if p.pos_z > max_pos_component:
        max_pos_component = p.pos_z
steps: int = 1000*max(max_pos_component, max_velo_component, max_accel_component)

min_dist_after = particles[0].distance_after(steps)
min_dist_after_ids: list[int] = [0]

for i, particle in enumerate(particles[1:], start=1):
    if particle.distance_after(steps) < min_dist_after:
        min_dist_after = particle.distance_after(steps)
        min_dist_after_ids = [i]
    elif particle.distance_after(steps) == min_dist_after:
        min_dist_after_ids.append(i)

print(min_dist_after)
print(min_dist_after_ids)

intersections: dict[int, list[tuple[int, int]]] = defaultdict(list)
max_intersection_time: int = 0
for i, particle1 in enumerate(particles):
    for j, particle2 in enumerate(particles[i+1:], start=i+1):
        for t in particle1.intersections(particle2):
            intersections[t].append((i,j))
            if t > max_intersection_time:
                max_intersection_time = t



remaining: set[int] = set(range(len(particles)))

for t in range(max_intersection_time + 1):
    to_remove: set[int] = set()
    for (p1, p2) in intersections[t]:
        if p1 in remaining and p2 in remaining:
            to_remove.add(p1)
            to_remove.add(p2)
    remaining -= to_remove

print(len(remaining))