"""
--- Day 20: Trench Map ---
With the scanners fully deployed, you turn their attention to mapping the floor of the ocean trench.

When you get back the image from the scanners, it seems to just be random noise. Perhaps you can combine an image enhancement algorithm and the input image (your puzzle input) to clean it up a little.

For example:

..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
The first section is the image enhancement algorithm. It is normally given on a single line, but it has been wrapped to multiple lines in this example for legibility. The second section is the input image, a two-dimensional grid of light pixels (#) and dark pixels (.).

The image enhancement algorithm describes how to enhance an image by simultaneously converting all pixels in the input image into an output image. Each pixel of the output image is determined by looking at a 3x3 square of pixels centered on the corresponding input image pixel. So, to determine the value of the pixel at (5,10) in the output image, nine pixels from the input image need to be considered: (4,9), (4,10), (4,11), (5,9), (5,10), (5,11), (6,9), (6,10), and (6,11). These nine input pixels are combined into a single binary number that is used as an index in the image enhancement algorithm string.

For example, to determine the output pixel that corresponds to the very middle pixel of the input image, the nine pixels marked by [...] would need to be considered:

# . . # .
#[. . .].
#[# . .]#
.[. # .].
. . # # #
Starting from the top-left and reading across each row, these pixels are ..., then #.., then .#.; combining these forms ...#...#.. By turning dark pixels (.) into 0 and light pixels (#) into 1, the binary number 000100010 can be formed, which is 34 in decimal.

The image enhancement algorithm string is exactly 512 characters long, enough to match every possible 9-bit binary number. The first few characters of the string (numbered starting from zero) are as follows:

0         10        20        30  34    40        50        60        70
|         |         |         |   |     |         |         |         |
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
In the middle of this first group of characters, the character at index 34 can be found: #. So, the output pixel in the center of the output image should be #, a light pixel.

This process can then be repeated to calculate every pixel of the output image.

Through advances in imaging technology, the images being operated on here are infinite in size. Every pixel of the infinite output image needs to be calculated exactly based on the relevant pixels of the input image. The small input image you have is only a small region of the actual infinite input image; the rest of the input image consists of dark pixels (.). For the purposes of the example, to save on space, only a portion of the infinite-sized input and output images will be shown.

The starting input image, therefore, looks something like this, with more dark pixels (.) extending forever in every direction not shown here:

...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............
By applying the image enhancement algorithm to every pixel simultaneously, the following output image can be obtained:

...............
...............
...............
...............
.....##.##.....
....#..#.#.....
....##.#..#....
....####..#....
.....#..##.....
......##..#....
.......#.#.....
...............
...............
...............
...............
Through further advances in imaging technology, the above output image can also be used as an input image! This allows it to be enhanced a second time:

...............
...............
...............
..........#....
....#..#.#.....
...#.#...###...
...#...##.#....
...#.....#.#...
....#.#####....
.....#.#####...
......##.##....
.......###.....
...............
...............
...............
Truly incredible - now the small details are really starting to come through. After enhancing the original input image twice, 35 pixels are lit.

Start with the original input image and apply the image enhancement algorithm twice, being careful to account for the infinite size of the images. How many pixels are lit in the resulting image?
"""

def get_input(filename):
    """
    Takes a filename and returns a list of lines from the file
    """
    output = []
    with open(filename) as f:
        for line in f:
            tmp_line = line.strip()
            output.append(tmp_line)
    return output


def convert_image_to_2d_array(image):
    image_array = []
    for line in image:
        line_array = list(line)
        image_array.append(line_array)
    return image_array


def pad_image(image_array):
    """
    used to add a row of ... to the start and end of the image and also a . at the start and end of each line.
    """
    tmp_image = []
    for row in image_array:
        new_row = ['.'] + ['.'] + row + ['.'] + ['.']
        tmp_image.append(new_row)

    row_padding = ['.'] * len(tmp_image[0])
    tmp_image.insert(0, row_padding)
    tmp_image.insert(0, row_padding)
    tmp_image.append(row_padding)
    tmp_image.append(row_padding)

    return tmp_image


