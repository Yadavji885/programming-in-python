n = int(input("Enter any two digit no. : "))

r = n%10
q = n//10
reverse = (r*10)+q
print(f"Reverse of {n} is {reverse}")