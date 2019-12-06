import sys
import time

start_secs = time.time()

def countOrbits(tObj,tOrbits,tList):
    tList.append(tObj)
    if tObj == 'COM':
        return
    else:
        return countOrbits(tOrbits[tObj],tOrbits,tList)

with open('input1.txt') as f:
    content = f.readlines()
arr = [x.strip() for x in content] 

orbits = {}
for orbit in arr:
    x = orbit.split(")")
    orbits[x[1]] = x[0]

you_orbits = []
santa_orbits = []

countOrbits('YOU',orbits,you_orbits)  # get the objects YOU orbit
countOrbits('SAN',orbits,santa_orbits)  # get the objects SAN orbits

# find intersection where the YOU and SAN paths meet
intersecting_obj = ''
for obj in you_orbits:
    if obj in santa_orbits:
        intersecting_obj = obj
        break
print('\n' + intersecting_obj)

sum = you_orbits.index(intersecting_obj) - 1  # sum my orbits back to the intersection
sum = sum + santa_orbits.index(intersecting_obj) - 1  # add on SAN's orbits back to the intersection
print(sum)

end_secs = time.time()
print('\nelapsed time: ' + str(end_secs - start_secs) + ' seconds')