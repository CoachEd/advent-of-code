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
# only consider sensors that y value is at most 9 spots above and 9 spots below the
# line we are checking (i.e., y=2000000)
# for each sensor in that range, calculate the beacon it sees and where the beacon cannot be for that sensor
# do the same for each sensor.
# count up the # symbols on line y=2000000




print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')