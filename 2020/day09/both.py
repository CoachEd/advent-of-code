import sys
import time

start_secs = time.time()
len1 = 1000 # from input file
l=[None]*len1
ans = 0

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for i in range(0,len1):
    l[i] = int(Lines[i].strip())

sums=dict()
for x in range(0,24):
    tmp=[None] * (25-(x+1))
    idx = 0
    for y in range(x+1,25):
        tmp[idx] = l[x]+l[y]
        idx = idx + 1
    sums[x] = tmp

for i in range (25,len1):
    found=False
    for j in range(i-25,i-1):
        arr=sums[j]
        if l[i] in arr:
            found=True
            break
    if not found:
        ans = l[i]
        print('Part 1: ' + str(l[i])) # answer: 167829540
        break
    del sums[i-25]
    sums[i-1]=[]
    for x in range(i-25+1,i):
        sums[x].append(l[x]+l[i])

# Part 2
num = ans
done = False
for i in range(0,len1-1):
    sum = l[i]
    for j in range(i+1,len1):
        sum = sum + l[j]
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
            done = True     
            break
        elif sum > num:
            break
    if done:
        break

end_secs = time.time()
print(str(end_secs-start_secs))            
sys.exit()
        


