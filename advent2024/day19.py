def design_ways(design: str, towels: list[str], cache: dict[str, int]) -> int:
    if design == "":
        return 1
    if design not in cache:
        ways: int = 0
        for towel in towels:
            if design.startswith(towel):
                ways += design_ways(design[len(towel):], towels, cache)
        cache[design] = ways
    return cache[design]

with open("input-19.txt") as f:
    data: list[str] = [line.strip() for line in f]

towels: list[str] = data[0].split(", ")
designs: list[str] = data[2:]

possible_count: int = 0
total_ways: int = 0
cache: dict[str, int] = {}
for design in designs:
    ways: int = design_ways(design, towels, cache)
    if ways > 0:
        possible_count += 1
    total_ways += ways
print(possible_count)
print(total_ways)