import random

def password_generator():
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

ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ll = "abcdefghijklmnopqrstuvwxyz"
no = "1234567890"
sl ="!@#$%^&*?"

n = int(input("Enter the number of password you want :\n"))

for k in range(n):
    password_generator()
