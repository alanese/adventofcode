def parse_part1(edges):
    side_a = edges[0] * edges[1]
    side_b = edges[0] * edges[2]
    side_c = edges[1] * edges[2]
    min_side = min(side_a, side_b, side_c)
    return 2*side_a + 2*side_b + 2*side_c + min_side

def parse_part2(edges):
    perim_1 = 2*edges[0] + 2*edges[1]
    perim_2 = 2*edges[0] + 2*edges[2]
    perim_3 = 2*edges[1] + 2*edges[2]
    vol = edges[0] * edges[1] * edges[2]

    return min(perim_1, perim_2, perim_3) + vol

total_p1 = 0
total_p2 = 0
with open("input-02.txt") as f:
    for line in f:
        box = [int(x) for x in line.strip().split('x')]
        total_p1 += parse_part1(box)
        total_p2 += parse_part2(box)

print(total_p1)
print(total_p2)