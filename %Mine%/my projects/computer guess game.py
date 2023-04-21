import random

comp = random.randint(1,100)
a = None
guesses = 0

while (comp != a):

    a = int(input("Guess any number : "))
    guesses += 1
    if(guesses == 5):
        print("You failed to guess the correct no. in 5 times")
        print(f"The correct no. is {comp}")
        break
    if(comp == a):
        print(f"You guessed the correct no. in {guesses} guesses")

    elif(comp < a):
        print("Enter a smaller no.")

    elif(comp > a):
        print("Enter a greater no.")