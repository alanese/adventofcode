def error_or_complete(line: str) -> tuple[str, list[str]]:
    chars: list[str] = []
    for char in line:
        match char:
            case "(" | "[" | "{" | "<":
                chars.append(char)
            case ")":
                if len(chars) > 0 and chars[-1] == "(":
                    chars.pop()
                else:
                    return char, []
            case "]":
                if len(chars) > 0 and chars[-1] == "[":
                    chars.pop()
                else:
                    return char, []
            case "}":
                if len(chars) > 0 and chars[-1] == "{":
                    chars.pop()
                else:
                    return char, []
            case ">":
                if len(chars) > 0 and chars[-1] == "<":
                    chars.pop()
                else:
                    return char, []
            case _:
                raise ValueError(f"Invalid character {char}")
    return "", chars

SCORE_VALUES: dict[str, int] = {"(": 1, "[": 2, "{": 3, "<": 4}
def score_completion(remaining_stack: list[str]) -> int:
    score: int = 0
    for char in reversed(remaining_stack):
        score = score*5 + SCORE_VALUES[char]
    return score


with open("input-10.txt") as f:
    data: list[str] = [line.strip() for line in f]

ERROR_VALS: dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}

#Parts 1 & 2
error_score: int = 0
completion_scores: list[int] = []
for line in data:
    error, stack = error_or_complete(line)
    if error != "":
        error_score += ERROR_VALS[error]
    else:
        completion_scores.append(score_completion(stack))
print(error_score)

completion_scores.sort()
print(completion_scores[len(completion_scores)//2])