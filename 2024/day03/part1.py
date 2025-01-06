#!/usr/bin/env python3
# pylint: disable=W0611,C0103,W0511,C0200,C0116,C0301,W0621
"""
FOO
"""

import time
import sys
import re
from copy import copy, deepcopy

# read in input file
fname = 'inp.txt'
with open(fname, 'r', encoding="utf-8") as file:
    data = file.read()
lines = data.split('\n')
l=[None for i in range(len(lines))]
for i, line in enumerate(lines):
    l[i] = line.strip()

# SOLUTION START - start timing
start_secs = time.time()

def extract_mult_patterns(input_string):
    # Define the regular expression pattern
    pattern = r'mul\((\d+),(\d+)\)'

    # Find all matches in the input string
    matches = re.findall(pattern, input_string)

    # Return the matches
    return matches

# TODO
tot = 0
x = 0
y = 0
for s in l:
    matches = extract_mult_patterns(s)
    for m in matches:
        (x,y) = m
        tot += int(x) * int(y)

print(tot)

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing
