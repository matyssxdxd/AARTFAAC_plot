import re
import matplotlib.pyplot as plt
import numpy as np

x = [] 
y = []
original_file = open("AARTFAAC_DELTA_DELTA.log", "r")
lines = original_file.readlines()[::-1]
original_file.close()

for i in range(len(lines)):
    if "InputBuffer 0-0, valid" in lines[i]:
        lines = lines[i+1:]
        break

for i in range(len(lines)):
    if "InputBuffer 1-1" in lines[i]:
        lines = lines[:i]
        break

lines = lines[::-1]

for i in range(len(lines)):
    lines[i] = lines[i][lines[i].find('(') + 1:]
    lines[i] = lines[i][:lines[i].find(',')]
    power = int(lines[i][lines[i].find('+') + 1:])
    lines[i] = lines[i][:lines[i].find('e')]
    y.append((float(lines[i]) * 10**power))
    lines[i] = f"{i} " + str(float(lines[i]) * 1**power)
    print(lines[i])
    x.append(i)

xpoints = np.array(x)
ypoints = np.array(y)

plt.plot(xpoints, ypoints)
plt.show()
new_file = open("AARTFAAC_EDIT.log", 'w')
new_file.writelines(lines)
new_file.close()
