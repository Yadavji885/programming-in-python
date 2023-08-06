limit = 11
a = 0
b = 1
nt = b
for i in range(2,limit):
    print(nt,"")
    a , b = b , nt
    nt = a + b