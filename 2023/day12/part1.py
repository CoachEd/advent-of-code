import time
import sys
from copy import copy, deepcopy
import itertools as IT

# read in input file
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()


def isMatch(p,s):
  # p is the pattern to match:
  #                ?###????????
  # s is a potential
  #  match         .###.##..#..
  #  no match:     ###.##.....#
  # return True/False
  # TODO: See https://stackoverflow.com/questions/4697882/how-can-i-find-all-matches-to-a-regular-expression-in-python
  return False

def arrangements(a,n):
  # arrangements of groups must always have one '.' between them at minimum
  # a is the array of int sizes: [3,2,1]
  # n is length of string
  # example for [3,2,1],12
  #             .###.##...#.
  # return array of all possible arrangements (even ones )
  s = ''
  for i in range(len(a)):
    s = s + '#' * a[i]
    if i < len(a)-1:
      s += '.'
  
  #  ###.##.#  need to randomly add '.' to make it long enough to meet size n

  # 2 balls into 3 slots is like...
  # 2 balls around 2 sticks (always one fewer stick than slots)
  # so 4 choose 2
  # list(IT.combinations(range(4), 2))
  # [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
  num_balls = n - len(s)
  slots = len(a) + 1
  x = list(IT.combinations(range(num_balls), slots))

  # s is ###.##.# (len 8)
  # max len 12
  # bins = 4
  # num_balls = 4
  # possibles: (4,0,0,0), (3,1,0,0), (0,0,3,1), (0,0,0,4) HOW?
  # REGEX? for ###.##.# ? 

  # return array of possibles
  #(4,0,0,0) (3,1,0,0) (2,2,0,0) 
  #a2 = list(IT.permutations(range(4), 3))
  #print(a2)
# [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

  l = ['###','##','#','.','.','.','.','.','.']
  perms = list(IT.permutations(l))
  permsu = set()
  for p in perms:
    permsu.add(''.join(p))

  for p in permsu:
    print(p)
  print()
  print(len(permsu))
  return a


# SOLUTION START - start timing
start_secs = time.time()
# TODO


arrangements([3,2,1],12)

  

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing