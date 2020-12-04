import sys
import time

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# TODO
passports = []
s1 = ''
for s in l:
  if len(s) > 0:
    s1 = s1 + ' ' + s
  else:
    passports.append(s1.strip())
    s1 = ''

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

validps = 0
for p in passports:
  num = 0
  b1 = p.find('byr:') != -1
  b2 = p.find('iyr:') != -1
  b3 = p.find('eyr:') != -1
  b4 = p.find('hgt:') != -1
  b5 = p.find('hcl:') != -1
  b6 = p.find('ecl:') != -1
  b7 = p.find('pid:') != -1
  b8 = p.find('cid:') != -1

  if b1:
    num = num + 1
  if b2:
    num = num + 1    
  if b3:
    num = num + 1
  if b4:
    num = num + 1
  if b5:
    num = num + 1
  if b6:
    num = num + 1
  if b7:
    num = num + 1
  if b8:
    num = num + 1    
  
  if num == 8 or (num == 7 and not b8):
    validps = validps + 1

print('Part 1: ' + str(validps))
  
end_secs = time.time()
print()
print(str(end_secs-start_secs))