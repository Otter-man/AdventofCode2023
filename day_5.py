import copy
import datetime
import multiprocessing as mp
from multiprocessing import Pool


with open("inputs/day_5_input.txt") as f:
    inputs = f.readlines()

def parse_input(inputs):
    line_list = []
    category_list = []
    for c, line in enumerate(inputs):
        if line == "\n":
            line_list.append(category_list)
            category_list = []
            continue

        category_list.append(line)

    line_list.append(category_list)
    category_list = []

    for c, line in enumerate(line_list):
        if c == 0:
            line = [int(seed) for seed in line[0].split(":")[1].split() if seed]
        else:
            line = "".join(line[1:]).split("\n")
            line = [[int(i) for i in address.split()] for address in line if address]

        category_list.append(line)

    return category_list



def format_ranges(category_list):
    for c, entry in enumerate(category_list):
        if c == 0: continue

        for cc, range in enumerate(category_list[c]):
            destination_start = range[0]
            destination_end = range[0] + range[2] - 1
            source_start = range[1]
            source_end = range[1] + range[2] - 1
            category_list[c][cc] = [source_start, source_end, destination_start, destination_end]



    return category_list

def smallest_location(category_list):
    seeds = category_list[0]
    destination = 0
    for seed in seeds:
        chain_map = []
        for c, entry in enumerate(category_list[1:]):
            chain_map.append(seed)
            # map_chain.append(seed)
            for line in category_list[1:][c]:
                if seed >= line[0] and seed <= line[1]:
                    seed = seed + line[2] - line[0]
                    break
        if seed < destination or destination == 0:
            destination = seed
    return destination

def smallest_location_range(category_list):
    # print timestamp
    print(datetime.datetime.now())
    seeds = get_seed_ranges(category_list[0])
    location_number = 0
    while location_number < 100000000000:
        seed = location_number

        for c, entry in enumerate(category_list[1:]):
            # map_chain.append(seed)
            for line in category_list[1:][c]:
                if seed >= line[0] and seed <= line[1]:
                    seed = seed + line[2] - line[0]
                    break
        for seed_range in seeds:
            if seed_range[0] <= seed <= seed_range[1]:
                print(datetime.datetime.now())
                return location_number
        location_number += 1

    return location_number


def get_seed_ranges(seeds):
    all_seeds = []
    for c, seed in enumerate(seeds):
        if c % 2 == 0:
            all_seeds.append([seed, seed+seeds[c+1]])

    return all_seeds

def reverse_category(category_list):
    reversed_list = copy.deepcopy(category_list)
    reversed_list.reverse()
    seed = reversed_list.pop(-1)
    reversed_list.insert(0, seed)
    for c, line in enumerate(reversed_list):
        if c == 0: continue
        for cc, item in enumerate(reversed_list[c]):
            reversed_list[c][cc] = [item[2], item[3], item[0], item[1]]

    return reversed_list


if __name__ == '__main__':
    category_list = parse_input(inputs)
    category_list = format_ranges(category_list)
    part1 = smallest_location(category_list)
    category_list_reversed = reverse_category(category_list)
    seeds = get_seed_ranges(category_list_reversed[0])

    part2 = smallest_location_range(category_list_reversed) ## takes around 4 minutes
    print(part1)
    print(part2)
