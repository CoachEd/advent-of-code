import sys
import time
from random import randrange

start_secs = time.time()

print()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
arr = None
d = dict()
for line in lines: 
    arr = line.strip().replace(': ',':').split(':')
    d[arr[0]] = int(arr[1])

"""
Magic Missile, Drain, Shield, Poison, and Recharge.
Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
"""
# Name, cost, duration, timer, damage, healing, plus_mana, armor, repeat effect
spells = [
    ['Magic Missile',53,0,0,4,0,0,0,False], # instant
    ['Drain',73,0,0,2,2,0,0,False],      # instant
    ['Shield',113,6,0,0,0,0,7,False],    # effect one-time boost
    ['Poison',173,6,0,3,0,0,0,True],    # effect repeating
    ['Recharge',229,5,0,0,0,101,0,True] # effect repeating
]

# Boss stats
bpoints = d['Hit Points']
bdamage = d['Damage']

# Player stats
pmana = 500
ppoints = 50
parmor = 0
pmana_spent = 0

def get_move_interactive():
    global spells
    global bpoints
    global bdamage
    global ppoints
    global pmana
    global pmana_spent
    global parmor
    
    move = input("move? (  0-magic missile  1-drain  2-shield  3-poison  4-recharge  ) ")
    return int(move)

"""
test_moves = None
def get_move():
    global spells
    global bpoints
    global bdamage
    global ppoints
    global pmana
    global pmana_spent
    global parmor
    global test_moves
    return test_moves.pop(0)
"""

