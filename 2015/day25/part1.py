import sys
import time

start_secs = time.time()
print('')

# To continue, please consult the code grid in the manual.
# Enter the code at row 3010, column 3019.
maxlen = 8000
rows = maxlen + 1
cols = maxlen + 1
m = [[0 for i in range(cols)] for j in range(rows)]

codes = []


r = 1
c = 1
mr = rows
mc = cols
top_r = 1
top_c = 1
code_num = 0
while True:
  for i in range(top_r, top_r - 1, -1):
    temp_r = top_r
    for j in range(1, top_r + 1):
      r1 = temp_r
      c1 = j
      #print('code ' + str(code_num) + ': ' + str(temp_r) + ',' + str(j))  # index of codes in order

      val = 0
      #print(str(r1) + ',' + str(c1))
      if code_num == 0:
        val = 20151125
      else:
        # ted by taking the previous one, multiplying it by 252533, 
        # and then keeping the remainder from dividing that value by 33554393.
        val = (codes[code_num - 1] * 252533) % 33554393
      
      if r1 < rows and c1 < cols:
        m[r1][c1] = val
      codes.append(val)

      if r1 == 3010 and c1 == 3019:
        print(val)
        break
      code_num = code_num + 1
      temp_r = temp_r - 1
  top_r = top_r + 1
  if top_r > mr:
    break

"""
str1 = ''
for r in m:
  for c in r:
    str1 = str1 + str(c) + ' '
  str1 = str1 + '\n'
print(str1)
"""

# e.g.,
"""
code 1: 1,1
code 2: 2,1
code 3: 1,2
code 4: 3,1
code 5: 2,2
code 6: 1,3
code 7: 4,1
code 8: 3,2
code 9: 2,3
code 10: 1,4
code 11: 5,1
code 12: 4,2
code 13: 3,3
code 14: 2,4
code 15: 1,5
code 16: 6,1
code 17: 5,2
code 18: 4,3
code 19: 3,4
code 20: 2,5
code 21: 1,6
.
.
.
"""







print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')