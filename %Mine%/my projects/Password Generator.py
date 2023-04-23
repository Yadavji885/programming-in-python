import random

ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ll = "abcdefghijklmnopqrstuvwxyz"
no = "1234567890"
sl ="!@#$%^&*?"

n = int(input("Enter the number of password you want :\n"))
uc = int(input("Enter the number of upper letters you want in the password :\n"))
lc = int(input("Enter the number of small letters you want in the password :\n"))
nc = int(input("Enter the number of numeric letters you want in the password :\n"))
sc = int(input("Enter the number of special letters you want in the password :\n"))

for j in range(n):
    password = ""
    for i in range(1):
        for a in range(uc):
            l1 = random.choice(ul)
            password = password + l1
        for b in range(lc):
            l2 = random.choice(ll)
            password = password + l2
        for c in range(nc):
            l3 = random.choice(no)
            password = password + l3
        for d in range(sc):
            l4 = random.choice(sl)
            password = password + l4
    print(password)