import numpy as np

with open("inputs/day_10_test.txt") as f:
    test = np.array([list(line.strip()) for line in f])

with open("inputs/day_10_input.txt") as f:
    inputs = np.array([list(line.strip()) for line in f])
    # print(inputs)

VALID_POINTS = {"up": ["7", "F", "|"],
                "right": ["7", "J", "-"],
                "down": ["L", "J", "|"],
                "left": ["F", "L", "-"]}

VALID_DIRECTIONS = {"J": ["up", "left"],
                    "F": ["down", "right"],
                    "7": ["left", "down"],
                    "|": ["up", "down"],
                    "-": ["right", "left"],
                    "L": ["up", "right"]}


def validate_step(step, step_map):
    for k, v in step.items():
        return v in VALID_POINTS[k] and step["coordinates"] not in step_map[-4:]


def generate_surrounds(loop_map, coordinates, step_map):
    surrounds = []
    current_step = loop_map[coordinates[0]][coordinates[1]]

    if start_y != 0:
        surrounds.append({"up": loop_map[coordinates[0] - 1][coordinates[1]],
                          "coordinates": (coordinates[0] - 1, coordinates[1])})
    if start_y != len(loop_map) - 1:
        surrounds.append({"down": loop_map[coordinates[0] + 1][coordinates[1]],
                          "coordinates": (coordinates[0] + 1, coordinates[1])})
    if start_x != 0:
        surrounds.append({"left": loop_map[coordinates[0]][coordinates[1] - 1],
                          "coordinates": (coordinates[0], coordinates[1] - 1)})
    if start_x != len(loop_map[0]) - 1:
        surrounds.append({"right": loop_map[coordinates[0]][coordinates[1] + 1],
                          "coordinates": (coordinates[0], coordinates[1] + 1)})

    try:
        valid_step = [step for step in surrounds
                      if list(step.keys())[0] in VALID_DIRECTIONS[current_step]
                      and step["coordinates"] not in step_map[-4:]]
    except KeyError:
        valid_step = [step for step in surrounds if validate_step(step, step_map)]
        starting_pipe = [letter for letter in VALID_DIRECTIONS
                                                if list(valid_step[0].keys())[0] in VALID_DIRECTIONS[letter]
                                                and list(valid_step[1].keys())[0] in VALID_DIRECTIONS[letter]][0]
        inputs[coordinates[0]][coordinates[1]] = starting_pipe

    return valid_step




def find_furtherst_point(loop_map, coordinates):
    step_map = [coordinates]
    next_steps = generate_surrounds(loop_map, coordinates, step_map)
    all_steps = 1
    step_map.extend([next_steps[0]["coordinates"], next_steps[1]["coordinates"]])

    while next_steps[0]["coordinates"] != next_steps[1]["coordinates"]:
        all_steps += 1
        step_1 = generate_surrounds(loop_map, next_steps[0]["coordinates"], step_map)[0]
        step_2 = generate_surrounds(loop_map, next_steps[1]["coordinates"], step_map)[0]
        step_map.append(step_1["coordinates"])
        step_map.append(step_2["coordinates"])
        next_steps = [step_1, step_2]

    return all_steps, step_map


def transform_map(step_map, loop_map):
    for y in range(len(loop_map)):
        for x in range(len(loop_map[y])):
            if (y, x) not in step_map:
                loop_map[y][x] = "."

    replacements = {"F": "╔",
                   "L": "╚",
                   "J": "╝",
                   "7": "╗",
                   "|": "║",
                   "-": "═"}

    for old, new in replacements.items():
        loop_map = np.where(loop_map == old, new, loop_map)

    return loop_map

def count_dots(loop_map):
    for y in range(len(loop_map)):
        inside = [False, False]
        for x in range(len(loop_map[y])):
            if loop_map[y][x] in ["╔", "╗"]:
                inside[0] = not inside[0]

            if loop_map[y][x] in ["╚", "╝"]:
                inside[1] = not inside[1]

            if loop_map[y][x] == "║":
                inside[0] = not inside[0]
                inside[1] = not inside[1]

            if loop_map[y][x] == "." and all(inside):
                loop_map[y][x] = "i"
            elif loop_map[y][x] == "." and not all(inside):
                loop_map[y][x] = "o"

    inside_count = np.count_nonzero(loop_map == "i")
    outside_count = np.count_nonzero(loop_map == "o")
    return [f'Outside: {outside_count}, Inside: {inside_count}', loop_map]

if __name__ == "__main__":

    start = np.where(inputs == "S")
    start_y, start_x = int(start[0][0]), int(start[1][0])
    part_1 = find_furtherst_point(inputs, (start_y, start_x))
    print(part_1[0])
    new_inputs = transform_map(part_1[1], inputs)
    part_2 = count_dots(new_inputs)
    print(part_2[0])
    # np.savetxt("day_10.txt", part_2[1], fmt="%s", delimiter="")