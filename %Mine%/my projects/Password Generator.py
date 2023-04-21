import random

ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ll = "abcdefghijklmnopqrstuvwxyz"
no = "1234567890"
sl ="!@#$%^&*?"

n = int(input("Enter the number of password you want :\n"))

for j in range(n):
    password = ""
    for i in range(2):
        l1 = random.choice(ul)
        password = password + l1
        l2 = random.choice(ll)
        password = password + l2
        l3 = random.choice(no)
        password = password + l3
        l4 = random.choice(sl)
        password = password + l4
    print(password)