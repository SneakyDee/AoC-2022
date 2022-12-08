import unittest

import get


def format_rows(rows):
    formatted_rows = []
    for row in rows:
        formatted_rows.append([int(number) for number in row])
    rows = formatted_rows
    return rows


def check_if_tree_is_visible(map, rows):
    visible_trees = 0
    for row_index in range(len(map)):
        for tree_index in range(len(map[row_index])):
            if tree_is_visible(map, row_index, rows, tree_index):
                visible_trees += 1
    return visible_trees


def tree_is_visible(map, row_index, rows, tree_index):
    if (tree_visible_from_below(map, row_index, rows, tree_index) or
            tree_visible_from_right(map, row_index, rows, tree_index) or
            tree_visible_from_left(map, row_index, rows, tree_index) or
            tree_visible_from_above(map, row_index, rows, tree_index)):
        return True
    return False


def tree_visible_from_below(map, row_index, rows, tree_index):
    start_row = row_index + 2
    tree = tree_index + 1
    for row in rows[start_row:]:
        if row[tree] >= map[row_index][tree_index]:
            return False
    return True


def tree_visible_from_right(map, row_index, rows, tree_index):
    start_tree = tree_index + 2
    for tree in rows[row_index + 1][start_tree:]:
        if tree >= map[row_index][tree_index]:
            return False
    return True


def tree_visible_from_left(map, row_index, rows, tree_index):
    for tree in rows[row_index + 1][:tree_index + 1]:
        if tree >= map[row_index][tree_index]:
            return False
    return True


def tree_visible_from_above(map, row_index, rows, tree_index):
    for row in rows[:row_index + 1]:
        tree_above = row[tree_index + 1]
        if tree_above >= map[row_index][tree_index]:
            return False
    return True


class Runner(unittest.TestCase):
    def test_part_1(self):
        rows = get.input().split("\n")
        rows = format_rows(rows)
        map = []
        for index in range(len(rows)):
            if index == 0:
                continue
            if index == len(rows) - 1:
                break
            trees = []
            for tree_index in range(len(rows[index])):
                if tree_index == 0:
                    continue
                if tree_index == (len(rows[index]) - 1):
                    break
                tree = rows[index][tree_index]
                trees.append(tree)
            map.append(trees)
        visible_trees = check_if_tree_is_visible(map, rows)

        visible_trees += len(rows[0])
        visible_trees += len(rows[-1])
        for row in rows[1:-1]:
            visible_trees += 2
        print(visible_trees)
