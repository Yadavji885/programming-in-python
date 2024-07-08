import xlsxwriter

with open ("Items list.txt") as f:
    r = f.read()

items = {
    1  : "Toothpaste",
    2  : "Shampoo",
    3  : "Hand Sanitizer",
    4  : "Toilet Paper",
    5  : "Laundry Detergent",
    6  : "Dishwashing Liquid",
    7  : "Aluminum Foil",
    8  : "Garbage Bags",
    9  : "Light Bulbs",
    10 : "Batteries",
    11 : "USB Charging Cable",
    12 : "Kitchen Towels",
    13 : "Hand Soap",
    14 : "Air Freshener Spray",
    15 : "Wet Wipes",
    16 : "Multi Purpose Cleaner",
    17 : "Picture Frames",
    18 : "Indoor Plant",
    19 : "Umbrella",
    20 : "Reading Glasses",
    "Toothpaste" : 50,
    "Shampoo" : 80,
    "Hand Sanitizer" : 120,
    "Toilet Paper" : 60,
    "Laundry Detergent" : 150,
    "Dishwashing Liquid" : 70,
    "Aluminum Foil" : 40,
    "Garbage Bags" : 100,
    "Light Bulbs" : 100,
    "Batteries" : 50,
    "USB Charging Cable" : 80,
    "Kitchen Towels" : 90,
    "Hand Soap" : 60,
    "Air Freshener Spray" : 70,
    "Wet Wipes" : 40,
    "Multi Purpose Cleaner" : 120,
    "Picture Frames" : 100,
    "Indoor Plant" : 80,
    "Umbrella" : 150,
    "Reading Glasses" : 200
}

class MeraBharatMaahan:
    
    def welcome(self):
        print("Ram Ram Ji")
    
    def items(self):
        print(r)

    def buy(self):
        workbook = xlsxwriter.Workbook("Bill.xlsx")
        Bill = workbook.add_worksheet("Bill")
        data = []
        bill = 0
        i = int(input("Enter the number of the product you want to buy :\n"))
        p = items.get(i)
        pr= int(items.get(p))
        q = int(input("In how much quantity do you want it :\n"))

        if q == 1:
            print("Thank you")
            bill += pr
            d = ({"Product": p,
                  "Price" : pr,
                  "Quantity" : q,
                  "Net Amount" : (pr*q)})
            data.append(d)
            a = int(input("Do you want to shop more (1 for yes & 2 for no) :\n"))

            while True:

                if a == 1:

                    i = int(input("Enter the number of the product you want to buy :\n"))
                    p = items.get(i)
                    pr= int(items.get(p))
                    q = int(input("In how much quantity do you want it :\n"))

                    if q == 1:

                        print("Thank you")
                        bill += pr
                        d = ({"Product": p,
                              "Price" : pr,
                              "Quantity" : q,
                              "Net Amount" : (pr*q)})
                        data.append(d)

                    else:

                        print("Thank you")
                        bill += pr*q
                        d = ({"Product": p,
                              "Price" : pr,
                              "Quantity" : q,
                              "Net Amount" : (pr*q)})
                        data.append(d)
                        a = int(input("Do you want to shop more (1 for yes & 2 for no) :\n"))

                if a == 2:

                    print("Thanks for your visit, We are eagerly waiting for your next visit")
                    print(f"Your total bill is {bill}")
                    d = ({"Product": p,
                          "Price" : pr,
                          "Quantity" : q,
                          "Net Amount" : (pr*q)})
                    data.append(d)

        else:

            print("Thank you")
            bill += pr*q
            d = {"Product": p,
                "Price" : pr,
                "Quantity" : q,
                "Net Amount" : (pr*q)}
            data.append(d)
            a = int(input("Do you want to shop more (1 for yes & 2 for no) :\n"))

            while True:

                if a == 1:

                    i = int(input("Enter the number of the product you want to buy :\n"))
                    p = items.get(i)
                    pr= int(items.get(p))
                    q = int(input("In how much quantity do you want it :\n"))

                    if q == 1:

                        print("Thank you")
                        bill += pr
                        d = ({"Product": p,
                              "Price" : pr,
                              "Quantity" : q,
                              "Net Amount" : (pr*q)})
                        data.append(d)
                        a = int(input("Do you want to shop more (1 for yes & 2 for no) :\n"))

                    else:

                        print("Thank you")
                        bill += pr*q
                        d = ({"Product": p,
                            "Price" : pr,
                            "Quantity" : q,
                            "Net Amount" : (pr*q)})
                        data.append(d)
                        a = int(input("Do you want to shop more (1 for yes & 2 for no) :\n"))
                    
                elif a == 2:

                    print(f"Your total bill is {bill}")
                    break
        print("Thanks for your visit, We are eagerly waiting for your next visit")
        print("Your Bill receipt has been formed, You can check it by opening Bill.xlsx")
                
        Bill.write(0,0,"Item no.")
        Bill.write(0,1,"Product")
        Bill.write(0,2,"Price")
        Bill.write(0,3,"Quantity")
        Bill.write(0,4,"Net Amount")


        for index, entry in enumerate(data):
            Bill.write(index+1,0,str(index))
            Bill.write(index+1,1,entry["Product"])
            Bill.write(index+1,2,entry["Price"])
            Bill.write(index+1,3,entry["Quantity"])
            Bill.write(index+1,4,entry["Net Amount"])
        workbook.close()

mbm = MeraBharatMaahan()
mbm.welcome()
mbm.items()
mbm.buy()