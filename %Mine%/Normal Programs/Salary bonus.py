Name = input("Enter your name : ")
Gender = input("Enter your gender [M,F] : ")
Salary = int(input("Enter your salary : "))

if(Salary >= 10000):
    if(Gender == "M"):
        print("Congratulations! ,You got a bonus of 15000")
        b = Salary + 15000
        print(f"Now your Salary is {b}")
    elif(Gender == "F"):
        print("Congratulations! ,You got a bonus of 20000")
        b = Salary + 20000
        print(f"Now your Salary is {b}")

else:
    print("Congratulations! ,You got a bonus of 10000")
    b = Salary + 10000
    print(f"Now your Salary is {b}")