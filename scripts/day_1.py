class Elf:
    def __init__(self, inventory):
        self._inventory = inventory.split("\n")

    def get_amount_of_calories(self):
        total = 0
        for item in self._inventory:
            total += int(item)
        return total


def part_1():
    list_of_calories = get_list_of_calories_carried()
    print(max(list_of_calories))


def part_2():
    list_of_calories = get_list_of_calories_carried()
    sorted_list = sorted(list_of_calories, reverse=True)
    total_calories = 0
    for calories in sorted_list[0:3]:
        total_calories += calories
    print(total_calories)


def get_list_of_calories_carried():
    list_of_elves = get_elves()
    list_of_calories = []
    for elf in list_of_elves:
        list_of_calories.append(elf.get_amount_of_calories())
    return list_of_calories


def get_input():
    complete_input = ""
    with open("input", "r") as input:
        for line in input:
            complete_input += line
    return complete_input


def get_elves():
    input = get_input()
    list_of_elves = []
    elves = input.split("\n\n")
    for inventory in elves:
        list_of_elves.append(Elf(inventory))
    return list_of_elves


part_2()
