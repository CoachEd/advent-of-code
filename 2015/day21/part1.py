import sys
import time

start_secs = time.time()
def player_wins(pd,pa,pp,bd,ba,bp):
    # player damage, armor, points, boss damage, armor, points
    while True:
        bp = bp - (pd-ba)
        pp = pp - (bd-pa)
        if bp <= 0 or pp <= 0:
            break
    if bp <= 0:
        return True
    else:
        return False

print()

# Weapons Cost Damage Armor
wstr = """Dagger 8 4 0
Shortsword 10 5 0
Warhammer 25 6 0
Longsword 40 7 0
Greataxe 74 8 0"""

# Armor Cost Damage Armor
astr="""Leather 13 0 1
Chainmail 31 0 2
Splintmail 53 0 3
Bandedmail 75 0 4
Platemail 102 0 5"""

# Rings Cost Damage Armor
rstr="""Damage_+1 25 1 0
Damage_+2 50 2 0
Damage_+3 100 3 0
Defense_+1 20 0 1
Defense_+2 40 0 2
Defense_+3 80 0 3"""

weapons = [] # weapon , cost, damage, armor
arr = wstr.split('\n')
for s in arr:
    tarr = s.split()
    for i in range(1,len(tarr)):
        tarr[i] = int(tarr[i])
    weapons.append(tarr)

armor = [] # armor, cost, damage, armor
arr = astr.split('\n')
for s in arr:
    tarr = s.split()
    for i in range(1,len(tarr)):
        tarr[i] = int(tarr[i])
    armor.append(tarr)
armor.append(['None', 0, 0, 0])

rings = [] # ring, cost, damage, armor
arr = rstr.split('\n')
for s in arr:
    tarr = s.split()
    for i in range(1,len(tarr)):
        tarr[i] = int(tarr[i])
    rings.append(tarr)

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
arr = None
d = dict()
for line in lines: 
    arr = line.strip().replace(': ',':').split(':')
    d[arr[0]] = int(arr[1])

# Boss stats
bpoints = d['Hit Points']
bdamage = d['Damage']
barmor = d['Armor']

# my stat
ppoints = 100
pdamage = 0
parmor = 0
pcost = 0

# 0 rings
mincost = sys.maxsize
for i in range(0,len(weapons)):
    for j in range(0,len(armor)):
        pdamage = weapons[i][2] + armor[j][2]
        parmor = weapons[i][3] + armor[j][3]
        pcost = weapons[i][1] + armor[j][1]
        if player_wins(pdamage,parmor,ppoints,bdamage,barmor,bpoints) and pcost < mincost:
            mincost = pcost

# 1 ring
mincost2 = sys.maxsize
for i in range(0,len(weapons)):
    for j in range(0,len(armor)):
        for k in range(0,len(rings)):
            pdamage =  weapons[i][2] + armor[j][2] + rings[k][2]
            parmor = weapons[i][3] + armor[j][3] + rings[k][3]
            pcost = weapons[i][1] + armor[j][1] + rings[k][1]
            if player_wins(pdamage,parmor,ppoints,bdamage,barmor,bpoints) and pcost < mincost2:
                mincost2 = pcost

# 2 rings
mincost3 = sys.maxsize
for i in range(0,len(weapons)):
    for j in range(0,len(armor)):
        for k in range(0,len(rings)):
            for l in range(0,len(rings)):
                if k == l:
                    continue
                pdamage =  weapons[i][2] + armor[j][2] + rings[k][2] + rings[l][2]
                parmor = weapons[i][3] + armor[j][3] + rings[k][3] + rings[l][3]
                pcost = weapons[i][1] + armor[j][1] + rings[k][1] + rings[l][1]
                if player_wins(pdamage,parmor,ppoints,bdamage,barmor,bpoints) and pcost < mincost3:
                    mincost3 = pcost

costs = [mincost,mincost2,mincost3]
costs.sort()
print('part 1: ' + str(costs[0]))
print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')