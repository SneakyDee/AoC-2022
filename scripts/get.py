def input():
    complete_input = ""
    with open("input", "r") as input:
        for line in input:
            complete_input += line
    return complete_input
