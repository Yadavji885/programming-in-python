jk = "__1__|__2__|__3__\n__4__|__5__|__6__\n  7  |  8  |  9"
t = jk
print(jk)

player1 = input("Enter First player's Name (You will get X) :\n")
player2 = input("Enter second player's Name (You will get O) :\n")

for i in range(6):
    print(f"{player1}'s turn")
    x = input("Enter any number which you want to replace :\n")
    jk = jk.replace(x,"X")
    print(jk)
    if jk[2]=="X" and jk[8]=="X" and jk[14]=="X":
        print(f"{player1} won!!")
        break
    elif jk[20]=="X" and jk[26]=="X" and jk[32]=="X":
        print(f"{player1} won!!")
        break
    elif jk[38]=="X" and jk[44]=="X" and jk[50]=="X":
        print(f"{player1} won!!")
        break
    elif jk[2]=="X" and jk[20]=="X" and jk[38]=="X":
        print(f"{player1} won!!")
        break
    elif jk[8]=="X" and jk[26]=="X" and jk[44]=="X":
        print(f"{player1} won!!")
        break
    elif jk[14]=="X" and jk[32]=="X" and jk[50]=="X":
        print(f"{player1} won!!")
        break
    elif jk[2]=="X" and jk[26]=="X" and jk[50]=="X":
        print(f"{player1} won!!")
        break
    elif jk[14]=="X" and jk[26]=="X" and jk[38]=="X":
        print(f"{player1} won!!")
        break
    elif jk[2] != t[2] and jk[8] != t[8] and jk[14] != t[14] and jk[20] != t[20] and jk[26] != t[26] and jk[32] != t[32] and jk[38] != t[38] and jk[44] != t[44] and jk[50] != t[50]:
        print("It's a tie match")
        break

    print(f"{player2}'s turn")
    y = input("Enter any number which you want to replace :\n")
    jk = jk.replace(y,"O")
    print(jk)
    
    if jk[2]=="O" and jk[8]=="O" and jk[14]=="O":
        print(f"{player1} won!!")
        break
    if jk[20]=="O" and jk[26]=="O" and jk[32]=="O":
        print(f"{player1} won!!")
        break
    if jk[38]=="O" and jk[44]=="O" and jk[50]=="O":
        print(f"{player1} won!!")
        break
    if jk[2]=="O" and jk[20]=="O" and jk[38]=="O":
        print(f"{player1} won!!")
        break
    if jk[8]=="O" and jk[26]=="O" and jk[44]=="O":
        print(f"{player1} won!!")
        break
    if jk[14]=="O" and jk[32]=="O" and jk[50]=="O":
        print(f"{player1} won!!")
        break
    if jk[2]=="O" and jk[26]=="O" and jk[50]=="O":
        print(f"{player1} won!!")
        break
    if jk[14]=="O" and jk[26]=="O" and jk[38]=="O":
        print(f"{player1} won!!")
        break
    if jk[2] != t[2] and jk[8] != t[8] and jk[14] != t[14] and jk[20] != t[20] and jk[26] != t[26] and jk[32] != t[32] and jk[38] != t[38] and jk[44] != t[44] and jk[50] != t[50]:
        print("It's a tie match")
        break

