"""
--- Day 12: Passage Pathing ---
With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to find all of them.

Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:

start-A
start-b
A-c
A-b
b-d
A-end
b-end
This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.

So, the above cave system looks roughly like this:

    start
    /   \
c--A-----b--d
    \   /
     end
Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

Given these rules, there are 10 paths through this example cave system:

start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
(Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)

Note that in this cave system, cave d is never visited by any path: to do so, cave b would need to be visited twice (once on the way to cave d and a second time when returning from cave d), and since cave b is small, this is not allowed.

Here is a slightly larger example:

dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
The 19 paths through it are as follows:

start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end
Finally, this even larger example has 226 paths through it:

fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
How many paths through this cave system are there that visit small caves at most once?
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
        'start',
        'b',
        'c',
        'end',
      ]
      "b": [
        'start',
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
        sensor_links[parts[0]].add(parts[1])
        if END_NODE != parts[1]:
            sensor_links[parts[1]].add(parts[0])
    return sensor_links


def crawl_next(graph, path, mutable_paths):
    """
    recursive method that will do a depth first search to find paths. Only those the end with 'end' are returned
    """
    valid_links = valid_paths(graph, path, path[-1])

    if len(valid_links) == 0:
        if END_NODE == path[-1]:
            mutable_paths.append(path)
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
    return valid_paths


def process_sensors(sensor_graph):
    """
    Given a graph, will find the start node and then for each node linked from start, retrieve all the valid paths
    """
    start_links = sensor_graph[START_NODE]
    # horrible but works
    final_paths = []
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
    process_file('input_example01.txt', 10, False)
    process_file('input_example02.txt', 19, False)
    process_file('input_example03.txt', 226, False)
    process_file('input.txt', 5254, False)
