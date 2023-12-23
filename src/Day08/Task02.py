"""
convert segments to a 2n value, used for generating unique values for numbers
"""
segment_value = {
    "t": 1,
    "tl": 2,
    "tr": 4,
    "m": 8,
    "bl": 16,
    "br": 32,
    "b": 64,
}


"""
map a number total to a value for the number
"""
number_total = {
    "119": 0,
    "36": 1,
    "93": 2,
    "109": 3,
    "46": 4,
    "107": 5,
    "123": 6,
    "37": 7,
    "127": 8,
    "111": 9,
}


def get_t(input_list):
    two_char_entry = ""
    three_char_entry = ""
    for input in input_list:
        if len(input) == 2:
            two_char_entry = input
        if len(input) == 3:
            three_char_entry = input

    for char in list(two_char_entry):
        three_char_entry = three_char_entry.replace(char, "")

    t = "".join(three_char_entry)

    return t


def get_b(input_list, t):
    b = ""
    four_char_entry = []
    six_char_entries = []
    for input in input_list:
        if len(input) == 4:
            four_char_entry = list(input)
        if len(input) == 6:
            six_char_entries.append(input)

    # almost 9, missing b
    four_char_entry.append(t)

    for six_char_entry in six_char_entries:
        six_char_entry_list = list(six_char_entry)
        for char in four_char_entry:
            if six_char_entry_list.__contains__(char):
                six_char_entry_list.remove(char)
            else:
                break
        if len(six_char_entry_list) == 1:
            b = "".join(six_char_entry_list)
            break

    return b


def get_bl(input_list, t, b):
    bl = ""
    four_char_entry = []
    seven_char_entry = []
    for input in input_list:
        if len(input) == 4:
            four_char_entry = list(input)
        if len(input) == 7:
            seven_char_entry = list(input)

    # 9
    four_char_entry.append(t)
    four_char_entry.append(b)

    for char in four_char_entry:
        if seven_char_entry.__contains__(char):
            seven_char_entry.remove(char)

    if len(seven_char_entry) == 1:
        bl = "".join(seven_char_entry)
    else:
        print("SOMETHING GONE WRONG")

    return bl


def get_tl(input_list, b, bl):
    tl = ""
    three_char_entry = []
    six_char_entries = []
    for input in input_list:
        if len(input) == 3:
            three_char_entry = list(input)
        if len(input) == 6:
            six_char_entries.append(input)

    # almost 0, missing tl
    three_char_entry.append(b)
    three_char_entry.append(bl)

    for six_char_entry in six_char_entries:
        six_char_entry_list = list(six_char_entry)
        for char in three_char_entry:
            if six_char_entry_list.__contains__(char):
                six_char_entry_list.remove(char)
            else:
                break
        if len(six_char_entry_list) == 1:
            tl = "".join(six_char_entry_list)
            break
    return tl


def get_m(input_list, tl):
    m = ""
    two_char_entry = ""
    four_char_entry = ""
    six_char_entries = []
    for input in input_list:
        if len(input) == 2:
            two_char_entry = input
        if len(input) == 4:
            four_char_entry = input
        if len(input) == 6:
            six_char_entries.append(input)

    for char in list(two_char_entry):
        four_char_entry = four_char_entry.replace(char, "")
    m = four_char_entry.replace(tl, "")
    return m


def get_br(input_list, t, b, bl, tl, m):
    br = ""
    six_char_entries = []
    for input in input_list:
        if len(input) == 6:
            six_char_entries.append(input)

    almost_six = [t, b, bl, tl, m]

    for six_char_entry in six_char_entries:
        six_char_entry_list = list(six_char_entry)
        for char in almost_six:
            if six_char_entry_list.__contains__(char):
                six_char_entry_list.remove(char)
            else:
                break
        if len(six_char_entry_list) == 1:
            br = "".join(six_char_entry_list)
            break

    return br


def get_tr(input_list, br):
    tr = ""
    two_char_entry = ""
    for input in input_list:
        if len(input) == 2:
            two_char_entry = input

    tr = two_char_entry.replace(br, "")

    return tr


def process_input(input_list):
    """
    takes an input list and converts to a configuration mapping a letter to a segment
    """
    t = get_t(input_list)
    b = get_b(input_list, t)
    bl = get_bl(input_list, t, b)
    tl = get_tl(input_list, b, bl)
    m = get_m(input_list, tl)
    br = get_br(input_list, t, b, bl, tl, m)
    tr = get_tr(input_list, br)
    return {
        str(t): "t",
        str(tl): "tl",
        str(tr): "tr",
        str(m): "m",
        str(bl): "bl",
        str(br): "br",
        str(b): "b",
    }


def convert_output(config, output_list):
    """
    takes an encoded output and converts to a number list
    """
    return_value = []
    for output_entry in output_list:
        letters = list(output_entry)

        word_total = 0
        for letter in letters:
            position = config[letter]
            word_total = word_total + segment_value[position]
        number = number_total[str(word_total)]
        return_value.append(str(number))

    return return_value


def solve(file_content):
    output_list_total = 0
    for file_entry in file_content:
        input_output = file_entry.split("|", -1)
        input_list = input_output[0].split()
        output_list = input_output[1].split()

        config = process_input(input_list)

        decoded_output_list = convert_output(config, output_list)
        joined_decoded_output_list = "".join(decoded_output_list)
        output_list_total = output_list_total + int(joined_decoded_output_list)
    return output_list_total
