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
ecolors = 'amb blu brn gry grn hzl oth'
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
  
  if not (num == 8 or (num == 7 and not b8)):
    continue

  arr = p.split(' ')
  d = dict()
  for f in arr:
    arr2 = f.split(':')
    d[arr2[0]] = arr2[1]
  
  if not (d['byr'].isdigit() and int(d['byr']) >= 1920 and int(d['byr']) <= 2002):
    continue
  if not (d['iyr'].isdigit() and int(d['iyr']) >= 2010 and int(d['iyr']) <= 2020):
    continue
  if not (d['eyr'].isdigit() and int(d['eyr']) >= 2020 and int(d['eyr']) <= 2030):
    continue  

  if not(d['hgt'].find('cm') != -1 or d['hgt'].find('in') != -1):
    continue
  
  units = d['hgt'][-2:]
  d['hgt'] = int(d['hgt'][:-2])
  if units == 'cm':
    #at least 150 and at most 193
    if not(d['hgt'] >= 150 and d['hgt'] <= 193):
      continue
  if units == 'in':
    #at least 59 and at most 76
    if not(d['hgt'] >= 59 and d['hgt'] <= 76):
      continue
    
  # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
  h = d['hcl']
  if not (h[0] == '#'):
    continue
  if not (len(h) == 7):
    continue
  if not h[1:].isalnum():
    continue
  
  #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
  if len(d['ecl']) != 3:
    continue
  if ecolors.find(d['ecl']) == -1:
    continue
  
  #pid (Passport ID) - a nine-digit number, including leading zeroes
  if not (len(d['pid']) == 9 and d['pid'].isdigit()):
    continue
  
  #cid (Country ID) - ignored, missing or not
  
  # made it here, valid
  validps = validps + 1



print('Part 2: ' + str(validps))
  
end_secs = time.time()
print()
print(str(end_secs-start_secs))