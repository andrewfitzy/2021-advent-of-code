def process_list(list):
    length = len(list)
    i = 0

    increasedCount = 0
    decreasedCount = 0
    sameCount = 0

    while i < length:
        if i == 0:
            print("Start")
        elif list[i] < list[i - 1]:
            print("Decrease")
            decreasedCount += 1
        elif list[i] > list[i - 1]:
            print("Increase")
            increasedCount += 1
        else:
            print("Same")
            sameCount += 1

        i += 1

    return {
        "increasedCount": increasedCount,
        "decreasedCount": decreasedCount,
        "sameCount": sameCount
    }
