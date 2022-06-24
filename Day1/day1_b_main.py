# Copyright 2021 Noah Soliday Bench
# Made for Advent of Code 2021

import os
from Util import input_util

script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "day1_input.txt")

input_data = input_util.parse_lines_input(data_path)

last_value = int(input_data[0]) + int(input_data[1]) + int(input_data[2])
num_increases = 0

for i in range(len(input_data)):
    try:
        depth_sum = int(input_data[i]) + int(input_data[i + 1]) + int(input_data[i + 2])
        if depth_sum > last_value:
            num_increases += 1

        last_value = depth_sum
    except:
        break

print(num_increases)
