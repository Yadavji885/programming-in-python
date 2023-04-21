import random
rand = random.randint(1,3)

if rand == 1:
    comp = "r"
elif rand == 2:
    comp = "p"
else:
    comp = "s"

me = input("Choose any of the three [r,p,s] : \n")

def gamerule(comp,me):

    if comp == me:

        return None
    
    elif(comp == "r"):

        if(me == "p"):

            return True
        
        elif me == "s":

            return False
        
    elif comp == "p":

        if me == "s":

            return True
        
        elif me == "r":

            return False
        
    elif comp == "s":

        if me == "r":

            return True
        
        elif me == "p":

            return False
        
g = gamerule(comp,me)

print(f"Computer choose {comp} and you choose {me}")

if g == None:

    print("It is a tie")

elif g == True:

    print("You won! congratulations")
    
elif g == False:

    print("You lose! Try again")

print("Have a nice day!")