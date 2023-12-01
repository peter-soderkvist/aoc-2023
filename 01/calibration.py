import re


number_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five' : 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def convert_to_number(number):
    try:
        return int(number)
    except:
        return int(number_map[number])

if __name__ == '__main__':
    values = []
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        for i, line in enumerate(data):
            digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
            value = f"{convert_to_number(digits[0])}{convert_to_number(digits[-1])}"
            print(f"{i + 1}: {value} - {line}")
            values.append(int(value))

    print(f"Sum: {sum(values)}")
