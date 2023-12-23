# From apps
from Day01.ListProcessor import process_list


def solve(file_content):
    list = []
    for line in file_content:
        list.append(int(line))

    result = process_list(list)

    return result["increasedCount"]
