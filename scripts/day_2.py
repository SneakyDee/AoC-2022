import get


ROCK = "A"
PAPER = "B"
SCISSORS = "C"

MY_ROCK = "X"
MY_PAPER = "Y"
MY_SCISSORS = "Z"

OUTCOME_WIN = "Z"
OUTCOME_LOSS = "X"
OUTCOME_DRAW = "Y"

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

WIN = 6
DRAW = 3
LOSS = 0


def rock_vs(my_move):
    if my_move == MY_PAPER:
        return WIN + PAPER_SCORE
    if my_move == MY_SCISSORS:
        return LOSS + SCISSORS_SCORE
    return DRAW + ROCK_SCORE


def paper_vs(my_move):
    if my_move == MY_ROCK:
        return LOSS + ROCK_SCORE
    if my_move == MY_SCISSORS:
        return WIN + SCISSORS_SCORE
    return DRAW + PAPER_SCORE


def scissors_vs(my_move):
    if my_move == MY_ROCK:
        return WIN + ROCK_SCORE
    if my_move == MY_PAPER:
        return LOSS + PAPER_SCORE
    return DRAW + SCISSORS_SCORE


def part_1():
    rounds = get_rounds()
    my_score = 0
    for round in rounds:
        if round[0] == ROCK:
            my_score += rock_vs(round[1])
        if round[0] == PAPER:
            my_score += paper_vs(round[1])
        if round[0] == SCISSORS:
            my_score += scissors_vs(round[1])
    print(my_score)


def part_2():
    rounds = get_rounds()
    score = 0
    for round in rounds:
        move = Move(round[0])
        if round[1] == OUTCOME_WIN:
            score += move.get_winning_score()
        if round[1] == OUTCOME_LOSS:
            score += move.get_loosing_score()
        if round[1] == OUTCOME_DRAW:
            score += move.get_draw_score()
    print(score)


def get_rounds():
    input = get.input()
    pair_of_moves = [moves.split(" ") for moves in input.split("\n")]
    return pair_of_moves


class Move:
    def __init__(self, enemy_move):
        self._enemy_move = enemy_move

    def get_winning_score(self):
        if self._enemy_move == ROCK:
            return WIN + PAPER_SCORE
        if self._enemy_move == PAPER:
            return WIN + SCISSORS_SCORE
        return WIN + ROCK_SCORE

    def get_loosing_score(self):
        if self._enemy_move == ROCK:
            return SCISSORS_SCORE + LOSS
        if self._enemy_move == PAPER:
            return ROCK_SCORE + LOSS
        return PAPER_SCORE + LOSS

    def get_draw_score(self):
        if self._enemy_move == ROCK:
            return ROCK_SCORE + DRAW
        if self._enemy_move == PAPER:
            return PAPER_SCORE + DRAW
        return SCISSORS_SCORE + DRAW


part_2()
