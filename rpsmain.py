import random

def play_r():
    user = input("What's your choice \n'r' for rock , 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return [0 , computer]
    
    if is_win(user,computer):
        return [1,computer]
    
    return [2,computer]


def is_win(player,opponent):
  #Decide Winner for a round
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def play():
    #Main Game Controller Function
    rounds = 3
    win = 0
    lost = 0
    while(rounds!=0):
        result = play_r()
        print("Computer's choice {}".format(result[1]))
        if(result[0] == 1):
            win += 1
        elif result[0] == 2:
            lost += 1
        
        rounds-=1
    
    if(win >= 2):
        print("You Won!")
    
    elif(lost >= 2):
        print("You Lost!")
    else:
        print("Its a tie")






play()
