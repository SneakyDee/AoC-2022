import unittest

import get


class Runner(unittest.TestCase):
    def test_part_1(self):
        input = get.input().split("\n")
        pairs = []
        for line in input:
            elf_1, elf_2 = line.split(",")
            pairs.append([elf_1.split("-"), elf_2.split("-")])
        print(pairs)
