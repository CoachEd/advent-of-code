import sys
import time
import re

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
dallergens = dict()
food = []
for line in lines: 
    line = line.replace(')','').replace('contains ','').replace(', ',',').strip()
    arr = re.split('\(',line.strip())
    ingredients = arr[0].strip().split()
    ingredients.sort()
    allergens = arr[1].strip().split(',')
    allergens.sort()
    food.append([ingredients.copy(),allergens.copy()])

# create list of all allergens
combos = set()
arr = []
for i in range(0,len(food)):
    f = food[i]
    temp_arr = []
    for a in f[1]:
        dallergens[a] = ''
    if 'nuts' in f[1]:
        #print(str(i) + '  ' + str(f[0]) + ' : ' + str(f[1]) )
        #print()
        arr.append(i)

s1 = set(food[arr[0]][0])
for i in range(1,len(arr)):
    s2 = set( food[arr[i]][0] )
    s1 = s1.intersection(s2)
print()
print(s1)

"""THROUGH INTERSECTIONS (e.g., everything that contains soy against each other, then another round of whittling down to get the remaining two items (i.e., comparing any food that had that singular item), we whittle down to:)
soy may be:       {'vkdxfj'}
eggs may be:      {'hn'}
fish IS:          {'dgsdtj'}
peanuts IS:       {'sjcvsr'}
sesame may be:    {'bstzgn'}
shellfish may be: {'kmmqmv'}
nuts:             {'kpksf'}
wheat:            {'bsfqgb'}
"""
found_allergens = ['vkdxfj','hn','dgsdtj','sjcvsr','bstzgn','kmmqmv','kpksf','bsfqgb']
found_allregens_names = ['soy','eggs','fish','peanuts','sesame','shellfish','nuts','wheat']
no_allergens = dict()
count = 0
for f in food:
    for ingr in f[0]:
        if not ingr in found_allergens:
            count = count + 1
print('part 1: ' + str(count))



"""
fish
peanuts
soy
eggs
nuts
sesame
shellfish
wheat
"""



"""unique combos
peanuts|soy|wheat
peanuts|sesame|soy
fish
fish|peanuts|shellfish
eggs|fish|sesame
soy
eggs
shellfish
nuts|peanuts
fish|sesame|shellfish
eggs|shellfish
sesame
eggs|fish|soy
eggs|nuts|peanuts
eggs|fish
fish|wheat
nuts|sesame
eggs|wheat
fish|nuts
sesame|shellfish|soy
eggs|fish|shellfish
eggs|fish|peanuts
fish|nuts|shellfish
peanuts
peanuts|shellfish
peanuts|soy
peanuts|sesame
eggs|nuts|soy
nuts|wheat
eggs|sesame
peanuts|shellfish|wheat
sesame|shellfish
fish|nuts|sesame
fish|soy
"""




#e = a.intersection(b).intersection(c).intersection(d)
#print('possibly soy: ' + str(e))




end_secs = time.time()
print(str(end_secs-start_secs))