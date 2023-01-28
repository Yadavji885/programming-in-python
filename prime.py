n = int(input("Enter any no. : "))
a = 0

for i in range(2,n):
    if((n%i) == 0):
        a += 1

if(a > 0):
    print(f"{n} is not a prime no.")

else:
    print(f"{n} is a prime no.")