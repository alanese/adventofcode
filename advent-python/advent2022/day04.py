def parse_assignment(assignment: str) -> tuple[tuple[int, int], tuple[int, int]]:
    fst, _, snd = assignment.partition(",")
    left, _, right = fst.partition("-")
    l1, r1 = int(left), int(right)
    left, _, right = snd.partition("-")
    l2, r2 = int(left), int(right)
    return (l1,r1), (l2,r2)

#Check whether one of the two ranges completely contains the other
def contained(range_1: tuple[int, int], range_2: tuple[int, int]) -> bool:
    return (range_1[0] <= range_2[0] and range_1[1] >= range_2[1]) or\
           (range_2[0] <= range_1[0] and range_2[1] >= range_1[1])

def overlap(range_1: tuple[int, int], range_2: tuple[int, int]) -> bool:
    return range_1[0] <= range_2[0] <= range_1[1] or range_2[0] <= range_1[0] <= range_2[1]

with open("input-04.txt") as f:
    data: list[tuple[tuple[int, int], tuple[int, int]]] = [parse_assignment(line.strip()) for line in f]

print(sum(contained(p1, p2) for p1,p2 in data))
print(sum(overlap(p1, p2) for p1,p2 in data))