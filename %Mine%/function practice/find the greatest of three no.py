def Greatest(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

n1 = int(input("Enter first no. : \n"))
n2 = int(input("Enter second no. : \n"))
n3 = int(input("Enter third no. : \n"))

result = Greatest(n1,n2,n3)

print(f"The greatest of the entered no. is : {result}")