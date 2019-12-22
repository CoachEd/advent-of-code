import sys
import time
import math
from copy import copy, deepcopy
import cProfile, pstats
from io import StringIO

"""
pr = cProfile.Profile()  # create a profile object
pr.enable()  # start profiling
"""

print()
start_secs = time.time()

s = """deal into new stack
cut 9037
deal with increment 49
cut -9932
deal with increment 5
cut 6434
deal with increment 73
cut 1023
deal into new stack
cut 4227
deal with increment 57
cut -6416
deal with increment 48
cut 5020
deal with increment 15
deal into new stack
deal with increment 7
cut -7421
deal with increment 63
cut 6786
deal into new stack
deal with increment 37
cut -6222
deal into new stack
deal with increment 3
cut -4755
deal with increment 31
cut 2694
deal with increment 67
deal into new stack
deal with increment 42
cut 2634
deal into new stack
cut 2358
deal with increment 35
cut 9700
deal with increment 49
cut 264
deal with increment 55
cut 2769
deal with increment 27
cut 593
deal with increment 60
cut -6145
deal into new stack
deal with increment 75
deal into new stack
cut -7065
deal into new stack
cut -2059
deal with increment 30
cut -8773
deal into new stack
deal with increment 60
deal into new stack
deal with increment 22
deal into new stack
cut -2124
deal into new stack
deal with increment 66
cut -6962
deal with increment 31
deal into new stack
deal with increment 48
deal into new stack
deal with increment 62
cut 8716
deal with increment 27
deal into new stack
cut -679
deal into new stack
cut 1069
deal with increment 25
cut 7118
deal into new stack
cut -5787
deal into new stack
cut 9539
deal with increment 11
deal into new stack
deal with increment 49
cut 7631
deal with increment 73
cut -3476
deal into new stack
cut 1401
deal with increment 9
deal into new stack
cut -9773
deal with increment 60
cut 5149
deal with increment 13
cut 5892
deal into new stack
cut 2704
deal with increment 33
cut -3776
deal into new stack
cut -893
deal with increment 11"""

#s = """deal with increment 3"""

arr = s.split('\n')
numcards = 10007
repetitions = 1

deck = [ n for n in range(numcards) ]
len_deck = len(deck)

def deal_into_new_stack():
    global deck
    deck = deck[::-1]

def cut_cards(n):
    global deck
    global len_deck

    if n >= 0:
        l1 = deck[0:n]
        l2 = deck[n:]
    else:
        l2 = deck[n:]
        l1 = deck[0:len_deck+n]
    pos = 0
    for i in range(len(l2)):
        deck[pos] = l2[i]
        pos = pos + 1
    for i in range(len(l1)):
        deck[pos] = l1[i]
        pos = pos + 1

def deal_with_increment(n):
    global len_deck
    global deck

    if n <= 0:
        print('ERROR: n cannot be 0 or negative')
        return

    l1 = [ -1 for n2 in range(len_deck) ]
    pos=0
    l1[pos] = deck[pos]

    for x in deck[1:]:
        placed = False
        while not placed:
            # move pos
            for i in range(n):
                pos = pos + 1
                if pos >= len_deck:
                    pos = 0
            while l1[pos] != -1:
                pos = pos + 1
                if pos >= len_deck:
                    pos = 0


            if l1[pos] == -1:
                l1[pos] = x
                placed = True

    deck.clear()
    deck.extend(l1)

# convert num args in arr
instructions = []
for instr in arr:
    temp = []
    if instr.startswith('deal into'):
        temp.append(instr)
    elif instr.startswith('deal with'):
        arr2 = instr.split(' ')
        temp.extend(arr2[0:3])
        temp.append(int(arr2[3]))
    elif instr.startswith('cut'):
        arr2 = instr.split(' ')
        temp.append(arr2[0])
        temp.append(int(arr2[1]))
    else:
        print('ERROR: invalid instruction: ' + instr)
        sys.exit()
    instructions.append(temp)

for rep in range(repetitions):
    for instr in instructions:
        if len(instr) == 1:
            deal_into_new_stack()
        elif len(instr) == 4:
            deal_with_increment(instr[3])
            pass
        else:
            cut_cards(instr[1])

print(deck[3377])


"""
# print out some stats.
pr.disable()  # end profiling
s = StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
"""

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
