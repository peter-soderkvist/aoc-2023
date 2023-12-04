if __name__ == '__main__':
    result = []
    with open("../input.txt", "r") as f:
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            my_winning_numbers = []
            winning_numbers, my_numbers = line.split(':')[1].split('|')

            for winning_num in winning_numbers.strip().split(' '):
                for my_num in my_numbers.strip().split(' '):
                    if not my_num.isdigit():
                        continue
                    if my_num == winning_num:
                        my_winning_numbers.append(int(my_num))

            points = 0
            for i, _ in enumerate(my_winning_numbers):
                if i == 0:
                    points = 1
                else:
                    points = points * 2
            result.append(points)
    print(len(result))
    print(f"{result=}")
    print(f"Sum: {sum(result)}")
