import re
  

def parse_input(filename: str) -> (list, list):
    with open(filename, 'r') as f:
        file_content = f.read()
        time, distance = file_content.splitlines()
        time = "".join(re.findall(r'[\d]+', time))
        distance = "".join(re.findall(r'[\d]+', distance))
        return ([time], [distance])


def get_race_result(race_time: int, race_record: int) -> int:
    race_results = []
    for time_index in range(race_time):
        race_distance = time_index * (race_time - time_index)
        
        if race_distance > race_record:
            race_results.append(time_index)

    return len(race_results)
    


def get_result(time: list, distance: list) -> int:
    result = []
    print(f"{time=}, {distance=}")
    
    for race_time, record_distance in zip(time, distance):
        race_time = int(race_time)
        record_distance = int(record_distance)
        print(f"{race_time=}, {record_distance=}")
        result.append(get_race_result(
            race_time=race_time,
            race_record=record_distance))
    
    sum = 1
    for result_index in result:
        sum = sum * result_index
    print(f"{result=}, {sum=}")
    return sum


if __name__ == '__main__':
    
    for filename in ['example-input.txt', 'input.txt']:
        
        time, distance = parse_input(filename=f"../{filename}")
        result = get_result(time, distance)
        print(f"Result from {filename}: {result}")
