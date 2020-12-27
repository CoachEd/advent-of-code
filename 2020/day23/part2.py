
import sys
import time

start_secs = time.time()

#s = '389125467' # sample
s = '538914762' # puzzle input
arr = [0] * (len(s)+1)
for i in range(0,len(s)):
  idx = int(s[i])  
  if i == len(s)-1:
    arr[idx] = int(s[0])
  else:
    arr[idx] = int(s[i+1])

# add additional
arr2 = [0]*(1000000-9)
i2=10
for i in range(0,len(arr2)):
  if i == len(arr2)-1:
    arr2[i] = int(s[0])
  else:
    arr2[i] = i2+1
    i2 = i2 + 1
arr = arr + arr2
arr[int(s[-1])] = 10

curr_val = int(s[0])  # 3
moves = 10000000
for i in range(1,moves+1):
  if i % 1000000 == 0:
    print('move ' + str(i))

  """
  curr1 = curr_val
  s1 = 'move ' + str(i)+'  '
  for i in range(1,len(arr)):
    s1 = s1 + str(arr[curr1]) + ' '
    curr1 = arr[curr1]
  """
  
  # get curr, and next three vals
  next_val1 = arr[curr_val]  # 8
  next_val2 = arr[next_val1] # 9
  next_val3 = arr[next_val2] # 1

  # find dest
  dest = curr_val - 1
  while dest == 0 or dest == next_val1 or dest == next_val2 or dest == next_val3:
    dest = dest - 1
    if dest < 1:
      dest = 1000000
  
  #s1 = s1 + '  dest: ' + str(dest)
  #print(s1)
  
  
  # place cups
  arr[curr_val] = arr[next_val3]
  temp = arr[dest]
  arr[dest] = next_val1
  arr[next_val3] = temp
  curr_val = arr[curr_val]


print ('final')  # wrong: 374445587660
#curr1 = curr_val
#s1 = ''
#for i in range(1,len(arr)):
#  s1 = s1 + str(arr[curr1]) + ' '
#  curr1 = arr[curr1]
#print(s1)
n1=arr[1]
n2=arr[n1]
print(n1)
print(n2)
print(str(n1*n2))

print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs)+ ' secs ---')
