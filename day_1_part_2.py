import re

with open("input") as input:
    input_list = [line for line in input]
       
num_dict = {
    'one':1, 
    'two':2, 
    'three':3, 
    'four':4, 
    'five':5, 
    'six':6, 
    'seven':7, 
    'eight':8, 
    'nine':9,
}

total_sum = 0
for item in input_list:
    # Test n-grams of size 5, 4, and 3
    n_grams = []
    for n in range(5, 2, -1):  
        for i, _ in enumerate(item):
            n_gram = item[i:i + n]
            if n_gram in num_dict:
                n_grams.append((n_gram, i, i + n))
    
    n_grams.sort(key=lambda x: x[1])
    
    # Replace number words based on n-gram list and indexes
    current_depth = 0
    for n_gram, start, end in n_grams:
        item = item.replace(n_gram, str(num_dict[n_gram]))

    # Add numbers
    numerals = re.findall(r'\d', item)
    if numerals:
        first_num, last_num = map(int, (numerals[0], numerals[-1]))
        total_sum += int(f'{first_num}{last_num}')

print(total_sum)