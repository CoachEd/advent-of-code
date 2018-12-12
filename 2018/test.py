

import numpy as np

truestr = "00011 00100 01000 01010 01011 01100 01111 10101 10111 11010 11011 11100 11101 11110"

arr1 = truestr.split()
truevals = np.zeros(shape=(len(arr1)))
for i in range(0,len(arr1)):
  truevals[i] = int(arr1[i],2)

print(truevals)
