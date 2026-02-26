def area(t1, t2):
    w = abs(t1[0] - t2[0]) + 1
    h = abs(t1[1] - t2[1]) + 1
    return w*h


with open("input-09.txt") as f:
    tiles = [ tuple([int(x) for x in pair.strip().split(",")]) for pair in f.readlines()]

max_size = -1
for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        size = area(tiles[i], tiles[j])
        if size > max_size:
            max_size = size

print(max_size)

#--------------

def edges(corner1, corner2):
    left_coord = min(corner1[0], corner2[0])
    right_coord = max(corner1[0], corner2[0])
    top_coord = min(corner1[1], corner2[1])
    bottom_coord = max(corner1[1], corner2[1])

    top = ( (left_coord, top_coord), (right_coord, top_coord) )
    bottom = ( (left_coord, bottom_coord), (right_coord, bottom_coord) )
    left = ( (left_coord, top_coord), (left_coord, bottom_coord) )
    right = ( (right_coord, top_coord), (right_coord, bottom_coord) )
    return  (top, bottom, left, right)

def get_points_on_edge(v1, v2):
    point_set = set()
    if v1[0] == v2[0]:
        min_y = min(v1[1], v2[1])
        max_y = max(v1[1], v2[1])
        for y in range(min_y, max_y+1):
            point_set.add((v1[0], y))

    elif v1[1] == v2[1]:
        min_x = min(v1[0], v2[0])
        max_x = max(v1[0], v2[0])
        for x in range(min_x, max_x+1):
            point_set.add((x, v1[1]))

    else:
        print(f"Nonorthogonal line: {v1}-{v2}")

    return point_set

def get_perimeter_points(corner1, corner2):
    point_set = set()
    for edge in edges(corner1, corner2):
        point_set.update(get_points_on_edge(*edge))
    return point_set


def get_adjacent_points(point):
    adj = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx != 0 or dy != 0:
                adj.append( (point[0] + dx, point[1] + dy))
    return adj

def adjacent_to_edge(point, boundary):
    for adj_point in get_adjacent_points(point):
        if adj_point in boundary:
            return True
    return False

def fill_outer_edge(boundary, test_point):
    edge_queue = [test_point]
    edge = set()

    while len(edge_queue) > 0:
        next_point = edge_queue.pop(0)
        edge.add(next_point)
        for pt in get_adjacent_points(next_point):
            if pt not in boundary and pt not in edge and pt not in edge_queue and adjacent_to_edge(pt, boundary):
                edge_queue.append(pt)
    return edge

def cast_to_bad(point, bad_points, max_x, max_y):
    right = max_x
    for x in range(point[0]+1, max_x + 1):
        if (x, point[1]) in bad_points:
            right = x-1
            break

    up = 0
    for y in range(point[1]-1, -1, -1):
        if (point[0], y) in bad_points:
            up = y+1
            break
    
    down = max_y
    for y in range(point[1] + 1, max_y + 1):
        if (point[0], y) in bad_points:
            down = y-1

    return right, up, down



pairs = [ (tiles[i], tiles[i+1]) for i in range(len(tiles)-1)]
pairs.append((tiles[-1], tiles[0]))

tiles.sort(key=lambda x: x[0])

edge_points = set()
max_x_pair = None
max_x = -1
max_y = -1
for v1, v2 in pairs:
    edge_points.update(get_points_on_edge(v1, v2))
    if v1[0] == v2[0] and v1[0] > max_x:
        max_x = v1[0]
        max_x_pair = v1, v2
    if v1[1] > max_y:
        max_y = v1[1]
test_y_coord = min(max_x_pair[0][1], max_x_pair[1][1]) + 1
test_point = max_x+1, test_y_coord

outer_border = fill_outer_edge(edge_points, test_point)

max_area = -1
for i in range(len(tiles)):
    right_bd, up_bd, down_bd = cast_to_bad(tiles[i], outer_border, max_x, max_y)
    for j in range(i+1, len(tiles)):
        if tiles[j][0] > right_bd or tiles[j][1] < up_bd or tiles[j][1] > down_bd:
            continue
        if area(tiles[i], tiles[j]) > max_area:
            ok = True
            #check for bad tiles
            for perim_pt in get_perimeter_points(tiles[i], tiles[j]):
                if perim_pt in outer_border:
                    ok = False
                    break
            if ok:
                max_area = area(tiles[i], tiles[j])

print(max_area)