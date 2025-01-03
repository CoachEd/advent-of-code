#!/usr/bin/env python3
# pylint: disable=W0611,C0103,W0511,C0200,C0116
"""
FOO
"""

import time
import sys
from copy import copy, deepcopy

def safeReport(a):
    a2 = None

    if sorted(a, reverse=True) == a:
        # sorted descending
        a2 = a.copy()
        a2.reverse()
    elif sorted(a) == a:
        # sorted ascending
        a2 = a.copy()

    if a2 is not None:
        # candidate
        # skip any dups
        if len(a2) != len(set(a2)):
            return False

        good = True
        for j in range(len(a2)-1):
            gap = a2[j+1] - a2[j]
            if gap > 3:
                good = False
                break
        return good

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
count = 0
for i, row in enumerate(l):
    arr = [int(x) for x in row.split()]
    for j in range(len(arr)):
        arr2 = arr.copy()
        arr2.pop(j)
        if safeReport(arr2):
            count += 1
            break

print(count)





end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing
