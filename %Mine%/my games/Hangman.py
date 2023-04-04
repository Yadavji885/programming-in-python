import random

Hangman = {
    "crumbs" : "रोटी का आटा",
    "seldom" : "कभी-कभी",
    "marvel" : "अद्भुत",
    "Hustle" : "जल्दबाज़ी",
    "Worthy" : "योग्य",
    "Exotic" : "विदेशी",
    "Kindle" : "उजाला",
    "Unique" : "अद्वितीय"
}

words = random.choice(list(Hangman.keys()))
l = Hangman.get(words)
print("\n",l)

chances = 8

print("********Welcome to the Hangman Game - By Jatin Yadav********")

word = words.replace(words,"!@#_$%")
print(word)

for i in range(chances):
    if word == words:
        print("Congratulations, You completed the word")
        break
    while word != words:
        letter = input("Guess any letter :\n")
        if letter in words:
            print("You guessed the correct letter, congrats!")
            f = words.find(letter)
            i = word[f]
            word = word.replace(i , letter)
            print(word)
        elif letter not in words:
            chances -= 1
            print("You guessed the wrong word")
            print(f"Chances left are {chances}")
        elif chances == 0:
            print(f"You lose the game, The word was {words}")
            break
