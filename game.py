import random

def game(comp,you):
    if(comp == you):
        return Draw
    elif(comp == s and you == w):
        return lost
    elif(comp == s and you == g):
        return win
    elif(comp == g and you == w):
        return win
    elif(comp == g and you == s):
        return lost
    elif(comp == w and you == s):
        return win
    elif(comp == w and you == g):
        return lost

print("Computer Choice :> Snake(s)    Water(w)    Gun(g)")
ranChoice = random.randint(1, 3)
if (ranChoice == 1):
    comp = 's'
elif (ranChoice == 2):
    comp = 'w'
elif (ranChoice == 3):
    comp = 'g' 
user = input("Your Choice :> Snake(s)    Water(w)    Gun(g)")

result = game(comp, user)
print("Computer Choice :>" +str(comp))
print("User Choice :>" +str(user))