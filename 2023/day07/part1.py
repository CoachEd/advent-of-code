# Day 7 Part 1
import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION
cards = 'AKQJT98765432'
ranks = {}
points = 13
for c in cards:
  ranks[c] = points
  points -= 1

def handRank(a):
  global cards
  d = {}
  seen = 0
  for i in range(len(cards)):
    n = a.count(cards[i])
    if n > 0:
      seen += n
      d[cards[i]] = n
    if seen == 5:
      break
      
  max_count = -1
  for k,v in d.items():
    if v > max_count:
      max_count = v
  
  m = len(d)
  if m == 1:
    return 7
  elif m == 2:
    if max_count == 4:
      return 6
    else:
      return 5
  elif m == 3:
    if max_count == 3:
      return 4
    else:
      return 3
  elif m == 4:
    return 2
  else:
    return 1

def higherCards(a,b):
  # break tie a > b
  global ranks
  for i in range(len(a)):
    if a[i] == b[i]:
      continue
    else:
      return ranks[a[i]] > ranks[b[i]]

def greater(a,b):
  # if a greater than b return True
  # else return False
  if handRank(a) > handRank(b):
    return True
  elif handRank(b) > handRank(a):
    return False
  elif handRank(b) == handRank(a):
    if higherCards(a,b):
      return True
    else:
      return False
  
def bubbleSort(arr,arr2):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if greater(arr[j],arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
        if not swapped:
            return
  
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

hands = ['' for i in range(len(l))]
bids = [0 for i in range(len(l))]
for i in range(len(l)):
  a = l[i].split()
  hands[i] = a[0]
  bids[i] = int(a[1])
  
bubbleSort(hands,bids)

#print(hands)
#print(bids)
tot = 0
x = 1
for n in bids:
  tot += n * x
  x += 1
print(tot)
 
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
