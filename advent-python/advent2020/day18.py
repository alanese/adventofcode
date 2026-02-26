def evaluate_postfix(expr: str) -> int:
    stack: list[int] = []
    for token in expr:
        match token:
            case "+":
                stack.append(stack.pop() + stack.pop())
            case "*":
                stack.append(stack.pop() * stack.pop())
            case _:
                stack.append(int(token))
    return stack[0]

def infix_to_postfix(infix: str, precedence: dict[str, int]) -> str:
    stack: list[str] = []
    postfix: str = ""

    for token in infix:
        if token == " ":
            continue
        elif token == "(":
            stack.append("(")
        elif token == ")":
            while stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        elif token in "+*":
            while len(stack) > 0 and precedence[stack[-1]] >= precedence[token]:
                postfix += stack.pop()
            stack.append(token)
        else:
            postfix += token
    while len(stack) > 0:
        postfix += stack.pop()
    return postfix
    

with open("input-18.txt") as f:
    data: list[str] = [line.strip() for line in f]

#Part 1
precedence_p1: dict[str, int] = {"+": 1, "*": 1, "(": 0}
print(sum(evaluate_postfix(infix_to_postfix(line, precedence_p1)) for line in data))

precedence_p2: dict[str, int] = {"+": 2, "*": 1, "(": 0}
print(sum(evaluate_postfix(infix_to_postfix(line, precedence_p2)) for line in data))