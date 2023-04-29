s = input("Enter any no. : \n")
n = int(s)
sno = ""
sno = sno + s[-1]
sno = sno + s[-2]
sno = sno + s[-3]
sno = sno + s[-4]
sno = sno + s[-5]

no = int(sno)

if(no == n):
    print("The no. you entered is a palindrome no.")
else :
    print("The no. you entered is not a palindrome no.")