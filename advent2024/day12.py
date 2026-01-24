from collections import Counter, defaultdict

def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

#Check which, if any, regions have vertices at the point in the center of the 
#2x2 block of squares with top-left at (x,y)
def check_vertices(x: int, y: int, region_ids: dict[tuple[int, int], int]) -> list[int]:
    ne: int = region_ids.get((x,y), -1)
    nw: int = region_ids.get((x+1,y), -1)
    se: int = region_ids.get((x,y+1), -1)
    sw: int = region_ids.get((x+1,y+1), -1)   

    edge_n: bool = ne != nw
    edge_e: bool = ne != se
    edge_w: bool = nw != sw
    edge_s: bool = se != sw

    #Check whether each square's region has an "inner" or "outer" vertex at center
    vertices: list[int] = []
    if (edge_n and edge_e) or (edge_s and edge_w and not edge_n and not edge_e):
        vertices.append(ne)
    if (edge_n and edge_w) or (edge_s and edge_e and not edge_n and not edge_w):
        vertices.append(nw)
    if (edge_s and edge_e) or (edge_n and edge_w and not edge_s and not edge_e):
        vertices.append(se)
    if (edge_s and edge_w) or (edge_n and edge_e and not edge_s and not edge_w):
        vertices.append(sw)

    return vertices


with open("input-12.txt") as f:
    data: list[list[str]] = [list(line.strip()) for line in f]

region_ids: dict[tuple[int, int], int] = {}
next_id: int = 1
for y, line in enumerate(data):
    for x, plant in enumerate(line):
        if (x,y) not in region_ids:
            to_fill: set[tuple[int, int]] = {(x,y)}
            while len(to_fill) > 0:
                x_2, y_2 = to_fill.pop()
                region_ids[(x_2, y_2)] = next_id
                for n_x, n_y in get_neighbors(x_2, y_2):
                    if 0 <= n_x < len(line) and 0 <= n_y < len(data) and\
                       data[n_y][n_x] == plant and (n_x, n_y) not in region_ids:
                        to_fill.add((n_x, n_y))
            next_id += 1

region_areas: dict[int, int] = defaultdict(int)
region_perims: dict[int, int] = defaultdict(int)
vertex_count: dict[int, int] = Counter()
for x in range(-1, len(data[0])):
    for y in range(-1, len(data)):
        region = region_ids.get((x,y), -1)
        region_areas[region] += 1
        for v_region in check_vertices(x, y, region_ids):
            vertex_count[v_region] += 1
        for n_x, n_y in get_neighbors(x,y):
            if region_ids.get((n_x, n_y), -1) != region:
                region_perims[region] += 1


print(sum(region_areas[id] * region_perims[id] for id in region_areas if id != -1))

print(sum(region_areas[id] * vertex_count[id] for id in region_areas if id != -1))
