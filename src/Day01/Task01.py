def solve(file_content):
    list = []
    for line in file_content:
        list.append(int(line))

    length = len(list)
    i = 1

    increasedCount = 0
    decreasedCount = 0
    sameCount = 0

    while i < length:
        if list[i] < list[i - 1]:
            decreasedCount += 1
        elif list[i] > list[i - 1]:
            increasedCount += 1
        else:
            sameCount += 1

        i += 1

    return increasedCount
