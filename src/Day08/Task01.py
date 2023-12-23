def get_output_values(file_content):
    """
    Takes a filename and returns a list of ints from the file
    """
    output = []
    for line in file_content:
        char_list = line.split("|", -1)
        output_list = char_list[1].split()
        output = output + output_list
    return output


def solve(file_content):
    # get file content
    output_values = get_output_values(file_content)
    output_summary = {}
    for output_value in output_values:
        current_value_length = str(len(output_value))
        current_value_count = output_summary.get(current_value_length, 0)
        current_value_count += 1
        output_summary[current_value_length] = current_value_count

    return output_summary["2"] + output_summary["3"] + output_summary["4"] + output_summary["7"]
