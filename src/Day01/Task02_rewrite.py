# From apps
from Day01.ListProcessor import process_list


def solve(file_content):
    list = []
    for line in file_content:
        list.append(int(line))

    # Firstly process the list into a list of sums of 3 values, e.g.
    # given 149, 163, 165, 160, 179
    # then there is a list with values:
    # 477
    # 488
    # 504
    length = len(list)
    totalValuesList = []
    recordIndex = 0
    while recordIndex < length:
        if recordIndex + 2 == length:
            break
        value = list[recordIndex] + list[recordIndex + 1] + list[recordIndex + 2]
        totalValuesList.append(value)
        recordIndex += 1

    result = process_list(totalValuesList)

    return result["increasedCount"]
