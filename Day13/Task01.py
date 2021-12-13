"""
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?

Your puzzle answer was 704.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?
"""


def get_input(filename):
    """
    Takes a filename and returns a list of co-ordinates from the file
    """
    output = []
    with open(filename) as f:
        for line in f:
            tmp_line = line.strip()
            char_list = tmp_line.split(',', -1)
            char_mapped_to_int = map(int, char_list)
            row = list(char_mapped_to_int)

            entry = {
                'x': row[0],
                'y': row[1],
            }

            output.append(entry)
    return output


def get_folds(filename):
    """
    Takes a filename and returns a list of folds from the file
    """
    output = []
    with open(filename) as f:
        for line in f:
            fold = line.strip()
            output.append(fold)
    return output



def get_paper_dimensions(folds):
    """
    takes a list of folds and co-ordinates and builds an unfolded piece of paper
    """
    max_x_fold = 0
    max_y_fold = 0
    for fold in folds:
        split_line = fold.split('=', -1)
        instruction = split_line[0]
        value = int(split_line[1])

        if value > max_x_fold and instruction == 'fold along x':
            max_x_fold = value

        if value > max_y_fold and instruction == 'fold along y':
            max_y_fold = value

    paper_width = (2 * max_x_fold) + 1
    paper_height = (2 * max_y_fold) + 1
    return {
        'width': paper_width,
        'height': paper_height,
    }


def get_paper(folds, input):
    """
    Create a paper given the original input based on a paper determined from the fold index.
    """
    dimensions = get_paper_dimensions(folds)

    paper_width = dimensions['width']
    paper_height = dimensions['height']

    y = 0
    paper = []
    while y < paper_height:
        x = 0
        row = []
        while x < paper_width:
            row.append('.')
            x += 1
        paper.append(row)
        y += 1

    # now we can go through the co-ordinates and change . to #
    for entry in input:
        paper[entry['y']][entry['x']] = '#'
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

    print('folding X height: ' + str(paper_height) + ' width: ' + str(paper_width) + ' value: ' + str(value))

    y = 0
    folded_paper = []
    while y < paper_height:
        x = 0
        row = []
        while x < value:
            right_x = paper_width - (1 + x)
            left = paper[y][x]
            right = paper[y][right_x]

            cell_value = '#' if left.__eq__('#') or right.__eq__('#') else '.'
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

    print('folding Y height: ' + str(paper_height) + ' width: ' + str(paper_width) + ' value: ' + str(value))

    y = 0
    folded_paper = []
    while y < value:
        x = 0
        row = []
        while x < paper_width:
            bottom_y = paper_height - (1 + y)
            top = paper[y][x]
            bottom = paper[bottom_y][x]

            cell_value = '#' if top.__eq__('#') or bottom.__eq__('#') else '.'
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
        split_line = fold.split('=', -1)
        instruction = split_line[0]
        value = int(split_line[1])

        if instruction == 'fold along x':
            final_board = fold_along_x(final_board, value)

        if instruction == 'fold along y':
            final_board = fold_along_y(final_board, value)

    return final_board


def count_marks(paper):
    """
    count the number of squares that contain #
    """
    paper_height = len(paper)
    paper_width = len(paper[0])

    print('Count board height: ' + str(paper_height) + ' width: ' + str(paper_width))
    y = 0
    hash_count = 0
    while y < paper_height:
        x = 0
        while x < paper_width:
            cell_value = paper[y][x]
            if '#' == cell_value:
                hash_count += 1
            x += 1
        y += 1
    return hash_count


def print_paper(folded_paper):
    for row in folded_paper:
        print(row)


if __name__ == '__main__':
    """
    Read in first x fold - x = 2x + 1
    Read in first y fold - y = 2y + 1
    build an array seeded with .
    go through co-ords flipping . to #

    """
    folds = get_folds('folds.txt')
    input = get_input('input.txt')

    paper = get_paper(folds, input)

    print('First board: ' + str(count_marks(paper)))

    folded_paper = process_folds(folds, paper)

    marks = count_marks(folded_paper)
    print('marks_count: ' + str(count_marks(folded_paper)))

    print_paper(folded_paper)
