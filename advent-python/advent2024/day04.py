TARGET_WORD: str = "XMAS"

def get_word(x_start: int, y_start: int, x_delta: int, y_delta: int, length: int, letters: dict[tuple[int, int], str]) -> str:
    return "".join(letters.get((x_start + i*x_delta, y_start + i*y_delta), "") for i in range(length))

def check_x_mas(center_x: int, center_y: int, letters: dict[tuple[int, int], str]) -> bool:
    mas_count: int = 0
    if get_word(center_x-1, center_y-1, 1, 1, 3, letters) in ["MAS", "SAM"]:
        if get_word(center_x-1, center_y+1, 1, -1, 3, letters) in ["MAS", "SAM"]:
            return True
    return False

with open("input-04.txt") as f:
    data: list[str] = [line.strip() for line in f]

letters: dict[tuple[int, int], str] = {}
for y, line in enumerate(data):
    for x, char in enumerate(line):
        letters[(x,y)] = char

#Part 1
count: int = 0
for x in range(len(data[0])):
    for y in range(len(data)):
        for dx,dy in [ (1,0), (0,1), (1,1), (1,-1)]:
            word = get_word(x, y, dx, dy, 4, letters)
            if word == TARGET_WORD or word[::-1] == TARGET_WORD:
                count += 1
print(count)

#Part 2
xmas_count: int = 0
for x in range(len(data[0])):
    for y in range(len(data)):
        if check_x_mas(x, y, letters):
            xmas_count += 1
print(xmas_count)