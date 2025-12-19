from collections import defaultdict

def parse_line(line: str) -> tuple[int, int, int, int, int]:
    line_split: list[str] = line.split()
    id: int = int(line_split[0][1:])
    coords: list[str] = line_split[2][:-1].split(",")
    x: int = int(coords[0])
    y: int = int(coords[1])
    dims: list[str] = line_split[3].split("x")
    width: int = int(dims[0])
    height: int = int(dims[1])
    return id, x, y, width, height

def rects_intersect(pos_1: tuple[int, int], size_1: tuple[int, int], pos_2: tuple[int, int], size_2: tuple[int, int]) -> bool:
    if pos_1[0] <= pos_2[0] < pos_1[0] + size_1[0] or pos_2[0] <= pos_1[0] < pos_2[0] + size_2[0]:
        if pos_1[1] <= pos_2[1] < pos_1[1] + size_1[1] or pos_2[1] <= pos_1[1] < pos_2[1] + size_2[1]:
            return True
    return False

with open("input-03.txt") as f:
    data = [line.strip() for line in f]

#Part 1
squares: dict[tuple[int, int], int] = defaultdict(int)
double_claims: int = 0
for line in data:
    _, x, y, width, height = parse_line(line)
    for x_pos in range(x, x+width):
        for y_pos in range(y, y+height):
            squares[(x_pos,y_pos)] += 1
            if squares[(x_pos,y_pos)] == 2:
                double_claims += 1
print(double_claims)

#Part 2
claims: list[tuple[int, int, int, int, int]] = []
valid_ids: set = set()
for line in data:
    parsed_line: tuple[int, int, int, int, int] = parse_line(line)
    claims.append(parsed_line)
    valid_ids.add(parsed_line[0])

for i, claim_1 in enumerate(claims):
    for claim_2 in claims[i+1:]:
        if rects_intersect( (claim_1[1], claim_1[2]), (claim_1[3], claim_1[4]), (claim_2[1], claim_2[2]), (claim_2[3], claim_2[4]) ):
            if claim_1[0] in valid_ids:
                valid_ids.remove(claim_1[0])
            if claim_2[0] in valid_ids:
                valid_ids.remove(claim_2[0])

print(valid_ids)
