ATM = {
    4614664645413 : "Virender Kumar",
    "Virender Kumar" : 100000,
    4546354251244 : "Muskan Yadav",
    "Muskan Yadav" : 50000,
    4224554715455 : "Sunita Devi",
    "Sunita Devi" : 100000
}

a = int(input("Enter your account no. : \n"))
if a in ATM:
    print(f"Welcome {ATM.get(a)}, We are glad you are here!!")
    print(f"Your current balance is {ATM.get(ATM.get(a))}")

    q = input("What do you want to do [Withdraw or Deposite]:\n")
    if q == "Withdraw":

        amount = int(input("How much amount you want to Withdraw :\n"))

        if amount > ATM.get(ATM.get(a)):
            print("Sorry, Your account balance is not enough")

        elif amount < ATM.get(ATM.get(a)):

            print("Thank you!")
            ATM[(ATM.get(a))] = (ATM.get(ATM.get(a))) - amount
            print(f"Now your bank balance is {ATM.get(ATM.get(a))}")
            print("Please visit again\n")

    elif q == "Deposite":
        amount = int(input("How much amount you want to deposite :\n"))
        print("Thank you!")
        ATM[(ATM.get(a))] = (ATM.get(ATM.get(a))) + amount
        print(f"Now your bank balance is {ATM.get(ATM.get(a))}")
        print("Please visit again\n")
else:
    print("We have no account registered with this number, Please recheck the account no you entered")