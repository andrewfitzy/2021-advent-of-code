# Standard Library
from collections import defaultdict

# From apps
from src.util.timer import Timer

START_NODE = "start"
END_NODE = "end"


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
        parts = sensor_reading.split("-", -1)
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


def solve(file_content):
    """
    Given a file and an expected result, process the file and see if the number of paths matches the expected result
    """
    t = Timer()
    t.start()

    sensor_graph = convert_sensor_reading_to_dictionary(file_content)

    result = process_sensors(sensor_graph)

    result_length = len(result)
    t.stop()
    return result_length
