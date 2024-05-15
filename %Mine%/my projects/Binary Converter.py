db = {
    "0" : "00",
    "1" : "01",
    "2" : "10",
    "3" : "11",
    "4" : "100",
    "5" : "101",
    "6" : "110",
    "7" : "111",
    "8" : "1000",
    "9" : "1001",
    "10" : "1010",
    "11" : "1011",
    "12" : "1100",
    "13" : "1101",
    "14" : "1110",
    "15" : "1111",
}

ob = {
    "0" : "00",
    "1" : "01",
    "2" : "10",
    "3" : "11",
    "4" : "100",
    "5" : "101",
    "6" : "110",
    "7" : "111"
}

hb = {
    "0" : "00",
    "1" : "01",
    "2" : "10",
    "3" : "11",
    "4" : "100",
    "5" : "101",
    "6" : "110",
    "7" : "111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111",
}

class Binary_Converter:

    def Decimal_to_Binary(self):
        n = int(input("Enter the number : \n"))
        temp = n
        hans = ""
        d = n//2
        while d != 1:
            d = n//2
            if n%2 != 0:
                n += 1
                r = n//2 - d
                hans = hans + str(r)
                n = d
            else:
                r = n//2 - d
                hans = hans + str(r)
                n = d
            if d == 1:
                hans = hans + str(d)
                ans = ""
                sr = str(hans)
                l = len(sr)
                for i in range(-1,-(l+1),-1):
                    ans = ans + sr[i]
                ans = str(ans)
                print(f"{temp} in Binary is {ans}")
                break

    def Decimal_to_Octal(self):
        n = int(input("Enter the number : \n"))
        temp = n
        hans = ""
        d = n//8
        while n != 1:
            d = n//8
            if n % 8 != 0 and n > 16:
                t = n
                while t % 8 != 0:
                    t -= 1
                r = n - t
                hans += str(r)
            elif n % 8 == 0 and n > 16:
                hans += "0"
            elif n % 8 != 0 and n > 8 and n < 16:
                tm = n
                while tm % 8 != 0:
                    tm -= 1
                r = n - tm
                hans += str(r)
            elif n == 8 or n == 16:
                hans += "01"
                break
            n = d
            if n == 1 or (n > 1 and n <= 7):
                hans += str(n)
                break
        ans = ""
        sr = str(hans)
        l = len(sr)
        for i in range(-1,-(l+1),-1):
            ans = ans + sr[i]
        ans = str(ans)
        print(f"{temp} in Octal is {ans}")
    
    def Decimal_to_Hexadecimal(self):
        n = int(input("Enter the number : \n"))
        temp = n
        hans = ""
        d = n//16
        while n != 1:
            d = n//16
            if n % 16 != 0 and n > 32:
                t = n
                while t % 16 != 0:
                    t -= 1
                r = n - t
                if r >= 10 and r <= 15:
                    print(r)
                    for i in hb.keys():
                        if hb.get(i) == db.get(str(r)):
                            hans += str(i)
                else:
                    hans += str(r)       
            elif n % 16 == 0 and n > 32:
                hans += "0"
            elif n % 16 != 0 and n > 16 and n < 32:
                tm = n
                while tm % 16 != 0:
                    tm -= 1
                r = n - tm
                hans += str(r)
                print(r)
            elif n == 16 or n == 32:
                hans += "01"
                break
            n = d
            if n >= 1 and n <= 15:
                if n >= 10:
                    for i in hb.keys():
                        if hb.get(i) == db.get(str(n)):
                            hans += str(i)
                        else:
                            continue           
                else:
                    hans += str(n)
                break
        ans = ""
        sr = str(hans)
        l = len(sr)
        for i in range(-1,-(l+1),-1):
            ans = ans + sr[i]
        ans = str(ans)
        print(f"{temp} in Octal is {ans}")

    def Binary_to_Decimal(self):
        n = input("Enter the number : \n")
        l = len(n)
        a = l
        ans = 0
        for i in range(0,l):
            ans = ans + (int(n[i]) * 2**(a-1))
            a -= 1
        print(f"{n} in decimal is {ans}")

    def Binary_to_Octal(self):
        n = input("Enter the no. (it should be only 0 and 1) :\n")
        ans = ""
        temp1 = ""
        for a in n:
            temp1 = temp1 + a
        temp2 = ""
        if len(temp1)%3 == 0:
            pass
        else:
            for c in range(2):
                temp1 = "0" + temp1
                if len(temp1)%3 == 0:
                    break
        for d in range(len(temp1)):
            temp2 = temp2 + temp1[d]
            if len(temp2)%3 == 0:
                for e in ob.keys():
                    if temp2.startswith("0"):
                        temp2 = temp2[-2] + temp2[-1]
                        f = ob.get(e)
                        if f == temp2:
                            ans = ans + e
                    else:
                        f = ob.get(e)
                        if f == temp2:
                            ans = ans + e
                temp2 = ""        
        print(f"{n} in Octal is {ans}")

    def Binary_to_Hexadecimal(self):
        n = input("Enter the no. (it should be only 0 and 1) :\n")
        ans = ""
        temp1 = ""
        for a in n:
            temp1 = temp1 + a
        temp2 = ""
        if len(temp1)%4 == 0:
            pass
        else:
            for c in range(3):
                temp1 = "0" + temp1
                if len(temp1)%4 == 0:
                    break
        for d in range(len(temp1)):
            temp2 = temp2 + temp1[d]
            if len(temp2)%4 == 0:
                for e in hb.keys():
                    if temp2 == "0000" or temp2 == "0001" or temp2 == "0010" or temp2 == "0011":
                        temp2 = temp2[-2] + temp2[-1]
                        f = hb.get(e)
                        if f == temp2:
                            ans = a + e
                        else:
                            continue
                        temp2 = ""
                    elif temp2 == "0100" or temp2 == "0101" or temp2 == "0110" or temp2 == "0111":
                        temp2 = temp2[-3] + temp2[-2] + temp2[-1]
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                        elif len(temp2) == 2:
                            temp2 = temp2[-2] + temp2[-1]
                            f = hb.get(e)
                            if f == temp2:
                                ans = ans + e
                    else:
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                temp2 = ""
        print(f"{n} in Hexadecimal is {ans}")
    def Octal_to_Decimal(self):
        n = input("Enter the number : \n")
        l = len(n)
        a = l
        ans = 0
        for i in range(0,l):
            ans = ans + (int(n[i]) * 8**(a-1))
            a -= 1
        print(f"{n} in decimal is {ans}")
    def Octal_to_Binary(self):
        n = input("Enter the number : \n")
        ans = ""
        for i in n:
            if i == "0" or i == "1" or i == "2" or i == "3":
                ans = ans + ("0" + hb.get(i))
            else:
                ans = ans + hb.get(i)
        print(f"{n} in Binary is {ans}")
    def Octal_to_Hexadecimal(self):
        n = input("Enter the number : \n")
        hans = ""
        for i in n:
            if i == "0" or i == "1" or i == "2" or i == "3":
                hans = hans + ("0" + hb.get(i))
            else:
                hans = hans + hb.get(i)
        hans = int(hans)
        hans = str(hans)    
        if len(hans)%4 == 0:
            pass
        else:
            for c in range(3):
                hans = "0" + hans
                if len(hans)%4 == 0:
                    break
        temp2 = ""
        ans = ""
        for d in range(len(hans)):
            temp2 = temp2 + hans[d]
            if len(temp2)%4 == 0:
                for e in hb.keys():
                    if temp2 == "0100" or temp2 == "0101" or temp2 == "0110" or temp2 == "0111":
                        temp2 = temp2[-3] + temp2[-2] + temp2[-1]
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                    elif temp2 == "0000" or temp2 == "0001" or temp2 == "0010" or temp2 == "0011":
                        temp2 = temp2[-2] + temp2[-1]
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                        else:
                            continue
                        temp2 = ""
                    else:
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                temp2 = ""
        print(f"{n} in Hexadecimal is {ans}")
            
    def Hexadecimal_to_Decimal(self):
        n = input("Enter the number : \n")
        l = len(n)
        a = l
        hans = 0
        for i in range(0,l):
            if n[i] == "A" or n[i] == "B" or n[i] == "C" or n[i] == "D" or n[i] == "E" or n[i] == "F":
                b = hb.get(n[i])
                for j in db.keys():
                    if db.get(j) == b:
                        hans = hans + (int(j) * 16**(a-1))
                    else:
                        continue
            else:
                hans = hans + (int(n[i]) * 16**(a-1))
            a -= 1
        print(f"{n} in decimal is {hans}")

    def Hexadecimal_to_Binary(self):
        n = input("Enter the number : \n")
        ans = ""
        for i in n:
            if i == "0" or i == "1" or i == "2" or i == "3":
                ans = ans + ("00" + hb.get(i))
            elif i == "4" or i == "5" or i == "6" or i == "7":
                ans = ans + ("0" + hb.get(i))
            else:
                ans = ans + hb.get(i)
        print(f"{n} in Binary is {ans}")

    def Hexadecimal_to_Octal(self):
        n = input("Enter the number : \n")
        hans = ""
        for i in n:
            if i == "0" or i == "1" or i == "2" or i == "3":
                hans = hans + ("00" + hb.get(i))
            elif i == "4" or i == "5" or i == "6" or i == "7":
                hans = hans + ("0" + hb.get(i))
            else:
                hans = hans + hb.get(i)
        ans = ""
        temp1 = hans
        temp2 = ""
        if len(temp1)%3 == 0:
            pass
        else:
            for c in range(2):
                temp1 = "0" + temp1
                if len(temp1)%3 == 0:
                    break
        for d in range(len(temp1)):
            temp2 = temp2 + temp1[d]
            if len(temp2)%3 == 0:
                for e in ob.keys():
                    if temp2.startswith("0"):
                        temp2 = temp2[-2] + temp2[-1]
                        f = ob.get(e)
                        if f == temp2:
                            ans = ans + e
                    else:
                        f = ob.get(e)
                        if f == temp2:
                            ans = ans + e
                temp2 = ""
        print(f"{n} in Binary is {ans}")

Bc = Binary_Converter()
# Bc.Decimal_to_Binary()  d
# Bc.Decimal_to_Octal()  d
# Bc.Decimal_to_Hexadecimal() d 
# Bc.Binary_to_Decimal()  d
# Bc.Binary_to_Octal()  d
# Bc.Binary_to_Hexadecimal()  d
# Bc.Octal_to_Decimal()  d
# Bc.Octal_to_Binary()  d
# Bc.Octal_to_Hexadecimal()  d
# Bc.Hexadecimal_to_Decimal()  d
# Bc.Hexadecimal_to_Binary()  d
# Bc.Hexadecimal_to_Octal()  d
