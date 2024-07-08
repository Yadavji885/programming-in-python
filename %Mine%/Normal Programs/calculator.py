a = float(input("Enter any no. : "))
b = float(input("Enter another no. : "))
o = input("Choose a operator [+ ,- ,* ,** ,/ ,// ,%]")

if(o == "+"):
    print(f"Result is {a + b}")

elif(o == "-"):
    print(f"Result is {a - b}")

elif(o == "*"):
    print(f"Result is {a * b}")

elif(o == "**"):
    print(f"Result is {a ** b}")

elif(o == "/"):
    print(f"Result is {a / b}")

elif(o == "//"):
    print(f"Result is {a // b}")

elif(o == "%"):
    print(f"Result is {a % b}")

print("Thank you!")
