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

# {'Hit Points': 103, 'Damage': 9, 'Armor': 2}
print(d)


print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')