def get_cell_block(tmp_image, row, column):
    """
    Gets the cells around a point, including the point
    """
    cell_block = []
    cell_block.append(tmp_image[row - 1][column - 1])
    cell_block.append(tmp_image[row - 1][column])
    cell_block.append(tmp_image[row - 1][column + 1])

    cell_block.append(tmp_image[row][column - 1])
    cell_block.append(tmp_image[row][column])
    cell_block.append(tmp_image[row][column + 1])

    cell_block.append(tmp_image[row + 1][column - 1])
    cell_block.append(tmp_image[row + 1][column])
    cell_block.append(tmp_image[row + 1][column + 1])
    return cell_block


def is_border_cell(row_pointer, height, cell_pointer, width):
    if row_pointer == 1 or cell_pointer == 1:
        return True
    elif row_pointer + 1 == height or cell_pointer + 1 == width:
        return True
    return False


def get_new_cell_value(enhancement_algorithm, cell_block, border_cell, iteration):
    '''
    At this point, need to know if it's a 'border' cell (1,1 to len-1,len-1), if so and the value is 0 then ignore as
    otherwise we are flipping the light on/off on the infinite space around the actual image.
    '''

    binary_string = []
    for cell in cell_block:
        if cell == '.':
            binary_string.append('0')
        else:
            binary_string.append('1')
    binary_number = ''.join(binary_string)
    decimal_number = int(binary_number, 2)
    if border_cell and decimal_number == 0 and iteration > 0 and iteration % 2 == 0:
        return '.'
    new_cell_value = enhancement_algorithm[decimal_number]
    return new_cell_value


def process_image(iterations, enhancement_algorithm, image_array):
    """
    Used to apply the enhancement algorithm to image iterations number of times.
    """
    tmp_image = image_array
    for iteration in range(iterations):
        # print("<<<< Iteration " + str(iteration) + ">>>>")
        # print('IN')
        # for row in tmp_image:
        #     print(''.join(row))
        # print("tmp_image size = " + str(len(tmp_image)) + " " + str(len(tmp_image[0])))
        tmp_image = pad_image(tmp_image)

        processed_outcome = []
        for row_pointer in range(1, len(tmp_image)-1):
            processed_row = []
            for cell_pointer in range(1, len(tmp_image[row_pointer])-1):

                border_cell = is_border_cell(row_pointer, len(tmp_image)-1, cell_pointer, len(tmp_image[row_pointer])-1)

                cell_block = get_cell_block(tmp_image, row_pointer, cell_pointer)
                new_cell_value = get_new_cell_value(enhancement_algorithm, cell_block, border_cell, iteration)
                # if iteration == 1:
                #   print(str(cell_pointer) + "  " + str(row_pointer) + " " + str(border_cell) + "  " + ''.join(cell_block) + " ==> " + new_cell_value)
                processed_row.append(new_cell_value)
            processed_outcome.append(processed_row)
        tmp_image = processed_outcome

        # print('OUT')
        # for row in tmp_image:
        #     print(''.join(row))
    return tmp_image


def get_result(processed_image):
    result = 0
    for row in processed_image:
        for cell in row:
            if cell == '#':
                result += 1
    return result


if __name__ == '__main__':
    # get file content
    input_from_file = get_input('input.txt')

    # input_from_file = ['..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#',
    #                    '',
    #                    '#..#.',
    #                    '#....',
    #                    '##..#',
    #                    '..#..',
    #                    '..###']

    enhancement_algorithm = input_from_file[0]
    image = input_from_file[2:]

    print(enhancement_algorithm)
    print(image)

    image_array = convert_image_to_2d_array(image)

    processed_image_2 = process_image(2, enhancement_algorithm, image_array)

    for row in processed_image_2:
        print(''.join(row))

    result = get_result(processed_image_2)
    print("RESULT: " + str(result))
    # is it which if these that are correct:
    # 5231 (https://youtu.be/zDCLWtnW0Mg?t=1081) or
    # 5354 (https://youtu.be/pT-m7jz_zm4?t=481) or
    # 5846 (https://youtu.be/kw58sT4Ocos?t=1971)
    # 5391? 5391? 5391? -> looks like this is my solution

    processed_image_50 = process_image(50, enhancement_algorithm, image_array)

    for row in processed_image_50:
        print(''.join(row))

    result = get_result(processed_image_50)
    print("RESULT: " + str(result))
