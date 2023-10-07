import random

with open("scrabble game ke words.txt","r") as f:
    words = (f.read()).split()

word = random.choice(words)

temp = word

jw = ""

for i in word:
    r = random.choice(word)
    word = word.replace(r,"")
    jw += r

while True:

    print(jw)

    ans = input("Enter your guessing :\n")

    if ans == temp:
        print("You guessed it correct")
        break
    else:
        print("You guessed it wrong! Please try it again")