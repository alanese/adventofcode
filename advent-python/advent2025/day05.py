with open("input-05.txt") as f:
    lines = [line.strip() for line in f.readlines()]

sep = lines.index("")
range_str = lines[:sep]
ingredients = [int(x) for x in lines[sep+1:]]

ranges = []
for x in range_str:
    bounds_str = x.split("-")
    ranges.append((int(bounds_str[0]), int(bounds_str[1])))

fresh_count = 0

for ing in ingredients:
    for low, high in ranges:
        if low <= ing <= high:
            fresh_count += 1
            break

print(fresh_count)

def merge_ranges(r1, r2):
    if r1[0] > r2[1] or r2[0] > r1[1]:
        return None
    return min(r1[0], r2[0]), max(r1[1], r2[1])

def ranges_intersect(r1, r2):
    return r1[0] <= r2[1] and r2[0] <= r1[1]

new_ranges = ranges
old_ranges = []

while len(new_ranges) != len(old_ranges):
    old_ranges = new_ranges
    new_ranges = []
    for r1 in old_ranges:
        merged = False
        for i, r2 in enumerate(new_ranges):
            if ranges_intersect(r1, r2):
                new_ranges[i] = merge_ranges(r1, r2)
                merged = True
                break
        if not merged:
            new_ranges.append(r1)

print(sum([high - low + 1 for low,high in new_ranges]))

