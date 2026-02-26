BOARD_SIZE: int = 5

def check_bingo(marked: set[tuple[int, int]]) -> bool:
    for x in range(BOARD_SIZE):
        if {(x,y) for y in range(BOARD_SIZE)} < marked:
            return True
    for y in range(BOARD_SIZE):
        if {(x,y) for x in range(BOARD_SIZE)} < marked:
            return True
    return False

#Returns turn of bingo, winning number, and sum of unmarked numbers, or -1,-1,-1 if no bingo
def play_bingo(board: dict[int, tuple[int, int]], numbers: list[int]) -> tuple[int, int, int]:
    turn: int = 0
    unmarked: set[int] = set(board.keys())
    marked: set[tuple[int, int]] = set()
    for number in numbers:
        turn += 1
        if number in board:
            unmarked.remove(number)
            marked.add(board[number])
            if check_bingo(marked):
                return turn, number, sum(unmarked)
    return -1, -1, -1

with open("input-04.txt") as f:
    data: list[str] = [line.strip() for line in f]

numbers: list[int] = [int(x) for x in data[0].split(",")]

board_data: list[str] = data[1:]
boards: list[dict[int, tuple[int, int]]] = []
while len(board_data) > 0:
    next_board: dict[int, tuple[int, int]] = {}
    for y in range(BOARD_SIZE):
        for x, num in enumerate(board_data[y+1].split()):
            next_board[int(num)] = (x,y)
    boards.append(next_board)
    board_data = board_data[BOARD_SIZE+1:]
#Part 1
results: list[tuple[int, int, int]] = [play_bingo(board, numbers) for board in boards]
results = [res for res in results if res[0] > 0]
results.sort()
print(results[0][1] * results[0][2])

#Part 2
print(results[-1][1] * results[-1][2])