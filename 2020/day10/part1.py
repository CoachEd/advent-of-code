import sys

l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(int(line.strip()))

l.sort()

one=0
three=0
src=0
for i in range(0,len(l)):
    diff = l[i] - src
    if diff == 1:
        one = one + 1
    elif diff == 3:
        three = three+ 1
    src = l[i]

three = three + 1
ans  = one * three
print('part 1: ' + str(ans))