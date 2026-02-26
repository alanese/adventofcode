DIRECTIONS: dict[str, tuple[int, int]] = {"^": (0, -1),
                                          ">": (1, 0),
                                          "v": (0, 1),
                                          "<": (-1, 0)}

def can_move(x: int, y: int, dx: int, dy: int, grid: dict[tuple[int, int], str]) -> bool:
    obj: str = grid.get((x,y), "#")
    target_obj: str = grid.get((x+dx, y+dy), "#")
    match obj:
        case "#":
            return False
        case "@" | "O":
            return target_obj == "." or can_move(x+dx, y+dy, dx, dy, grid)
        case "[":
            if dx == 0:
                return (target_obj == "." or can_move(x+dx, y+dy, dx, dy, grid)) and\
                        (grid[(x+1, y+dy)] == "." or can_move(x+1, y+dy, dx, dy, grid))
            elif dx == 1:
                return can_move(x+1, y, dx, dy, grid)
            else:
                return target_obj == "." or can_move(x+dx, y+dy, dx, dy, grid)
        case "]":
            if dx == 0:
                return (target_obj == "." or can_move(x+dx, y+dy, dx, dy, grid)) and\
                       (grid[x-1, y+dy] == "." or can_move(x-1, y+dy, dx, dy, grid))
            elif dx == 1:
                return target_obj == "." or can_move(x+dx, y+dy, dx, dy, grid)
            else:
                return can_move(x-1, y, dx, dy, grid)
        case _:
            raise ValueError(f"Cannot move object {obj}")
        
def move(x: int, y: int, dx: int, dy: int, grid: dict[tuple[int, int], str]):
    obj: str = grid[(x,y)]
    match obj:
        case "." | "#":
            return
        case "@" | "O":
            move(x+dx, y+dy, dx, dy, grid)
            grid[(x+dx, y+dy)] = obj
            grid[(x, y)] = "."
        case "[":
            if dx == 0:
                move(x+dx, y+dy, dx, dy, grid)
                move(x+1+dx, y+dy, dx, dy, grid)
                grid[(x+dx, y+dy)] = "["
                grid[(x+1+dx, y+dy)] = "]"
                grid[(x,y)] = "."
                grid[(x+1,y)] = "."
            else:
                move(x+dx, y+dy, dx, dy, grid)
                grid[(x+dx, y+dy)] = "["
                grid[(x,y)] = "."
        case "]":
            if dx == 0:
                move(x+dx, y+dy, dx, dy, grid)
                move(x-1+dx, y+dy, dx, dy, grid)
                grid[(x+dx, y+dy)] = "]"
                grid[(x-1+dx, y+dy)] = "["
                grid[(x,y)] = "."
                grid[(x-1,y)] = "."
            else:
                move(x+dx, y+dy, dx, dy, grid)
                grid[(x+dx, y+dy)] = "]"
                grid[(x,y)] = "."

def execute_directions(robot_x: int, robot_y: int, instructions: str, grid: dict[tuple[int, int], str]):
    for step in instructions:
        dx, dy = DIRECTIONS[step]
        if can_move(robot_x, robot_y, dx, dy, grid):
            move(robot_x, robot_y, dx, dy, grid)
            robot_x += dx
            robot_y += dy

def score_grid(grid: dict[tuple[int, int], str], target_object: str) -> int:
    score: int = 0
    for (x,y), obj in grid.items():
        if obj == target_object:
            score += 100*y + x
    return score

with open("input-15.txt") as f:
    data: list[str] = [line.strip() for line in f]

delim: int = data.index("")

grid: dict[tuple[int, int], str] = {}
grid_2: dict[tuple[int, int], str] = {}
robot_x: int = -1
robot_y: int = -1
for y, line in enumerate(data[:delim]):
    for x, char in enumerate(line):
        grid[(x,y)] = char
        match char:
            case "#" | ".":
                grid_2[(2*x, y)] = char
                grid_2[(2*x+1, y)] = char
            case "@":
                grid_2[(2*x, y)] = "@"
                grid_2[(2*x+1, y)] = "."
            case "O":
                grid_2[(2*x, y)] = "["
                grid_2[(2*x+1, y)] = "]"
        if char == "@":
            robot_x, robot_y = x,y

if robot_x == -1 or robot_y == -1:
    raise ValueError("No robot found")

instructions: str = "".join(data[delim+1:])


#Part 1
execute_directions(robot_x, robot_y, instructions, grid)
print(score_grid(grid, "O"))

#Part 2 - robot_x*2 to account for wider grid
execute_directions(robot_x*2, robot_y, instructions, grid_2)
print(score_grid(grid_2, "["))