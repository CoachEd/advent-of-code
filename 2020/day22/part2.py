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

def play_subgame():
    global d1
    global d2
    global subgame_round
    global subgame_num    
    if len(d1) == 0:
        return 'p2'
    if len(d2) == 0:
        return 'p1'

    print()
    print('-- Round ' + str(subgame_round) + ' (Game ' + str(subgame_num) + ') --')
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
            print('Player 1 wins round ' + str(subgame_round) + ' of game ' + str(subgame_num) + '!')
        else:
            d2 = d2 + [c2,c1]
            print('Player 2 wins round ' + str(subgame_round) + ' of game ' + str(subgame_num) + '!')
    else:
        print('Playing a sub-game to determine the winner...')
        subgame_num = subgame_num + 1
        subgame_round = 1        
        winner = play_subgame()
        subgame_num = subgame_num + 1
        if winner == 'p1':
            print('The winner of game ' + str(subgame_num) + ' is player 1!')
            d1 = d1 + [c1,c2]
        else:
            print('The winner of game ' + str(subgame_num) + ' is player 2!')
            d2 = d2 + [c2,c1]
    subgame_round = subgame_round + 1
    return play_subgame()


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
        return 'p2'
    if len(p2) == 0:
        return 'p1'

    p1_hist.append(p1)
    p2_hist.append(p2)

    print()
    print('-- Round ' + str(round) + ' (Game ' + str(game_num) + ') --')
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
            print('Player 1 wins round ' + str(round) + ' of game ' + str(game_num) + '!')
        else:
            p2 = p2 + [c2,c1]
            print('Player 2 wins round ' + str(round) + ' of game ' + str(game_num) + '!')
    else:
        d1 = p1.copy()
        d2 = p2.copy()
        print('Playing a sub-game to determine the winner...')
        subgame_num = subgame_num + 1
        subgame_round = 1
        winner = play_subgame()
        if winner == 'p1':
            p1 = p1 + [c1,c2]
        else:
            p2 = p2 + [c2,c1]
        d1 = []
        d2 = []
    round = round + 1
    print()
    return play()


# main
play()
print(p1)
print(p2)

arr = None
if len(p1) > 0:
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








print()
end_secs = time.time()
print(str(end_secs-start_secs))