n = int(input("Enter any number: \n"))
sum = 0 
for i in range(1,n+1):
    fact = 1
    for j in range(2,i+1):
        fact = fact*j
    sum += i/fact
print(sum)