import sys
import time

start_secs = time.time()
print()

# read in input file
# Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
l=[]
arr=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    line = line.strip().replace(':','').replace(',','').replace('capacity','').replace('durability','').replace('flavor','').replace('texture','').replace('calories','')
    temp = line.split()
    for i in range(1,len(temp)):
        temp[i] = int(temp[i])
    arr.append(temp)

n = 100
max_score = 0
for x in range(1,n+1):
    for y in range(1,n+1):
        if y == x:
            continue

        if not ((x+y) == n):
            continue
        factors = [x,y]
        scores = [0,0,0,0,0]
        for i in range(1, 6):
            findex = 0
            for i1 in range(0,len(arr)):
                ingr = arr[i1]
                scores[i-1] = scores[i-1] + factors[findex]*ingr[i]
                findex = findex + 1
            if scores[i-1] < 0:
                scores[i-1] = 0
        if scores[4] != 500:
            continue
        score =  scores[0] * scores[1] * scores[2] * scores[3]
        if score > max_score:
            max_score = score

print('part 2: ' + str(max_score))

print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')