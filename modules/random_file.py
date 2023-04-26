import random
# x = [1,2,3,4,5]
# print(random.choice(x))
"""Write a program that stimulate a game of rock-paper-scissors should ask the user for their choice (rock,paper,or scissors)
and then randomly generate a choice for the computer. The program should then print out the winner of the game (either the user of the computer )
based on the following rules:
* Rock beats scissors
* Scissors beats paper
* Paper beats rock
If both the user and the computer choose the same option, the dame is a tie."""

x = input('Enter your choice ( Rock, Scissors, Paper):')

print()

y = ['rock','paper','scissors'] 

computer = (random.choice(y))
print('computers choice:',computer)

print()



if x==computer:
    print("Tie match")
elif x=='Scissors' or 'scissors' or 'SCISSORS':
    if computer=='rock':
        print('user win')
    else:
        print('computer win') 

elif x=='PAPER' or 'paper' or 'Paper':
    if computer=='scissors':
        print('user win')   
    else:
        print('computer win')

elif x=='Rock' or 'rock' or 'ROCK':
    if computer=='paper':
        print('user win')      
    else:
        print('computer win')

