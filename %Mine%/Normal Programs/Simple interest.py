p = float(input("Enter the amount borrowed : "))
r = float(input("Enter the rate of interst : "))
t = float(input("Enter the years given to repay the loan : "))

si = (p * r * t)/100

print(f"The simple interst is {si}")

a = p + si

print(f"The total amout to be repayed is {a}")