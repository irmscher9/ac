import random

rn = random.randint(1,10)
myn = 0

while myn != rn:
    myn = input("Guess a number between 1 and 10: ")
    if type(myn) is int:
        if myn < rn:
            print('Too Low :(')
        if myn > rn:
            print('Too High :(')
    else:
        print("Please type in numbers only")

print("You won, the number was {} ".format(rn))
        
