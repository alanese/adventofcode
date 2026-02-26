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


pos_counts: list[int] = []
equivalents: list[int] = []
with open("input-15.txt") as f:
    for t, line in enumerate(f, start=1):
        line_split: list[str] = line.split()
        pos_count: int = int(line_split[3])
        pos_counts.append(pos_count)
        start_pos: int = int(line_split[-1][:-1])
        #x + init_pos + t ~ pos_count
        #x ~ pos_count - init_pos - t
        equivalents.append((pos_count - start_pos - t) % pos_count)

print(chinese_remainder(list(zip(equivalents, pos_counts))))

pos_counts.append(11)
equivalents.append(11-(len(equivalents)+1))
print(chinese_remainder(list(zip(equivalents, pos_counts))))