import sys
import time

start_secs = time.time()

def count_paths(src):

    if src == max:
        return 1
    num_paths = 0
    left = src+1
    mid = src+2
    right = src+3

    if left in d:
        if left in dcounts:
            num_paths = num_paths + dcounts[left]
        else:
            x = count_paths(left)
            dcounts[left] = x
            num_paths = num_paths + x
    if mid in d:
        if mid in dcounts:
            num_paths =  num_paths + dcounts[mid]
        else:
            x = count_paths(mid)
            dcounts[mid] = x
            num_paths = num_paths + x
    if right in d:
        if right in dcounts:
            num_paths = num_paths + dcounts[right]
        else:
            x = count_paths(right)
            dcounts[right] = x
            num_paths = num_paths + x
    return num_paths

l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(int(line.strip()))

l.sort()
max = l[-1]
d = dict()
dcounts = dict()
for i in range(0,len(l)):
    d[l[i]] = 1

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
print()
print('Part 1: ' + str(ans))
print('Part 2: ' + str(count_paths(0)))

end_secs = time.time()
print()
print(str(end_secs-start_secs))    