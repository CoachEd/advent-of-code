"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

version_number_sum = 0

def hex2bin(h):
  int_value = int(h, base=16)
  bin_value = bin(int_value)
  s = str(bin_value)[2:]
  while len(s) % 4 != 0:
    s = '0' + s
  return s

def opval(b):
  global version_number_sum
  packet_version = int(b[0:3],2)
  version_number_sum += packet_version
  packet_type_id = int(b[3:6],2)
  length_type_id = b[6]  # I == 0, 15-bit number, number of bits in sub-packets
  if length_type_id == '0':
    # mode 0
    #001110 0 000000000011011 11010001010 0101001000100100 0000000
    #                         11010001010 0101001000100100
    #VVVTTT I LLLLLLLLLLLLLLL AAAAAAAAAAA BBBBBBBBBBBBBBBB
    length_of_subpackets = int(b[7:22],2)
    b1 = b[22:22+length_of_subpackets]
    return b1
  elif length_type_id == '1':
    # mode 1
    # 111 011 1 00000000011 01010000001 10010000010 00110000011 00000
    # VVV TTT I LLLLLLLLLLL AAAAAAAAAAA BBBBBBBBBBB CCCCCCCCCCC
    num_subpackets = int(b[7:18],2)
    litvals =[0 for i in range(num_subpackets)]
    for j in range(num_subpackets):
      subpacket = b[18:29]
      litvals[j] = litval(subpacket)
    return (litvals, 'ignore', 23+(num_subpackets*11))

def litval(b):
  global version_number_sum
  if len(b) == 0:
    return ( 0, '' )
  i = 0
  packet_version = int(b[i:i+3],2)
  version_number_sum += packet_version
  packet_type_id = int(b[i+3:i+6],2)
  i += 6
  # 0011100000000000011011 11010001010 0101001000100100 0000000
  # VVVTTTILLLLLLLLLLLLLLL AAAAAAAAAAA BBBBBBBBBBBBBBBB
  last_group = False
  bstr2 = ''
  while not last_group:
    group_ind = b[i]  # starts with 1, not the last group 
    if group_ind != '1':
      last_group = True
    group = b[i+1:i+5]  # 4 bit group
    bstr2 += group
    i = i + 5

  # any bits to ignore?
  value = int(bstr2,2)
  retval = b[i:]
  rest = b[i:].replace('0','')
  if len(rest) == 0:
    retval = rest
  print(retval)
  return ( value, retval )

"""
def sum_version_numbers(b):
  i = 0
  blen = len(b)
  while True:
    packet_type_id = int(b[i+3:i+6],2)
    if packet_type_id == 4:
      # literval value
      (value , len1) = litval(b[i:])
      #print(value)
    else:
      (value1, value2, len1) = operator(b[i:])
      #print('here1: ' + str(value1) + ',' + str(value2) + ',' + str(len1))

    i += len1
    if i >= blen:
      break
"""

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())


def parse_bin(s):
  if len(s) == 0:
    return ''
  packet_version = int(s[0:3],2)
  packet_type_id = int(s[3:6],2)
  if packet_type_id == 4:
    # literval value
    (value, s) = litval(s)
    print('value: ' + str(value) + '  s: ' + s)
    return s
  else:
    # operator
    # TODO
    s = opval(s)
    return s

# main
s = hex2bin(l[0])
while len(s) > 0:
  s = parse_bin(s)

  






"""
sum_version_numbers(s)
print(version_number_sum)
"""

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
