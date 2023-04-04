'''units :- 
    0-200 = Rs. 2
    201-400 = Rs. 3
    401-600 = Rs. 4
    601-....= Rs. 5'''

unit = int(input("Enter the units : \n"))

if unit <= 200:
    bill = unit*2
    print(f"The elctricity bill is {bill}")

elif unit >= 201 and unit < 400:
    bill = (unit-200)*3 + 400
    print(f"The elctricity bill is {bill}")

elif unit >= 401 and unit < 600:
    bill = (unit-400)*4 + 400 + 600
    print(f"The elctricity bill is {bill}")

elif unit > 601 :
    bill = (unit-600)*5 + 400 + 600 + 800
    print (f"The elctricity bill is {bill}")