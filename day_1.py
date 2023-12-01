# Here we have a dictionary that maps strings of spelled-out numbers to their integer counterparts
NUMBERS_DICT = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def extract_digits(line):
    """
    This function removes all non-numeric characters from the input string and returns the result.
    :param line: A string from which to remove all non-numeric characters
    :return: A string containing only the digits from the input string
    """
    line = "".join(filter(str.isdigit, line))  # Remove everything but integers
    return line


def sum_all_results(lines):
    """
    This function calculates the sum of the first and last integer from each line in the input list.
    :param lines: A list of strings to extract integers from
    :return: An integer which is the sum of all extracted integers from each line
    """
    result = 0
    for line in lines:
        line = add_spelled_digits_to_the_line(line)  # Add numerical values before spelled-out digits
        digits = extract_digits(line)  # Extract all digits from the line
        final_int = int("".join([digits[0], digits[-1]]))  # Join the first and last digit and convert to integer
        result += final_int  # Add the integer to the result
    return result


def add_spelled_digits_to_the_line(line):
    """
    This method processes a line of string, it adds numerical digits next to each occurrence of the spelled-out digit in the line.
    :param line: The string line to be processed.
    :return: The line with spelled-out digits with numerical digits added.
    """
    line_index = dict()
    for spelling, digit in NUMBERS_DICT.items():
        if spelling in line:
            # find spelled out characters in line
            occurrences_dict = dict((i, spelling) for i in find_occurrences(line, spelling))  # Map each occurrence to its index
            line_index.update(occurrences_dict)  # Update line_index with the occurrence index
    line_index = {k: line_index[k] for k in sorted(line_index)}  # Sort line_index so changes happen from left to right

    while line_index:  # While there are items in line_index
        index = next(iter(line_index))  # Get the leftmost index
        spelling = line_index.pop(index)  # Remove and get the spelled out character at the current index
        line = line[:index] + NUMBERS_DICT[spelling] + line[index:]  # Insert the numeric equivalent of the spelled-out character into the line
        line_index = {index+1: spelling for index, spelling in line_index.items()}  # +1 each index in line_index items to account for inserted char
    print(line)
    return line


def find_occurrences(line, spelling):
    """
    This function yields the index of each occurrence of a spelling in the line.
    :param line: A string to find the spelled out characters in
    :param spelling: A spelled out number to find in the line
    :return: A generator that yields the index of each occurrence of the spelled out number
    """
    start = 0
    while True:
        start = line.find(spelling, start)  # Find next occurrence of spelling
        if start == -1:
            return  # If spelling is not in line, stop
        yield start  # Yield the current occurrence position
        start += len(spelling)  # Move start index past the current occurrence


# Open the file, read the lines into a list, and then print the sum of the results
with open("inputs/day_1_input.txt") as f:
    print(sum_all_results(f.readlines()))
    