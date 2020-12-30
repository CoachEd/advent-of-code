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
        for z in range(1,n+1):
            if z == y or z == x:
                continue
            for w in range(1,n+1):
                if w == y or w == x or w == z:
                    continue
                if not ((x+y+z+w) == n):
                    continue
                factors = [x,y,z,w]
                scores = [0,0,0,0,0]
                for i in range(1, 6):
                    findex = 0
                    for i1 in range(0,len(arr)):
                        ingr = arr[i1]
                        scores[i-1] = scores[i-1] + factors[findex]*ingr[i]
                        findex = findex + 1
                    if scores[i-1] < 0:
                        scores[i-1] = 0
                score =  scores[0] * scores[1] * scores[2] * scores[3]
                if score >= max_score and scores[4] == 500:
                    max_score = score

print('part 2: ' + str(max_score)) 
# part1: # 13882464
#          11162880 too low

print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')