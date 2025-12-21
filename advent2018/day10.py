from typing import NamedTuple
import tkinter as tk
from tkinter import ttk


class Vector2D(NamedTuple):
    x: int
    y: int

class Star(NamedTuple):
    start_pos: Vector2D
    velocity: Vector2D

    def position_after(self: Star, seconds: int) -> Vector2D:
        return Vector2D(x=self.start_pos.x + seconds * self.velocity.x, y=self.start_pos.y + seconds * self.velocity.y)

def parse_line(line: str) -> Star:
    pos_start: int = line.index("<")
    pos_sep: int = line.index(",")
    pos_end: int = line.index(">")
    vel_start: int = line.index("<", pos_end+1)
    vel_sep: int = line.index(",", pos_end+1)
    vel_end: int = line.index(">", pos_end+1)
    p_x: int = int(line[pos_start+1: pos_sep])
    p_y: int = int(line[pos_sep+1:pos_end])
    v_x: int = int(line[vel_start+1:vel_sep])
    v_y: int = int(line[vel_sep+1:vel_end])    
    return Star(Vector2D(p_x, p_y), Vector2D(v_x, v_y))

#returns min_x, max_x, min_y, max_y
def get_bounding_coords(points: list[Vector2D]) -> tuple[int, int, int, int]:
    min_x: int = points[0].x
    max_x: int = points[0].x
    min_y: int = points[0].y
    max_y: int = points[0].y
    for point in points[1:]:
        min_x = min(min_x, point.x)
        max_x = max(max_x, point.x)
        min_y = min(min_y, point.y)
        max_y = max(max_y, point.y)
    return min_x, max_x, min_y, max_y


with open("input-10.txt") as f:
    data: list[str] = [line.strip() for line in f]

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

stars: list[Star] = [parse_line(line) for line in data]

root: tk.Tk = tk.Tk()
slider_value: tk.IntVar = tk.IntVar()
spinner_value: tk.IntVar = tk.IntVar()
value_label = ttk.Label(root, text=str(int(slider_value.get())))
canvas: tk.Canvas = tk.Canvas(root, width=600, height=400, bg="white")
def slider_changed(event):
    time: int = slider_value.get()
    value_label.configure(text=str(time))
    canvas.delete('all')
    new_star_pos: list[Vector2D] = [star.position_after(time) for star in stars]
    min_x, max_x, min_y, max_y = get_bounding_coords(new_star_pos)
    for star_pos in new_star_pos:
        canvas.create_rectangle(star_pos.x, star_pos.y, star_pos.x, star_pos.y)

slider: ttk.Scale = ttk.Scale(root, from_=10000, to=10100, orient='horizontal', variable=slider_value, command=slider_changed)

slider.pack()
value_label.pack()
canvas.pack()
root.mainloop()