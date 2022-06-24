# Copyright 2021 Noah Soliday Bench
# Made for Advent of Code 2021

import os
from Util import input_util

script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "day3_input.txt")

input_data = input_util.parse_lines_input(data_path)


def count_of_0_at_index(data: list, index: int):
    rate = 0
    for val in data:
        if val[index] == "0":
            rate += 1

    return rate


def find_value_recursively(data: list, index: int, most_common: bool):
    if len(data) == 1:
        return data[0].strip()

    new_data = []
    # calculate the count of 0s
    rate = count_of_0_at_index(data, index)
    for line in data:
        # if equal number of 1s and 0s
        if rate == len(data) * 0.5:
            if most_common and line[index] == "1":
                new_data.append(line)
            elif not most_common and line[index] == "0":
                new_data.append(line)

        # if 0s are most common
        elif rate > len(data) * 0.5:
            if most_common and line[index] == "0":
                new_data.append(line)
            elif not most_common and line[index] == "1":
                new_data.append(line)

        # if 1s are most common
        elif rate < len(data) * 0.5:
            if most_common and line[index] == "1":
                new_data.append(line)
            elif not most_common and line[index] == "0":
                new_data.append(line)

    return find_value_recursively(new_data, index + 1, most_common)


if __name__ == "__main__":
    o2_gen_rating = find_value_recursively(input_data, 0, True)
    co2_scrub_rating = find_value_recursively(input_data, 0, False)

    print(f"O2 Generator: {o2_gen_rating} CO2 Scrubber: {co2_scrub_rating}")
    print(int(o2_gen_rating,2) * int(co2_scrub_rating,2))
