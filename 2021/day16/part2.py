"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

def process_packet(b):
  i = 0
  packet_version = int(b[i:i+3],2)
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
    return (value, b[i:])
  else:
    # operator
    length_type_id = int(b[i],2)
    i += 1
    values = []
    rest = ''
    if length_type_id == 0:
      total_length_bits = int(b[i:i+15],2)
      i += 15
      subpackets = b[i:i+total_length_bits]
      rest = b[i+total_length_bits:]
      while True:
        (x,subpackets) = process_packet(subpackets)
        values.append(x)
        if len(subpackets) == 0:
          break
    elif length_type_id == 1:
      num_subpackets = int(b[i:i+11],2)
      i += 11
      subpackets = b[i:]
      for n in range(num_subpackets):
        (x, subpackets) = process_packet(subpackets)
        values.append(x)
      rest = subpackets
    
    if packet_type_id == 0:
      # sum
      result = 0
      for x in values:
        result += x
    elif packet_type_id == 1:
      # product
      result = 1
      for x in values:
        result *= x
    elif packet_type_id == 2:
      values.sort()
      result = values[0]
    elif packet_type_id == 3:
      values.sort()
      result = values[-1]
    elif packet_type_id == 5:
      if values[0] > values[1]:
        result = 1
      else:
        result = 0
    elif packet_type_id == 6:
      if values[0] < values[1]:
        result = 1
      else:
        result = 0
    elif packet_type_id == 7:
      if values[0] == values[1]:
        result = 1
      else:
        result = 0        
    return(result, rest)


def hex2bin(h):
  len1 = len(h*4)
  int_value = int(h, base=16)
  bin_value = bin(int_value)
  s = str(bin_value)[2:]
  while len(s) != len1:
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
(value, b) = process_packet(b)
print(value)
print('')

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
