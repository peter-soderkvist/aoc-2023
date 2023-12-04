import re


if __name__ == '__main__':
    values = []
    number_matches = []
    symbol_regexp = re.compile(r'[\%\#\@\/\=\&\-\*\$\+]+')
    with open("../input.txt", 'r') as f:
        data = f.read().splitlines()
        for i, line in enumerate(data):
            number_matches = re.finditer(r'[0-9]+', line)
            for number in number_matches:
                index_start = number.span(0)[0]
                index_stop = number.span(0)[1]

                symbols_next_to = re.search(symbol_regexp, data[i][index_start - (0 if index_start == 0 else 1):index_stop + (0 if index_stop == 0 else 1)])
                if symbols_next_to:
                    value = number.group()
                    values.append(int(value))
                    print(f"Symbol next to {value} on line {i + 1}: {symbols_next_to}")
                else:
                    symbols_above = ""
                    if i:   # Skip on index 0
                        symbols_above = re.search(symbol_regexp, data[i - 1][index_start - (0 if index_start == 0 else 1):index_stop + (0 if index_stop == 0 else 1)])
                    if symbols_above:
                        value = number.group()
                        values.append(int(value))
                        print(f"Symbol above {value} on line {i + 1}: {symbols_above}")
                    else:
                        symbols_below = ""
                        if i < len(data) - 1:
                            symbols_below = re.search(symbol_regexp, data[i + 1][index_start - (0 if index_start == 0 else 1):index_stop + (0 if index_stop == 0 else 1)])
                        if symbols_below:
                            value = number.group()
                            values.append(int(value))
                            print(f"Symbol below {value} on line {i + 1}: {symbols_below}")

    print(f"Sum: {sum(values)}")
