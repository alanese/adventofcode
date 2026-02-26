from enum import Enum

class Result(Enum):
    WIN = 6
    TIE = 3
    LOSE = 0

class Throw(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    #Implementing nontransitive __gt__ makes me feel dirty somehow
    def __gt__(self: Throw, other: Throw):
        if self.__class__ is not other.__class__:
            return NotImplemented
        match self:
            case Throw.ROCK:
                return other == Throw.SCISSORS
            case Throw.PAPER:
                return other == Throw.ROCK
            case Throw.SCISSORS:
                return other == Throw.PAPER

THROW_CODES: dict[str, Throw] = {"A": Throw.ROCK, "X": Throw.ROCK,
                                 "B": Throw.PAPER, "Y": Throw.PAPER,
                                 "C": Throw.SCISSORS, "Z": Throw.SCISSORS}
RESULT_CODES: dict[str, Result] = {"X": Result.LOSE, "Y": Result.TIE, "Z": Result.WIN}

THROWS: list[Throw] = [Throw.ROCK, Throw.PAPER, Throw.SCISSORS]
def force_result(opponent: Throw, result: Result) -> Throw:
    opponent_index = THROWS.index(opponent)
    match result:
        case Result.LOSE:
            return THROWS[(opponent_index-1)%3]
        case Result.TIE:
            return opponent
        case Result.WIN:
            return THROWS[(opponent_index+1)%3]
        

data: list[tuple[str, str]] = []
with open("input-02.txt") as f:
    for line in f:
        opponent, _, you = line.strip().partition(" ")
        data.append((opponent, you))

total_score: int = 0
for opponent, you in data:
    total_score += THROW_CODES[you].value
    if THROW_CODES[you] > THROW_CODES[opponent]:
        total_score += Result.WIN.value
    elif THROW_CODES[you] == THROW_CODES[opponent]:
        total_score += Result.TIE.value
    else:
        total_score += Result.LOSE.value
print(total_score)

total_score = 0
for opponent, result in data:
    you = force_result(THROW_CODES[opponent], RESULT_CODES[result])
    total_score += you.value + RESULT_CODES[result].value
print(total_score)