# Standard Library
import re

PAIR_PATTERN = re.compile("\\[[0-9]+,[0-9]+\\]")
MULTIDIGIT_PATTERN = re.compile("[0-9]{2,}")
WHOLE_NUMBER_PATTERN = re.compile("[0-9]+")


def solve(file_content):
    max_magnitude = 0
    for i in range(len(file_content)):
        for j in range(len(file_content)):
            if i == j:
                continue
            sum = add(file_content[i], file_content[j])
            reduced_number = reduce(sum)
            magnitude = calculate_magnitude(reduced_number)
            if magnitude > max_magnitude:
                max_magnitude = magnitude

    return max_magnitude


def add(input01, input02):
    return "[{input01},{input02}]".format(input01=input01, input02=input02)


def reduce(input):
    input_copy = str(input)

    # repeat reduce until the input "number" is fully reduced
    fully_reduced = False
    while not fully_reduced:
        # check if it needs exploding, explode once and then continue
        if needs_exploding(input_copy):
            input_copy = explode(input_copy)
            continue

        # check if it needs splitting, split once and then continue
        if needs_splitting(input_copy):
            input_copy = split(input_copy)
            continue

        # If we get here we didn't need to explode and didn't need to split so we're reduced
        fully_reduced = True

    return input_copy


def needs_exploding(input):
    # go through, if we get to 5 items in the stack we explode
    counter = 0
    for character in input:
        if counter >= 5:
            return True
        if "[" == character:
            counter = counter + 1
        if "]" == character:
            counter = counter - 1

    return False


def add_to_previous_num(number, input):
    # find next number
    match = None
    for match in WHOLE_NUMBER_PATTERN.finditer(input):
        continue

    if not match:
        return input

    to_insert = int(match.group()) + int(number)

    left = input[: match.start()]
    right = input[match.end() :]

    result = "{left}{to_insert}{right}".format(left=left, to_insert=to_insert, right=right)

    return result


def add_to_next_num(number, input):
    # find next number
    match = None
    for match in WHOLE_NUMBER_PATTERN.finditer(input):
        break

    if not match:
        return input

    to_insert = int(match.group()) + int(number)

    left = input[: match.start()]
    right = input[match.end() :]

    result = "{left}{to_insert}{right}".format(left=left, to_insert=to_insert, right=right)

    return result


def explode(input):
    # go through, explode left most match
    counter = 0
    pointer = 0
    for character in input:
        if counter >= 5:
            end_pointer = input.find("]", pointer)

            # need to minus and plus 1 to capture the []
            start = pointer - 1
            end = end_pointer + 1

            # check that it's a range, if so break, else continue,
            check_range = input[start:end]

            if PAIR_PATTERN.match(check_range):
                explode_range = (start, end)
                break
        if "[" == character:
            counter = counter + 1
        if "]" == character:
            counter = counter - 1
        pointer = pointer + 1

    if not explode_range:
        raise Exception("Can't find the number that needs exploding")

    left = input[: explode_range[0]]
    right = input[explode_range[1] :]

    pair_left, pair_right = input[explode_range[0] : explode_range[1]].replace("[", "").replace("]", "").split(",")

    result_left = add_to_previous_num(pair_left, left)
    result_right = add_to_next_num(pair_right, right)

    # concat
    result = "{result_left}0{result_right}".format(result_left=result_left, result_right=result_right)

    #  now how to explode?
    return result


def needs_splitting(input):
    # need to find consecutive numbers and check if they are greater than 10
    result = MULTIDIGIT_PATTERN.search(input)
    if result:
        return True
    return False


def split(input):
    # go through, split left most match
    result = MULTIDIGIT_PATTERN.search(input)
    if not result:
        raise Exception("Can't find the number that needs splitting")

    # get the number to split as an int then perform the maths
    number_to_split = int(input[result.start() : result.end()])
    left = number_to_split // 2
    right = number_to_split - left

    # get the right and left strings around the original number
    start = input[: result.start()]
    end = input[result.end() :]

    # concat it all together and return
    new_string = "{start}[{left},{right}]{end}".format(start=start, left=left, right=right, end=end)
    return new_string


def calculate_magnitude(input):
    # find pairs
    pairs = list(PAIR_PATTERN.finditer(input))

    # if not a pair, it's a number so return it
    if not pairs:
        return int(input)

    # for each pair, starting from end
    for pair in pairs[::-1]:
        # calculate the magnitude
        left, right = pair.group().replace("[", "").replace("]", "").split(",")
        value = int(left) * 3 + int(right) * 2

        # find where our pair was
        start = input[: pair.start()]
        end = input[pair.end() :]

        # replace our pair with our number
        input = "{start}{value}{end}".format(start=start, value=value, end=end)

        return calculate_magnitude(input)

    raise ValueError(f"cannot parse snailfish number: {input}")
