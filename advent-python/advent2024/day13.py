from fractions import Fraction

def min_int(x: Fraction, y: Fraction) -> int:
    if x.is_integer() and y.is_integer():
        return min(int(x), int(y))
    elif x.is_integer():
        return int(x)
    elif y.is_integer():
        return int(y)
    else:
        return -1

#Find the cost of the cheapest way to get to (px,py) in steps of
#(ax,ay) (costing a_cost) and (bx,by) (costing b_cost)
def cheapest_prize(ax: int, ay: int, bx: int, by: int, px: int, py: int, a_cost: int=3, b_cost: int=1) -> int:
    #Check if both button vectors are parallel to prize vector - I don't think any of these conditions actually trigger
    #in the puzzle input:
    if ax*py == ay*px and bx*py == by*px:
        return min_int(Fraction(a_cost * px, ax), Fraction(b_cost * px, bx))
    #If a is parallel but not b
    elif ax*py == ay*px:
        if px%ax == 0:
            return a_cost * (px//ax)
        else:
            return -1
    #If b is parallel but not a
    elif bx*py == by*px:
        if px % bx == 0:
            return b_cost * (px//bx)
        else:
            return -1
    #If a and b are parallel to each other but not to p
    elif ax*by == bx*ay:
        return -1
    else:
        #Solve a*ax + b*bx = px, a*ay + b*by = py for integer a,b
        #Yes, I worked this out on paper
        b: Fraction = (Fraction(py, ay) - Fraction(px, ax)) / (Fraction(by, ay) - Fraction(bx, ax))
        a: Fraction = (px - b*bx)/ax
        if a.is_integer() and b.is_integer():
            return int(a)*a_cost + int(b)*b_cost
        else:
            return -1

    

with open("input-13.txt") as f:
    data: list[str] = [line.strip() for line in f]

machines: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]] = []
while len(data) > 0:
    cur_machine: list[str] = data[:4]
    data = data[4:]
    a: str = cur_machine[0][10:]
    x, _, y = cur_machine[0][10:].partition(", ")
    button_a: tuple[int, int] = int(x[2:]), int(y[2:])
    x, _, y = cur_machine[1][10:].partition(", ")
    button_b: tuple[int, int] = int(x[2:]), int(y[2:])
    x, _, y = cur_machine[2][7:].partition(", ")
    prize: tuple[int, int] = int(x[2:]), int(y[2:])
    machines.append((button_a, button_b, prize))

#Parts 1 and 2
ADDED: int = 10**13
total_tokens_p1: int = 0
total_tokens_p2: int = 0
for (ax, ay), (bx, by), (px, py) in machines:
    cost_p1: int = cheapest_prize(ax, ay, bx, by, px, py)
    if cost_p1 >= 0:
        total_tokens_p1 += cost_p1
    cost_p2: int = cheapest_prize(ax, ay, bx, by, px+ADDED, py+ADDED)
    if cost_p2 >= 0:
        total_tokens_p2 += cost_p2
print(total_tokens_p1)
print(total_tokens_p2)