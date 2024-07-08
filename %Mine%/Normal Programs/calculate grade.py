s1 = int(input("Enter the marks scored in English : "))
s2 = int(input("Enter the marks scored in Science : "))
s3 = int(input("Enter the marks scored in Maths : "))
s4 = int(input("Enter the marks scored in Social Studies : "))
s5 = int(input("Enter the marks scored in Computer : "))

tm = s1+s2+s3+s4+s5
print (tm)

p = (tm/500)*100
print(f"You scored {p}%")

if(p >= 85):
    print("Your grade is A")

elif(p >= 75 and p < 85):
    print("Your grade is B")

elif(p >= 55 and p < 75):
    print("Your grade is C")

elif(p < 55):
    print("Your grade is D")