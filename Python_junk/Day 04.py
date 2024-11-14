mylist=[' ','O',' ']

from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1, or 2:  ")
    return int(guess)    

def checkguess(shuffle_list,player_guess):
    if mylist[guess]=="O":
        print("guess right")
    else:
        print("wrong")
