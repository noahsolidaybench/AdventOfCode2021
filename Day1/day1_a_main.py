# Copyright 2021 Noah Soliday Bench
# Made for Advent of Code 2021

import os
from Util import input_util

script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "day1_input.txt")

input_data = input_util.parse_lines_input(data_path)

last_value = int(input_data[0])
num_increases = 0

for depth in input_data:
    if int(depth) > last_value:
        num_increases += 1

    last_value = int(depth)

print(num_increases)
