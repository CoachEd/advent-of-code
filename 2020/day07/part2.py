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
            arr3.append(col+':'+num)
    d[c1]=arr3

def countBags(qty,c):
    arr=d[c]
    if arr[0] == 'no other':
        return 0
    num = 0
    for e in arr:
        if arr[0] != 'no other':
            arr2=e.split(':')
            n = int(arr2[1])
            c1=arr2[0]
            num = num + n + n*countBags(qty,c1)
    return num

bags = countBags(1,'shiny gold')
print(bags)
end_secs = time.time()
print(str(end_secs-start_secs))
        
    
        
       
