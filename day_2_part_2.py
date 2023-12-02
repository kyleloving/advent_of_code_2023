import re

with open("day_2\input.txt") as input:
    input_list = [line for line in input]

games_dict = {int(line.split(':')[0][5:]): line.split(':')[1].strip() for line in input_list}

total_sum = 0
for game, result in games_dict.items():
    red = [int(x) for x in re.findall(r'(\d+)(?: red)', result)]
    blue = [int(x) for x in re.findall(r'(\d+)(?: blue)', result)]
    green = [int(x) for x in re.findall(r'(\d+)(?: green)', result)]

    total_sum += max(red) * max(blue) * max(green)

print(total_sum)