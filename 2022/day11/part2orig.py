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

"""
Original:
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
"""

initial_items = [
  [73, 77],
  [57, 88, 80],
  [61, 81, 84, 69, 77, 88],
  [78, 89, 71, 60, 81, 84, 87, 75],
  [60, 76, 90, 63, 86, 87, 89],
  [88],
  [84, 98, 78, 85],
  [98, 89, 78, 73, 71],
]

numMonkeys = len(initial_items)

cols = 1000
items = [ [ -1 for x in range(cols) ] for y in range(numMonkeys) ]
itemIndexes = [ 0 for y in range(numMonkeys) ]
for y in range(len(initial_items)):
  for x in range(len(initial_items[y])):
    items[y][x] = initial_items[y][x]
    itemIndexes[y] = x + 1

counts = [0 for x in range(numMonkeys)]
def playRound():
  global numMonkeys,items,counts
  for i in range(numMonkeys):
    if i == 0:
      counts[i] += itemIndexes[i]
      for j in range(len(items[i])):
        item = items[i][j]
        if item == -1:
          break
        wl = item * 5
        if wl % 11 == 0:
            items[6][itemIndexes[6]] = wl
            itemIndexes[6] += 1
        else:
          items[5][itemIndexes[5]] = wl
          itemIndexes[5] += 1
        items[i][j] = -1
      itemIndexes[i] = 0
    elif i == 1:
      for j in range(len(items[i])):
        item = items[i][j]
        if item == -1:
          break
        #counts[i] += 1
        wl = item + 5
        if wl % 19 == 0:
          items[6][itemIndexes[6]] = wl
          itemIndexes[6] += 1
        else:
          items[0][itemIndexes[0]] = wl
          itemIndexes[0] += 1
        items[i][j] = -1
      itemIndexes[i] = 0
    elif i == 2:
      for j in range(len(items[i])):
        item = items[i][j]
        if item == -1:
          break
        #ounts[i] += 1
        wl = item * 19
        if wl % 5 == 0:
          items[3][itemIndexes[3]] = wl
          itemIndexes[3] += 1
        else:
          items[1][itemIndexes[1]] = wl
          itemIndexes[1] += 1
        items[i][j] = -1
      itemIndexes[i] = 0
    elif i == 3:
      for j in range(len(items[i])):
        item = items[i][j]
        if item == -1:
          break
        #counts[i] += 1
        wl = item + 7
        if wl % 3 == 0:
          items[1][itemIndexes[1]] = wl
          itemIndexes[1] += 1
        else:
          items[0][itemIndexes[0]] = wl
          itemIndexes[0] += 1
        items[i][j] = -1
      itemIndexes[i] = 0
    elif i == 4:
      for j in range(len(items[i])):
        item = items[i][j]
        if item == -1:
          break
        #counts[i] += 1
        wl = item + 2
        if wl % 13 == 0:
          items[2][itemIndexes[2]] = wl
          itemIndexes[2] += 1
        else:
          items[7][itemIndexes[7]] = wl
          itemIndexes[7] += 1
        items[i][j] = -1
      itemIndexes[i] = 0
    elif i == 5:
      for j in range(len(items[i])):
        item = items[i][j]
        if item == -1:
          break
        #counts[i] += 1
        wl = item + 1
        if wl % 17 == 0:
          items[4][itemIndexes[4]] = wl
          itemIndexes[4] += 1
        else:
          items[7][itemIndexes[7]] = wl
          itemIndexes[7] += 1
        items[i][j] = -1
      itemIndexes[i] = 0
    elif i == 6:
      for j in range(len(items[i])):
        item = items[i][j]
        if item == -1:
          break
        #counts[i] += 1
        wl = item * item
        if wl % 7 == 0:
          items[5][itemIndexes[5]] = wl
          itemIndexes[5] += 1
        else:
          items[4][itemIndexes[4]] = wl
          itemIndexes[4] += 1
        items[i][j] = -1
      itemIndexes[i] = 0
    elif i == 7:
      counts[i] += itemIndexes[i]
      for j in range(len(items[i])):
        item = items[i][j]
        if item == -1:
          break
        wl = item + 4
        if wl % 2 == 0:
          items[3][itemIndexes[3]] = wl
          itemIndexes[3] += 1
        else:
          items[2][itemIndexes[2]] = wl
          itemIndexes[2] += 1
        items[i][j] = -1
      itemIndexes[i] = 0

m0 = ''
m7 = ''
rounds = 200 # TODO CHANGE TO 10000 ?
for r in range(rounds):
  playRound()
  # just the counts
  #m0 += str(counts[0]) + '\n'
  #m7 += str(counts[7]) + '\n'
 

for i in range(numMonkeys):
  if i == 0 or i == 7:
    print('%s:  %s' % (str(i), str(counts[i])) )
#print('1:\n ' + m1)
print('answer %s' % (counts[0] * counts[7]))

# 0:295 , 7:307

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')