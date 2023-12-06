import re
from enum import Enum


class Ranges(Enum):
    destination_range_start = 0
    source_range_start = 1
    range_length = 2


seeds = []
destinations = []
map_data = {
    "seeds": [],
    "seed_to_soil": [],
    "soil_to_fertilizer": [],
    "fertilizer_to_water": [],
    "water_to_light": [],
    "light_to_temperature": [],
    "temperature_to_humidity": [],
    "humidity_to_location": [],
}
seed_map = map_data.copy()
seed_map.pop("seeds")


def dest_src_mapping(dict_key: str, seed_num: int) -> int :

    for row in map_data[dict_key]:
        row_dest = int(row[Ranges.destination_range_start.value])
        row_src = int(row[Ranges.source_range_start.value])
        range_length = int(row[Ranges.range_length.value])

        if seed_num < row_src or seed_num > (row_src + range_length):
            continue

        dest = row_dest + seed_num - row_src
        return dest

    return seed_num


def get_next_dest(key: str, seed_num: int) -> int:
    try:
        index = seed_map[key][0].index(seed_num)
        return seed_map[key][1][index]
    except ValueError:
        return seed_num


if __name__ == '__main__':
    result = []

    #with open('../example-input.txt', 'r') as f:
    with open('../input.txt', 'r') as f:
        data = f.read()
        parsed_data = re.findall(r'.+?(?=\n\s*\n|\Z)', data, re.DOTALL)
        for i, key in enumerate(map_data.keys()):
            if i == 0:
                map_data[key] = re.findall(r'[\d]+', parsed_data[i])
            else:
                numbers = re.findall(r'[\d]+', parsed_data[i])
                map_data[key] = [numbers[i:i+3] for i in range(0, len(numbers), 3)]

    seeds = [int(seed) for seed in map_data.pop("seeds")]

    for seed in seeds:
        destination = seed
        for key in seed_map.keys():
            destination = dest_src_mapping(dict_key=key, seed_num=destination)
        destinations.append(destination)

    #print(f"{seeds=}")
    #print(f"{destinations=}")
    print(f"{min(destinations)=}")
