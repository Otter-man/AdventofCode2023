from collections import Counter

with open('inputs/day_9_input.txt') as f:
    inputs = f.readlines()

with open('inputs/day_9_test.txt') as f:
    test = f.readlines()


def prepare_line_for_prediction(line, all_lines):

    new_line = []

    for c, i in enumerate(line):
        try:
            new_line.append(line[c+1] - line[c])
        except IndexError:
            break

    if new_line:
        all_lines.append(new_line)
    zero_check = Counter(i for i in new_line)
    if zero_check[0] != len(new_line):
        return prepare_line_for_prediction(new_line, all_lines)
    else:
        return all_lines


def predict_ending(all_lines):
    for i in range(1, len(all_lines)+1):
        try:
            prev = all_lines[-i-1][-1]
            prediction = all_lines[-i][-1]
            all_lines[-i-1].append(prev+prediction)
            pass
        except IndexError:
            break
    return all_lines[0][-1]


def part_1(inputs):
    answer = []
    all_lines = []
    for line in inputs:
        line = [int(i) for i in line.split()]
        all_lines.append(line)
        prepare_line_for_prediction(line, all_lines)
        answer.append(predict_ending(all_lines))
        all_lines = []

    return sum(answer)


if __name__ == "__main__":
    print(part_1(inputs))