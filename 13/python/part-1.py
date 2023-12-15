import numpy as np


def parse_input(filename) -> list[tuple[str, str]]:
    parsed_input = []
    with open(filename) as file:
        lines = file.read().split('\n\n')
        for line in lines:
            char_list = []
            for row in line.split('\n'):
                char_list.append(list(row))
            parsed_input.append(char_list)
    return parsed_input


def find_mirror(pattern: np.array) -> int:
    for i in range(1, len(pattern)):
        top_half = pattern[:i][::-1]
        bottom_half = pattern[i:]

        top_half = top_half[:len(bottom_half)]
        bottom_half = bottom_half[:len(top_half)]

        top_string = ''.join([str(i) for i in np.ndarray.tolist(top_half)])
        bottom_string = ''.join([str(i) for i in np.ndarray.tolist(bottom_half)])

        if top_string == bottom_string:
            return i
    return 0

if __name__ == '__main__':
    input_files = []
    input_files.append('../example-input.txt')
    input_files.append('../input.txt')
    results = [0, 0]

    for file_index, filename in enumerate(input_files):
        print(f"Input file: {filename}")

        patterns = parse_input(filename)

        for i, pattern in enumerate(patterns):
            pattern = np.array(pattern)

            pattern = pattern=np.rot90(pattern, k=-1)
            cols = find_mirror(pattern=pattern)
            results[file_index] += cols

            pattern = np.rot90(pattern, k=1)
            rows = find_mirror(pattern)
            results[file_index] += rows * 100


    print("")
    for result in results:
        print(f"Result: {result}")

    try:
        assert results[0] == 405
    except AssertionError:
        print(f"\nAssertionError: {results[0]} != 405")
