# Open the file and read it line by line
with open('day_1_1.input.txt', 'r') as file:
    result = 0
    for line in file:
        line = "".join(filter(str.isdigit, line))  # Remove everything but ints
        final_int = int("".join([line[0], line[-1]]))
        result += final_int

    print(result)