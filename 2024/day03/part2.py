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

def extract_patterns(input_string):
    # Define the regular expression pattern
    pattern = r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)'

    # Find all matches in the input string
    matches = re.finditer(pattern, input_string)

    # Collect results
    results = []
    for match in matches:
        if match.group(1) and match.group(2):
            # If it's a mul(xxx,yyy) match
            results.append(f"mul({match.group(1)},{match.group(2)})")
        else:
            # If it's a do() or don't() match
            results.append(match.group(0))

    return results

# TODO
tot = 0
x = 0
y = 0
do = True
for s in l:
    matches = extract_patterns(s)
    for m in matches:
        if m == 'do()':
            do = True
        elif m == "don't()":
            do = False
        else:
            if do:
                m = m.replace('mul(','').replace(')','')
                (x,y) = m.split(',')
                tot += int(x) * int(y)

print(tot)

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing
