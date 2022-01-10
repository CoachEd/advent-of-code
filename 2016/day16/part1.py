"""
AoC
"""
import time
import sys

start_secs = time.time()
print('')

# test data
initial_state = '10000'
disk_length = 20

# real data
initial_state = '10111011111001111'
disk_length = 272

arr = [ -1 for i in range(disk_length*2) ]

def get_checksum(arr, n):
  while True:
    s = ''
    for i in range(0,n-1,2):
      if arr[i] == arr[i+1]:
        s += '1'
      else:
        s += '0'
    if len(s) % 2 != 0:
      break
    arr = [ int(c) for c in s ]
    n = len(arr)
  
  return s

def dragon_curve(a,len_state, n):
  new_len = -1
  while new_len < n:
    idx2 = len_state + 1
    for i in range(len_state-1,-1,-1):
      b = a[i]
      if b == 0:
        b = 1
      else:
        b = 0
      a[idx2] = b
      idx2 += 1
    a[len_state] = 0
    new_len = len_state * 2 + 1
    len_state = new_len

# test
for i in range(len(initial_state)):
  arr[i] = int(initial_state[i])

dragon_curve(arr, len(initial_state), disk_length)
print( get_checksum(arr,disk_length) )

#idx = arr.index(-1)
#print( arr[0:idx] )


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
