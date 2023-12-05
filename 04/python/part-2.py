import re


result = [0]


def increment_card(index: int):
    try:
        result[index] = result[index] + 1
    except:
        result.append(1)


if __name__ == '__main__':
    with open("../input.txt", "r") as f:
        lines = f.read().splitlines()
        
        for i, line in enumerate(lines):
            increment_card(i)
            winning_numbers, my_numbers = line.split(':')[1].split('|')
            winning_numbers = re.findall(r'[\d]+', winning_numbers)
            my_numbers = re.findall(r'[\d]+', my_numbers)

            extra_cards = result[i]
            for _ in range(extra_cards):
                my_winning_numbers = []
                for winning_num in winning_numbers:
                    for my_num in my_numbers:
                        if my_num == winning_num:
                            my_winning_numbers.append(int(my_num))

                for j, _ in enumerate(my_winning_numbers):
                    next_card = i + j + 1
                    if next_card < len(lines):
                        increment_card(next_card)

    print(len(result))
    print(f"{result=}")
    print(f"Sum: {sum(result)}")
