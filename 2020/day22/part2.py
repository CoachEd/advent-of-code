import sys
import time

start_secs = time.time()

round = 1
game_num = 1
subgame_num = 1
subgame_round = 1

# read in input file
l=[]
p1=[]
p2=[]
p1_hist = []
p2_hist = []
d1=[]
d2=[]
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

def play_subgame(d1,d2,game_num1,round_num):   
    global game_num
    if len(d1) == 0:
        print('The winner of game ' + str(game_num1) + ' is player 2!')
        return 'p2'
    if len(d2) == 0:
        print('The winner of game ' + str(game_num1) + ' is player 1!')
        return 'p1'

    print('\n-- Round ' + str(round_num) + ' (Game ' + str(game_num1) + ') --')
    print('Player 1\'s deck: ' + str(d1))
    print('Player 2\'s deck: ' + str(d2))

    c1 = d1[0]
    d1 = d1[1:]
    c2 = d2[0]
    d2 = d2[1:]
    print('Player 1 plays: ' + str(c1))
    print('Player 2 plays: ' + str(c2))
    if len(d1) < c1 or len(d2) < c2:
        # classic mode
        if c1 >= c2:
            d1 = d1 + [c1,c2]
            print('Player 1 wins round ' + str(round_num) + ' of game ' + str(game_num1) + '!')
        else:
            d2 = d2 + [c2,c1]
            print('Player 2 wins round ' + str(round_num) + ' of game ' + str(game_num1) + '!')
    else:
        print('Playing a sub-game to determine the winner...\n')
        game_num = game_num + 1
        winner = play_subgame(d1.copy()[:c1],d2.copy()[:c2],game_num1+1,1)
        if winner == 'p1':
            print('The winner of game ' + str(game_num1) + ' is player 1!')
            d1 = d1 + [c1,c2]
        else:
            print('The winner of game ' + str(game_num1) + ' is player 2!')
            d2 = d2 + [c2,c1]

    return play_subgame(d1,d2,game_num1,round_num+1)


def play():
    global p1
    global p2
    global d1
    global d2
    global round
    global game_num
    global subgame_num

    # p1_hist p2_hist
    # if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1.
    if p1 in p1_hist:
        print('INSTANT WIN for p1')
        return 'p1'
    if p2 in p2_hist:
        print('INSTANT WIN for p2')
        return 'p2'        
    if len(p1) == 0:
        print('CLASSIC WIN for p2')
        return 'p2'
    if len(p2) == 0:
        print('CLASSIC WIN for p1')
        return 'p1'

    p1_hist.append(p1)
    p2_hist.append(p2)
    print()
    print('-- Round ' + str(round) + ' (Game ' + str(1) + ') --')
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
            print('Player 1 wins round ' + str(round) + ' of game ' + str(1) + '!')
        else:
            p2 = p2 + [c2,c1]
            print('Player 2 wins round ' + str(round) + ' of game ' + str(1) + '!')     
    else:
        print('Playing a sub-game to determine the winner...\n')
        subgame_num = subgame_num + 1
        subgame_round = 1
        game_num = game_num + 1
        winner = play_subgame(p1.copy()[:c1],p2.copy()[:c2],game_num,1)
        if winner == 'p1':
            p1 = p1 + [c1,c2]
        else:
            p2 = p2 + [c2,c1]
              
    round = round + 1
    print()
    return play()


# main
result = play()
print(p1)
print(p2)

if result == 'p1':
    arr = p1
else:
    arr = p2

score = 0
mult = 1
for i in range(len(arr)-1,-1,-1):
    score = score + arr[i]*mult
    mult = mult + 1
print('part 2: ' + str(score)) 
# 35162 too high
# 31300 too high
# 9428 too low

print()
end_secs = time.time()
print(str(end_secs-start_secs))