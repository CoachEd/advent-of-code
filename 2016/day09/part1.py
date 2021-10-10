"""
AoC
"""
import time

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0]
s1 = ''
i = 0
while i < len(s):
  c = s[i]
  if c != '(':
    s1 += c
    i += 1
  else:
    i2 = s.find(')',i)
    if i2 == -1:
      s1 += s[i:]
      break # remaining characters are just end of string
    else:
      # get marker
      marker = s[i+1:i2]
      marr = marker.split('x')
      nlen = int(marr[0])
      nrep = int(marr[1])
      stemp = s[i2+1:i2+1+nlen]
      for j in range(nrep):
        s1 += stemp
      i = i2 + nlen + 1
      
print(len(s1))

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
