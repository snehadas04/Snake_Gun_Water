import random

def game(comp,you):
    if(comp == you):
        return '    ## Match Draw ##'
    elif(comp == 's' and you == 'w'):
        return '    !! You lost the Match !!'
    elif(comp == 's' and you == 'g'):
        return '    << You win the Match >>'
    elif(comp == 'g' and you == 'w'):
        return '    << You win the Match >>'
    elif(comp == 'g' and you == 's'):
        return '    !! You lost the Match !!'
    elif(comp == 'w' and you == 's'):
        return '    << You win the Match >>'
    elif(comp == 'w' and you == 'g'):
        return '    !! You lost the Match !!'

print("Computer Choice :> Snake(s)    Water(w)    Gun(g)")
ranChoice = random.randint(1, 3)
if (ranChoice == 1):
    comp = 's'
elif (ranChoice == 2):
    comp = 'w'
elif (ranChoice == 3):
    comp = 'g' 
you = input("Your Choice :> Snake(s)    Water(w)    Gun(g)")

result = game(comp, you)
print("Computer Choice :>" +str(comp))
print("User Choice :>" +str(you))
print(result)