# play game
min_mana = sys.maxsize
min_moves = []
min_str = ''
moves_played = 0
def play_game():
    global spells
    global bpoints
    global bdamage
    global ppoints
    global pmana
    global pmana_spent
    global parmor
    global min_mana
    global min_str
    global min_moves
    global moves_played
    global d

    # Name, cost, duration, timer, damage, healing, plus_mana, armor, repeat effect
    spells = [
        ['Magic Missile',53,0,0,4,0,0,0,False], # instant
        ['Drain',73,0,0,2,2,0,0,False],      # instant
        ['Shield',113,6,0,0,0,0,7,False],    # effect one-time boost
        ['Poison',173,6,0,3,0,0,0,True],    # effect repeating
        ['Recharge',229,5,0,0,0,101,0,True] # effect repeating
    ]
    

    #test_moves = [3, 4, 2, 3, 4, 2, 3, 4, 2, 0, 3, 0]
    test_moves = [2,4,3,     2,4,3, 2,4,3,   2, 4,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    test_moves[0] = randrange(5) # YES!!! starting with 3 yielded 1824!!!
    test_moves[1] = randrange(5)
    test_moves[2] = randrange(5) # 0:1990 1:bad 3:1937

    test_moves[3] = randrange(5)
    test_moves[4] = randrange(5)
    test_moves[5] = randrange(5)

    test_moves[6] = randrange(5)
    test_moves[7] = randrange(5)
    test_moves[8] = randrange(5)

    test_moves[9] = randrange(5)
 
    test_moves[10] = randrange(5)
    test_moves[11] = randrange(5)
    test_moves[12] = randrange(5)
    test_moves[13] = randrange(5)
    test_moves[14] = randrange(5)
    test_moves[15] = randrange(5)
    test_moves[16] = randrange(5)
    test_moves[17] = randrange(5)
    test_moves[18] = randrange(5)
    test_moves[19] = randrange(5)
    test_moves[20] = randrange(5)
    test_moves[21] = randrange(5)
    test_moves[22] = randrange(5)
    test_moves[23] = randrange(5)
    test_moves[24] = randrange(5)
    test_moves[25] = randrange(5)
    test_moves[26] = randrange(5)
    test_moves[27] = randrange(5)
    test_moves[28] = randrange(5)
    test_moves[29] = randrange(5)
    test_moves[30] = randrange(5)
    temp_str = str(test_moves)

    # Boss stats
    bpoints = d['Hit Points']
    bdamage = d['Damage']

    # Player stats
    pmana = 500
    ppoints = 50
    parmor = 0
    pmana_spent = 0    
    temp_moves_played = 0
    while True:
        
        # PLAYER TURN
        ##print('-- Player turn --')
        ##print('- Player has ' + str(ppoints) + ' hit points, ' +  str(parmor) + ' armor, ' + str(pmana) + ' mana')
        ##print('- Boss has ' + str(bpoints) + ' hit points')
        
        # apply shield effect


        ppoints = ppoints - 1 #PART 2
        if ppoints <= 0:
            ##print('player lost on hit points')
            break
            


        eff = spells[2]
        if eff[3] > 0:
            eff[3] = eff[3] - 1
            ##print('Shield\'s timer is now ' + str(eff[3]) + '.')
            if eff[3] == 0:
                ##print('Shield wears off, decreasing armor by 7.')
                parmor = 0
            else:            
                parmor = eff[7]
            
        # apply poison effect
        eff = spells[3]
        if eff[3] > 0:
            eff[3] = eff[3] - 1
            ##print('Poison deals ' + str(eff[4]) +' damage; its timer is now ' + str(eff[3]) + '.')
            if eff[3] == 0:
                ##print('Poision wears off.')
                pass
            bpoints = bpoints - eff[4]
        
        # apply recharge effect
        eff = spells[4]
        if eff[3] > 0:
            eff[3] = eff[3] - 1
            ##print('Recharge provides ' + str(eff[6]) + ' mana; its timer is now ' + str(eff[3]) + '.')        
            if eff[3] == 0:
                ##print('Recharge wears off.')      
                pass  
            pmana = pmana + eff[6]

        if bpoints <= 0:
            ##print('player WON. mana spent: ' + str(pmana_spent))
            if pmana_spent < min_mana:
                min_mana = pmana_spent
                min_str = temp_str
                moves_played = temp_moves_played
                #min_moves = test_moves.copy()
            break
        if ppoints <= 0:
            ##print('player lost on hit points')
            break
        if pmana <= 0:
            ##print('player lost on mana')
            break

        """
        Name, 
        cost, 
        duration, 
        timer, 
        damage, 
        healing,
        plus_mana, 
        armor, 
        repeat effect
        """

        # process new move

        #move = get_move()
        move = test_moves.pop(0)
        temp_moves_played = temp_moves_played + 1
        
        spell = spells[move]
        if spell[3] > 0:
            #print("can't cast effect if already in effect")
            break
            
        if pmana < spell[1]:
            ##print("can't afford spell. lose turn!!")
            # boss turn
            battack = bdamage - parmor
            if battack <= 0:
                battack = 1
            ppoints = ppoints - battack    
            break

        if move == 0:
            # magic missile
            ##print('Player casts ' + spell[0] + ', dealing ' + str(spell[4]) + ' damage.')
            pmana = pmana - spell[1]
            bpoints = bpoints - spell[4] # instant
            pmana_spent = pmana_spent + spell[1]
        elif move == 1:
            # drain
            ##print('Player casts Drain, dealing ' + str(spell[4])  + ' damage, and healing ' + str(spell[5]) +' hit points.')
            pmana = pmana - spell[1] # instant
            pmana_spent = pmana_spent + spell[1]
            bpoints = bpoints - spell[4]
            ppoints = ppoints + spell[5]
        elif move == 2:
            # shield
            ##print('Player casts ' + spell[0] + ', increasing armor by ' + str(spell[7]) + '.')
            pmana = pmana - spell[1]
            pmana_spent = pmana_spent + spell[1]
            parmor = spell[7]
            spell[3] = spell[2] # instant start
        elif move == 3:
            # poison
            ##print('Player casts ' + spell[0] +'.')
            pmana = pmana - spell[1]
            pmana_spent = pmana_spent + spell[1]
            spell[3] = spell[2]
        elif move == 4:
            # recharge
            ##print('Player casts ' + spell[0] +'.')
            pmana = pmana - spell[1]
            pmana_spent = pmana_spent + spell[1]
            spell[3] = spell[2]

        # BOSS TURN
        # player effects
        # apply shield effect
        ##print('\n-- Boss turn --')
        ##print('- Player has ' + str(ppoints) + ' hit points, ' +  str(parmor) + ' armor, ' + str(pmana) + ' mana')
        ##print('- Boss has ' + str(bpoints) + ' hit points')        
        eff = spells[2]
        if eff[3] > 0:
            eff[3] = eff[3] - 1
            ##print('Shield\'s timer is now ' + str(eff[3]) + '.')
            if eff[3] == 0:
                ##print('Shield wears off, decreasing armor by 7.')        
                parmor = 0
            else:
                parmor = eff[7]
            
        # apply poison effect
        eff = spells[3]
        if eff[3] > 0:
            eff[3] = eff[3] - 1
            ##print('Poison deals ' + str(eff[4]) +' damage; its timer is now ' + str(eff[3]) + '.')
            bpoints = bpoints - eff[4]
            if eff[3] == 0:
                ##print('Poision wears off.')    
                pass    
        
        # apply recharge effect
        eff = spells[4]
        if eff[3] > 0:
            eff[3] = eff[3] - 1
            ##print('Recharge provides ' + str(eff[6]) + ' mana; its timer is now ' + str(eff[3]) + '.')   
            if eff[3] == 0:
                ##print('Recharge wears off.')   
                pass     
            pmana = pmana + eff[6]
        
        if bpoints <= 0:
            ##print('player WON. mana spent: ' + str(pmana_spent))
            if pmana_spent < min_mana:
                min_mana = pmana_spent 
                min_str = temp_str    
                moves_played = temp_moves_played  
                #min_moves = test_moves.copy()     
            break
        if ppoints <= 0:
            ##print('player lost on hit points')
            break
        if pmana <= 0:
            ##print('player lost on mana')
            break
        
        battack = bdamage - parmor
        if battack <= 0:
            battack = 1
        ppoints = ppoints - battack
        ##print('Boss attacks for ' + str(battack) +' damage.')
        ##print()


for i in range(0,5000000):
    play_game()

#print(str(min_moves))
print(min_str)
print(moves_played)
print('part 1: ' + str(min_mana)) # 1824 CORRECT!!

##print()
##print('part 1 mana spent: ' + str(pmana_spent))
# 2226 too high
# 1957 too high
# 1831 too high
# 1489 INCORRECT
# 1429 INCORRECT


print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')