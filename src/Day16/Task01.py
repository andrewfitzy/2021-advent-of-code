# From apps
from src.util.timer import Timer


def get_input(filename):
    """
    Takes a filename and returns a list of lines from the file
    """
    output = []
    with open(filename) as f:
        for line in f:
            tmp_line = line.strip()
            output.append(tmp_line)
    return output


def get_version(input_as_binary):
    tmp_version = input_as_binary.pop()
    print(tmp_version)
    return 1


def get_type(input_as_binary):
    return 1


def process_reading(input_from_file):
    """
    convert to binary
    """
    input_as_integer = int(input_from_file, 16)
    input_as_binary = bin(input_as_integer)[2:]
    input_as_binary_list = list(input_as_binary)
    while len(input_as_binary_list) != 0:
        version = input_as_binary_list[:3]
        input_as_binary_list = input_as_binary_list[3:]

        type = input_as_binary_list[:3]
        input_as_binary_list = input_as_binary_list[3:]

        decimal_version = int("".join(version), 2)
        decimal_type = int("".join(type), 2)
        print("Type: " + str(decimal_type) + " Version: " + str(decimal_version))

        print(decimal_type)
        if decimal_type == 1:
            print("Type 1")
        elif decimal_type == 4:
            prefix = 1
            while prefix == 1:
                literal = input_as_binary_list[:5]
                print(literal)
                input_as_binary_list = input_as_binary_list[5:]

                prefix = literal[0]
        else:
            print("UNKNOWN TYPE: " + str(type))

        """
        need to iterate through the number, popping
        get 3 chars, this is version
        put version in a list
        get 3 chars, this is type
            process type X - nasty ifs but will do the job - would usually invert... actually no, will create classes with
            process and a class for each type.
            process type y etc etc
        do we care about the rest... understand and popuntil the next version
        """
    print(input_as_binary)
    return 2012


def process_file(filename, expected_result, print_result):
    """
    Given a file and an expected result, process the file and see if the result is as expected
    """
    t = Timer()
    t.start()
    input_from_file = get_input(filename)

    assert len(input_from_file) == 1, "Input " + filename + " should contain only one line"

    result = process_reading(input_from_file[0])

    if print_result:
        print("result")

    result = 0
    assert result == expected_result, (
        "Output is not as expected, expected " + str(expected_result) + " but got " + str(result)
    )

    print("RESULT: there are " + str(result) + " paths for input " + filename)
    t.stop()


if __name__ == "__main__":
    process_file("input_example00.txt", 16, False)
    process_file("input_example01.txt", 16, False)
    process_file("input_example02.txt", 12, False)
    process_file("input_example03.txt", 23, False)
    process_file("input_example04.txt", 31, False)
    process_file("input.txt", 1, False)
