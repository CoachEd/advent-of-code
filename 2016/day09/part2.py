"""
AoC
"""
import time

start_secs = time.time()
print('')

def decomp(s):
  s1 = ''
  i = 0
  while i < len(s):
    c = s[i]
    if c != '(':
      i3 = s.find('(',i)
      if i3 == -1:
        s1 += s[i:]
        break
      else:
        s1 += s[i:i3]
        i = i3
        continue
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
  return s1  

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0]

while True:
  s1 = decomp(s)
  if s1.find(')') == -1:
    break
  s = s1
  print(len(s1))

   
print(len(s1))

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
