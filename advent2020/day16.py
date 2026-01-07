from math import prod

def parse_range(line: str) -> tuple[int, int]:
    ends: list[str] = line.split("-")
    return int(ends[0]), int(ends[1])

def parse_field(field: str) -> tuple[str, list[tuple[int, int]]]:
    colon: int = field.index(":")
    field_name: str = field[:colon]
    ranges: list[str] = field[colon+2:].split(" or ")
    return field_name, [parse_range(r) for r in ranges]

def validate_range(value: int, ranges: list[tuple[int, int]]) -> bool:
    for low, high in ranges:
        if low <= value <= high:
            return True
    return False

def ticket_validity(ticket: list[int], fields: list[tuple[str, list[tuple[int, int]]]]) -> tuple[bool, int]:
    invalid: int = 0
    for num in ticket:
        ok: bool = False
        for _, ranges in fields:
            if validate_range(num, ranges):
                ok = True
                break
        if not ok:
            return False, num
    return True, 0

#Read and parse data
with open("input-16.txt") as f:
    data: list[str] = [line.strip() for line in f]

cutoff: int = data.index("")
fields: list[tuple[str, list[tuple[int, int]]]] = [parse_field(field) for field in data[:cutoff]]
my_ticket: list[int] = [int(x) for x in data[cutoff+2].split(",")]
cutoff2: int = data.index("nearby tickets:")
tickets: list[list[int]] = [ [int(x) for x in line.split(",")] for line in data[cutoff2+1:]]

#Part 1
invalid_rate: int = 0
for ticket in tickets:
    invalid_rate += ticket_validity(ticket, fields)[1]
print(invalid_rate)

#Part 2
field_names: list[str] = [field[0] for field in fields]
field_possibilities: list[set[str]] = [{field[0] for field in fields} for i in range(len(fields))]

valid_tickets = [ticket for ticket in tickets if ticket_validity(ticket, fields)[0]]
for ticket in valid_tickets:
    for i, num in enumerate(ticket):
        for name, ranges in fields:
            if not validate_range(num, ranges):
                field_possibilities[i].discard(name)

for _ in range(len(field_possibilities)):
    for i, poss in enumerate(field_possibilities):
        if len(poss) == 1:
            elt: str = list(poss)[0]
            for j in range(len(field_possibilities)):
                if i != j:
                    field_possibilities[j].discard(elt)

departure_fields: list[int] = [i for i in range(len(field_possibilities)) if list(field_possibilities[i])[0].startswith("departure")]
print(departure_fields)
print(prod([my_ticket[i] for i in departure_fields]))