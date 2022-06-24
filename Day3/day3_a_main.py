# Copyright 2021 Noah Soliday Bench
# Made for Advent of Code 2021

import os
from Util import input_util

script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "day3_input.txt")

input_data = input_util.parse_lines_input(data_path)

rates_of_0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma_rate = ""
epsilon_rate = ""

for line in input_data:
    for i, bit in enumerate(line):
        if bit == "0":
            rates_of_0[i] += 1

for count in rates_of_0:
    if count > len(input_data) * 0.5:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"

print(f"gamma: {int(gamma_rate, 2)} epsilon: {int(epsilon_rate, 2)}")
print(int(gamma_rate,2) * int(epsilon_rate,2))
