def handle_token(sequence: str) -> tuple[str, str]:
    if "(" not in sequence:
        return sequence, ""
    else:
        lparen_pos: int = sequence.index("(")
        x_pos: int = sequence.index("x", lparen_pos)
        rparen_pos: int = sequence.index(")")
        count: int = int(sequence[lparen_pos+1:x_pos])
        times: int = int(sequence[x_pos+1:rparen_pos])
        return sequence[:lparen_pos] + sequence[rparen_pos+1:rparen_pos+1+count]*times, sequence[rparen_pos+1+count:]
    
def handle_token_v2(sequence: str) -> tuple[str, str]:
    if "(" not in sequence:
        return sequence, ""
    else:
        lparen_pos: int = sequence.index("(")
        x_pos: int = sequence.index("x", lparen_pos)
        rparen_pos: int = sequence.index(")", x_pos)
        count: int = int(sequence[lparen_pos+1:x_pos])
        times: int = int(sequence[x_pos+1:rparen_pos])
        return sequence[:lparen_pos], sequence[rparen_pos+1:rparen_pos+1+count]*times + sequence[rparen_pos+1+count:]

    

def decompress_sequence(sequence: str) -> str:
    result: str = ""
    next: str
    while len(sequence) > 0:
        next, sequence = handle_token(sequence)
        result += next
    return result

# This works for the examples but isn't efficient enough to handle the actual p2 in a reasonable time
# Gotta find some workaround
def decompressed_length_v2(sequence: str) -> int:
    total = 0
    head: str = ""
    rest: str = sequence
    remaining_markers: int = 0
    iterations: int = 0

    while len(rest) > 0:
        iterations += 1
        head, rest = handle_token_v2(rest)
        remaining_markers = rest.count("(")
        print(f"Iteration {iterations}; Total: {total}; Remaining: {len(rest)}; Remaining markers: {remaining_markers}")
        total += len(head)

    return total

with open("input-09.txt") as f:
    compressed: str = "".join([line.strip() for line in f])

decompressed = decompress_sequence(compressed)
print(len(decompressed))

print(decompressed_length_v2("(27x12)(20x12)(13x14)(7x10)(1x12)A"))