def get_paper_dimensions(folds):
    """
    takes a list of folds and co-ordinates and builds an unfolded piece of paper
    """
    max_x_fold = 0
    max_y_fold = 0
    for fold in folds:
        split_line = fold.split("=", -1)
        instruction = split_line[0]
        value = int(split_line[1])

        if value > max_x_fold and instruction == "fold along x":
            max_x_fold = value

        if value > max_y_fold and instruction == "fold along y":
            max_y_fold = value

    paper_width = (2 * max_x_fold) + 1
    paper_height = (2 * max_y_fold) + 1
    return {
        "width": paper_width,
        "height": paper_height,
    }


def get_paper(folds, input):
    """
    Create a paper given the original input based on a paper determined from the fold index.
    """
    dimensions = get_paper_dimensions(folds)

    paper_width = dimensions["width"]
    paper_height = dimensions["height"]

    y = 0
    paper = []
    while y < paper_height:
        x = 0
        row = []
        while x < paper_width:
            row.append(".")
            x += 1
        paper.append(row)
        y += 1

    # now we can go through the co-ordinates and change . to #
    for entry in input:
        paper[entry["y"]][entry["x"]] = "#"
    return paper


def fold_along_x(paper, value):
    """
    iterate through with 2 indexes
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9....
    width - (1+i)
    while i < value

    append to new list for row
    append each row
    """
    paper_height = len(paper)
    paper_width = len(paper[0])

    y = 0
    folded_paper = []
    while y < paper_height:
        x = 0
        row = []
        while x < value:
            right_x = paper_width - (1 + x)
            left = paper[y][x]
            right = paper[y][right_x]

            cell_value = "#" if left.__eq__("#") or right.__eq__("#") else "."
            row.append(cell_value)
            x += 1
        folded_paper.append(row)
        y += 1
    return folded_paper


def fold_along_y(paper, value):
    """
    iterate through with 2 indexes
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9....
    height - (1+i)
    while i < value

    append to new list for row
    append each row
    """
    paper_height = len(paper)
    paper_width = len(paper[0])

    y = 0
    folded_paper = []
    while y < value:
        x = 0
        row = []
        while x < paper_width:
            bottom_y = paper_height - (1 + y)
            top = paper[y][x]
            bottom = paper[bottom_y][x]

            cell_value = "#" if top.__eq__("#") or bottom.__eq__("#") else "."
            row.append(cell_value)
            x += 1
        folded_paper.append(row)
        y += 1

    return folded_paper


def process_folds(folds, paper):
    """
    process the folds, iterating through the folds list doing the fold each time
    """
    final_board = paper
    for fold in folds:
        split_line = fold.split("=", -1)
        instruction = split_line[0]
        value = int(split_line[1])

        if instruction == "fold along x":
            final_board = fold_along_x(final_board, value)

        if instruction == "fold along y":
            final_board = fold_along_y(final_board, value)

    return final_board


def count_marks(paper):
    """
    count the number of squares that contain #
    """
    paper_height = len(paper)
    paper_width = len(paper[0])

    y = 0
    hash_count = 0
    while y < paper_height:
        x = 0
        while x < paper_width:
            cell_value = paper[y][x]
            if "#" == cell_value:
                hash_count += 1
            x += 1
        y += 1
    return hash_count


def print_paper(folded_paper):
    for row in folded_paper:
        print(row)


def solve(file_content):
    input = []
    folds = []
    processing_input = True
    for file_line in file_content:
        if len(file_line) == 0:
            processing_input = False
            continue

        if processing_input:
            char_list = file_line.split(",", -1)
            char_mapped_to_int = map(int, char_list)
            row = list(char_mapped_to_int)

            entry = {
                "x": row[0],
                "y": row[1],
            }

            input.append(entry)
            continue

        folds.append(file_line)

    paper = get_paper(folds, input)
    folded_paper = process_folds(folds, paper)
    # print_paper(folded_paper)
    marks = count_marks(folded_paper)
    return marks
