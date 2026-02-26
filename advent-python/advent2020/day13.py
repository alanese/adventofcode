#Functions brought over from 2016 day 15
def bezout(x: int, y: int) -> tuple[int, int]:
    """
    Docstring for bezout
    
    :param x: A positive integer
    :type x: int
    :param y: A positive integer
    :type y: int
    :return: The Bezout coefficients - i.e. s, t such that sx + ty = gcd(x, y)
    :rtype: tuple[int, int]
    """
    if y > x:
        s, t = bezout(y, x)
        return t, s
    
    r_prev: int = x
    r: int = y
    s_prev: int = 1
    s: int = 0
    t_prev: int = 0
    t: int = 1
    while r != 0:
        q: int = r_prev // r
        r_prev, r = r, r_prev - q*r
        s_prev, s = s, s_prev - q*s
        t_prev, t = t, t_prev - q*t
    return s_prev, t_prev

def chinese_remainder(congruences: list[tuple[int, int]]) -> int:
    if len(congruences) == 1:
        return congruences[0][0]
    
    a1: int
    a2: int
    n1: int
    n2: int
    a1, n1 = congruences[0]
    a2, n2 = congruences[1]

    m1: int
    m2: int
    m1, m2 = bezout(n1, n2)
    x: int = (a1*m2*n2 + a2*m1*n1) % (n1*n2)
    return chinese_remainder( [(x, n1*n2)] + congruences[2:])

with open("input-13.txt") as f:
    earliest_departure: int = int(f.readline().strip())
    bus_ids: list[str] = f.readline().strip().split(",")

#Part 1
bus_id_nums: list[int] = [int(x) for x in bus_ids if x != "x"]

earliest_buses: list[tuple[int, int]] = []
for id in bus_id_nums:
    next_bus: int = 0
    while next_bus < earliest_departure:
        next_bus += id
    earliest_buses.append((next_bus, id))

best_bus: tuple[int, int] = sorted(earliest_buses)[0]
score = best_bus[1] * (best_bus[0] - earliest_departure)
print(score)

#Part 2
congruences: list[tuple[int, int]] = []
for i, num in enumerate(bus_ids):
    if num != "x":
        id_num: int = int(num)
        congruences.append(((-i) % id_num, id_num))
print(chinese_remainder(congruences))