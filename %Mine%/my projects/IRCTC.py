import csv
import random

Accounts = {
    "Jatin Yadav" : "Yadav09*",
    "Virender Kumar" : "Yadav885*"
}

Train = {
    "Jalandhar to Jind" : "Sarbat Da Bhala  - 22480",
    "Delhi to Jalandhar" : "Sarbat Da Bhala  - 22479"
}

lst = []
for i in range(1,1001):
    lst.append(i)

class IRCTC:

    def welcome(self):
        print(f"Welcome to IRCTC")

    def route(self):
        s = Train.get(route)
        print(f"Your Train name and Train no. is {s}")

    def Personconfirm(self):
        with open ("Ticket.csv","w") as t:
            ts = csv.writer(t)
            if c == "y": 
                n = input("Enter your name :\n")
                age = int(input("Enter your age :\n"))
                gender = input("Enter your gender [Male,Female] : \n")
                sp = input("What is your seat preference [Window,Middle,Aisle] :\n")
                print(f"pricing of this train according to coach type per person is :\n{pricing}")
                bp = input("Enter which type of coach you want to book : \n")
                seat = random.choice(lst)
                info = [f"Name : {n} \nAge : {age} \nGender : {gender} \nSeat preference : {sp} \nCoach type : {bp}\nSeat No. : {seat}\n"]
                ts.writerow(info)
                print(f"You have to pay Rs.{pricing.get(bp)} only")

            else:
                q = int(input("For how many persons you want to book ticket :\n"))
                with open ("Ticket.csv","w") as t:
                    ts = csv.writer(t)
                    seat = random.choice(lst)
                    for i in range(q):
                        n = input("Enter the name of the person :\n")
                        age = int(input("Enter the age of the person :\n"))
                        gender = input("Enter the gender of the person [Male,Female] : \n")
                        sp = input("What is the seat preference of the person [Window,Middle,Aisle] :\n")
                        print(f"pricing of this train according to coach type per person is :\n{pricing}")
                        bp = input("Enter which type of coach the person want to book : \n")
                        seat = seat + 1
                        print("\nOk ,Thank you\n")
                        info = [f"Name : {n} \nAge : {age} \nGender : {gender} \nSeat preference : {sp} \nCoach type : {bp}\nSeat No. : {seat}\n"]
                        ts.writerow(info)
                print(f"You have to pay Rs.{(pricing.get(bp))*q} only")

    @staticmethod
    def Thankyou():
        print("Your ticket slip has been released in the form of csv file named Ticket.csv")
        print("Thank you for using IRCTC")

pricing = {
    "Seating Coach" : 150,
    "Sleeping Coach" : 350,
    "Ac Tier I" : 650,
    "Ac Tier II" : 850,
    "Ac Sleeper" : 1050
        }

i = IRCTC()
i.welcome()

n = input("Enter your account name :\n")
if n in list(Accounts.keys()):
    p = input("Enter your password : \n")
    if p == Accounts.get(n):
        print(f"Welcome {n}, We are glad to see you here")
    while p != Accounts.get(n):
        if p != Accounts.get(n):
            print("Your password is not correct, Please recheck")
            p = input("Enter your password : \n")
else :
    while n not in Accounts.keys():
        print("No account existes with this Account name")
        n = input("Enter your account name :\n")
        if n in list(Accounts.keys()):
            p = input("Enter your password : \n")
            if p == Accounts.get(n):
                print(f"Welcome {n}, We are glad to see you here")
            while p != Accounts.get(n):
                if p != Accounts.get(n):
                    print("Your password is not correct, Please recheck")
                    p = input("Enter your password : \n")

route = input("Home station to Destination :\n")
i.route()
c = input("Are you here to book ticket for youself or for others [y for yourself,o for others] : \n")
print("Ok, Just wait a minute, we are processing...........")
i.Personconfirm()
i.Thankyou()
