import sys

# read in input file
l=[]
p1=[]
p2=[]
game_num=1
found_p2 = False
my_file = open('inp.txt', 'r')
lines = my_file.readlines()
for line in lines:
    line = line.strip()
    if len(line) == 0:
        continue
    if 'Player 2' in line:
        found_p2 = True
        continue
    if 'Player 1' in line:
        continue
    if found_p2:
        p2.append(int(line))
    else:
        p1.append(int(line))

def playgame(p1,p2):
    global game_num

    p1_hist = []
    p2_hist = []

    gameno = game_num
    round=1
    while True:
        if len(p1) == 0:
            return ['p2',p2]
        if len(p2) == 0:
            return ['p1',p1]

        if p1 in p1_hist:
            #print('INSTANT WIN for p1')
            #print(p1)
            return ['p1',p1]
        if p2 in p1_hist:
            return ['p1',p1]
        
        p1_hist.append(p1)
        p2_hist.append(p2)

        print()

        print('-- Round ' + str(round) + ' (Game ' + str(gameno) + ') --')
        print('Player 1\'s deck: ' + str(p1))
        print('Player 2\'s deck: ' + str(p2))

        c1 = p1[0]
        p1 = p1[1:]
        c2 = p2[0]
        p2 = p2[1:]
        
        print('Player 1 plays: ' + str(c1))
        print('Player 2 plays: ' + str(c2))
        
        if len(p1) < c1 or len(p2) < c2:
            # classic mode
            if c1 >= c2:
                p1 = p1 + [c1,c2]
                print('Player 1 wins round ' + str(round) + ' of game ' + str(gameno) + '!')
            else:
                p2 = p2 + [c2,c1]
                print('Player 2 wins round ' + str(round) + ' of game ' + str(gameno) + '!')
        else:
            # recursive mode
            print('Playing a sub-game to determine the winner...\n')
            game_num = game_num + 1
            winner = playgame(p1.copy()[:c1],p2.copy()[:c2])
            if winner[0] == 'p1':
                p1 = p1 + [c1,c2]
            else:
                p2 = p2 + [c2,c1]
        
        #print()     
        round = round + 1

result = playgame(p1,p2)
winner = result[0]
arr = result[1]


"""
[46, 24, 50, 10, 47, 21, 36, 16, 31, 27]
p1:
[23, 32, 46, 47, 27, 35, 1, 16, 37, 50, 15, 11, 14, 31, 4, 38, 21, 39, 26, 22, 3, 2, 8, 45, 19]
p2:
[13, 20, 12, 28, 9, 10, 30, 25, 18, 36, 48, 41, 29, 24, 49, 33, 44, 40, 6, 34, 7, 43, 42, 17, 5]
arr:
[32, 46, 47, 27, 35, 1, 16, 37, 50, 15, 11, 14, 31, 4, 38, 21, 39, 26, 22, 3, 2, 8, 45, 19]
"""
# 35162 too high
# 31300 too high
# 9428 too low
# 30891

score = 0
mult = 1
for i in range(len(arr)-1,-1,-1):
    score = score + arr[i]*mult
    mult = mult + 1
print()
print('part 2: ' + str(score)) 
print()
