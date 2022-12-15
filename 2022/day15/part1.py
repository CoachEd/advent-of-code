import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# TODO:
# for all sensors
#  find closest beacon
#  determine manhattan distance X to that beacon
#  if the sensor is X away from y=2000000 (above or below):
#    fill matrix with # where other beacons CANNOT be
#
# Add up all #s in line y=2000000




print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')