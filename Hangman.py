import random

a = True

with open("words.txt") as f:
    words = (f.read()).split()

chances = 5

while (a == True):

    print("********Welcome to Hangman - By Jatin Yadav********")

    word = random.choice(words)

    letter1 = random.choice(word)
    letter2 = random.choice(word)
    letter3 = random.choice(word)
    letter4 = random.choice(word)

    word1 = word.replace(letter1 , " @ ")
    word1 = word1.replace(letter2 , " # ")
    word1 = word1.replace(letter3 , " $ ")
    word1 = word1.replace(letter4 , " ! ")

    print(word1)

    for i in range(chances):

        letter = input("Guess any letter : \n")

        if (letter in word):

            if(letter == letter1):

                word1 = word1.replace(" @ " , letter)
                print("You guessed the correct letter!\n")
                print(word1)

            elif(letter == letter2):

                word1 = word1.replace(" # " , letter)
                print("You guessed the correct letter!\n")
                print(word1)

            elif(letter == letter3):

                word1 = word1.replace(" $ " , letter)
                print("You guessed the correct letter!\n")
                print(word1)

            elif(letter == letter4):

                word1 = word1.replace(" ! " , letter)
                print("You guessed the correct letter!\n")
                print(word1)

            if word == word1:

                print("Congratulations!, You completed the word\n")
                break
        else :

            print("You guessed the wrong letter try again\n")
            chances = chances - 1

            if chances == 0:

                print(f"You lost, The word was {word}")

            else:

                print("Chances left are", chances)

    c = input("Do you want to play again : \n")

    if(c == "yes"):

        a = True
        chances = 5

    elif(c == "no"):

        a = False
        print("Thank you for playing!, Have a nice day")