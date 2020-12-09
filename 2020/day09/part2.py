import sys
import time

start_secs = time.time()
l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(int(line.strip()))

num = 167829540
i=0
sz=0
while True:
    for i in range(0,len(l)):
        if l[i] >= num:
            continue
        sum  = l[i]
        skip = False
        for j in range(i+1,sz):
            if l[j] >= num or sum > num:
                skip=True
                break
            sum = sum + l[j]
        if skip:
            continue
        if sum == num:         
            min1=99999999999999999
            max1=-1
            for i in range(i,j+1):
                if l[i] > max1:
                    max1 = l[i]
                if l[i] < min1:
                    min1 = l[i]
            ans = max1+min1
            print('Part 2: ' + str(ans)) # answer: 28045630
            
            end_secs = time.time()
            print()
            print(str(end_secs-start_secs))
            
            sys.exit()
    sz = sz + 1
