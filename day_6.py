import copy
import datetime
from functools import reduce
import operator

with open("inputs/day_6_input.txt") as f:
    inputs = f.readlines()

with open("inputs/day_6_test.txt") as f:
    test = f.readlines()

def parse_input(inputs):
    inputs_copy = copy.deepcopy(inputs)
    for c, line in enumerate(inputs_copy):
        inputs_copy[c] = line.split(":")[1].split()
        inputs_copy[c] = [int(i) for i in inputs_copy[c]]

    inputs_copy = zip(inputs_copy[0], inputs_copy[1])
    return list(inputs_copy)


def calculate_winning_positions(parsed_inputs):
    first_position = 0
    last_position = 0
    all_races = []
    for item in parsed_inputs:
        for i in range(1,item[0]+1):
            distance = i*(item[0] - i)
            if distance > item[1]:
                first_position = i
                break

        for ii in range(item[0], 1, -1):
            distance = ii * (item[0] - ii)
            if distance > item[1]:
                last_position = ii
                break

        all_races.append(last_position - first_position + 1)

    all_races = reduce(operator.mul, all_races)

    return all_races


def better_parse_input(inputs):
    for c, line in enumerate(inputs):
        inputs[c] = line.split(":")[1].split()
        inputs[c] = int("".join(inputs[c]))

    return [list(inputs)]


if __name__ == "__main__":
    parsed_inputs = parse_input(inputs)
    part1 = calculate_winning_positions(parsed_inputs)
    print(part1)
    print(datetime.datetime.now())
    improved_parsed_inputs = better_parse_input(inputs)
    part2 = calculate_winning_positions(improved_parsed_inputs)
    print(part2)
    print(datetime.datetime.now())
