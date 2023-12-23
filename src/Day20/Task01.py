LIGHT_PIXEL = "#"
DARK_PIXEL = "."


def convert_image_to_2d_array(image):
    """
    takes the raw bitmap image and converts into a 2d array of values.
    """
    image_array = []
    for line in image:
        line_array = list(line)
        image_array.append(line_array)
    return image_array


def pad_image(image_array, pad_char):
    """
    used to add a row of ... to the start and end of the image and also a . at the start and end of each line.
    """
    tmp_image = []
    for row in image_array:
        new_row = [pad_char] + [pad_char] + row + [pad_char] + [pad_char]
        tmp_image.append(new_row)

    row_padding = [pad_char] * len(tmp_image[0])
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


def get_new_cell_value(enhancement_algorithm, cell_block):
    """
    Convert the cell block to a binary number and find the location in the codex to know what the new cell value will be
    """
    binary_string = []
    for cell in cell_block:
        if cell == DARK_PIXEL:
            binary_string.append("0")
        else:
            binary_string.append("1")
    binary_number = "".join(binary_string)
    decimal_number = int(binary_number, 2)
    new_cell_value = enhancement_algorithm[decimal_number]
    return new_cell_value


def is_blinking_image(enhancement_algorithm):
    """
    convenience method to work out if the codec causes the image to blink. By default, the infinite space around the
    image contains . but if position 0 in the codec converts to # it means after the first iteration the infinite space
    will contain #, this gets flipped again on the next iteration if the codec contains . at position 511.
    """
    return (
        enhancement_algorithm[0] == LIGHT_PIXEL and enhancement_algorithm[len(enhancement_algorithm) - 1] == DARK_PIXEL
    )


def get_pad_char(default_infinite_char, is_blinking, iteration):
    """
    convenience method to work out what the pad char should be around the given image. This will indicate that the
    infinite space should wither be dark or light. If it's identified that the codec causes the space to blink, then
    depending on the default for the infinite space, and the iteration number, this could return the default or the
    opposite value.
    """
    pad_char = default_infinite_char
    if is_blinking and iteration % 2 == 1:
        # blinking and an odd numbered iteration so flip the pad char
        pad_char = LIGHT_PIXEL if default_infinite_char == DARK_PIXEL else DARK_PIXEL
    return pad_char


def process_image(iterations, enhancement_algorithm, image_array):
    """
    Used to apply the enhancement algorithm to image iterations number of times.
    """
    is_blinking = is_blinking_image(enhancement_algorithm)

    tmp_image = image_array
    for iteration in range(iterations):
        pad_char = get_pad_char(DARK_PIXEL, is_blinking, iteration)
        tmp_image = pad_image(tmp_image, pad_char)

        processed_outcome = []
        for row_pointer in range(1, len(tmp_image) - 1):
            processed_row = []
            for cell_pointer in range(1, len(tmp_image[row_pointer]) - 1):
                cell_block = get_cell_block(tmp_image, row_pointer, cell_pointer)
                new_cell_value = get_new_cell_value(enhancement_algorithm, cell_block)
                processed_row.append(new_cell_value)
            processed_outcome.append(processed_row)
        tmp_image = processed_outcome
    return tmp_image


def get_result(processed_image):
    """
    analyse the processed image, counting the lit pixels
    """
    result = 0
    for row in processed_image:
        for cell in row:
            if cell == LIGHT_PIXEL:
                result += 1
    return result


def solve(file_content, enhancement_iterations):
    """
    Given a file, a number of enhancement iterations and an expected result, process the file based on the inputs and
    assert that the result is as expected
    """
    enhancement_algorithm = file_content[0]
    image = file_content[2:]

    image_array = convert_image_to_2d_array(image)

    processed_image = process_image(enhancement_iterations, enhancement_algorithm, image_array)

    result = get_result(processed_image)

    return result
