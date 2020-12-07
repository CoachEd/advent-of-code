import sys
import time

start_secs = time.time()

l=[]
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(line.strip())
    
d=dict()
for e in l:
    arr=e.split('bags contain')
    c1=arr[0].strip()
    temp=arr[1].strip()
    temp=temp.replace('bags','').replace('bag','').replace('.','')
    arr2=temp.split(',')  
    arr3=[]
    for e2 in arr2:
        temp2=e2.strip()
        if temp2=='no other':
            arr3.append(temp2)
        else:
            idx=temp2.find(' ')
            num=temp2[0:idx]
            col=temp2[idx+1:]
            arr3.append(col)
    d[c1]=arr3

def findGold(c,seen):
    if c == 'shiny gold':
        return 1
    if c == 'no other':
        return 0
    if c in seen:
        return 0
    seen.append(c)
    arr = d[c]
    num=0
    for c2 in arr:
        num =num+findGold(c2,seen)
    return num

tot=0
for x, y in d.items():
    sarr =[]
    if x == 'shiny gold':
        continue
    n2 = findGold(x,sarr)
    if n2 > 0:
        tot = tot + 1
print(tot)
end_secs = time.time()
print(str(end_secs-start_secs))