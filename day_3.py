def solve_part1(filepath):
    all_parts_numbers = []

    all_lines = dict()
    with open (filepath, "r") as f:
        for line_no, line in enumerate(f, start=1):
            all_lines[line_no] = line.strip()

    all_digits = []
    for line_ind, line in all_lines.items():
        line = index_character(line)
        all_lines[line_ind] = line

    for line_ind in all_lines:
        digits = find_numbers(all_lines[line_ind], line_ind)
        if digits:
            all_digits.extend(digits)
            parts_number = validate_digits(all_lines, digits)
            all_parts_numbers.extend(parts_number)

    sum_of_parts = sum([int(i["strings"]) for i in all_parts_numbers])
    return [sum_of_parts,all_digits, all_lines]

def solve_part2(all_digits, all_lines):
    all_gears = []
    for line_ind in all_lines:
        for char_ind in all_lines[line_ind]:
            if all_lines[line_ind][char_ind] == "*":
                all_gears.append({"line": line_ind,
                                  "char_index": char_ind})

    adjacent_parts = validate_gears(all_gears, all_lines, all_digits)

    return sum(adjacent_parts)



def validate_gears(all_gears, all_lines, all_digits):
    all_adjacent_parts = []

    for gear in all_gears:
        adjacent_parts = []
        gear_line = gear["line"]
        gear_index = gear["char_index"]

        index_to_check = [{"line": gear_line - 1, "range": [gear_index - 1, gear_index, gear_index + 1]},
                          {"line": gear_line, "range": [gear_index - 1, gear_index + 1]},
                          {"line": gear_line + 1, "range": [gear_index - 1, gear_index, gear_index + 1]}]

        for item in index_to_check:
            line_ind = item["line"]
            if line_ind in all_lines:
                for ind in item["range"]:
                    if ind in all_lines[line_ind]:
                        if all_lines[line_ind][ind].isdigit():
                            digit = find_digit(all_digits, line_ind, ind)
                            if digit not in adjacent_parts:
                                adjacent_parts.append(digit)

        if adjacent_parts and len(adjacent_parts) == 2:
            power_of_two = int(adjacent_parts[0]["strings"]) * int(adjacent_parts[1]["strings"])
            all_adjacent_parts.append(power_of_two)

    return all_adjacent_parts



def find_digit(all_digits, line_ind, ind):
    all_digits_on_line = [digit for digit in all_digits if digit["line"] == line_ind]
    digit_with_index = [digit for digit in all_digits_on_line if ind in digit["range"]]
    return digit_with_index[0]

def validate_digits(all_lines, digits):
    parts_number = []
    for digit in digits:
        line = digit["line"]
        ind_range = digit["range"]

        index_to_check = [{"line": line-1, "range": [ind_range[0]-1, *ind_range, ind_range[-1]+1]},
                          {"line": line, "range": [ind_range[0]-1, ind_range[-1]+1]},
                          {"line": line+1, "range": [ind_range[0] - 1, *ind_range, ind_range[-1]+1]}]

        for item in index_to_check:
            line_ind = item["line"]
            if line_ind in all_lines:
                for ind in item["range"]:
                    if ind in all_lines[line_ind]:
                        if check_if_symbol(all_lines[line_ind][ind]):
                            if digit not in parts_number:
                                parts_number.append(digit)

    return parts_number

def index_character(line):
    return {char_ind: char for char_ind, char in enumerate(line, start=0)}

def find_numbers(ref_line, ref_line_ind):
    digits = list()
    number = []
    for char_ind in ref_line:
        if ref_line[char_ind].isnumeric():
            number.append([char_ind, ref_line[char_ind]])
        else:
            if number:
                integers = [i[0] for i in number]
                strings = "".join([i[1] for i in number])
                digits.append({"line": ref_line_ind, "range": integers, "strings": strings})
            number = []

    return digits


def check_if_symbol(char):
    if char.isalnum() or char == ".":
        return False
    else:
        return True


if __name__ == "__main__":
    part1, all_digits, all_lines = solve_part1("inputs/day_3_input.txt")
    part2 = solve_part2(all_digits, all_lines)
    print(part2)