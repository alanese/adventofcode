from typing import Dict, Tuple

buttons: Tuple[Tuple[str, ...], ...] = ( ("1", "2", "3"),
                                         ("4", "5", "6"),
                                         ("7", "8", "9"))

x = 1
y = 1
code = ""
with open("input-02.txt") as f:
    lines = f.readlines()
for line in lines:
    for char in line.strip():
        match char:
            case "U":
                y = max(y-1, 0)
            case "D":
                y = min(y+1, 2)
            case "L":
                x = max(x-1, 0)
            case "R":
                x = min(x+1, 2)
    code += buttons[y][x]

print(code)

#oh god this is awful
diamond_buttons: Dict[str, Dict[str, str]] = {"1": {"D": "3"},
                                              "2": {"D": "6", "R": "3"},
                                              "3": {"U": "1", "D": "7", "L": "2", "R": "4"},
                                              "4": {"D": "8", "L": "3"},
                                              "5": {"R": "6"},
                                              "6": {"U": "2", "D": "A", "L": "5", "R": "7"},
                                              "7": {"U": "3", "D": "B", "L": "6", "R": "8"},
                                              "8": {"U": "4", "D": "C", "L": "7", "R": "9"},
                                              "9": {"L": "8"},
                                              "A": {"U": "6", "R": "B"},
                                              "B": {"U": "7", "D": "D", "L": "A", "R": "C"},
                                              "C": {"U": "8", "L": "B"},
                                              "D": {"U": "B"}}

code = ""
position = "5"
for line in lines:
    for char in line.strip():
        position = diamond_buttons[position].get(char, position)
    code += position

print(code)