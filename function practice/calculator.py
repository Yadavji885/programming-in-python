n1 = int(input("Enter a no. : \n"))
o = input("Enter any opetor you want [+,-,*,**,/,//,%]: \n")
n2 = int(input("Enter another no. : \n"))


def Calculator(n1,n2):
    if(o == "+"):
        return n1+n2
    elif(o == "-"):
        return n1-n2
    elif(o == "*"):
        return n1*n2
    elif(o == "**"):
        return n1**n2
    elif(o == "/"):
        return n1/n2
    elif(o == "//"):
        return n1//n2
    elif(o == "%"):
        return n1%n2
    
result = Calculator(n1,n2)

print(f"The result is : {result}")