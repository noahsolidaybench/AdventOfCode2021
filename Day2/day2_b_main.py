# Copyright 2021 Noah Soliday Bench
# Made for Advent of Code 2021

import os
from Util import input_util

script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "day2_input.txt")

input_data = input_util.parse_lines_input(data_path)

h_pos = 0
d_pos = 0
aim = 0

for cmd in input_data:
    parsed_cmd = cmd.split()

    if parsed_cmd[0] == "forward":
        h_pos += int(parsed_cmd[1])
        d_pos += aim * int(parsed_cmd[1])
    elif parsed_cmd[0] == "down":
        aim += int(parsed_cmd[1])
    elif parsed_cmd[0] == "up":
        aim -= int(parsed_cmd[1])

print(f"h pos: {h_pos} d pos: {d_pos}")
print(h_pos * d_pos)
