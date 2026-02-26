#axial coordinates, per https://www.redblobgames.com/grids/hexagons/
class Hex:
    q: int
    r: int
    s: int

    def __init__(self: Hex, q: int, r: int, s: int):
        self.q = q
        self.r = r
        self.s = s

    def distance_to(self: Hex, other: Hex) -> int:
        return (abs(self.q - other.q) + abs(self.r - other.r) + abs(self.s - other.s))//2


position: Hex = Hex(0, 0, 0)
ZERO: Hex = Hex(0, 0, 0)
furthest_distance: int = 0
with open("input-11.txt") as f:
    for direction in f.read().strip().split(","):
    #for direction in "se,sw,se,sw,sw".split(","):
        match direction:
            case "n":
                position.r -= 1
                position.s += 1
            case "ne":
                position.q += 1
                position.r -= 1
            case "nw":
                position.q -= 1
                position.s += 1
            case "s":
                position.r += 1
                position.s -= 1
            case "se":
                position.q += 1
                position.s -= 1
            case "sw":
                position.q -= 1
                position.r += 1
        if position.distance_to(ZERO) > furthest_distance:
            furthest_distance = position.distance_to(ZERO)

print(position.distance_to(Hex(0, 0, 0)))
print(furthest_distance)