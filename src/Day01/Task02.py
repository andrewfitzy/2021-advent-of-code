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

    # now process our list using the code from Task01 - duplicated here
    length = len(totalValuesList)
    i = 1

    increasedCount = 0
    decreasedCount = 0
    sameCount = 0

    while i < length:
        if totalValuesList[i] < totalValuesList[i - 1]:
            decreasedCount += 1
        elif totalValuesList[i] > totalValuesList[i - 1]:
            increasedCount += 1
        else:
            sameCount += 1

        i += 1

    return increasedCount
