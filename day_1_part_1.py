import re

with open("input") as input:
    input_list = [line for line in input]

total_sum = 0
for item in input_list:
    numerals = re.findall(r'\d', item)
    if numerals:
        first_num, last_num = map(int, (numerals[0], numerals[-1]))
        total_sum += int(f'{first_num}{last_num}')

print(total_sum)