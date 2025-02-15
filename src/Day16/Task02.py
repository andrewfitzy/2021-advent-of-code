character_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Node:
    def __init__(self, type, version, literals=[], operations=[]):
        self.type = type
        self.version = version
        self.literals = literals
        self.operations = operations

    def get_decimal_value(self):
        decimal_value = int("".join(self.literals), 2)
        return decimal_value

    def __str__(self):
        return "Type: {type}\nVersion: {version}\nLiterals: {literals}\nOperations: {operations}".format(
            type=self.type, version=self.version, literals=self.literals, operations=self.operations
        )


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


def convert_to_binary(input):
    result = []
    for char in input:
        result.append(character_map[char])
    return "".join(result)


def process_packet(packet):
    version = packet[:3]
    packet = packet[3:]

    type_id = packet[:3]
    packet = packet[3:]

    decimal_version = int("".join(version), 2)
    decimal_type = int("".join(type_id), 2)

    if decimal_type == 4:
        literal_values, remaining_date = get_literal_values(packet)
        node = Node(decimal_type, decimal_version, literal_values, [])
        return (node, remaining_date)
    else:
        nodes = []
        length_type_id = packet[:1]
        packet = packet[1:]
        length_type = int(length_type_id[0])  # single binary digit so will be '0' or '1'
        if length_type == 0:
            length_of_bits_bin = packet[:15]
            length_of_bits = int("".join(length_of_bits_bin), 2)

            packet = packet[15:]
            subpacket = packet[:length_of_bits]

            packet = packet[length_of_bits:]
            while len(subpacket) > 0:
                node, remaining_data = process_packet(subpacket)
                subpacket = remaining_data
                nodes.append(node)

        else:
            number_of_subpackets_bin = packet[:11]
            packet = packet[11:]
            number_of_subpackets = int("".join(number_of_subpackets_bin), 2)
            for _ in range(number_of_subpackets):
                node, remaining_data = process_packet(packet)
                nodes.append(node)
                packet = remaining_data

        node = Node(decimal_type, decimal_version, [], nodes)
        return (node, packet)


def get_literal_values(input_as_binary_list):
    values = []
    while True:
        prefix = input_as_binary_list[0]
        literal = input_as_binary_list[1:5]

        values.append("".join(literal))
        input_as_binary_list = input_as_binary_list[5:]

        if prefix == "0":
            break
    return (values, input_as_binary_list)


def solve(file_content):
    packet = list(convert_to_binary(file_content[0]))
    node, remaining_date = process_packet(packet)
    for datum in remaining_date:
        if "0" != datum:
            raise ValueError("We have more than just '0' left in the stream")
    result = process_calculation(node)
    return result


def process_calculation(node):
    value = 0
    if 0 == node.type:
        # sum value of subpackets
        for op_node in node.operations:
            value = value + process_calculation(op_node)

    if 1 == node.type:
        value = 1
        # multiply value of subpackets
        for op_node in node.operations:
            value = value * process_calculation(op_node)

    if 2 == node.type:
        # Get smallest subpacket value
        value = float("inf")
        for op_node in node.operations:
            node_val = process_calculation(op_node)
            if node_val < value:
                value = node_val

    if 3 == node.type:
        # Get largest subpacket value
        for op_node in node.operations:
            node_val = process_calculation(op_node)
            if node_val > value:
                value = node_val

    if 4 == node.type:
        # literal value
        value = node.get_decimal_value()

    if 5 == node.type:
        # Test first subpacket greater than second
        first_node_val = process_calculation(node.operations[0])
        second_node_val = process_calculation(node.operations[1])
        if first_node_val > second_node_val:
            value = 1

    if 6 == node.type:
        # Test first subpacket less than second
        first_node_val = process_calculation(node.operations[0])
        second_node_val = process_calculation(node.operations[1])
        if first_node_val < second_node_val:
            value = 1

    if 7 == node.type:
        # Test for subpacket equality
        first_node_val = process_calculation(node.operations[0])
        second_node_val = process_calculation(node.operations[1])
        if first_node_val == second_node_val:
            value = 1
    return value
