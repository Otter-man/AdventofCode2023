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
        return v in VALID_POINTS[k] and {"y": step["y"], "x": step["x"]} not in step_map


def generate_surrounds(test, start_y, start_x, step_map):
    surrounds = []
    current_step = test[start_y][start_x]

    if start_y != 0:
        surrounds.append({"up": test[start_y - 1][start_x], "y": start_y - 1, "x": start_x})
    if start_y != len(test) - 1:
        surrounds.append({"down": test[start_y + 1][start_x], "y": start_y + 1, "x": start_x})
    if start_x != 0:
        surrounds.append({"left": test[start_y][start_x - 1], "y": start_y, "x": start_x - 1})
    if start_x != len(test[0]) - 1:
        surrounds.append({"right": test[start_y][start_x + 1], "y": start_y, "x": start_x + 1})

    valid_step = [step for step in surrounds if validate_step(step, step_map)]

    if test[start_y][start_x] != "S" and len(valid_step) != 1:
        valid_step = [step for step in valid_step
                      if list(step.keys())[0] in VALID_DIRECTIONS[current_step]]
    return valid_step




def find_furtherst_point(test, start_y, start_x):
    step_map = []
    next_steps = generate_surrounds(test, start_y, start_x, step_map)
    all_steps = 1
    step_map = [{"y": next_steps[0]["y"], "x": next_steps[0]["x"]},
                {"y": next_steps[1]["y"], "x": next_steps[1]["x"]}]

    while (next_steps[0]["y"], next_steps[0]["x"]) != (next_steps[1]["y"], next_steps[1]["x"]):
        all_steps += 1
        step_1 = generate_surrounds(test, next_steps[0]["y"], next_steps[0]["x"], step_map)[0]
        step_2 = generate_surrounds(test, next_steps[1]["y"], next_steps[1]["x"], step_map)[0]
        step_map.append({"y": step_1["y"], "x": step_1["x"]})
        step_map.append({"y": step_2["y"], "x": step_2["x"]})
        next_steps = [step_1, step_2]
    return all_steps

if __name__ == "__main__":

    start = np.where(inputs == "S")
    start_y, start_x = int(start[0][0]), int(start[1][0])
    part_1 = find_furtherst_point(inputs, start_y, start_x)
    print(part_1)