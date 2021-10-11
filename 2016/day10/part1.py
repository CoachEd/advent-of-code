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

# bots 0 - 209; no negative values
# bot 99 gives low to bot 194 and high to bot 171

# bot 195 gives low to output 4 and high to bot 130
# bot 130 gives low to output 1 and high to output 13

# value 61 goes to bot 49
instr = [ [-1,-1] for x in range(210)] # low high destinations for each bot
low = [-1 for x in range(210)]
high = [-1 for x in range(210)]
out = [-1 for x in range(21)] # 20 output bins
for s in l:
  arr = s.split()
  if arr[0] == 'bot':
    botnum = int(arr[1])
    dest1 = arr[5]
    dest1num = int(arr[6])
    dest2 = arr[10]
    dest2num = int(arr[11])
    instr[botnum][0] = [dest1, dest1num] # low
    instr[botnum][1] = [dest2, dest2num] # high
  elif arr[0] == 'value':
    val = int(arr[1])
    bot = int(arr[5])
    # store in low if first time
    if low[bot] == -1:
      low[bot] = val
    else:
      if val > low[bot]:
        high[bot] = val
      else:
        tmp = low[bot]
        low[bot] = val
        high[bot] = tmp


done = False
while not done:
  done = True
  for i in range(len(low)):
    if low[i] != -1 and high[i] != -1:
      # a bot has two values
      done = False
      
      # process low
      lowdest = instr[i][0]
      if lowdest[0] == 'output':
        out[lowdest[1]] = low[i]
        low[i] = -1
      else:
        # is low bot ready to receive?
        swapflag = False
        if low[lowdest[1]] == -1:
          low[lowdest[1]] = low[i]
          low[i] = -1
          swapflag = True
        elif high[lowdest[1]] == -1:
          high[lowdest[1]] = low[i]
          low[i] = -1
          swapflag = True
        if swapflag and low[lowdest[1]] != -1 and high[lowdest[1]] != -1:
          if (low[lowdest[1]] == 17 and high[lowdest[1]] == 61) or (low[lowdest[1]] == 61 and high[lowdest[1]] == 17):
            print(lowdest[1])
          if low[lowdest[1]] > high[lowdest[1]]:
            temp = low[lowdest[1]]
            low[lowdest[1]] = high[lowdest[1]]
            high[lowdest[1]] = temp

      # process high
      highdest = instr[i][1]
      if highdest[0] == 'output':
        out[highdest[1]] = high[i]
        high[i] = -1
      else:      
        # is high bot ready to receive?
        swapflag = False
        if low[highdest[1]] == -1:
          low[highdest[1]] = high[i]
          high[i] = -1
          swapflag = True
        elif high[highdest[1]] == -1:
          high[highdest[1]] = high[i]
          high[i] = -1
          swapflag = True
        if swapflag and low[highdest[1]] != -1 and high[highdest[1]] != -1:
          if (low[highdest[1]] == 17 and high[highdest[1]] == 61) or (low[highdest[1]] == 61 and high[highdest[1]] == 17):
            print(highdest[1])
          if low[highdest[1]] > high[highdest[1]]:
            temp = low[highdest[1]]
            low[highdest[1]] = high[highdest[1]]
            high[highdest[1]] = temp





    
# Wrong: 59



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
