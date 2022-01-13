"""
AoC
"""
import time

start_secs = time.time()
print('')
num_elves = 3014603

calc_winner = 1
incr = 1
elf_num = 0
for i in range(10,num_elves+1):
  elf_num = elf_num + incr
  #winner = get_winner(i)
  #print('game ' + str(i) + '  Elf ' + str(winner) + ' calc winner: ' + str(elf_num))
  if i == elf_num:
    elf_num = 0
    incr = 1
  if i // 2 == elf_num and i % 2 == 0:
    incr = 2

print(elf_num)

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
