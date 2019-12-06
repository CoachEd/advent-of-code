import sys
import time
# WRONG: 264
start_secs = time.time()

def countOrbits(tObj,tOrbits,tList):
    tList.append(tObj)
    if tObj == 'COM':
        return 1
    else:
        return 1 + countOrbits(tOrbits[tObj],tOrbits,tList)

with open('input1.txt') as f:
    content = f.readlines()
arr = [x.strip() for x in content] 

orbits = {}
for orbit in arr:
    x = orbit.split(")")
    orbits[x[1]] = x[0]

you_orbits = []
santa_orbits = []

countOrbits('YOU',orbits,you_orbits)
countOrbits('SAN',orbits,santa_orbits)

print(you_orbits)
print(santa_orbits)

# find intersection
intersecting_obj = ''
for obj in you_orbits:
    if obj in santa_orbits:
        intersecting_obj = obj
        break
print(intersecting_obj)

sum = you_orbits.index(intersecting_obj) - 1
sum = sum + santa_orbits.index(intersecting_obj) - 1
print(sum)

end_secs = time.time()
print()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')