n = int(input("Enter any no. : "))
fact = 1

while(n >= 2):
    fact = fact * n
    n -= 1

print(f"Factorial is {fact}")