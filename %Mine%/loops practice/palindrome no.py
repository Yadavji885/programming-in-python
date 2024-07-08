n = input("Enter any number : \n") 
no = ""
for i in range(-1 , -6 , -1):
    no = no + n[i]

if no == n :
    print("The number you entered is a palindrome number")
else :
    print("The number you entered is not a palindrome number")
    