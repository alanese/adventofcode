with open("input-07.txt") as f:
    data: list[str] = [line.strip() for line in f]

def parse_bags(data: list[str]) -> dict[str, list[tuple[int, str]]]:
    bags: dict[str, list[tuple[int, str]]]  = {}
    for line in data:
        boundary_1: int = line.index(" bags")
        bag_color: str = line[:boundary_1]
        bags[bag_color] = []

        rest: str = line[boundary_1+14:-1]
        contained_bags: list[str] = rest.split(", ")
        if contained_bags[0] == "no other bags":
            continue
        for bag in contained_bags:
            split_bag: list[str] = bag.split(maxsplit=1)
            count: int = int(split_bag[0])
            color: str = split_bag[1].rsplit(maxsplit=1)[0]
            bags[bag_color].append((count, color))
    return bags
            
def contains(color: str, target: str, bags: dict[str, list[tuple[int, str]]]) -> bool:
    for _, subcolor in bags[color]:
        if subcolor == target or contains(subcolor, target, bags):
            return True
    return False

def count_contained(color: str, bags: dict[str, list[tuple[int, str]]]) -> int:
    count: int = 0
    for number, subcolor in bags[color]:
        count += number * (1 + count_contained(subcolor, bags))
    return count

#Part 1
bags = parse_bags(data)
count: int = 0
for color in bags:
    if contains(color, "shiny gold", bags):
        count += 1

print(count)

#Part 2
bags = parse_bags(data)
print(count_contained("shiny gold", bags))