import sys
import time

start_secs = time.time()
seconds = 2503
print()

# read in input file
# Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
arr=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    line = line.strip().replace('can fly ','').replace('km/s for ','').replace('seconds, but then must rest for ','').replace(' seconds.','')
    arr2 = line.split()
    arr2[1] = int(arr2[1]) # speed
    arr2[2] = int(arr2[2]) # speed duration
    arr2[3] = int(arr2[3]) # rest duration
    arr2.append(0) # distance
    arr2.append(0) # points
    arr.append(arr2)

fr = [None] * len(arr) # flight / rest
n = 0
for r in arr:
    temp = [0]*(seconds+10)
    i = 0
    done = False
    while i < (seconds+10):
        for j in range(0,r[2]):
            if i < len(temp):
                temp[i] = 1 # flying
                i = i + 1
            else:
                done = True
                break
        if done:
            break
        i = i + r[3]
        if i >= len(temp):
            done = True
            break
    fr[n] = temp
    n = n + 1

t = 0
while t < seconds:
    maxd = -1*sys.maxsize
    maxi = -1
    leaders = []
    for i in range(0,len(arr)):
        if fr[i][t] == 1:
            arr[i][4] = arr[i][4] + arr[i][1]
        if arr[i][4] == maxd:
            leaders.append(i)
        if arr[i][4] > maxd:
            maxd = arr[i][4]
            leaders = [i]
    for l in leaders:
        arr[l][5] = arr[l][5] + 1
    t = t + 1

maxp = -1*sys.maxsize
for r in arr:
    print(r)
    if r[5] > maxp:
        maxp = r[5]

print('part 2: ' + str(maxp)) # too low
    







print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')