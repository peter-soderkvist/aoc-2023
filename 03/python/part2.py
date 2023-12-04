import re


def check_index_in_range(start_left: int, stop_left: int, start_right: int, stop_right: int) -> bool:
    if (start_left > start_right and \
       stop_left < stop_right) or \
       (stop_left > start_right and \
       start_left < stop_right):
        return True
    return False

if __name__ == '__main__':
    values = []
    number_matches = []
    symbol_regexp = re.compile(r'[\*]')
    number_regexp = re.compile(r'\d+')
    with open("../input.txt", 'r') as f:
        data = f.read().splitlines()
        for i, line in enumerate(data):
            asterisk_matches = re.finditer(symbol_regexp, line)
            for j, asterisk_match in enumerate(asterisk_matches):
                index_start = int(asterisk_match.span(0)[0])
                index_stop = int(asterisk_match.span(0)[1])

                gear_numbers = []
                numbers_above = ""
                if i:
                    numbers_above = re.finditer(number_regexp, data[i - 1])
                    for match in numbers_above:
                        if check_index_in_range(start_left=match.span(0)[0],
                                                stop_left=match.span(0)[1],
                                                start_right=(index_start - (0 if index_start == 0 else 1)),
                                                stop_right=(index_stop + (0 if index_stop == 0 else 1))):
                            gear_numbers.append(int(match.group()))

                numbers_next_to = re.finditer(number_regexp, data[i])
                for match in numbers_next_to:
                    if check_index_in_range(start_left=match.span(0)[0],
                                            stop_left=match.span(0)[1],
                                            start_right=(index_start - (0 if index_start == 0 else 1)),
                                            stop_right=(index_stop + (0 if index_stop == 0 else 1))):
                        gear_numbers.append(int(match.group()))

                numbers_below = ""
                if i < len(data) - 1:
                    numbers_below = re.finditer(number_regexp, data[i + 1])
                    for match in numbers_below:
                        if check_index_in_range(start_left=match.span(0)[0],
                                                stop_left=match.span(0)[1],
                                                start_right=(index_start - (0 if index_start == 0 else 1)),
                                                stop_right=(index_stop + (0 if index_stop == 0 else 1))):
                            gear_numbers.append(int(match.group()))

                if len(gear_numbers) == 2:
                    values.append(int(gear_numbers[0]) * int(gear_numbers[1]))

    print(f"Sum: {sum(values)}")
