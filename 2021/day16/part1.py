"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

tot_version_nums = 0

def process_packet(b):
  global tot_version_nums
  i = 0
  packet_version = int(b[i:i+3],2)
  tot_version_nums += packet_version
  packet_type_id = int(b[i+3:i+6],2)
  i += 6
  if packet_type_id == 4:
    # literal value
    # process groups
    last_group = False
    b2 = ''
    while not last_group:
      group_ind = b[i]  # starts with 1, not the last group 
      if group_ind != '1':
        last_group = True
      group = b[i+1:i+5]  # 4 bit group
      b2+= group
      i = i + 5
    value = int(b2,2)
    #print(value) #KEEP
    return b[i:]
  else:
    # operator
    length_type_id = int(b[i],2)
    i += 1
    if length_type_id == 0:
      total_length_bits = int(b[i:i+15],2)
      i += 15
      return process_packet(b[i:i+total_length_bits]) + b[i+total_length_bits:]
    elif length_type_id == 1:
      num_subpackets = int(b[i:i+11],2)
      i += 11
      sp = b[i:]
      for n in range(num_subpackets):
        sp = process_packet(sp)
      return sp

def hex2bin(h):
  int_value = int(h, base=16)
  bin_value = bin(int_value)
  s = str(bin_value)[2:]
  while len(s) % 4 != 0:
    s = '0' + s
  return s

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# main
b = hex2bin(l[0])
while True:
  b = process_packet(b)
  len1 = len(b)
  if len1 == 0 or len1 == b.count('0'):
    break
  
print(tot_version_nums)

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
