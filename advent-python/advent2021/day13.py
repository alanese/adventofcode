def parse_points(points: list[str]) -> set[tuple[int, int]]:
    parsed: set[tuple[int, int]] = set()
    for point in points:
        x, _, y = point.partition(",")
        parsed.add((int(x), int(y)))
    return parsed

def fold_vert(dots: set[tuple[int, int]], axis: int) -> set[tuple[int, int]]:
    folded: set[tuple[int, int]] = set()
    for x,y in dots:
        if x <= axis:
            folded.add((x,y))
        else:
            folded.add((2*axis-x, y))
    return folded

def fold_horiz(dots: set[tuple[int, int]], axis: int) -> set[tuple[int, int]]:
    folded: set[tuple[int, int]] = set()
    for x,y in dots:
        if y <= axis:
            folded.add((x,y))
        else:
            folded.add((x, 2*axis-y))
    return folded

def fold(dots: set[tuple[int, int]], direction: str, axis: int) -> set[tuple[int, int]]:
    if direction == "y":
        return fold_horiz(dots, axis)
    elif direction == "x":
        return fold_vert(dots, axis)
    else:
        raise ValueError(f"Invalid direction {direction}")

with open("input-13.txt") as f:
    data: list[str] = [line.strip() for line in f]

delim: int = data.index("")
points: set[tuple[int, int]] = parse_points(data[:delim])

folds: list[tuple[str, int]] = []
for line in data[delim+1:]:
    dir, _, axis = line.split()[-1].partition("=")
    folds.append((dir, int(axis)))

#Part 1
points = fold(points, folds[0][0], folds[0][1])
print(len(points))

for dir, axis in folds[1:]:
    points = fold(points, dir, axis)

#Part 2
min_xfold: int = 10**10
min_yfold: int = 10**10
for dir, axis in folds:
    if dir == "x" and axis < min_xfold:
        min_xfold = axis
    if dir == "y" and axis < min_yfold:
        min_yfold = axis

for y in range(min_yfold+1):
    for x in range(min_xfold+1):
        if (x,y) in points:
            print("#", end="")
        else:
            print(" ", end="")
    print()