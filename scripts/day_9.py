import unittest
import math

import get


def make_move(position, direction):
    if direction == "R":
        position[0] += 1
    if direction == "L":
        position[0] -= 1
    if direction == "U":
        position[1] += 1
    if direction == "D":
        position[1] -= 1


class Runner(unittest.TestCase):
    def test_part_1(self):
        input = get.input().split("\n")
        moves = []
        for row in input:
            direction, amount = row.split(" ")
            moves.append([direction, int(amount)])
        head = [0, 0]
        tail = [0, 0]
        visited_positions = [[0, 0]]
        for move in moves:
            for amount in range(1, move[1] + 1):
                make_move(head, move[0])
                self.make_tail_move(head, tail, visited_positions)
            print(f"head: {head}, tail: {tail}")
        print("--------")
        print(len(visited_positions))
        print(head)
        print(tail)

    def test_part_2(self):
        input = get.input().split("\n")
        moves = []
        for row in input:
            direction, amount = row.split(" ")
            moves.append([direction, int(amount)])
        head = [0, 0]
        one = [0, 0]
        two = [0, 0]
        three = [0, 0]
        four = [0, 0]
        five = [0, 0]
        six = [0, 0]
        seven = [0, 0]
        eight = [0, 0]
        tail = [0, 0]
        visited_positions = [[0, 0]]
        for move in moves:
            for amount in range(1, move[1] + 1):
                make_move(head, move[0])
                self._make_moves(head, one)
                self._make_moves(one, two)
                self._make_moves(two, three)
                self._make_moves(three, four)
                self._make_moves(four, five)
                self._make_moves(five, six)
                self._make_moves(six, seven)
                self._make_moves(seven, eight)
                self.make_tail_move(eight, tail, visited_positions)
        print(visited_positions)
        print(len(visited_positions))

    def make_tail_move(self, head, tail, visited_positions):
        self._make_moves(head, tail)
        if tail not in visited_positions:
            visited_positions.append([tail[0], tail[1]])

    def _make_moves(self, head, tail):
        if self.move_tail_up_diagonal_right(head, tail):
            tail[0] += 1
            tail[1] += 1
        if self.move_tail_down_diagonaly_right(head, tail):
            tail[0] += 1
            tail[1] -= 1
        if self.move_tail_down_diagonaly_left(head, tail):
            tail[0] -= 1
            tail[1] -= 1
        if self.move_tail_up_diagonaly_left(head, tail):
            tail[0] -= 1
            tail[1] += 1
        if self.move_up(head, tail):
            tail[1] += 1
        if self.move_tail_down(head, tail):
            tail[1] -= 1
        if self.move_tail_right(head, tail):
            tail[0] += 1
        if self.move_tail_left(head, tail):
            tail[0] -= 1

    def move_up(self, leader, follower):
        return (math.dist([leader[1]], [follower[1]]) == 2 and
                (follower[1] < leader[1]) and
                (follower[0] == leader[0]))

    def move_tail_down(self, head, tail):
        return (math.dist([head[1]], [tail[1]]) == 2 and
                (tail[1] > head[1]) and
                (tail[0] == head[0]))

    def move_tail_right(self, head, tail):
        return (math.dist([head[0]], [tail[0]]) == 2 and
                (tail[0] < head[0]) and
                (tail[1] == head[1]))

    def move_tail_left(self, head, tail):
        return (math.dist([head[0]], [tail[0]]) == 2 and
                (tail[0] > head[0]) and
                (tail[1] == head[1]))

    def move_tail_up_diagonaly_left(self, head, tail):
        return (self.head_is_left_two_up_one(head, tail) or
                self.head_is_left_one_up_two(head, tail))

    def head_is_left_one_up_two(self, head, tail):
        return ((math.dist([head[1]], [tail[1]]) == 2) and
                (tail[0] > head[0]) and
                (tail[1] < head[1]))

    def head_is_left_two_up_one(self, head, tail):
        return ((math.dist([head[0]], [tail[0]]) == 2) and
                (tail[0] > head[0]) and
                (tail[1] < head[1]))

    def move_tail_down_diagonaly_left(self, head, tail):
        return (self.head_is_left_two_down_one(head, tail) or
                self.head_is_left_one_down_two(head, tail))

    def head_is_left_two_down_one(self, head, tail):
        return ((math.dist([head[0]], [tail[0]]) == 2) and
                (tail[0] > head[0]) and
                (tail[1] > head[1]))

    def head_is_left_one_down_two(self, head, tail):
        return ((math.dist([head[1]], [tail[1]]) == 2) and
                (tail[0] > head[0]) and
                (tail[1] > head[1]))

    def move_tail_down_diagonaly_right(self, head, tail):
        return (self.head_is_right_two_down_one(head, tail) or
                self.head_is_right_one_down_two(head, tail))

    def head_is_right_one_down_two(self, head, tail):
        return ((math.dist([head[1]], [tail[1]]) == 2) and
                (tail[0] < head[0]) and
                (tail[1] > head[1]))

    def head_is_right_two_down_one(self, head, tail):
        return ((math.dist([head[0]], [tail[0]]) == 2) and
                (tail[0] < head[0]) and
                (tail[1] > head[1]))

    def move_tail_up_diagonal_right(self, head, tail):
        return (self.head_is_right_two_up_one(head, tail) or
                self.head_is_right_one_up_two(head, tail))

    def head_is_right_two_up_one(self, head, tail):
        return ((math.dist([head[0]], [tail[0]]) == 2) and
                (tail[0] < head[0]) and
                (tail[1] < head[1]))

    def head_is_right_one_up_two(self, head, tail):
        return ((math.dist([head[1]], [tail[1]]) == 2) and
                (tail[0] < head[0]) and
                (tail[1] < head[1]))
