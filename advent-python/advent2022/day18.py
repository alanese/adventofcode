from typing import TypeVar

T = TypeVar("T")

def get_neighbors(x: int, y: int, z: int) -> list[tuple[int, int, int]]:
    return [(x+1,y,z), (x-1,y,z),
            (x,y+1,z), (x,y-1,z),
            (x,y,z+1), (x,y,z-1)]

#Compute surface area and find all non-included cubes on the boundary
def get_surface_area(data: set[tuple[int, int, int]]) -> tuple[int, set[tuple[int, int, int]]]:
    surface_area: int = 0
    cubes: set[tuple[int, int, int]] = set()
    boundary: set[tuple[int, int, int]] = set()
    for cube in data:
        cubes.add(cube)
        boundary.discard(cube)
        surface_area += 6
        for neighbor in get_neighbors(*cube):
            if neighbor in cubes:
                surface_area -= 2
            else:
                boundary.add(neighbor)

    return surface_area, boundary

def in_any(elt: T, sets: list[set[T]]) -> bool:
    for set_ in sets:
        if elt in set_:
            return True
    return False

with open("input-18.txt") as f:
    data: list[str] = [line.strip() for line in f]

cubes: set[tuple[int, int, int]] = set()
for line in data:
    x, y, z = (int(x) for x in line.split(","))
    cubes.add((x,y,z))

#Part 1, a bit of setup for part 2
surface_area, boundary = get_surface_area(cubes)
print(surface_area)

#Part 2
#Identify bounding box
random_cube = cubes.pop()
cubes.add(random_cube)
min_x, min_y, min_z = random_cube
max_x, max_y, max_z = random_cube
for x,y,z in cubes:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
    min_z = min(min_z, z)
    max_z = max(max_z, z)

#identify all empty spaces by flood-filling from each boundary cube
#that isn't already in an empty space
empty_spaces: list[set[tuple[int, int, int]]] = []
for point in boundary:
    if not in_any(point, empty_spaces):
        space: set[tuple[int, int, int]] = set()
        to_check: set[tuple[int, int, int]] = {point}
        while len(to_check) > 0:
            next = to_check.pop()
            space.add(next)
            for n_x, n_y, n_z in get_neighbors(*next):
                if min_x-1 <= n_x <= max_x+1 and min_y-1 <= n_y <= max_y+1 and\
                   min_z-1 <= n_z <= max_z+1 and (n_x,n_y,n_z) not in space and\
                   (n_x, n_y, n_z) not in to_check and (n_x,n_y,n_z) not in cubes:
                    to_check.add((n_x, n_y, n_z))
        empty_spaces.append(space)

#Discard the exterior space
for space in empty_spaces:
    if (min_x-1, min_y-1, min_z-1) in space:
        empty_spaces.remove(space)

#Compute the total surface area of remaining empty spaces
inner_surface_area: int = 0
for void in empty_spaces:
    surface, _ = get_surface_area(void)
    inner_surface_area += surface

#Subtract from total surface area
print(surface_area - inner_surface_area)