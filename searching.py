import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode = "r") as json_file:
        data = json.load(json_file)

    return data[field]

def linear_search(numbers, my_number):
    results = {"positions": [], "count": 0}
    for index in range(len(numbers)):
        if numbers[index] == my_number:
            results["positions"].append(index)
            results["count"] = results["count"]+1
    return results


def pattern_search(sequence, pattern):
    positions = set()
    sequence_index = 0
    n = len(pattern)
    m = len(sequence)
    while sequence_index < n - m:
        pattern_index = 0
        while pattern_index < m:
            if sequence[sequence_index + pattern_index] != pattern[pattern_index]:
                break
            pattern_index = pattern_index + 1
        if pattern_index == m:
            positions.add(sequence_index + m // 2)
        sequence_index = sequence_index + 1
    return positions



def main():
    numbers = read_data("sequential.json", "unordered_numbers")
    my_number = 0
    number_positions = linear_search(numbers, my_number)
    print(number_positions)

    sequence = read_data("sequential.json", "dna_sequence")
    print(sequence)
    pattern_positions = pattern_search(sequence, "ATA")
    print(pattern_positions)



if __name__ == '__main__':
    main()