import re
import matplotlib.pyplot as plt
import numpy as np

data_dict = {}

with open("irib.out", "r") as original_file:
    lines = original_file.readlines()

def process_data(data):
    for index, line in enumerate(data):
        match_group = re.search(r"vis: (\d+)", line)
        value_match = re.search(r"\((\d+\.\d+e[+-]?\d+)", line)
        
        if match_group and value_match:
            group = match_group.group(1)
            value = float(value_match.group(1))
            
            if group not in data_dict:
                data_dict[group] = {'x': [], 'y': []}
            
            data_dict[group]['x'].append(index)
            data_dict[group]['y'].append(value)

process_data(lines)

for group, data in data_dict.items():
    plt.figure() 
    plt.plot(data['x'], data['y'])
    plt.show() 

