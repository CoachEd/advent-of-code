import sys
import time

start_secs = time.time()
print()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
arr = None
d = dict()
for line in lines: 
    arr = line.strip().replace(': ',':').split(':')
    d[arr[0]] = int(arr[1])

"""
Magic Missile, Drain, Shield, Poison, and Recharge.
Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
"""
# Name, cost, duration, damage, healing, plus_mana, armor
spells = [
    ['Magic Missile',53,0,4,0,0,0], # instant
    ['Drain',73,0,2,2,0,0],      # instant
    ['Shield',113,6,0,0,0,7],    # one-time buff
    ['Poison',173,6,3,0,0,0],    # per
    ['Recharge',229,5,0,0,101,0] # per
]
for s in spells:
    print(s)
# Boss stats
bpoints = d['Hit Points']
bdamage = d['Damage']

# Player stats
pmana = 500







print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')