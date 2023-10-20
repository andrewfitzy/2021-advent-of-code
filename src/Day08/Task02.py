"""
--- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
"""

"""
get the letters for a 1
get the letters for a 7
* the difference is the top so can work out the letter for top
get the letters for 4
the difference between 4 and 7 gives middle and top left
* letters for 4 and 7 are 1 away from 9 so can find out what bottom is
* once we have 9, the difference between that and 8 is bottom left
* get the other 6 letter codes, take away 1, top, bottom, bottom left, gives top left
* using 4, take away 1 to give the middle
* find 6 letter code, take away top, bottom, bottom left, top left, middle
"""


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


def get_file_content(filename):
    """
    Takes a filename and returns a list of ints from the file
    """
    output = []
    with open(filename) as f:
        for line in f:
            output.append(line.strip())
    return output


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


if __name__ == "__main__":
    # get file content
    file_content = get_file_content("input.txt")

    output_list_total = 0
    for file_entry in file_content:
        input_output = file_entry.split("|", -1)
        input_list = input_output[0].split()
        output_list = input_output[1].split()

        config = process_input(input_list)
        output = convert_output(config, output_list)

        decoded_output_list = convert_output(config, output_list)
        joined_decoded_output_list = "".join(decoded_output_list)
        output_list_total = output_list_total + int(joined_decoded_output_list)
    print(output_list_total)
