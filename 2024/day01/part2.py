#!/usr/bin/env python3
# pylint: disable=W0611,C0103,W0511,C0200
"""
FOO
"""

import time
import sys
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


# TODO
tot = 0
arr1 = []
arr2 = []
for i, row in enumerate(l):
    arr = row.split()
    arr1.append(int(arr[0]))
    arr2.append(int(arr[1]))

for i in range(len(arr1)):
    tot += arr2.count(arr1[i]) * arr1[i]

print(tot)





end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing
