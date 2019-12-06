import sys
import time

start_secs = time.time()

def countOrbits(tObj,tOrbits):
    if tObj == 'COM':
        return 1
    else:
        return 1 + countOrbits(tOrbits[tObj],tOrbits)

with open('input1.txt') as f:  # read in data
    content = f.readlines()
arr = [x.strip() for x in content] 

orbits = {}  # populate the dictionary
for orbit in arr:
    x = orbit.split(")")
    orbits[x[1]] = x[0]

sum = 0  # for each object, count the objects it orbits, both directly and indirectly
for obj in orbits:
    temp = countOrbits(obj,orbits) - 1
    sum = sum + temp

print(sum)

end_secs = time.time()
print()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')