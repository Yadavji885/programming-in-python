import random

Hangman = {
    "crumbs" : "रोटी का आटा",
    "seldom" : "कभी-कभी",
    "marvel" : "अद्भुत",
    "hustle" : "जल्दबाज़ी",
    "worthy" : "योग्य",
    "exotic" : "विदेशी",
    "kindle" : "उजाला"
}

words = random.choice(list(Hangman.keys()))
l = Hangman.get(words)
print("\n",l)

chances = 8

print("********Welcome to the Hangman Game - By Jatin Yadav********")

word = words.replace(words,"!@#_$%")
print(word)

for i in range(chances):

    letter = input("Guess any letter :\n")
    if word == words:
        print("Congratulations, You completed the word")
        break
    elif letter in words:
        print("You guessed the correct letter, congrats!")
        f = words.find(letter)
        j = word[f]
        word = word.replace(j , letter)
        print(word)
        if word == words:
            print("Congratulations, You completed the word")
            break
    elif chances == 0:
        print(f"You lose the game, The word was {words}")
        break
    elif letter not in words:
        chances -= 1
        print("You guessed the wrong word")
        print(f"Chances left are {chances}")
    
