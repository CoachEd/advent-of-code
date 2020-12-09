import sys

l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(int(line.strip()))

sums=dict()
for x in range(0,24):
    tmp=[]
    for y in range(x+1,25):
        tmp.append(l[x]+l[y])
    sums[x] = tmp

for i in range (25,len(l)):
    found=False
    for j in range(i-25,i-1):
        arr=sums[j]
        if l[i] in arr:
            found=True
            break
    if not found:
        print(l[i])
        break
    del sums[i-25]
    sums[i-1]=[]
    for x in range(i-25+1,i):
        sums[x].append(l[x]+l[i])

        