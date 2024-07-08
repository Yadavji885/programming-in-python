n = int(input("Enter any no. : "))
i = 1

while(i<=n):
    s = 0
    s = s + (n**i)
    i += 1

print(f"Sum of the series is {s}")