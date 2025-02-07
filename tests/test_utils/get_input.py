# Standard Library
import pathlib


def get_input(filename):
    """
    Takes a filename and returns a list of lines from the file
    """
    output = []
    current_working_directory = pathlib.Path().cwd()
    filename_splits = filename.split("/")
    if current_working_directory.name == filename_splits[0]:
        filename_splits.pop(0)
        filename = "/".join(filename_splits)

    file = pathlib.Path(filename)
    with open(file) as f:
        for line in f:
            tmp_line = line.strip()
            output.append(tmp_line)
    return output
