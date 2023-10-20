jk = "__1__|__2__|__3__\n__4__|__5__|__6__\n  7  |  8  |  9"
tempo = jk
print(jk)

for i in range(0,4):
    print("First players's turn")
    x = input("Enter any number which you want to replace :\n")
    jk = jk.replace(x,"X")
    print(jk)
    print("Second player's turn")
    y = input("Enter any number which you want to replace :\n")
    jk = jk.replace(y,"O")
    print(jk)
    