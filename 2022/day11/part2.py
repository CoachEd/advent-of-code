import time
import sys
import math
from copy import copy, deepcopy
start_secs = time.time()
print('')

"""
Monkey 0:
  Starting items: 73, 77
  Operation: new = old * 5
  Test: divisible by 11
    If true: throw to monkey 6
    If false: throw to monkey 5

Monkey 1:
  Starting items: 57, 88, 80
  Operation: new = old + 5
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 0

Monkey 2:
  Starting items: 61, 81, 84, 69, 77, 88
  Operation: new = old * 19
  Test: divisible by 5
    If true: throw to monkey 3
    If false: throw to monkey 1

Monkey 3:
  Starting items: 78, 89, 71, 60, 81, 84, 87, 75
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 0

Monkey 4:
  Starting items: 60, 76, 90, 63, 86, 87, 89
  Operation: new = old + 2
  Test: divisible by 13
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 5:
  Starting items: 88
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 6:
  Starting items: 84, 98, 78, 85
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 5
    If false: throw to monkey 4

Monkey 7:
  Starting items: 98, 89, 78, 73, 71
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 3
    If false: throw to monkey 2
"""

items = [
  [73, 77],
  [57, 88, 80],
  [61, 81, 84, 69, 77, 88],
  [78, 89, 71, 60, 81, 84, 87, 75],
  [60, 76, 90, 63, 86, 87, 89],
  [88],
  [84, 98, 78, 85],
  [98, 89, 78, 73, 71],
]

numMonkeys = len(items)
counts = [-2 for x in range(numMonkeys)]
def playRound():
  global numMonkeys,items,counts
  for i in range(numMonkeys):
    if i == 0:
      for item in items[i]:
        counts[i] += 1
        wl = item * 5
        if wl % 11 == 0:
          if (wl * wl) % 7 == 0:
            items[5].append(wl*wl)
          else:
            items[6].append(wl)
        else:
          items[5].append(wl)
      items[i].clear()
    elif i == 1:
      for item in items[i]:
        counts[i] += 1
        wl = item + 5
        if wl % 19 == 0:
          items[6].append(wl)
        else:
          items[0].append(wl)
      items[i].clear()
    elif i == 2:
      for item in items[i]:
        counts[i] += 1
        wl = item * 19
        if wl % 5 == 0:
          items[3].append(wl)
        else:
          items[1].append(wl)
      items[i].clear()
    elif i == 3:
      for item in items[i]:
        counts[i] += 1
        wl = item + 7
        if wl % 3 == 0:
          items[1].append(wl)
        else:
          items[0].append(wl)
      items[i].clear()
    elif i == 4:
      for item in items[i]:
        counts[i] += 1
        wl = item + 2
        if wl % 13 == 0:
          items[2].append(wl)
        else:
          items[7].append(wl)
      items[i].clear()
    elif i == 5:
      for item in items[i]:
        counts[i] += 1
        wl = item + 1
        if wl % 17 == 0:
          items[4].append(wl)
        else:
          items[7].append(wl)
      items[i].clear()
    elif i == 6:
      for item in items[i]:
        counts[i] += 1
        wl = item * item
        if wl % 7 == 0:
          items[5].append(wl)
        else:
          items[4].append(wl)
      items[i].clear()
    elif i == 7:
      for item in items[i]:
        counts[i] += 1
        wl = item + 4
        if wl % 2 == 0:
          items[3].append(wl)
        else:
          items[2].append(wl)
      items[i].clear()

rounds = 200
for r in range(rounds):
  playRound()

print('0: ' + str(counts[0]))
print('1: ' + str(counts[7]))
print(counts[0]*counts[-1]) # hard code multiplying top two counts

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')