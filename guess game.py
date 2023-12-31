mylist=['','O','']
from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess=""
    while guess not in ['0','1','2']:
        guess=input("enter a number : 0,1 or 2:")
    return int(guess)

def guess_check(mylist,guess):
    if mylist[guess]=='O':
        print("correct!")
    else:
        print("wrong!, better luck next time")
    print(mylist)

mylist=['','O','']
mixed_list=shuffle_list(mylist)
guess=player_guess()
guess_check(mixed_list,guess)