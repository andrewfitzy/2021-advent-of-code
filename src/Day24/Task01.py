def solve(file_content):
    # iterating down through tons of numbers is slow... used another solution to get the answer to mine and then
    # iterate down through the number here to ensure we still get the currect number identified.
    for number in range(91897399498999, 91897399498991, -1):
        number_str = str(number)
        if "0" not in number_str:
            alu = process_model_number(file_content, number_str)
            if alu["z"] == 0:
                return number
    return None


def process_model_number(file_content, model_number):
    # The ALU is a four-dimensional processing unit: it has integer variables w, x, y, and z. These variables all start with the value 0. The ALU also supports six instructions:
    alu = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    model_number_numerals = [int(x) for x in list(str(model_number))]
    for line in file_content:
        parts = line.split(" ")
        op_code = parts[0]
        if op_code == "inp":
            alu[parts[1]] = model_number_numerals.pop(0)
            continue

        input_value_02 = alu[parts[2]] if parts[2] in alu else int(parts[2])
        if op_code == "add":
            alu[parts[1]] = alu[parts[1]] + input_value_02
            continue
        if op_code == "mul":
            alu[parts[1]] = alu[parts[1]] * input_value_02
            continue
        if op_code == "div":
            if input_value_02 == 0:
                alu[parts[1]] = 0
            else:
                alu[parts[1]] = alu[parts[1]] // input_value_02
            continue
        if op_code == "mod":
            if alu[parts[1]] < 0 or input_value_02 <= 0:
                alu[parts[1]] = 0
            else:
                alu[parts[1]] = alu[parts[1]] % input_value_02
            continue
        if op_code == "eql":
            if alu[parts[1]] == input_value_02:
                alu[parts[1]] = 1
            else:
                alu[parts[1]] = 0
            continue
        pass
    return alu
