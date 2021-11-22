#bachpan vala snake water gun game

#importing ramdom for making ramdom choises interms of computer
import random


#Defining rules:
def game_win(comp, player):
    if comp == player:
        return None

    if comp == 's':
        if player == 'w':
            return True
        elif comp == 'w':
            return False
    
    if comp == 'w':
        if player == 's':
            return False
        elif player == 'g':
            return True
    
    if comp == 'g':
        if player == 'w':
            return False
        elif player == 's':
            return True
    
    




comp = print("Choose either of them: Snake(s), Water(w) & Gun(g):")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == '3':
    comp = 'g'

# WARNING!!
# SECERT RECEIPE TO WIN THE EVERY MATCH, DO NOT REMOVE THIS '#' IN BELOW LINE XD
# print(comp)

player = input("Choose either of them: Snake(s), Water(w) & Gun(g):\n ")
# print(player)

win_condition = game_win(comp, player)

#for fair game
print(f'Computer choose: {comp}')
print(f'You choose: {player }')
if win_condition == None:
    print('Game is a TIE!!')
elif win_condition == True:
    print('Computer Won')
else:
    print('Player Wins!')