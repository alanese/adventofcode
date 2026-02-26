def parse_deck(deck: list[str]) -> list[int]:
    return [int(x) for x in deck[1:]]

def score_deck(deck: list[int]) -> int:
    return sum(i*x for i,x in enumerate(deck[::-1], start=1))

def play_recursive_game(deck_p1: list[int], deck_p2: list[int]) -> tuple[int, list[int]]:
    seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    while len(deck_p1) > 0 and len(deck_p2) > 0:
        if (tuple(deck_p1), tuple(deck_p2)) in seen:
            return 1, deck_p1
        seen.add((tuple(deck_p1), tuple(deck_p2)))
        card_p1: int = deck_p1.pop(0)
        card_p2: int = deck_p2.pop(0)
        if card_p1 <= len(deck_p1) and card_p2 <= len(deck_p2):
            winner, _ = play_recursive_game(deck_p1[:card_p1], deck_p2[:card_p2])
        else:
            winner = 1 if card_p1 > card_p2 else 2
        
        if winner == 1:
            deck_p1 += [card_p1, card_p2]
        else:
            deck_p2 += [card_p2, card_p1]
    if len(deck_p1) > 0:
        return 1, deck_p1
    else:
        return 2, deck_p2
                                                                    
with open("input-22.txt") as f:
    data: list[str] = [line.strip() for line in f]

delim: int = data.index("")
deck_p1: list[int] = parse_deck(data[:delim])
deck_p2: list[int] = parse_deck(data[delim+1:])

working_p1: list[int] = deck_p1[:]
working_p2: list[int] = deck_p2[:]

#Part 1
while len(working_p1) > 0 and len(working_p2) > 0:
    card_p1: int = working_p1.pop(0)
    card_p2: int = working_p2.pop(0)
    if card_p1 > card_p2:
        working_p1 += [card_p1, card_p2]
    else:
        working_p2 += [card_p2, card_p1]
if len(working_p1) > 0:
    print(score_deck(working_p1))
else:
    print(score_deck(working_p2))

#Part 2
working_p1 = deck_p1[:]
working_p2 = deck_p2[:]

winner, deck = play_recursive_game(working_p1, working_p2)
print(score_deck(deck))