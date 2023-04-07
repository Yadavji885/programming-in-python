import csv

Train = {
    "Jalandhar to Jind" : "Sarbat Da Bhala  - 22480",
    "Delhi to Jalandhar" : "Sarbat Da Bhala  - 22479"
}


class IRCTC:

    def welcome(self):
        print(f"Welcome {name} to IRCTC")

    def route(self):
        s = Train.get(route)
        print(f"Your Train name and Train no. is {s}")

    def Personconfirm(self):
        with open ("Ticket.csv","w") as t:
            ts = csv.writer(t)
            ts.writerow(["Name" , "Age" , "Gender" , "Seat preference" ,"Coach Type"])
            if c == "y": 
                n = input("Enter your name :\n")
                age = int(input("Enter your age :\n"))
                gender = input("Enter your gender [male,female] : \n")
                sp = input("What is your seat preference [window,middle,aisle] :\n")
                print(f"pricing of this train according to coach type per person is :\n{pricing}")
                bp = input("Enter which type of coach you want to book : \n")
                info = [n ,age ,gender ,sp ,bp]
                ts.writerow(info)
                print(f"You have to pay Rs.{pricing.get(bp)} only")

            else:
                q = int(input("For how many persons you want to book ticket :\n"))
                with open ("Ticket.csv","w") as t:
                    ts = csv.writer(t)
                    ts.writerow(["Name" , "Age" , "Gender" , "Seat preference" ,"Coach Type"])
                    for i in range(q):
                        n = input("Enter the name of the person :\n")
                        age = int(input("Enter the age of the person :\n"))
                        gender = input("Enter the gender of the person [male,female] : \n")
                        sp = input("What is the seat preference of the person [window,middle,aisle] :\n")
                        print(f"pricing of this train according to coach type per person is :\n{pricing}")
                        bp = input("Enter which type of coach the person want to book : \n")
                        print("\nOk ,Thank you\n")
                        info = [n ,age ,gender ,sp ,bp]
                        ts.writerow(info)
                print(f"You have to pay Rs.{(pricing.get(bp))*q} only")

    @staticmethod
    def Thankyou():
        print("Your ticket slip has been released in the form of csv file named Ticket.csv")
        print("Thank you for using IRCTC")

pricing = {
    "seating coach" : 150,
    "sleeping coach" : 350,
    "ac tier I" : 650,
    "ac tier II" : 850,
    "ac sleeper" : 1050
        }

i = IRCTC()
name = input("Enter your name :\n")
i.welcome()
route = input("Home station to Destination :\n")
i.route()
c = input("Are you here to book ticket for youself or for others [y for yourself,o for others] : \n")
print("Ok, Just wait a minute, we are processing...........")
i.Personconfirm()
i.Thankyou()
