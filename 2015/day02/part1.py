import sys
import time

start_secs = time.time()

# read in input file
l1=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l1.append(line.strip())

tmp = [None]*3
sa = 0
ribbon = 0
for i in range(0,len(l1)):
    arr = l1[i].split('x')
    l = int(arr[0])
    w = int(arr[1])
    h = int(arr[2])
    tmp[0] = l*w
    tmp[1] = w*h
    tmp[2] = h*l
    x = l
    y = w
    small = tmp[0]
    if tmp[1] < tmp[0]:
        x = w
        y = h
        small = tmp[1]
    if tmp[2] < small:
        x = h
        y = l
        small = tmp[2]
    ribbon = ribbon +  l*w*h + 2*x + 2*y
    sa = sa + 2*tmp[0] + 2*tmp[1] + 2*tmp[2] + small

print('Part 1: ' + str(sa))
print('Part 2: ' + str(ribbon))

end_secs = time.time()
print(str(end_secs-start_secs))