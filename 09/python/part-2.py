def parse_input(filename: str) -> (str, map):
    with open(filename, 'r') as f:
        file_content = f.read().splitlines()
        return file_content


def all_diffs(numbers: list) -> list:
    diffs = []
    for i, num in enumerate(numbers):
        if i == 0:
            continue
        this_num = int(num)
        last_num = int(numbers[i - 1])
        #print(f"{this_num=}, {last_num=}")

        # get the diff between the two numbers
        diff = this_num - last_num
        #print(f"{diff=}")
        diffs.append(diff)
    
    return diffs


def extrapolated_value(a: list, b: int) -> int:
    #print(f"{a=}, {b=}: {b=}, {a[0]=}, {a[0]-b=}")
    return a[0] - b


if __name__ == '__main__':

    input_files = []
    input_files.append('../example-input.txt')
    input_files.append('../input.txt')

    for filename in input_files:
        diff_map = {}
        extrapolated_values = []
        lines = parse_input(filename)
        #print(f"{lines=}")


        for line in lines:
            diff_list = []
            #print(f"{line=}")
            diffs = all_diffs(numbers = line.split(' '))
            #print(f"{diffs=}")

            while all(diff == 0 for diff in diffs) == False:
                #print(f"{diffs=}")
                diff_list.append(diffs)
                diffs = all_diffs(numbers=diffs)

            diff_map[line] = diff_list

            #print(f"{diff_list=}")
        #print(f"{diff_map=}")

        for key, value in diff_map.items():    

            next_value = 0
            for i, diffs in enumerate(reversed(value)):
                #print(f"{i=} - {key}: {diffs=}, {next_value=}")
                next_value = extrapolated_value(a=diffs, b=next_value)
                if i == len(value) - 1:
                    this_value = int(key.split(' ')[0])
                    #print(f"\n{key}: {this_value=}, {next_value=}\n")
                    extrapolated_values.append(this_value - next_value)

        #print(f"{diff_map=}")
        print(f"{extrapolated_values=}")
        print(f"{filename} sum: {sum(extrapolated_values)}")
