"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

def hex2bin(h):
  int_value = int(h, base=16)
  bin_value = bin(int_value)
  s = str(bin_value)[2:]
  while len(s) % 4 != 0:
    s = '0' + s
  return s

def litval(bstr):
  # packet header
  packet_version = int(bstr[0:3],2)
  packet_type_id = int(bstr[3:6],2) # 4 - LITERAL VALUE
  if packet_type_id != 4:
    print('ERROR- not a LIT VALUE: ' + str(bstr))
    sys.exit()
  i = 6
  last_group = False
  bstr2 = ''
  while not last_group:
    group_ind = bstr[i]  # starts with 1, not the last group 
    if group_ind != '1':
      last_group = True
    group = bstr[i+1:i+5]  # 4 bit group
    bstr2 += group
    i = i + 5

  value = int(bstr2,2)
  return value

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())


# literal value example
# 110 100 10111 11110 00101 000
print('')
print('OPERATOR example:')
b = hex2bin('D2FE28')

# packet header
packet_version = int(b[0:3],2)
packet_type_id = int(b[3:6],2) # 4 - LITERAL VALUE

group_ind = b[6]  # starts with 1, not the last group 
group1 = b[7:11]  # 4 bit group
group_ind = b[11]  # starts with 1, not the last group 
group2 = b[12:16]  # 4 bit group
group_ind = b[16]  # starts with 0, last group 
group3 = b[17:21]  # 4 bit group
ignore_group = b[21:]
value = int(group1+group2+group3,2) # 2021


# operator example
# 001 110 0 000000000011011 11010001010 0101001000100100 0000000
# VVV TTT I LLLLLLLLLLLLLLL AAAAAAAAAAA BBBBBBBBBBBBBBBB
print('')
print('OPERATOR example:')
b = hex2bin('38006F45291200')

# packet header
packet_version = int(b[0:3],2) # 1
packet_type_id = int(b[3:6],2) # 6 - OPERATOR
length_type_id = b[6]  # I == 0, 15-bit number, number of bits in sub-packets
length_of_subpackets = b[7:22]   # 27
subpacket1 = b[22:33] # 110 100 01010 parses to: 10
subpacket2 = b[33:49] # 010 100 10001 00100 parses to: 20

print(litval(subpacket1))
print(litval(subpacket2))



end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
