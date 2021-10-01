import sys
import time

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# TODO
total = 0
for s in l:
  i1 = s.rindex('-')
  i2 = s.rindex('[')
  nm = s[0:i1]
  sc = int(s[i1+1:i2])
  cs = s[i2+1:len(s)-1]

  # TEST: make sure all checksum characters are in name
  d = {}
  valid = True
  for c in cs:
    d[c] = nm.count(c)
    if d[c] == 0:
      valid = False
      break
  if not valid:
    continue  # some checksum characters not found in name

  # TEST: look at each letter of checksum; later counts cannot be bigger than earlier counts
  first_time = True
  prev_c = ''
  prev_count = 0
  last_pos = -1
  last_count = -1
  for c in cs:
    i = nm.index(c)
    if first_time:
      # first time
      first_time = False
      prev_c = c
      prev_count = d[c]
    else:
      if d[c] > prev_count:
        valid = False  # later checksum count cannot be greater than earlier checksum count
        break
      elif d[c] == prev_count and ord(prev_c) > ord(c):
        valid = False  # tie, but later checksum car comes before earlier char alphabetically
        break
      prev_c = c
      prev_count = d[c]
    if i > last_pos:
      last_pos = i
      last_count = d[c]
  if not valid:
    continue

  # made it here, then valid!
  total = total + sc

# OUTPUT result
print(total)  # WRONG: 50583 (too low), 280724 (too high)



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')