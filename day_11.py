import numpy as np
import itertools

with open("inputs/day_11_test.txt") as f:
    test = np.array([list(line.strip()) for line in f])

with open("inputs/day_11_input.txt") as f:
    inputs = np.array([list(line.strip()) for line in f])


def find_empty_rows(galaxy_map):
    empty_rows = []
    for c, row in enumerate(galaxy_map):
        if len(set(list(row))) == 1:
            empty_rows.append(c)
    return empty_rows

def inflate_map_by(galaxy_map, multiplayer):

    galaxy_points = list(zip(*list(np.where(galaxy_map == "#"))))
    empty_rows = find_empty_rows(galaxy_map)
    galaxy_map = np.rot90(galaxy_map, k=-1)
    empty_cols = find_empty_rows(galaxy_map)

    new_points = []

    for point in galaxy_points:
        offset_x = sum([1 for x in empty_rows if x < point[0]])
        offset_y = sum([1 for y in empty_cols if y < point[1]])
        new_points.append((point[0]+offset_x * (multiplayer - 1),
                           point[1]+offset_y * (multiplayer - 1)))


    return new_points


def shortest_path(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


if __name__ == "__main__":
    galaxy_map = inputs
    galaxy_points = inflate_map_by(galaxy_map, 1000000)
    all_possible_pairs = list(itertools.combinations(galaxy_points, 2))
    answer = []
    for pair in all_possible_pairs:
        answer.append(shortest_path(pair[0], pair[1]))
    print(sum(answer))
