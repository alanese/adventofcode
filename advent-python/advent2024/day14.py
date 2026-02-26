from collections import Counter
import tkinter as tk
from tkinter import ttk

#Returns p_x, p_y, v_x, v_y
def parse_robot(robot: str) -> tuple[int, int, int, int]:
    p, _, v = robot.partition(" ")
    px, _, py = p[2:].partition(",")
    vx, _, vy = v[2:].partition(",")
    return int(px), int(py), int(vx), int(vy)

def sign(num: int) -> int:
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1

AREA_WIDTH: int = 101
AREA_HEIGHT: int = 103
STEPS = 100

with open("input-14.txt") as f:
    data: list[str] = [line.strip() for line in f]

robots: list[tuple[int, int, int, int]] = [parse_robot(line) for line in data]

#Part 1
robot_locations: list[tuple[int, int]] = []
for px, py, vx, vy in robots:
    robot_locations.append( ((px+STEPS*vx)%AREA_WIDTH, (py+STEPS*vy)%AREA_HEIGHT))

quadrant_counts: dict[tuple[int, int], int] = Counter()

for x,y in robot_locations:
    x_half: int = sign(AREA_WIDTH//2 - x)
    y_half: int = sign(AREA_HEIGHT//2 - y)
    quadrant_counts[(x_half,y_half)] += 1

print(quadrant_counts[(-1,-1)] * quadrant_counts[(-1,1)] * quadrant_counts[(1,-1)] * quadrant_counts[(1,1)])

#Part 2
root: tk.Tk = tk.Tk()
canvas: tk.Canvas = tk.Canvas(root, width=AREA_WIDTH, height=AREA_HEIGHT, bg="white")
spinner: ttk.Spinbox
def spinner_changed():
    time: int = int(spinner.get())
    canvas.delete('all')
    for px, py, vx, vy in robots:
        robot_x = (px + time*vx) % AREA_WIDTH
        robot_y = (py + time*vy) % AREA_HEIGHT
        canvas.create_rectangle(robot_x, robot_y, robot_x, robot_y)

spinner: ttk.Spinbox = ttk.Spinbox(root, from_=0, to=101*103-1, increment=AREA_WIDTH, command=spinner_changed)


spinner.pack()
canvas.pack()
root.mainloop()


