"""
--- Part Two ---
After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

Now, the 36 possible paths through the first example above are:

start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end
The slightly larger example above now has 103 paths through it, and the even larger example now has 3509 paths through it.

Given these new rules, how many paths through this cave system are there?
"""

from util.timer import Timer
from collections import defaultdict

START_NODE = 'start'
END_NODE = 'end'


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


def convert_sensor_reading_to_dictionary(sensor_graph):
    """
    Takes the raw input and processes into a dict such that:
    start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end

    becomes:
    {
      "start": [
        'A',
        'b',
      ]
      "A": [
        'b',
        'c',
        'end',
      ]
      "b": [
        'A',
        'd',
        'end',
      ]
      "c": [
        'A',
      ]
      "d": [
        'b',
      ]
    }
    """
    sensor_links = defaultdict(set)
    for sensor_reading in sensor_graph:
        parts = sensor_reading.split('-', -1)

        if START_NODE == parts[0] or START_NODE == parts[1]:
            if START_NODE == parts[0]:
                sensor_links[parts[0]].add(parts[1])
            else:
                sensor_links[parts[1]].add(parts[0])
        elif END_NODE == parts[0] or END_NODE == parts[1]:
            if END_NODE == parts[0]:
                sensor_links[parts[1]].add(parts[0])
            else:
                sensor_links[parts[0]].add(parts[1])
        else:
            sensor_links[parts[0]].add(parts[1])
            sensor_links[parts[1]].add(parts[0])

    return sensor_links


def crawl_next(graph, path, mutable_paths):
    """
    recursive method that will do a depth first search to find paths. Only those the end with 'end' are returned
    """
    valid_links = valid_paths(graph, path, path[-1])

    if len(valid_links) == 0:
        if END_NODE == path[-1]:
            t = tuple(path)
            if t not in mutable_paths:
                mutable_paths.add(t)
        return

    for node in valid_links:
        tmp_path = path.copy()
        tmp_path.append(node)
        crawl_next(graph, tmp_path, mutable_paths)


def valid_paths(graph, path, node):
    """
    get the paths from a node that are not the end path, an uppercase path or lowercase and not already seen.
    """
    valid_paths = []

    if node == END_NODE:
        return valid_paths

    node_paths = graph[node]

    for node_path in node_paths:
        if node_path.isupper():
            valid_paths.append(node_path)

        if node_path.islower() and node_path not in path:
            valid_paths.append(node_path)

        has_2_lowers_already = False
        for item in path:
            if item.islower() and path.count(item) == 2:
                has_2_lowers_already = True

        if not has_2_lowers_already:
            valid_paths.append(node_path)

    return valid_paths


def dedupe_list(final_paths):
    """
    Given a list of lists, iterate through determining whether we have already seen to list and if so ignore it...
    Converting to a tuple as list is not hashable whereas a tuple is.
    """
    seen = set()
    deduped_list = []
    for item in final_paths:
        t = tuple(item)
        if t not in seen:
            deduped_list.append(item)
            seen.add(t)
    return deduped_list


def process_sensors(sensor_graph):
    """
    Given a graph, will find the start node and then for each node linked from start, retrieve all the valid paths
    """
    start_links = sensor_graph[START_NODE]
    # horrible but works
    final_paths = set()
    for sensor in start_links:
        start_path = [START_NODE, sensor]
        crawl_next(sensor_graph, start_path, final_paths)

    return final_paths


def process_file(filename, expected_result, print_result):
    """
    Given a file and an expected result, process the file and see if the number of paths matches the expected result
    """
    t = Timer()
    t.start()
    input_from_file = get_input(filename)

    sensor_graph = convert_sensor_reading_to_dictionary(input_from_file)

    result = process_sensors(sensor_graph)

    if print_result:
        for row in result:
            print(', '.join(row))

    result_length = len(result)
    assert result_length == expected_result, 'Output is not as expected, expected ' + str(expected_result) + ' but got ' + str(result_length)

    print('RESULT: there are ' + str(result_length) + ' paths for input ' + filename)
    t.stop()


if __name__ == '__main__':
    process_file('input_example01.txt', 36, True)
    process_file('input_example02.txt', 103, False)
    process_file('input_example03.txt', 3509, False)
    process_file('input.txt', 5254, False)
