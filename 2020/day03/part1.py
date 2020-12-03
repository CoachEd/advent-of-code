import sys
from random import randrange


l=[None]*323
i=0
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines: 
    str1 = line.strip()
    lt = list(str1*32)
    l[i] = lt
    i = i + 1

x=0
y=0
num =0
while True:
    x = x + 3
    y = y + 1
    if y > 322:
        break
    c = l[y][x]
    if c == '#':
        num = num + 1
        
print('Part 1: ' + str(num))

print()
trees=['\U0001F332','\U0001F333','\U0001F334','\U0001F384']
reset='\x1b[0m'
bgwhite='\x1b[47m'
fgwhite='\x1b[37m'
flat='  '
s = ''

for r in range(0,32):
    for c in range(0,62):
        if l[r][c] == '#':
            s = s + bgwhite+fgwhite+ trees[randrange(len(trees))]
        else:
            s = s + bgwhite+fgwhite+flat
    s = s +reset+ '\n'
print(s) 

sys.stdout.flush()
print()
#print(tree)
#sys.stdout.write('\x1b[37m')

