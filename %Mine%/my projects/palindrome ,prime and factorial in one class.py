while True:

    class Project:
    
        def factorial(self):
            print("****Factorial****")
            n = int(input("--->Enter any number: \n--->"))
            fact = 1
            
            while(n >= 2):
                fact = fact * n
                n -= 1
    
            print(f"--->Factorial is {fact}")
    
        def primecheck(self):
            print("****Prime check****")
            n = int(input("--->Enter any number: \n--->"))
            a = 0
    
            for i in range(2,n):
                if((n%i) == 0):
                    a += 1
    
            if(a > 0):
                print(f"--->{n} is not a prime no.")
    
            else:
                print(f"--->{n} is a prime no.")
    
        def palindromecheck(self):
            print("****Palindrome check****")
            n = int(input("--->Enter any number: \n--->"))
            rev = ""
            sr = str(n)
            l = len(sr)

            for i in range(-1,-(l+1),-1):
                rev = rev + sr[i]

            rev = int(rev)
            if rev == n :
                print(f"--->{n} is a palindrome number")
            else :
                print(f"--->{n} is not a palindrome number")

    p = Project()
    print("Select the section of program you want to run:")
    print("1) for factorial\n2) for checking prime\n3) for checking palindrome")
    select = int(input("Enter your choice :\n"))

    if select == 1:
        p.factorial()

    elif select == 2:
        p.primecheck()

    elif select == 3:
        p.palindromecheck()
    
    ask = input("Do you want to continue(y,n): \n")

    if ask == "y":
        continue

    else:
        break