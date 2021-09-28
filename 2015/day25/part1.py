import sys
import time

start_secs = time.time()
print('')

# To continue, please consult the code grid in the manual.
# Enter the code at row 3010, column 3019.
rows = 6 + 1
cols = 6 + 1
m = [[0 for i in range(cols)] for j in range(rows)]

codes = []
first_code = 20151125
codes.append(first_code)
m[1][1] = first_code

r = 1
c = 1
mr = 6
mc = 6
top_r = 1
top_c = 1
code_num = 0
while True:
  for i in range(top_r, top_r - 1, -1):
    temp_r = top_r
    for j in range(1, top_r + 1):
      code_num = code_num + 1
      print('code ' + str(code_num) + ': ' + str(temp_r) + ',' + str(j))  # index of codes in order
      temp_r = temp_r - 1
  top_r = top_r + 1
  if top_r > mr:
    break

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