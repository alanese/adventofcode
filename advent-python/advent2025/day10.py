from itertools import combinations
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np


def parse_indicators(ind_str):
    return [light == "#" for light in ind_str[1:-1]]

def parse_button(button_str):
    return [int(x) for x in button_str[1:-1].split(",")]

def check_p1_combination(req, button_sequence):
    state = [False for _ in req]
    for button in button_sequence:
        for light in button:
            state[light] = not state[light]

    return state == req

def find_p1_combination(req, buttons):
    for i in range(1, len(buttons)+1):
        for combo in combinations(buttons, i):
            if check_p1_combination(req, combo):
                return i
    return -1
    

with open("input-10.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]

total = 0
for line in lines:
    req = parse_indicators(line[0])
    buttons = [parse_button(button) for button in line[1:-1]]
    total += find_p1_combination(req, buttons)

print(total)

#-----------

def parse_joltage(jolt_str):
    return [int(x) for x in jolt_str[1:-1].split(",")]

def buttons_on(buttons, length):
    return [ 1 if i in buttons else 0 for i in range(length)]

total = 0
for line in lines:
    joltage_req = np.array(parse_joltage(line[-1]))
    buttons = [parse_button(button) for button in line[1:-1]]
    button_matrix = np.array([buttons_on(b, len(joltage_req)) for b in buttons])

    coeffs = np.array([1 for _ in buttons])
    bounds = Bounds(lb = np.array([0]*len(buttons)))
    constraints = LinearConstraint(A = button_matrix.T, lb = joltage_req.T, ub = joltage_req.T)
    res = milp(coeffs, integrality=coeffs, bounds=bounds, constraints=constraints)

    total += int(res.fun)

print(total)