def evaluate(data: str) -> tuple[int, int]:
    current_depth: int = 0
    in_garbage: bool = False
    score: int = 0
    garbage_count: int = 0
    i: int = 0
    while i < len(data):
        if in_garbage:
            if data[i] == "!":
                i += 1
            elif data[i] == ">":
                in_garbage = False
            else:
                garbage_count += 1
        else:
            if data[i] == "{":
                current_depth += 1
            elif data[i] == "}":
                score += current_depth
                current_depth -= 1
            elif data[i] == "<":
                in_garbage = True
        i += 1
    return score, garbage_count


with open("input-09.txt") as f:
    data = f.read()
print(evaluate(data))

    