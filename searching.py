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
    print(results)
    return results


def pattern_search(numbers, pattern):
    indexes = set()
    pattern_lenght = len(pattern)
    for i in range(len(numbers)):
        if numbers[i:i+ pattern_lenght] == pattern:
            indexes.add(i)
    print(indexes)




def main():
    numbers = read_data("sequential.json", "dna_sequence")
    print(numbers)
    linear_search(numbers, 0)
    pattern_search(numbers, "TAA")


if __name__ == '__main__':
    main()