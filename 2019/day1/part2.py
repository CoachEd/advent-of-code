import math

# EASY- took 15 mins to solve both parts. This part required recursion and one edge case.
def calc(f):
  if (f < 0):
      return 0
  curr_fuel = math.trunc(f/3) - 2
  if (curr_fuel > 0):
      return curr_fuel + calc(curr_fuel) 
  else:
      return 0

with open('input1.txt') as f:
    content = f.readlines()
arr = [x.strip() for x in content] 

# to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
sum = 0
for num in arr:
    n = int(num)
    sum = sum  + calc(n)

print(sum)


