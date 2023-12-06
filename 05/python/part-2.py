import re
from enum import Enum

#Seeds:  1 753 244 662
#Lowest:    51 399 228

class Ranges(Enum):
    destination_range_start = 0
    source_range_start = 1
    range_length = 2


seeds = []
destinations = []
lowest_destination = None
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
        row_dest = row[Ranges.destination_range_start.value]
        row_src = row[Ranges.source_range_start.value]
        range_length = row[Ranges.range_length.value]

        if seed_num < row_src or seed_num > (row_src + range_length):
            continue

        dest = row_dest + seed_num - row_src
        return dest

    return seed_num


if __name__ == '__main__':
    result = []

    with open('../example-input.txt', 'r') as f:
    #with open('../input.txt', 'r') as f:
        data = f.read()
        parsed_data = re.findall(r'.+?(?=\n\s*\n|\Z)', data, re.DOTALL)
        for i, key in enumerate(map_data.keys()):
            if i == 0:
                map_data[key] = re.findall(r'[\d]+', parsed_data[i])
            else:
                numbers = re.findall(r'[\d]+', parsed_data[i])
                map_data[key] = [list(map(int, numbers[i:i+3])) for i in range(0, len(numbers), 3)]

    seeds = [int(seed) for seed in map_data.pop("seeds")]

    for seed_range_start, seed_range in zip(*[iter(seeds)] * Ranges.range_length.value):
        print(f"Next range: {seed_range_start=}, {seed_range=}")
        for seed_range_i in range(seed_range):
            
            destination = seed_range_start + seed_range_i
            for key in seed_map.keys():

                destination = dest_src_mapping(dict_key=key, seed_num=destination)

            if not lowest_destination or destination < lowest_destination:
                lowest_destination = destination
                print(f"\tNew lowest: {lowest_destination=}")

    print(f"{lowest_destination=}")
