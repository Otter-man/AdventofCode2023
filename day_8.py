with open('inputs/day_8_inputs.txt') as f:
    inputs = f.readlines()

with open('inputs/day_8_test.txt') as f:
    test = f.readlines()


def instruction_generator(inputs):
    while True:
        for char in inputs.strip():
            yield char

def map_parser(map_original):
    map_dict = dict()
    for coordinate in map_original:
        coordinate = coordinate.strip().split(' = ')
        point = coordinate[0]
        step_l = coordinate[1].split(",")[0][1:]
        step_r = coordinate[1].split(",")[1][:-1].strip()

        map_dict[point] = {"L": step_l, "R": step_r}

    return map_dict

if __name__ == "__main__":
    main_input = inputs

    step_gen = instruction_generator(main_input[0])
    map_dict = map_parser(main_input[2:])
    current_point = "AAA"
    steps = 0
    while True:
        next_step = next(step_gen)
        current_point = map_dict[current_point][next_step]
        steps += 1
        if current_point == "ZZZ":
            break
    print(steps)