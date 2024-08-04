import math
n = int(input("Enter any no. : "))
s = math.isqrt(n)
l = []

for i in range(2,s+1):
    a = 0
    for j in range(2,i):
        r = i%j
        if(r == 0):
            a = 1

    if(a == 0):
        l = l +[i]
b = 0
for k in l:
    if n%k == 0:
        b += 1
if b > 0:
    print("The number you entered is not prime")
else:
    print("The number you entered is prime")