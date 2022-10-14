# wap to find the sum, mmean, max annd min in a list of number

import math
from statistics import median, mode
import statistics


x = [12,34,56,23,7,2,66,78,]

total = sum(x)
mean = sum(x)/len(x)
x_max = max(x)
x_min = min(x)

print(f'sum: {total}, Mean: {mean}, Max: {x_max}, Min: {x_min}')

median = statistics.median(x)
mode =  statistics.mode(x)
print(median,mode)
